from django.views.generic import ListView, DetailView

from apps.catalog.models import Category, WebTemplate
from apps.catalog import selectors


class CategoryListView(ListView):
    template_name = "catalog/category_list.html"
    context_object_name = "categories"

    def get_queryset(self):
        return selectors.get_active_categories_with_counts()


class TemplateListView(ListView):
    template_name = "catalog/template_list.html"
    context_object_name = "templates"

    def get_queryset(self):
        category_slug = self.kwargs.get("category_slug")
        if category_slug:
            self.category, qs = selectors.get_templates_by_category(category_slug)
            return qs
        self.category = None
        return selectors.get_published_templates()

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["category"] = getattr(self, "category", None)
        ctx["categories"] = selectors.get_active_categories()
        return ctx


class TemplateDetailView(DetailView):
    template_name = "catalog/template_detail.html"
    context_object_name = "template"

    def get_object(self, queryset=None):
        return selectors.get_template_detail(
            category_slug=self.kwargs["category_slug"],
            template_slug=self.kwargs["slug"],
        )

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["related_templates"] = selectors.get_related_templates(self.object)
        return ctx
