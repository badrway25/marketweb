from django.urls import path

from apps.catalog.views import CategoryListView, TemplateDetailView, TemplateListView

app_name = "catalog"

urlpatterns = [
    path("", TemplateListView.as_view(), name="template_list"),
    path("categories/", CategoryListView.as_view(), name="category_list"),
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
]
