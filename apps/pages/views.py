from django.views.generic import TemplateView

from apps.catalog import selectors


class HomePageView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["categories"] = selectors.get_active_categories_with_counts()
        ctx["featured_templates"] = selectors.get_featured_templates(limit=6)
        return ctx
