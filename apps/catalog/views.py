from django.http import Http404, HttpRequest, JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.views.generic import DetailView, ListView, TemplateView

from apps.catalog import selectors, template_content, template_i18n
from apps.catalog.imagery_policy import (
    enforce_corporate_suite_imagery_policy,
    should_enforce as should_enforce_imagery,
)
from apps.catalog.template_dna import MOTION_PROFILES, get_dna
from apps.catalog.theme_safety import enrich_corporate_suite_theme, should_enrich
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


def _split_csv(value: str | None) -> list[str]:
    """Split a comma-separated query-string param into a cleaned list.

    The catalog filters (``cluster``, ``style``, ``price``, ``feature``,
    ``use_case``, ``audience``) accept multi-value URL shape
    ``?cluster=fine-dining,trattoria``. Values are stripped and empty
    entries are dropped so ``?cluster=`` (empty) resolves to ``None``.
    """
    if not value:
        return []
    return [v.strip() for v in value.split(",") if v.strip()]


class TemplateListView(ListView):
    template_name = "catalog/template_list.html"
    context_object_name = "templates"
    paginate_by = 12

    def get_queryset(self):
        self.search_query = self.request.GET.get("q", "").strip()
        self.sort_by = self.request.GET.get("sort", "recent")
        self.staff_preview = _staff_preview_mode(self.request)

        # X.2 Commit 4 · taxonomy v2 facet filters read from the query
        # string. Multi-value params use comma-separated lists.
        self.selected_clusters = _split_csv(self.request.GET.get("cluster"))
        self.selected_styles = _split_csv(self.request.GET.get("style"))
        self.selected_prices = _split_csv(self.request.GET.get("price"))
        self.selected_features = _split_csv(self.request.GET.get("feature"))
        self.selected_use_cases = _split_csv(self.request.GET.get("use_case"))
        self.selected_audiences = _split_csv(self.request.GET.get("audience"))

        self.category, qs = selectors.get_listing_templates(
            category_slug=self.kwargs.get("category_slug"),
            search_query=self.search_query or None,
            sort_by=self.sort_by,
            include_drafts=self.staff_preview,
            cluster_slugs=self.selected_clusters or None,
            style_slugs=self.selected_styles or None,
            price_tiers=self.selected_prices or None,
            feature_flags=self.selected_features or None,
            use_case_slugs=self.selected_use_cases or None,
            audience_slugs=self.selected_audiences or None,
        )
        # Stash the pre-pagination queryset so get_context_data can
        # compute facet counts across the full match set (not just
        # the current page).
        self._base_qs = qs
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["category"] = self.category
        ctx["categories"] = selectors.get_active_categories()
        ctx["search_query"] = self.search_query
        ctx["current_sort"] = self.sort_by
        ctx["sort_options"] = selectors.SORT_LABELS
        ctx["staff_preview"] = self.staff_preview

        # X.2 Commit 4 · facet sidebar context
        ctx["clusters"] = selectors.get_active_profession_clusters()
        ctx["visual_styles"] = selectors.get_all_visual_styles()
        ctx["feature_flag_labels"] = selectors.FEATURE_FLAG_LABELS
        ctx["facet_counts"] = selectors.get_facet_counts(self._base_qs)
        ctx["selected_clusters"] = self.selected_clusters
        ctx["selected_styles"] = self.selected_styles
        ctx["selected_prices"] = self.selected_prices
        ctx["selected_features"] = self.selected_features
        ctx["selected_use_cases"] = self.selected_use_cases
        ctx["selected_audiences"] = self.selected_audiences

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

        # X.2 Commit 4 · taxonomy v2 context for pills/badges on the
        # detail page. Resolved use-case entries let the template show
        # human labels instead of raw slugs in the use-case block.
        tpl = self.object
        ctx["use_case_entries"] = [
            {
                "slug": uc,
                "label": selectors.USE_CASE_DISCOVERY.get(uc, {}).get("label", uc),
                "detail_url": f"/templates/for-use-case/{uc}/",
            }
            for uc in (tpl.use_cases or [])
            if uc in selectors.USE_CASE_DISCOVERY
        ]
        ctx["feature_flag_labels"] = selectors.FEATURE_FLAG_LABELS
        ctx["active_feature_flags"] = [
            flag
            for flag in selectors.FEATURE_FLAG_LABELS
            if getattr(tpl, flag, False)
        ]
        return ctx


# ── X.2 Commit 4 · taxonomy-driven discovery views ─────────────


class TemplateTypeaheadJSON(View):
    """Lightweight JSON typeahead endpoint for the hero search bar.

    GET ``/templates/search/typeahead/?q=<query>&limit=<n>``
    → JSON dict with three pools: ``templates``, ``clusters``, ``roles``.
    Always returns 200 — empty query yields empty pools.
    """

    def get(self, request: HttpRequest, *args, **kwargs) -> JsonResponse:
        q = request.GET.get("q", "")
        try:
            limit = int(request.GET.get("limit", 8))
        except ValueError:
            limit = 8
        limit = max(1, min(limit, 20))
        payload = selectors.search_templates_typeahead(
            q,
            limit=limit,
            include_drafts=_staff_preview_mode(request),
        )
        return JsonResponse(payload)


class ClusterDetailView(TemplateView):
    """Landing page for a single profession cluster.

    Reuses the same card rendering as the listing page; the cluster
    name + description form the hero. 404s on unknown or inactive
    cluster slugs.
    """

    template_name = "catalog/cluster_detail.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        cluster_slug = kwargs["cluster_slug"]
        include_drafts = _staff_preview_mode(self.request)
        cluster, templates = selectors.get_templates_by_cluster(
            cluster_slug, include_drafts=include_drafts
        )
        ctx["cluster"] = cluster
        ctx["templates"] = templates
        ctx["total"] = templates.count()
        return ctx


class RoleDiscoveryView(TemplateView):
    """Role-driven discovery page (``/templates/for-role/<slug>/``).

    Resolves the role slug against the hardcoded ``ROLE_DISCOVERY``
    map in selectors and renders all published templates that sit in
    the role's cluster set. 404s on unknown role slugs.
    """

    template_name = "catalog/role_discovery.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        role_slug = kwargs["role_slug"]
        include_drafts = _staff_preview_mode(self.request)
        role, templates = selectors.get_templates_by_role(
            role_slug, include_drafts=include_drafts
        )
        ctx["role"] = role
        ctx["templates"] = templates
        ctx["total"] = templates.count()
        return ctx


class UseCaseDiscoveryView(TemplateView):
    """Use-case-driven discovery page.

    ``/templates/for-use-case/<slug>/`` · Resolves the use-case slug
    against ``USE_CASE_DISCOVERY`` and renders templates whose
    ``use_cases`` JSONField contains the slug. 404s on unknown slugs.
    """

    template_name = "catalog/use_case_discovery.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        use_case_slug = kwargs["use_case_slug"]
        include_drafts = _staff_preview_mode(self.request)
        use_case, templates = selectors.get_templates_by_use_case(
            use_case_slug, include_drafts=include_drafts
        )
        ctx["use_case"] = use_case
        ctx["templates"] = templates
        ctx["total"] = templates.count()
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

@method_decorator(xframe_options_sameorigin, name="dispatch")
class LiveTemplateView(TemplateView):
    """Render one page of a template's live multi-page preview.

    Phase A.1b (D-087): the project editor embeds this view inside an
    <iframe> on /projects/<uuid>/editor/. Django's project-wide default
    is X-Frame-Options: DENY — overriding to SAMEORIGIN on THIS view
    only keeps clickjacking protection everywhere else while letting
    the customer see their overrides render live next to the form.
    """

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        slug          = kwargs["slug"]
        category_slug = kwargs["category_slug"]
        page_slug     = kwargs.get("page", "home")
        post_slug     = kwargs.get("post_slug")

        # Tier gate (D-055). Drafts 404 on public access — authors can
        # still reach them via `?preview=1` when authenticated as staff.
        self.staff_preview = _staff_preview_mode(request)
        include_drafts = self.staff_preview
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
        #
        # D-088 (Phase A.2) adds ``?baseline=1`` which forces the catalog
        # render *without* applying the project overlay even when
        # ?project= is present. The editor before/after compare mount
        # two iframes — one with the overlay, one baseline — and slides
        # between them. Same pipeline, same skin, deterministic diff.
        project_uuid = request.GET.get("project")
        self.baseline_mode = request.GET.get("baseline") == "1"
        self.preview_project = None
        if project_uuid and not self.baseline_mode:
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
                self.preview_project, self.content, theme,
                locale=self.locale,
            )

        # Phase X.4a Step 1A · corporate-suite palette safety.
        # For archetypes that invert the paper convention (cream paper +
        # dark `--primary` reused as foreground text on paper and as the
        # filled background of navbar/KPI/footer), derive an on-primary
        # safety token and emit a UserWarning when the primary is too
        # light to be legible (CS-PAL-01). The enrichment is a no-op for
        # every other archetype.
        archetype = self.dna.get("archetype")
        if should_enrich(archetype):
            theme = enrich_corporate_suite_theme(
                theme, template_slug=self.template_obj.slug
            )

        # Phase X.4a Step 1C · corporate-suite imagery-sourcing policy.
        # Pexels-only (CS-IMG-SRC-01) is a blocking rule for every *new*
        # template on this archetype, with a documented legacy exemption
        # for the ``business-corporate`` pool (Pragma) pending retro-
        # curation. Archetype-gated so non-corporate-suite renders are
        # untouched. Emits a ``UserWarning`` on failure; never raises.
        if should_enforce_imagery(archetype):
            enforce_corporate_suite_imagery_policy(
                self.dna.get("imagery_key"),
                template_slug=self.template_obj.slug,
            )

        # Phase X.7d slice 01 · motion-gravity propagation. The DNA's
        # `motion_profile` key is an enum into `MOTION_PROFILES`; we look
        # up the per-pattern flags and surface them as flat context keys
        # so the chrome can opt patterns in/out via body classes without
        # forking layout files. Templates without a declared profile
        # default to "g3-institutional" (cluster's safe default) to keep
        # the change strictly additive on archetypes that haven't yet
        # been classified.
        motion_profile = self.dna.get("motion_profile", "g3-institutional")
        motion_config = MOTION_PROFILES.get(motion_profile, {})

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
        ctx["motion_profile"] = motion_profile
        ctx["motion_kpi_animate"] = bool(motion_config.get("kpi_animate", False))
        # Phase X.7d Causa retrofit slice 01 · two new per-pattern flags
        # surfaced as flat context keys so the chrome can opt patterns
        # in/out via body data-attributes without forking layout files.
        # See `factory/reports/hardening/causa-retrofit-slice-01.md`.
        ctx["motion_nav_condense"] = bool(motion_config.get("nav_condense_on_scroll", False))
        ctx["motion_evid5"] = bool(motion_config.get("evid5_provenance", False))

        # Blog parent page slug — used by blog_list/blog_detail chrome templates
        # so they don't have to hardcode the per-template slug ('pubblicazioni',
        # 'diario', ...). Resolved from the first page whose kind == 'blog_list'.
        ctx["blog_parent_slug"] = next(
            (p["slug"] for p in self.content["pages"] if p["kind"] == "blog_list"),
            None,
        )

        # Case-studies parent page slug — same pattern as blog_parent_slug, but
        # for templates whose home preview-band links to per-post case-study
        # detail pages. Each archetype names its case-study list page
        # differently ('case-studies' for Pragma, 'mandati' for Continua,
        # 'casi' for Solaria, 'casi-seguiti' for Fiscus, ...), so chrome must
        # not hardcode any single value.
        ctx["cases_parent_slug"] = next(
            (p["slug"] for p in self.content["pages"] if p["kind"] == "case_study_list"),
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

        # Phase X.4 Solaria Pass C — review-path legitimacy.
        # When the current request reached this draft template through the
        # staff `?preview=1` gate, internal links (nav · footer · language
        # switcher · mp-back · category-listing) used to drop the flag and
        # 404 on the next click. Exposing `staff_preview` lets the skin
        # propagate the flag on every internal href so a staff reviewer can
        # actually walk all 5 locales + 5 pages without losing access. For
        # `published_live` templates the flag is False and every href stays
        # untouched, so this is a strict superset of the prior behaviour.
        ctx["staff_preview"] = self.staff_preview
        return ctx
