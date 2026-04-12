"""Generate realistic preview images for all published templates.

Pipeline:
  1. Ensure category-appropriate stock imagery is cached on disk.
  2. Render a per-category HTML composition (templates/preview_compositions/<category>.html)
     using the template's brand palette + cached imagery.
  3. Screenshot the rendered HTML at 1600x900 with Playwright (Chromium).
  4. Save the resulting PNG as a TemplateAsset (asset_type='preview').

The TemplateAsset pipeline is unchanged: each template still has a single
preview asset; only the file format has moved from SVG wireframe to PNG
screenshot of a real homepage mockup.
"""
from __future__ import annotations

import tempfile
from pathlib import Path

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from django.template.loader import render_to_string

from apps.catalog.models import TemplateAsset, WebTemplate
from apps.catalog.preview_imagery import ensure_cached
from apps.catalog.template_dna import get_dna


# Legacy per-category compositions. Used for any template that does NOT
# have a DNA entry in `apps.catalog.template_dna.TEMPLATE_DNA`. As more
# categories migrate to per-template archetypes, these become safety nets.
CATEGORY_TO_COMPOSITION: dict[str, str] = {
    "restaurant": "restaurant.html",
    "medical": "medical.html",
    "lawyer": "lawyer.html",
    "agency": "agency.html",
    "business": "business.html",
    "real-estate": "real-estate.html",
    "portfolio": "portfolio.html",
    "ecommerce": "ecommerce.html",
}


def _resolve_composition(template: WebTemplate, dna: dict | None) -> str:
    """Pick the HTML composition path for a given template.

    With ``preview_archetype``: use that instead of ``archetype`` — allows
    two templates sharing a live archetype (e.g. specialist) to render
    visually distinct preview compositions.
    With DNA: ``preview_compositions/<category>/<archetype>.html``
    Without:  ``preview_compositions/<category>.html`` (legacy fallback)
    """
    if dna:
        arch = dna.get("preview_archetype") or dna.get("archetype")
        if arch:
            return f"preview_compositions/{template.category.slug}/{arch}.html"
    fallback = CATEGORY_TO_COMPOSITION.get(template.category.slug, "agency.html")
    return f"preview_compositions/{fallback}"


# Heading + body Google Font pairings derived from the brand's typography
# string. Best-effort match — anything we don't recognise falls back to
# Plus Jakarta Sans + Inter.
FONT_PAIRINGS: dict[str, tuple[str, str]] = {
    "playfair display + lato": ("Playfair Display", "Lato"),
    "libre baskerville + source sans 3": ("Libre Baskerville", "Source Sans 3"),
    "libre baskerville + nunito sans": ("Libre Baskerville", "Nunito Sans"),
    "nunito sans + inter": ("Nunito Sans", "Inter"),
    "cormorant garamond + nunito": ("Cormorant Garamond", "Nunito"),
    "cormorant garamond + inter": ("Cormorant Garamond", "Inter"),
    "cormorant garamond + montserrat": ("Cormorant Garamond", "Montserrat"),
    "dm sans + inter": ("DM Sans", "Inter"),
    "poppins + inter": ("Poppins", "Inter"),
    "inter + merriweather": ("Inter", "Merriweather"),
    "satoshi + inter": ("Manrope", "Inter"),  # Satoshi is paid; Manrope is the closest free swap
    "space grotesk + inter": ("Space Grotesk", "Inter"),
    "plus jakarta sans + inter": ("Plus Jakarta Sans", "Inter"),
    "syne + inter": ("Syne", "Inter"),
    "archivo + inter": ("Archivo", "Inter"),
}
DEFAULT_FONTS = ("Plus Jakarta Sans", "Inter")


def _hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
    h = hex_color.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)


def _darken(hex_color: str, factor: float = 0.65) -> str:
    r, g, b = _hex_to_rgb(hex_color)
    return f"#{int(r*factor):02x}{int(g*factor):02x}{int(b*factor):02x}"


def _luminance(hex_color: str) -> float:
    """Relative luminance per WCAG (rough)."""
    r, g, b = _hex_to_rgb(hex_color)
    return (0.2126 * r + 0.7152 * g + 0.0722 * b) / 255.0


def _on_color(hex_color: str) -> str:
    """Return contrasting text color (black or white) for a background."""
    return "#0f172a" if _luminance(hex_color) > 0.6 else "#ffffff"


def _resolve_fonts(typography: str) -> tuple[str, str]:
    if not typography:
        return DEFAULT_FONTS
    return FONT_PAIRINGS.get(typography.strip().lower(), DEFAULT_FONTS)


def _build_context(
    template: WebTemplate,
    image_uris: list[str],
    dna: dict | None = None,
) -> dict:
    brand = template.brand
    palette = brand.palette or {}
    primary = palette.get("primary", "#1B2A4A")
    secondary = palette.get("secondary", "#6366F1")
    accent = palette.get("accent", "#F59E0B")

    # DNA's font_pairing wins over brand.typography string parsing — the
    # registry is the source of truth for templates that have one.
    if dna and "font_pairing" in dna:
        heading_font, body_font = dna["font_pairing"]
    else:
        heading_font, body_font = _resolve_fonts(brand.typography)

    # Pad the imagery list so {{ imagery.5 }} never blows up if a download
    # failed: fall back to the wide hero for missing slots.
    safe_imagery = list(image_uris)
    while len(safe_imagery) < 6 and safe_imagery:
        safe_imagery.append(safe_imagery[0])

    return {
        "template": template,
        "brand_name": brand.brand_name,
        "tagline": brand.tagline or "",
        "hero_subtitle": template.short_description or brand.tagline or "",
        "primary": primary,
        "primary_dark": _darken(primary, 0.6),
        "secondary": secondary,
        "accent": accent,
        "on_primary": _on_color(primary),
        "imagery": safe_imagery,
        "heading_font": heading_font,
        "body_font": body_font,
        # Per-template DNA — None for legacy templates without an entry.
        "dna": dna,
    }


class Command(BaseCommand):
    help = "Generate realistic PNG preview images via HTML compositions + Playwright screenshots"

    def add_arguments(self, parser):
        parser.add_argument(
            "--force",
            action="store_true",
            help="Regenerate even if a preview asset already exists",
        )
        parser.add_argument(
            "--only",
            metavar="SLUG",
            help="Regenerate only the template with this slug",
        )

    def handle(self, *args, **options):
        force = options["force"]
        only_slug = options.get("only")

        templates_qs = (
            WebTemplate.objects.filter(status=WebTemplate.Status.PUBLISHED)
            .select_related("category", "brand")
            .order_by("category__order", "order")
        )
        if only_slug:
            templates_qs = templates_qs.filter(slug=only_slug)

        # Materialise the list NOW. Once we enter sync_playwright() the
        # event loop owns the thread and the ORM raises SynchronousOnlyOperation.
        templates = list(templates_qs)
        if not templates:
            self.stderr.write(self.style.ERROR("No published templates found. Run seed_templates first."))
            return

        # Pre-warm the imagery cache. Each template may pull from a different
        # imagery key — DNA can override the default `category.slug` lookup so
        # sibling templates use distinct photo pools (e.g. medical-family vs
        # medical-specialist).
        imagery_keys_needed: set[str] = set()
        for t in templates:
            dna = get_dna(t.slug)
            imagery_keys_needed.add(
                (dna or {}).get("imagery_key", t.category.slug)
            )
        self.stdout.write(self.style.MIGRATE_HEADING("Caching stock imagery..."))
        imagery_by_key: dict[str, list[str]] = {}
        for key in sorted(imagery_keys_needed):
            paths = ensure_cached(key)
            imagery_by_key[key] = [p.resolve().as_uri() for p in paths]
            self.stdout.write(f"  {key}: {len(paths)} images")

        # Decide up front which templates we will (re)render and which we
        # will skip. Render the HTML for each survivor while the ORM is
        # still safe to use.
        jobs: list[dict] = []  # list of {template, html, filename}
        skipped = 0
        for template in templates:
            if not hasattr(template, "brand"):
                self.stderr.write(f"  Skip (no brand): {template.name}")
                skipped += 1
                continue
            existing = template.assets.filter(asset_type=TemplateAsset.AssetType.PREVIEW)
            if existing.exists() and not force:
                self.stdout.write(f"  Exists: {template.name}")
                skipped += 1
                continue
            if force and existing.exists():
                existing.delete()

            dna = get_dna(template.slug)
            composition_path = _resolve_composition(template, dna)
            imagery_key = (dna or {}).get("imagery_key", template.category.slug)
            html = render_to_string(
                composition_path,
                _build_context(
                    template,
                    imagery_by_key.get(imagery_key, []),
                    dna=dna,
                ),
            )
            archetype_label = (dna or {}).get("archetype", "legacy")
            jobs.append({
                "template": template,
                "html": html,
                "filename": f"{template.slug}-preview.png",
                "archetype": archetype_label,
            })

        if not jobs:
            self.stdout.write(self.style.SUCCESS(f"Nothing to do. {skipped} skipped."))
            return

        # ---- Phase 2: Playwright screenshots (no ORM access inside) ----
        from playwright.sync_api import sync_playwright  # local import

        self.stdout.write(self.style.MIGRATE_HEADING(f"\nRendering {len(jobs)} previews via Playwright..."))
        screenshots: list[tuple[str, bytes]] = []  # (filename, png_bytes)

        with sync_playwright() as pw:
            browser = pw.chromium.launch(headless=True)
            context = browser.new_context(
                viewport={"width": 1600, "height": 900},
                device_scale_factor=2,
            )
            page = context.new_page()
            try:
                for job in jobs:
                    with tempfile.NamedTemporaryFile(
                        mode="w", suffix=".html", delete=False, encoding="utf-8"
                    ) as tmp:
                        tmp.write(job["html"])
                        tmp_path = Path(tmp.name)
                    try:
                        page.goto(tmp_path.resolve().as_uri(), wait_until="networkidle")
                        page.wait_for_timeout(450)  # let webfonts swap
                        png_bytes = page.screenshot(
                            type="png",
                            clip={"x": 0, "y": 0, "width": 1600, "height": 900},
                        )
                    finally:
                        try:
                            tmp_path.unlink()
                        except OSError:
                            pass
                    screenshots.append((job["filename"], png_bytes))
                    self.stdout.write(
                        f"  Rendered [{job['archetype']}]: {job['template'].name}"
                    )
            finally:
                context.close()
                browser.close()

        # ---- Phase 3: Persist TemplateAsset rows ----
        created = 0
        for job, (filename, png_bytes) in zip(jobs, screenshots):
            template = job["template"]
            asset = TemplateAsset(
                template=template,
                asset_type=TemplateAsset.AssetType.PREVIEW,
                alt_text=f"Anteprima del template {template.name}",
                order=0,
            )
            asset.file.save(filename, ContentFile(png_bytes))
            created += 1
            self.stdout.write(self.style.SUCCESS(
                f"  Saved: {template.name} -> {asset.file.name}"
            ))

        self.stdout.write(self.style.SUCCESS(
            f"\nDone. {created} previews created, {skipped} skipped."
        ))
