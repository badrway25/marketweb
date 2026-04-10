from django.http import Http404
from django.views.generic import DetailView, ListView, TemplateView

from apps.catalog import selectors, template_content
from apps.catalog.template_dna import get_dna


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
        ctx["has_live_preview"] = template_content.has_live_template(self.object.slug)
        return ctx


# ---------------------------------------------------------------------------
# Live multi-page template preview
# ---------------------------------------------------------------------------
#
# A template's "live preview" is the *actual* multi-page website product the
# customer is buying — Home, About, Services, Blog, Contact, etc. — rendered
# as standalone pages with the template's own DNA (chrome, fonts, palette).
#
# Routing:
#   /templates/<cat>/<slug>/preview/                       → home
#   /templates/<cat>/<slug>/preview/<page>/                → inner page
#   /templates/<cat>/<slug>/preview/<page>/<post>/         → blog/news article
#
# Template path resolution:
#   live_templates/<category>/<archetype>/<page-kind>.html
#   - <category>  comes from WebTemplate.category.slug
#   - <archetype> comes from the DNA registry
#   - <page-kind> comes from template_content.TEMPLATE_CONTENT[slug].pages
#
# A template needs BOTH a DNA entry AND a content registry entry to be
# eligible for live preview. Otherwise the view returns 404 — the system
# stays strictly opt-in per template, exactly like the DNA system itself.

class LiveTemplateView(TemplateView):
    """Render one page of a template's live multi-page preview."""

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        slug          = kwargs["slug"]
        category_slug = kwargs["category_slug"]
        page_slug     = kwargs.get("page", "home")
        post_slug     = kwargs.get("post_slug")

        # Resolve the template + DNA + content. The view requires BOTH a DNA
        # entry and a content registry entry — strictly opt-in per template.
        self.template_obj = selectors.get_template_detail(category_slug, slug)
        self.dna          = get_dna(slug)
        self.content      = template_content.get_content(slug)
        if not self.dna or not self.content:
            raise Http404("Template has no live preview yet.")

        # Find the page entry (drives nav highlighting + template kind)
        self.page_entry = template_content.find_page(slug, page_slug)
        if not self.page_entry:
            raise Http404(f"Page '{page_slug}' not found for this template.")

        archetype = self.dna["archetype"]
        page_kind = self.page_entry["kind"]

        # Blog/news detail uses a dedicated kind regardless of the parent slug
        if post_slug:
            self.post = template_content.find_post(slug, post_slug)
            if not self.post:
                raise Http404(f"Post '{post_slug}' not found.")
            page_kind = page_kind.replace("_list", "_detail")
        else:
            self.post = None

        self._resolved_template = (
            f"live_templates/{category_slug}/{archetype}/{page_kind}.html"
        )

    def get_template_names(self):
        return [self._resolved_template]

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        # WebTemplate object + brand palette injected as CSS-friendly hex
        brand   = self.template_obj.brand
        palette = brand.palette or {}

        ctx["template"]  = self.template_obj
        ctx["brand"]     = brand
        ctx["dna"]       = self.dna
        ctx["content"]   = self.content
        ctx["site"]      = self.content["site"]
        ctx["pages"]     = self.content["pages"]
        ctx["page"]      = self.page_entry
        ctx["page_data"] = self.content.get(self.page_entry["slug"], {})
        ctx["posts"]     = self.content.get("posts", [])
        ctx["post"]      = self.post

        # Theme tokens for CSS variable injection in the per-archetype _base
        heading_font, body_font = self.dna["font_pairing"]
        ctx["theme"] = {
            "primary":      palette.get("primary",   "#0f172a"),
            "secondary":    palette.get("secondary", "#f1f5f9"),
            "accent":       palette.get("accent",    "#f59e0b"),
            "heading_font": heading_font,
            "body_font":    body_font,
        }
        return ctx
