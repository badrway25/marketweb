from django.views.generic import DetailView, ListView

from apps.catalog import selectors


class CategoryListView(ListView):
    template_name = "catalog/category_list.html"
    context_object_name = "categories"

    def get_queryset(self):
        return selectors.get_active_categories_with_counts()


class TemplateListView(ListView):
    template_name = "catalog/template_list.html"
    context_object_name = "templates"
    paginate_by = 12

    def get_queryset(self):
        self.search_query = self.request.GET.get("q", "").strip()
        self.sort_by = self.request.GET.get("sort", "recent")

        self.category, qs = selectors.get_listing_templates(
            category_slug=self.kwargs.get("category_slug"),
            search_query=self.search_query or None,
            sort_by=self.sort_by,
        )
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["category"] = self.category
        ctx["categories"] = selectors.get_active_categories()
        ctx["search_query"] = self.search_query
        ctx["current_sort"] = self.sort_by
        ctx["sort_options"] = selectors.SORT_LABELS

        # Query string without 'page' — used for pagination links
        params = self.request.GET.copy()
        params.pop("page", None)
        ctx["filter_query_string"] = params.urlencode()

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
