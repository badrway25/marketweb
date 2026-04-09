"""Generate SVG preview images for all published templates.

Creates branded website-mockup SVGs using each template's brand palette,
then saves them as TemplateAsset records (asset_type='preview').

Each SVG looks like a browser window showing a website with the brand's
colors. Two layout variants alternate for visual variety.
"""
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from apps.catalog.models import TemplateAsset, WebTemplate


def _darken(hex_color, factor=0.7):
    """Darken a hex color by a factor (0 = black, 1 = unchanged)."""
    h = hex_color.lstrip("#")
    r = int(int(h[0:2], 16) * factor)
    g = int(int(h[2:4], 16) * factor)
    b = int(int(h[4:6], 16) * factor)
    return f"#{r:02x}{g:02x}{b:02x}"


def _alpha(hex_color, opacity):
    """Convert hex color to rgba string."""
    h = hex_color.lstrip("#")
    r = int(h[0:2], 16)
    g = int(h[2:4], 16)
    b = int(h[4:6], 16)
    return f"rgba({r},{g},{b},{opacity})"


# ---------------------------------------------------------------------------
# SVG Layout A — Split Hero (text left, visual placeholder right)
# ---------------------------------------------------------------------------
LAYOUT_SPLIT = """\
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 675" width="1200" height="675">
  <!-- Browser chrome -->
  <rect width="1200" height="32" rx="8" fill="#e2e8f0"/>
  <circle cx="22" cy="16" r="6" fill="#f87171"/>
  <circle cx="42" cy="16" r="6" fill="#fbbf24"/>
  <circle cx="62" cy="16" r="6" fill="#4ade80"/>
  <rect x="260" y="7" width="680" height="18" rx="9" fill="#f1f5f9"/>

  <!-- Navbar -->
  <rect y="32" width="1200" height="48" fill="{primary}"/>
  <rect x="40" y="46" width="90" height="20" rx="4" fill="{secondary}" opacity="0.9"/>
  <rect x="860" y="48" width="50" height="16" rx="3" fill="#fff" opacity="0.3"/>
  <rect x="926" y="48" width="50" height="16" rx="3" fill="#fff" opacity="0.3"/>
  <rect x="1060" y="42" width="100" height="28" rx="14" fill="{accent}"/>

  <!-- Hero gradient -->
  <defs>
    <linearGradient id="hg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{primary}"/>
      <stop offset="100%" stop-color="{primary_dark}"/>
    </linearGradient>
  </defs>
  <rect y="80" width="1200" height="280" fill="url(#hg)"/>

  <!-- Hero text (left side) -->
  <rect x="80" y="130" width="340" height="26" rx="4" fill="#fff" opacity="0.92"/>
  <rect x="80" y="168" width="280" height="14" rx="3" fill="#fff" opacity="0.45"/>
  <rect x="80" y="192" width="240" height="14" rx="3" fill="#fff" opacity="0.35"/>
  <rect x="80" y="232" width="130" height="38" rx="8" fill="{accent}"/>
  <rect x="228" y="232" width="110" height="38" rx="8" fill="none" stroke="rgba(255,255,255,0.35)" stroke-width="1.5"/>

  <!-- Hero visual (right side) — device frame -->
  <rect x="580" y="108" width="540" height="230" rx="12" fill="rgba(255,255,255,0.07)" stroke="rgba(255,255,255,0.12)" stroke-width="1"/>
  <rect x="600" y="124" width="500" height="10" rx="5" fill="rgba(255,255,255,0.12)"/>
  <rect x="600" y="148" width="500" height="172" rx="6" fill="rgba(255,255,255,0.05)"/>
  <rect x="620" y="164" width="200" height="16" rx="3" fill="rgba(255,255,255,0.15)"/>
  <rect x="620" y="190" width="160" height="10" rx="3" fill="rgba(255,255,255,0.08)"/>
  <rect x="620" y="230" width="80" height="26" rx="6" fill="{accent_alpha}"/>
  <rect x="860" y="164" width="220" height="130" rx="8" fill="rgba(255,255,255,0.08)"/>

  <!-- Content section title -->
  <rect x="460" y="388" width="280" height="22" rx="4" fill="{primary}" opacity="0.12"/>
  <rect x="490" y="390" width="220" height="18" rx="3" fill="{primary}" opacity="0.65"/>

  <!-- Three content cards -->
  <rect x="80" y="430" width="320" height="190" rx="12" fill="#fff" stroke="#e2e8f0" stroke-width="1"/>
  <rect x="80" y="430" width="320" height="90" rx="12" fill="{secondary}" opacity="0.07"/>
  <rect x="80" y="514" width="320" height="6" fill="#fff"/>
  <rect x="100" y="536" width="170" height="14" rx="3" fill="{primary}" opacity="0.55"/>
  <rect x="100" y="560" width="130" height="10" rx="3" fill="#94a3b8" opacity="0.5"/>
  <rect x="100" y="588" width="70" height="22" rx="6" fill="{secondary}" opacity="0.12"/>

  <rect x="440" y="430" width="320" height="190" rx="12" fill="#fff" stroke="#e2e8f0" stroke-width="1"/>
  <rect x="440" y="430" width="320" height="90" rx="12" fill="{secondary}" opacity="0.07"/>
  <rect x="440" y="514" width="320" height="6" fill="#fff"/>
  <rect x="460" y="536" width="170" height="14" rx="3" fill="{primary}" opacity="0.55"/>
  <rect x="460" y="560" width="130" height="10" rx="3" fill="#94a3b8" opacity="0.5"/>
  <rect x="460" y="588" width="70" height="22" rx="6" fill="{secondary}" opacity="0.12"/>

  <rect x="800" y="430" width="320" height="190" rx="12" fill="#fff" stroke="#e2e8f0" stroke-width="1"/>
  <rect x="800" y="430" width="320" height="90" rx="12" fill="{secondary}" opacity="0.07"/>
  <rect x="800" y="514" width="320" height="6" fill="#fff"/>
  <rect x="820" y="536" width="170" height="14" rx="3" fill="{primary}" opacity="0.55"/>
  <rect x="820" y="560" width="130" height="10" rx="3" fill="#94a3b8" opacity="0.5"/>
  <rect x="820" y="588" width="70" height="22" rx="6" fill="{secondary}" opacity="0.12"/>

  <!-- Footer -->
  <rect y="640" width="1200" height="35" fill="{primary}"/>
  <rect x="40" y="650" width="80" height="14" rx="3" fill="#fff" opacity="0.25"/>
  <rect x="1040" y="650" width="120" height="14" rx="3" fill="#fff" opacity="0.15"/>
</svg>"""


# ---------------------------------------------------------------------------
# SVG Layout B — Centered Hero (full-width, text centered)
# ---------------------------------------------------------------------------
LAYOUT_CENTERED = """\
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 675" width="1200" height="675">
  <!-- Browser chrome -->
  <rect width="1200" height="32" rx="8" fill="#e2e8f0"/>
  <circle cx="22" cy="16" r="6" fill="#f87171"/>
  <circle cx="42" cy="16" r="6" fill="#fbbf24"/>
  <circle cx="62" cy="16" r="6" fill="#4ade80"/>
  <rect x="260" y="7" width="680" height="18" rx="9" fill="#f1f5f9"/>

  <!-- Navbar -->
  <rect y="32" width="1200" height="48" fill="{primary}"/>
  <rect x="40" y="46" width="90" height="20" rx="4" fill="{secondary}" opacity="0.9"/>
  <rect x="860" y="48" width="50" height="16" rx="3" fill="#fff" opacity="0.3"/>
  <rect x="926" y="48" width="50" height="16" rx="3" fill="#fff" opacity="0.3"/>
  <rect x="1060" y="42" width="100" height="28" rx="14" fill="{accent}"/>

  <!-- Hero gradient -->
  <defs>
    <linearGradient id="hg" x1="0" y1="0" x2="0.5" y2="1">
      <stop offset="0%" stop-color="{primary_dark}"/>
      <stop offset="100%" stop-color="{primary}"/>
    </linearGradient>
  </defs>
  <rect y="80" width="1200" height="260" fill="url(#hg)"/>

  <!-- Centered hero text -->
  <rect x="360" y="130" width="480" height="28" rx="4" fill="#fff" opacity="0.92"/>
  <rect x="400" y="170" width="400" height="14" rx="3" fill="#fff" opacity="0.45"/>
  <rect x="430" y="194" width="340" height="14" rx="3" fill="#fff" opacity="0.35"/>
  <rect x="480" y="234" width="120" height="38" rx="8" fill="{accent}"/>
  <rect x="616" y="234" width="100" height="38" rx="8" fill="none" stroke="rgba(255,255,255,0.35)" stroke-width="1.5"/>

  <!-- Feature/stats bar -->
  <rect y="340" width="1200" height="60" fill="{secondary}" opacity="0.06"/>
  <rect x="120" y="358" width="80" height="24" rx="4" fill="{secondary}" opacity="0.15"/>
  <rect x="220" y="363" width="100" height="14" rx="3" fill="{primary}" opacity="0.35"/>
  <rect x="440" y="358" width="80" height="24" rx="4" fill="{secondary}" opacity="0.15"/>
  <rect x="540" y="363" width="100" height="14" rx="3" fill="{primary}" opacity="0.35"/>
  <rect x="760" y="358" width="80" height="24" rx="4" fill="{secondary}" opacity="0.15"/>
  <rect x="860" y="363" width="100" height="14" rx="3" fill="{primary}" opacity="0.35"/>

  <!-- Two-column content -->
  <rect x="80" y="424" width="520" height="180" rx="12" fill="#fff" stroke="#e2e8f0" stroke-width="1"/>
  <rect x="80" y="424" width="520" height="80" rx="12" fill="{secondary}" opacity="0.06"/>
  <rect x="80" y="500" width="520" height="4" fill="#fff"/>
  <rect x="104" y="518" width="240" height="16" rx="3" fill="{primary}" opacity="0.6"/>
  <rect x="104" y="544" width="460" height="10" rx="3" fill="#94a3b8" opacity="0.4"/>
  <rect x="104" y="564" width="380" height="10" rx="3" fill="#94a3b8" opacity="0.3"/>

  <rect x="640" y="424" width="480" height="180" rx="12" fill="#fff" stroke="#e2e8f0" stroke-width="1"/>
  <rect x="640" y="424" width="480" height="80" rx="12" fill="{secondary}" opacity="0.06"/>
  <rect x="640" y="500" width="480" height="4" fill="#fff"/>
  <rect x="664" y="518" width="240" height="16" rx="3" fill="{primary}" opacity="0.6"/>
  <rect x="664" y="544" width="420" height="10" rx="3" fill="#94a3b8" opacity="0.4"/>
  <rect x="664" y="564" width="340" height="10" rx="3" fill="#94a3b8" opacity="0.3"/>

  <!-- Footer -->
  <rect y="640" width="1200" height="35" fill="{primary}"/>
  <rect x="40" y="650" width="80" height="14" rx="3" fill="#fff" opacity="0.25"/>
  <rect x="1040" y="650" width="120" height="14" rx="3" fill="#fff" opacity="0.15"/>
</svg>"""


LAYOUTS = [LAYOUT_SPLIT, LAYOUT_CENTERED]


def _generate_svg(template, index):
    """Generate an SVG preview for a template using its brand palette."""
    brand = template.brand
    palette = brand.palette or {}
    primary = palette.get("primary", "#1B2A4A")
    secondary = palette.get("secondary", "#6366F1")
    accent = palette.get("accent", "#F59E0B")
    primary_dark = _darken(primary, 0.65)
    accent_alpha = _alpha(accent, 0.6)

    layout = LAYOUTS[index % 2]
    return layout.format(
        primary=primary,
        primary_dark=primary_dark,
        secondary=secondary,
        accent=accent,
        accent_alpha=accent_alpha,
    )


class Command(BaseCommand):
    help = "Generate SVG preview images for all published templates"

    def add_arguments(self, parser):
        parser.add_argument(
            "--force",
            action="store_true",
            help="Regenerate even if a preview asset already exists",
        )

    def handle(self, *args, **options):
        force = options["force"]
        templates = (
            WebTemplate.objects.filter(status=WebTemplate.Status.PUBLISHED)
            .select_related("category", "brand")
            .order_by("category__order", "order")
        )

        if not templates.exists():
            self.stderr.write(self.style.ERROR("No published templates found. Run seed_templates first."))
            return

        created = 0
        skipped = 0

        for idx, template in enumerate(templates):
            if not hasattr(template, "brand"):
                self.stderr.write(f"  Skipping {template.name} — no brand")
                skipped += 1
                continue

            existing = template.assets.filter(asset_type=TemplateAsset.AssetType.PREVIEW)
            if existing.exists() and not force:
                self.stdout.write(f"  Exists:  {template.name}")
                skipped += 1
                continue

            if force:
                existing.delete()

            svg_content = _generate_svg(template, idx)
            asset = TemplateAsset(
                template=template,
                asset_type=TemplateAsset.AssetType.PREVIEW,
                alt_text=f"Anteprima del template {template.name}",
                order=0,
            )
            filename = f"{template.slug}-preview.svg"
            asset.file.save(filename, ContentFile(svg_content.encode("utf-8")))
            # .save() on FileField also saves the model instance

            created += 1
            self.stdout.write(f"  Created: {template.name} -> {asset.file.name}")

        self.stdout.write(
            self.style.SUCCESS(f"\nDone. {created} previews created, {skipped} skipped.")
        )
