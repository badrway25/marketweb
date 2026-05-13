"""T43 · Django Sitemaps for the public marketplace surface.

Three sitemap sections, joined into /sitemap.xml via the registry in
``marketweb/urls.py``:

  - StaticSitemap     · 2 fixed routes (home, master template listing)
  - CategorySitemap   · one URL per Category that has ≥1 published template
  - TemplateSitemap   · one URL per ``WebTemplate(tier=published_live)``

Excluded (deliberately — must NOT appear in the index):
  - Preview URLs (``/templates/<cat>/<slug>/preview/``): they are
    duplicate content of the detail page from a search-engine
    perspective. The ``LiveTemplateView`` sets
    ``X-Robots-Tag: noindex, follow`` so even if a crawler discovers
    a preview link in the wild, it does not get indexed.
  - Draft / unpublished templates: ``tier != published_live``.
  - Discovery surfaces (clusters / roles / use-cases): these are
    derived navigation overlays — out of T43 scope to avoid
    duplicate-content risk vs the canonical category listings.
  - All private surfaces (admin, accounts, editor, projects, api).

Last-modified
-------------
``WebTemplate.updated_at`` (TimestampedModel) is the source of truth
for ``lastmod`` on detail entries. Static + category entries do not
emit ``lastmod`` because there is no reliable signal at that level
(the master listing changes when ANY template changes, but pegging
that to "now" would invalidate the sitemap on every fetch).
"""
from __future__ import annotations

from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from apps.catalog.models import Category, WebTemplate


class StaticSitemap(Sitemap):
    """Fixed marketplace routes — home + master template listing."""

    priority = 0.9
    changefreq = "weekly"

    def items(self) -> list[str]:
        return ["pages:home", "catalog:template_list", "catalog:category_list"]

    def location(self, item: str) -> str:
        return reverse(item)


class CategorySitemap(Sitemap):
    """One URL per category that currently has at least one published
    template. Categories that ship zero published templates are
    excluded — they would 200-render an empty listing, which is
    duplicate-style thin content that hurts crawl budget."""

    priority = 0.7
    changefreq = "weekly"

    def items(self) -> list[Category]:
        # `tier` lives on WebTemplate, not on Category — filter via
        # the reverse relation (Category → WebTemplate uses
        # related_name="templates", see apps/catalog/models.py).
        # ``distinct()`` avoids one row per template within the same
        # category.
        return list(
            Category.objects.filter(
                templates__tier=WebTemplate.Tier.PUBLISHED_LIVE,
            )
            .distinct()
            .order_by("slug")
        )

    def location(self, obj: Category) -> str:
        return reverse(
            "catalog:template_list_by_category",
            kwargs={"category_slug": obj.slug},
        )


class TemplateSitemap(Sitemap):
    """One URL per published template detail page. The detail page
    is the canonical sales surface for each template — preview URLs
    are noindex (set via X-Robots-Tag in ``LiveTemplateView``)."""

    priority = 0.8
    changefreq = "monthly"

    def items(self) -> list[WebTemplate]:
        return list(
            WebTemplate.objects.filter(tier=WebTemplate.Tier.PUBLISHED_LIVE)
            .select_related("category")
            .order_by("category__slug", "slug")
        )

    def location(self, obj: WebTemplate) -> str:
        return reverse(
            "catalog:template_detail",
            kwargs={"category_slug": obj.category.slug, "slug": obj.slug},
        )

    def lastmod(self, obj: WebTemplate):
        """``WebTemplate.updated_at`` from TimestampedModel — fires on
        every save, so it tracks content edits driven through admin or
        a future content-CMS write path. Returns None silently if the
        attribute is missing (defensive — TimestampedModel is the
        abstract parent, but a future override could remove it)."""
        return getattr(obj, "updated_at", None)


#: Registry consumed by ``django.contrib.sitemaps.views.sitemap`` in
#: ``marketweb/urls.py``. Keys are URL fragments inside the
#: sitemap-index; values are the Sitemap classes that produce a
#: nested sitemap.xml. Keeping each section addressable separately
#: (rather than rolling all rows into one massive sitemap) makes the
#: Search Console error reports actionable — a templates-only crawl
#: error doesn't taint the static-pages section.
SITEMAPS: dict[str, type[Sitemap]] = {
    "static":     StaticSitemap,
    "categories": CategorySitemap,
    "templates":  TemplateSitemap,
}
