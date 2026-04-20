from django.urls import path

from apps.catalog.views import (
    CategoryListView,
    ClusterDetailView,
    LiveTemplateView,
    RoleDiscoveryView,
    TemplateDetailView,
    TemplateListView,
    TemplateTypeaheadJSON,
    UseCaseDiscoveryView,
)

app_name = "catalog"

urlpatterns = [
    path("", TemplateListView.as_view(), name="template_list"),
    path("categories/", CategoryListView.as_view(), name="category_list"),
    # ── X.2 Commit 4 · taxonomy-driven discovery ───────────────────
    # These fixed-prefix paths MUST sit before the ``<slug:category_slug>/``
    # catch-all below — otherwise Django's resolver matches ``search``,
    # ``clusters``, ``for-role``, ``for-use-case`` as category slugs and
    # returns a 404 from the category lookup inside the listing view.
    path(
        "search/typeahead/",
        TemplateTypeaheadJSON.as_view(),
        name="search_typeahead",
    ),
    path(
        "clusters/<slug:cluster_slug>/",
        ClusterDetailView.as_view(),
        name="cluster_detail",
    ),
    path(
        "for-role/<slug:role_slug>/",
        RoleDiscoveryView.as_view(),
        name="role_discovery",
    ),
    path(
        "for-use-case/<slug:use_case_slug>/",
        UseCaseDiscoveryView.as_view(),
        name="use_case_discovery",
    ),
    path(
        "<slug:category_slug>/",
        TemplateListView.as_view(),
        name="template_list_by_category",
    ),
    path(
        "<slug:category_slug>/<slug:slug>/",
        TemplateDetailView.as_view(),
        name="template_detail",
    ),
    # ── Full multi-page live preview ─────────────────────────
    path(
        "<slug:category_slug>/<slug:slug>/preview/",
        LiveTemplateView.as_view(),
        name="live_template_home",
    ),
    path(
        "<slug:category_slug>/<slug:slug>/preview/<slug:page>/",
        LiveTemplateView.as_view(),
        name="live_template_page",
    ),
    path(
        "<slug:category_slug>/<slug:slug>/preview/<slug:page>/<slug:post_slug>/",
        LiveTemplateView.as_view(),
        name="live_template_post",
    ),
]
