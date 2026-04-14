"""Live-template i18n/RTL pilot infrastructure (Phase 2i.1 — Session 23).

This module is the single source of truth for the i18n/RTL pilot that
validates multilingual publishing for `tier=published_live` templates.
It is deliberately scoped to the live-template preview surface — NOT
the marketplace chrome (listing, detail, homepage), which stays in
Italian per the product's primary-market framing.

Why NOT Django {% trans %} + .po files for the pilot
-----------------------------------------------------
- Django gettext requires compiled .mo files, which needs a `gettext`
  binary on the dev box (Windows-flaky). Every content change becomes
  a build step.
- Every string in our live templates already lives inside a Python
  content registry keyed by template slug. Splitting strings across
  two files (.po + content dict) doubles the review surface.
- The pilot's job is to prove the *shape* of multilingual publishing
  for a premium marketplace; a locale-keyed dict is the smallest shape
  that delivers real localization + RTL + fallback + switcher without
  introducing new build tooling. When Phase 4 promotes this to the
  marketplace chrome itself we can migrate to {% trans %} per-locale
  and the content authoring process stays unchanged because every
  string is already namespaced by locale.

Shape
-----
- `SUPPORTED_LOCALES`: the 5 target languages for the pilot.
- `DEFAULT_LOCALE`: `it`. Italian stays the authoritative source.
- `RTL_LOCALES`: `{"ar"}`. Drives `<html dir="rtl">` + RTL CSS.
- `LOCALE_LABELS`: human-readable names for the language switcher.
- `CHROME_I18N`: labels the specialist skin itself renders (marketplace
  bar, footer section headers, form field labels, blog read-more link,
  etc.). Structured as `locale → key → string`. Any skin adopting the
  pilot reuses this dict — it is archetype-agnostic.
- `resolve_locale(request)`: reads `?lang=xx` and validates.
- `get_chrome(locale)`: returns the chrome dict for a locale, with
  IT fallback on missing keys.
- `is_rtl(locale)`: boolean.
- `html_dir(locale)`: `"rtl"` or `"ltr"`.
- `pick_localized(content_by_locale, locale)`: returns the locale-
  specific content block, falling back to IT if missing. Used by the
  template_content helpers.

Adding a language (future rollout)
----------------------------------
1. Add its code to `SUPPORTED_LOCALES`.
2. Add its entry to `LOCALE_LABELS`.
3. Add a full key block to `CHROME_I18N` (copy IT, translate every key).
4. If RTL, add to `RTL_LOCALES` and add the font stack to the skin's
   `_base.html` font loader.
5. For each `tier=published_live` template whose content has been
   localized, add a locale block to its entry in `template_content.py`.
   Templates without the new locale fall back to IT automatically.
"""
from __future__ import annotations

from typing import Any

from django.http import HttpRequest


# ---------------------------------------------------------------------------
# Locale metadata
# ---------------------------------------------------------------------------

DEFAULT_LOCALE = "it"

#: The 5 locales validated in the Phase 2i.1 pilot. Order matches the
#: language switcher display order.
SUPPORTED_LOCALES: tuple[str, ...] = ("it", "en", "fr", "es", "ar")

#: Locales that render right-to-left. Drives `dir="rtl"` + RTL CSS.
RTL_LOCALES: frozenset[str] = frozenset({"ar"})

#: Human-readable native names for the language switcher.
LOCALE_LABELS: dict[str, str] = {
    "it": "Italiano",
    "en": "English",
    "fr": "Français",
    "es": "Español",
    "ar": "العربية",
}

#: 2-letter ISO codes displayed as compact badges in the switcher.
LOCALE_BADGES: dict[str, str] = {
    "it": "IT",
    "en": "EN",
    "fr": "FR",
    "es": "ES",
    "ar": "AR",
}


# ---------------------------------------------------------------------------
# Chrome strings — the labels the specialist skin itself renders.
# Organized flat by locale so a reviewer can scan one language end-to-end.
# Keys are stable; values change per locale. Skin templates read via
# `{{ chrome.key_name }}`. Missing keys fall back to Italian at render time.
# ---------------------------------------------------------------------------

CHROME_I18N: dict[str, dict[str, str]] = {
    # ─────────────────────────────────────────────────────────────
    # ITALIAN — authoritative source, do not change without rereview
    # ─────────────────────────────────────────────────────────────
    "it": {
        # Marketplace bar (top of live preview)
        "mp_back":          "← Torna a MarketWeb",
        "mp_preview_of":    "Anteprima completa",
        "mp_other":         "Altri template medicali →",
        "mp_other_restaurant": "Altri template ristoranti →",
        "mp_other_business": "Altri template business →",
        "mp_other_portfolio": "Altri portfolio →",
        "mp_language":      "Lingua",
        # Footer section headings
        "foot_studio":      "Lo studio",
        "foot_pages":       "Pagine",
        "foot_contact":     "Contatti",
        "foot_hours":       "Orari",
        "foot_privacy":     "Privacy",
        "foot_cookie":      "Cookie",
        "foot_legal":       "Note legali",
        # Restaurant footer headings
        "foot_restaurant":  "Il ristorante",
        "foot_concierge":   "Concierge",
        "foot_services":    "Servizi",
        # Home links to other pages
        "home_all_doctors": "Tutti i medici",
        "home_publications":"Pubblicazioni",
        # Contact page form labels
        "form_name":        "Nome",
        "form_surname":     "Cognome",
        "form_email":       "Email",
        "form_phone":       "Telefono",
        "form_subject":     "Oggetto",
        "form_message":     "Messaggio",
        "form_submit":      "Invia messaggio",
        # Appointment alt link
        "apt_alternative_prefix": "In alternativa:",
        "apt_alternative_link":   "parla con la segreteria",
        # Blog list
        "blog_read_full":   "Leggi l'articolo completo",
        "blog_read_article":"Leggi l'articolo",
        # Blog detail
        "blog_read_minutes":"min di lettura",
        "blog_back_all_prefix": "← Tutte le",
        "blog_crumb_sep":   "/",
        # Restaurant-specific chrome
        "fd_wine_pairing":  "In abbinamento",
        "fd_email_label":   "Email",
        "fd_phone_label":   "Telefono",
        # Premium forms primitives (Session 33)
        "form_required":    "Richiesto",
        "form_optional":    "Facoltativo",
        "form_select_placeholder": "Seleziona…",
        "form_upload_browse_prefix": "Trascina un file qui oppure",
        "form_upload_browse_link":   "sfoglia i documenti",
        "form_upload_remove":        "Rimuovi",
    },

    # ─────────────────────────────────────────────────────────────
    # ENGLISH
    # ─────────────────────────────────────────────────────────────
    "en": {
        "mp_back":          "← Back to MarketWeb",
        "mp_preview_of":    "Full preview",
        "mp_other":         "More medical templates →",
        "mp_other_restaurant": "More restaurant templates →",
        "mp_other_business": "More business templates →",
        "mp_other_portfolio": "More portfolio templates →",
        "mp_language":      "Language",
        "foot_studio":      "The practice",
        "foot_pages":       "Pages",
        "foot_contact":     "Contact",
        "foot_hours":       "Hours",
        "foot_privacy":     "Privacy",
        "foot_cookie":      "Cookies",
        "foot_legal":       "Legal notes",
        "foot_restaurant":  "The restaurant",
        "foot_concierge":   "Concierge",
        "foot_services":    "Service",
        "home_all_doctors": "Meet the team",
        "home_publications":"Publications",
        "form_name":        "First name",
        "form_surname":     "Last name",
        "form_email":       "Email",
        "form_phone":       "Phone",
        "form_subject":     "Subject",
        "form_message":     "Message",
        "form_submit":      "Send message",
        "apt_alternative_prefix": "Or:",
        "apt_alternative_link":   "speak with the front desk",
        "blog_read_full":   "Read the full article",
        "blog_read_article":"Read the article",
        "blog_read_minutes":"min read",
        "blog_back_all_prefix": "← All",
        "blog_crumb_sep":   "/",
        "fd_wine_pairing":  "Paired with",
        "fd_email_label":   "Email",
        "fd_phone_label":   "Phone",
        "form_required":    "Required",
        "form_optional":    "Optional",
        "form_select_placeholder": "Select…",
        "form_upload_browse_prefix": "Drag a file here or",
        "form_upload_browse_link":   "browse your documents",
        "form_upload_remove":        "Remove",
    },

    # ─────────────────────────────────────────────────────────────
    # FRENCH
    # ─────────────────────────────────────────────────────────────
    "fr": {
        "mp_back":          "← Retour à MarketWeb",
        "mp_preview_of":    "Aperçu complet",
        "mp_other":         "Autres modèles médicaux →",
        "mp_other_restaurant": "Autres modèles de restaurant →",
        "mp_other_business": "Autres modèles business →",
        "mp_other_portfolio": "Autres portfolios →",
        "mp_language":      "Langue",
        "foot_studio":      "Le cabinet",
        "foot_pages":       "Pages",
        "foot_contact":     "Contact",
        "foot_hours":       "Horaires",
        "foot_privacy":     "Confidentialité",
        "foot_cookie":      "Cookies",
        "foot_legal":       "Mentions légales",
        "foot_restaurant":  "Le restaurant",
        "foot_concierge":   "Concierge",
        "foot_services":    "Service",
        "home_all_doctors": "Toute l'équipe",
        "home_publications":"Publications",
        "form_name":        "Prénom",
        "form_surname":     "Nom",
        "form_email":       "E-mail",
        "form_phone":       "Téléphone",
        "form_subject":     "Sujet",
        "form_message":     "Message",
        "form_submit":      "Envoyer le message",
        "apt_alternative_prefix": "Ou bien :",
        "apt_alternative_link":   "écrivez au secrétariat",
        "blog_read_full":   "Lire l'article complet",
        "blog_read_article":"Lire l'article",
        "blog_read_minutes":"min de lecture",
        "blog_back_all_prefix": "← Toutes les",
        "blog_crumb_sep":   "/",
        "fd_wine_pairing":  "Accord mets-vin",
        "fd_email_label":   "E-mail",
        "fd_phone_label":   "Téléphone",
        "form_required":    "Requis",
        "form_optional":    "Facultatif",
        "form_select_placeholder": "Sélectionner…",
        "form_upload_browse_prefix": "Glissez un fichier ici ou",
        "form_upload_browse_link":   "parcourez vos documents",
        "form_upload_remove":        "Retirer",
    },

    # ─────────────────────────────────────────────────────────────
    # SPANISH
    # ─────────────────────────────────────────────────────────────
    "es": {
        "mp_back":          "← Volver a MarketWeb",
        "mp_preview_of":    "Vista previa completa",
        "mp_other":         "Más plantillas médicas →",
        "mp_other_restaurant": "Más plantillas de restaurante →",
        "mp_other_business": "Más plantillas business →",
        "mp_other_portfolio": "Más portfolios →",
        "mp_language":      "Idioma",
        "foot_studio":      "La consulta",
        "foot_pages":       "Páginas",
        "foot_contact":     "Contacto",
        "foot_hours":       "Horario",
        "foot_privacy":     "Privacidad",
        "foot_cookie":      "Cookies",
        "foot_legal":       "Aviso legal",
        "foot_restaurant":  "El restaurante",
        "foot_concierge":   "Concierge",
        "foot_services":    "Servicio",
        "home_all_doctors": "Todo el equipo",
        "home_publications":"Publicaciones",
        "form_name":        "Nombre",
        "form_surname":     "Apellidos",
        "form_email":       "Correo electrónico",
        "form_phone":       "Teléfono",
        "form_subject":     "Asunto",
        "form_message":     "Mensaje",
        "form_submit":      "Enviar mensaje",
        "apt_alternative_prefix": "Alternativa:",
        "apt_alternative_link":   "hable con la secretaría",
        "blog_read_full":   "Leer el artículo completo",
        "blog_read_article":"Leer el artículo",
        "blog_read_minutes":"min de lectura",
        "blog_back_all_prefix": "← Todas las",
        "blog_crumb_sep":   "/",
        "fd_wine_pairing":  "Maridaje",
        "fd_email_label":   "Correo",
        "fd_phone_label":   "Teléfono",
        "form_required":    "Obligatorio",
        "form_optional":    "Opcional",
        "form_select_placeholder": "Seleccionar…",
        "form_upload_browse_prefix": "Arrastra un archivo aquí o",
        "form_upload_browse_link":   "busca en tus documentos",
        "form_upload_remove":        "Quitar",
    },

    # ─────────────────────────────────────────────────────────────
    # ARABIC (RTL) — strings localized, layout flips via html[dir="rtl"] CSS
    # Arrows adapted to RTL reading direction where they're directional cues.
    # ─────────────────────────────────────────────────────────────
    "ar": {
        "mp_back":          "العودة إلى MarketWeb →",
        "mp_preview_of":    "معاينة كاملة",
        "mp_other":         "← قوالب طبية أخرى",
        "mp_other_restaurant": "← قوالب مطاعم أخرى",
        "mp_other_business": "← قوالب أعمال أخرى",
        "mp_other_portfolio": "← محافظ أخرى",
        "mp_language":      "اللغة",
        "foot_studio":      "العيادة",
        "foot_pages":       "الصفحات",
        "foot_contact":     "اتصل بنا",
        "foot_hours":       "ساعات العمل",
        "foot_privacy":     "الخصوصية",
        "foot_cookie":      "ملفات الارتباط",
        "foot_legal":       "إشعار قانوني",
        "foot_restaurant":  "المطعم",
        "foot_concierge":   "الاستقبال",
        "foot_services":    "الخدمة",
        "home_all_doctors": "فريق الأطباء",
        "home_publications":"المنشورات",
        "form_name":        "الاسم",
        "form_surname":     "اللقب",
        "form_email":       "البريد الإلكتروني",
        "form_phone":       "الهاتف",
        "form_subject":     "الموضوع",
        "form_message":     "الرسالة",
        "form_submit":      "إرسال الرسالة",
        "apt_alternative_prefix": "أو:",
        "apt_alternative_link":   "تواصل مع السكرتارية",
        "blog_read_full":   "قراءة المقال كاملاً",
        "blog_read_article":"قراءة المقال",
        "blog_read_minutes":"دقائق قراءة",
        "blog_back_all_prefix": "→ جميع",
        "blog_crumb_sep":   "/",
        "fd_wine_pairing":  "مقترن مع",
        "fd_email_label":   "البريد الإلكتروني",
        "fd_phone_label":   "الهاتف",
        "form_required":    "إلزامي",
        "form_optional":    "اختياري",
        "form_select_placeholder": "اختَر…",
        "form_upload_browse_prefix": "اسحب ملفاً هنا أو",
        "form_upload_browse_link":   "تصفّح مستنداتك",
        "form_upload_remove":        "إزالة",
    },
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def resolve_locale(request: HttpRequest) -> str:
    """Read `?lang=xx` from the request, validated against SUPPORTED_LOCALES.

    Returns DEFAULT_LOCALE if the param is missing, empty, or unknown.
    Safe to call on every request — no session state, no cookies.
    """
    if request is None:
        return DEFAULT_LOCALE
    raw = (request.GET.get("lang") or "").strip().lower()
    if raw and raw in SUPPORTED_LOCALES:
        return raw
    return DEFAULT_LOCALE


def is_rtl(locale: str) -> bool:
    """True if the locale renders right-to-left."""
    return locale in RTL_LOCALES


def html_dir(locale: str) -> str:
    """`"rtl"` for Arabic (and any future RTL locale), `"ltr"` otherwise."""
    return "rtl" if is_rtl(locale) else "ltr"


def get_chrome(locale: str) -> dict[str, str]:
    """Return the chrome labels dict for a locale, with IT fallback.

    Any key missing in the requested locale is backfilled from IT so a
    partially-authored locale still renders (no blank labels). The return
    value is a NEW dict so callers can't mutate the module-level source.
    """
    base = dict(CHROME_I18N[DEFAULT_LOCALE])
    if locale != DEFAULT_LOCALE and locale in CHROME_I18N:
        base.update(CHROME_I18N[locale])
    return base


def pick_localized(content_by_locale: dict[str, Any], locale: str) -> Any:
    """Pick the locale-specific content tree from a `{locale: tree}` mapping.

    Falls back to IT if the requested locale is missing — every template
    is guaranteed to have an `it` entry, and Italian is the authoritative
    source. Also accepts a legacy flat tree (no locale keys) by detecting
    the absence of `DEFAULT_LOCALE` at the top level and returning it as-is
    — this is a safety net for templates that haven't been migrated to the
    locale-keyed shape yet (not used by cardio after Session 23 but kept
    for additive migration of future templates).
    """
    if not isinstance(content_by_locale, dict):
        return content_by_locale
    if DEFAULT_LOCALE not in content_by_locale:
        # Legacy flat shape — return unchanged.
        return content_by_locale
    if locale in content_by_locale:
        return content_by_locale[locale]
    return content_by_locale[DEFAULT_LOCALE]


def locale_switcher_entries(
    current_locale: str,
    available_locales: list[str] | tuple[str, ...] | None = None,
) -> list[dict[str, Any]]:
    """Build the data the language switcher template loops over.

    Each entry has: `code`, `label`, `badge`, `is_current`. The order
    matches SUPPORTED_LOCALES. Used by the marketplace bar in every
    live-template skin page.

    `available_locales` scopes the switcher to the languages actually
    authored for the current template. When omitted (or empty), the
    full SUPPORTED_LOCALES set is returned — preserved for callers
    that predate the per-template coverage check. A template that only
    authors Italian must pass `["it"]` and the returned list will contain
    a single entry (or zero, if the caller prefers to hide the switcher
    entirely when coverage is 1 or less).
    """
    if available_locales:
        codes = [c for c in SUPPORTED_LOCALES if c in available_locales]
    else:
        codes = list(SUPPORTED_LOCALES)
    return [
        {
            "code":       code,
            "label":      LOCALE_LABELS[code],
            "badge":      LOCALE_BADGES[code],
            "is_current": code == current_locale,
        }
        for code in codes
    ]
