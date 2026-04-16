from django.http import Http404, HttpRequest
from django.views.generic import DetailView, ListView, TemplateView

from apps.catalog import selectors, template_content, template_i18n
from apps.catalog.template_dna import get_dna
from apps.editor.rendering import apply_project_overrides
from apps.projects.selectors import get_project_for_preview


# ── Staff preview gate (D-055) ────────────────────────────────
#
# The draft tier is invisible to the public catalog. Staff can still
# reach a draft template for QA by (a) authenticating as staff AND
# (b) explicitly opting in via `?preview=1`. Both conditions must
# hold — a staff member who lands on a draft URL without the query
# string still sees the public behaviour (404) so accidental drive-by
# traffic never normalizes the draft surface. Views read this flag
# once and thread it into every selectors call they make.

def _staff_preview_mode(request: HttpRequest) -> bool:
    user = getattr(request, "user", None)
    if user is None or not user.is_authenticated or not user.is_staff:
        return False
    return request.GET.get("preview") == "1"


class CategoryListView(ListView):
    template_name = "catalog/category_list.html"
    context_object_name = "categories"

    def get_queryset(self):
        return selectors.get_active_categories_with_counts(
            include_drafts=_staff_preview_mode(self.request),
        )


class TemplateListView(ListView):
    template_name = "catalog/template_list.html"
    context_object_name = "templates"
    paginate_by = 12

    def get_queryset(self):
        self.search_query = self.request.GET.get("q", "").strip()
        self.sort_by = self.request.GET.get("sort", "recent")
        self.staff_preview = _staff_preview_mode(self.request)

        self.category, qs = selectors.get_listing_templates(
            category_slug=self.kwargs.get("category_slug"),
            search_query=self.search_query or None,
            sort_by=self.sort_by,
            include_drafts=self.staff_preview,
        )
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["category"] = self.category
        ctx["categories"] = selectors.get_active_categories()
        ctx["search_query"] = self.search_query
        ctx["current_sort"] = self.sort_by
        ctx["sort_options"] = selectors.SORT_LABELS
        ctx["staff_preview"] = self.staff_preview

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
            include_drafts=_staff_preview_mode(self.request),
        )

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["related_templates"] = selectors.get_related_templates(
            self.object,
            include_drafts=_staff_preview_mode(self.request),
        )
        # D-056 (Session 20): the legacy `has_live_preview` context var is
        # deleted. A template that reaches this view is published_live by
        # construction (see tier gate in selectors.get_template_detail),
        # so the detail page shows the real "Apri anteprima completa" CTA
        # unconditionally. No ghost `href="#"` fallback.
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
# D-055 adds a second gate: only `published_live` templates may render here
# publicly. Staff may preview a draft's live route via `?preview=1`.

class LiveTemplateView(TemplateView):
    """Render one page of a template's live multi-page preview."""

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        slug          = kwargs["slug"]
        category_slug = kwargs["category_slug"]
        page_slug     = kwargs.get("page", "home")
        post_slug     = kwargs.get("post_slug")

        # Tier gate (D-055). Drafts 404 on public access — authors can
        # still reach them via `?preview=1` when authenticated as staff.
        include_drafts = _staff_preview_mode(request)
        self.template_obj = selectors.get_template_detail(
            category_slug, slug, include_drafts=include_drafts
        )

        # Locale resolution (Phase 2i.1 — Session 23 i18n pilot).
        # Reads `?lang=xx` and validates. Falls back to `it` for unknown or
        # missing params. Every template is guaranteed to have an `it`
        # content block, so a locale miss always renders cleanly.
        self.locale = template_i18n.resolve_locale(request)

        # Resolve DNA + content registry entry. Both must exist — the
        # system stays strictly opt-in per template, exactly like the
        # DNA system itself. `get_content` takes the resolved locale and
        # handles the {locale: tree} -> tree unwrap; templates that haven't
        # been migrated to the locale-keyed shape still work via the
        # legacy-flat fallback inside `pick_localized`.
        self.dna     = get_dna(slug)
        self.content = template_content.get_content(slug, self.locale)
        if not self.dna or not self.content:
            raise Http404("Template has no live preview yet.")

        # Find the page entry (drives nav highlighting + template kind).
        # Uses the locale-specific content block — every locale is
        # required to declare the same `pages` list shape (same slugs +
        # kinds, localized labels), so the slug lookup works identically
        # across locales.
        self.page_entry = template_content.find_page(slug, page_slug, self.locale)
        if not self.page_entry:
            raise Http404(f"Page '{page_slug}' not found for this template.")

        archetype = self.dna["archetype"]
        page_kind = self.page_entry["kind"]

        # Blog/news detail uses a dedicated kind regardless of the parent slug
        if post_slug:
            self.post = template_content.find_post(slug, post_slug, self.locale)
            if not self.post:
                raise Http404(f"Post '{post_slug}' not found.")
            page_kind = page_kind.replace("_list", "_detail")
        else:
            self.post = None

        self._resolved_template = (
            f"live_templates/{category_slug}/{archetype}/{page_kind}.html"
        )

        # Project overlay (D-085 Phase A.1). When ?project=<uuid> is
        # present AND the current user is allowed to preview it, the
        # customer's ProjectContent + ProjectDesignTokens overlay the
        # catalog-side content + theme. The skin is unchanged — overrides
        # are applied server-side in get_context_data.
        project_uuid = request.GET.get("project")
        self.preview_project = None
        if project_uuid:
            self.preview_project = get_project_for_preview(
                project_uuid=project_uuid,
                user=request.user,
                template_slug=slug,
            )

    def get_template_names(self):
        return [self._resolved_template]

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        # WebTemplate object + brand palette injected as CSS-friendly hex
        brand   = self.template_obj.brand
        palette = brand.palette or {}

        heading_font, body_font = self.dna["font_pairing"]
        theme = {
            "primary":      palette.get("primary",   "#0f172a"),
            "secondary":    palette.get("secondary", "#f1f5f9"),
            "accent":       palette.get("accent",    "#f59e0b"),
            "heading_font": heading_font,
            "body_font":    body_font,
        }

        # Apply project overlay (D-085 Phase A.1) if a preview_project
        # was resolved in setup(). The skin sees exactly the same
        # context shape — site/pages/page_data/theme — just with the
        # customer's overrides merged in.
        content = self.content
        if self.preview_project is not None:
            content, theme = apply_project_overrides(
                self.preview_project, self.content, theme
            )

        ctx["template"]  = self.template_obj
        ctx["brand"]     = brand
        ctx["dna"]       = self.dna
        ctx["content"]   = content
        ctx["site"]      = content["site"]
        ctx["pages"]     = content["pages"]
        ctx["page"]      = self.page_entry
        ctx["page_data"] = content.get(self.page_entry["slug"], {})
        ctx["posts"]     = content.get("posts", [])
        ctx["post"]      = self.post
        ctx["preview_project"] = self.preview_project

        # Blog parent page slug — used by blog_list/blog_detail chrome templates
        # so they don't have to hardcode the per-template slug ('pubblicazioni',
        # 'diario', ...). Resolved from the first page whose kind == 'blog_list'.
        ctx["blog_parent_slug"] = next(
            (p["slug"] for p in self.content["pages"] if p["kind"] == "blog_list"),
            None,
        )

        # Theme tokens for CSS variable injection in the per-archetype _base
        # (already composed above so we can apply project overrides)
        ctx["theme"] = theme

        # i18n/RTL pilot context (Phase 2i.1 — Session 23).
        # - `locale`: current active language code (e.g. "it", "en", "ar")
        # - `chrome`: dict of localized labels the specialist skin itself
        #   renders (marketplace bar, footer headings, form labels, etc.)
        # - `html_dir`: "rtl" for Arabic, "ltr" otherwise — consumed by
        #   the <html dir="..."> attribute in _base.html
        # - `is_rtl`: boolean shortcut for conditional CSS loads
        # - `locale_switcher`: list of dicts for the language switcher
        #   (each with code/label/badge/is_current)
        # - `default_locale`: exposed so templates can suppress the
        #   `?lang=` query param when building links for the IT default
        # D-068 — the switcher must not advertise locales the template has
        # not actually authored. Without this, a template with only `it` shows
        # 5 pills that each silently fall back to IT — dishonest chrome that
        # contradicts the premium positioning. When a template ships a single
        # locale, the switcher is suppressed entirely (the IT pill alone adds
        # noise without utility). Template authors extend this by adding a new
        # locale block to `TEMPLATE_CONTENT[slug]` in `template_content.py`.
        available_locales = template_content.get_available_locales(
            self.template_obj.slug
        )
        ctx["locale"]            = self.locale
        ctx["chrome"]            = template_i18n.get_chrome(self.locale)
        ctx["html_dir"]          = template_i18n.html_dir(self.locale)
        ctx["is_rtl"]            = template_i18n.is_rtl(self.locale)
        ctx["available_locales"] = available_locales
        ctx["locale_switcher"]   = (
            template_i18n.locale_switcher_entries(self.locale, available_locales)
            if len(available_locales) > 1
            else []
        )
        ctx["default_locale"]    = template_i18n.DEFAULT_LOCALE
        return ctx
