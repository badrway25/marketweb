"""Seed Commerce Foundation v1 data for Bottega + Luxe storefronts.

Idempotent — safe to run multiple times. Pulls product data from the
existing IT content registries so the live preview and the real shop
stay in sync.

Bottega (artisan-workshop skin):
- 9 products (leather goods, ceramics, textiles, preserves)
- Variants: size pills + edition numbers
- Collections: Cuoio · Ceramica · Tessuti · Conserve

Luxe (fashion-editorial skin):
- 8 looks across 4 drops
- Variants: silhouette × tonality
- Collections: Drop 01 · Drop 02 · Drop 03 · Drop 04 · Atelier

Shipping methods per storefront reflect each brand's register.
"""
from __future__ import annotations

from decimal import Decimal
from typing import Any

from django.core.management.base import BaseCommand
from django.db import transaction

from django.contrib.auth import get_user_model

from apps.catalog.models import WebTemplate
from apps.commerce import content as commerce_content
from apps.commerce.models import (
    Collection,
    Product,
    ProductImage,
    ProductVariant,
    ShippingMethod,
    Storefront,
    StorefrontMember,
)


# Per-storefront, per-shipping-code translations. Picked up by the
# seeder to populate ShippingMethod.translations. New shipping codes
# without entries here render in IT only.
SHIPPING_TRANSLATIONS: dict[str, dict[str, dict[str, dict[str, str]]]] = {
    "bottega-shop-artigianale": {
        "italy-48h": {
            "it": {"title": "Italia · 48 ore",                  "description": "Corriere espresso, consegnato in 48 ore lavorative.",          "est_delivery_days": "48 ore"},
            "en": {"title": "Italy · 48h tracked",              "description": "Express courier within 48 working hours.",                     "est_delivery_days": "48 hours"},
            "fr": {"title": "Italie · livraison 48h",           "description": "Transporteur express en 48 heures ouvrées.",                  "est_delivery_days": "48 heures"},
            "es": {"title": "Italia · 48 horas",                "description": "Mensajería urgente en 48 horas laborables.",                  "est_delivery_days": "48 horas"},
            "ar": {"title": "إيطاليا · خلال 48 ساعة",          "description": "بريدٌ سريعٌ خلال 48 ساعة عمل.",                                "est_delivery_days": "48 ساعة"},
        },
        "italy-pickup": {
            "it": {"title": "Ritiro in bottega · Firenze",       "description": "Via dei Serragli 47/r · su appuntamento.",                     "est_delivery_days": "Quando vuoi"},
            "en": {"title": "Pickup in bottega · Florence",      "description": "Via dei Serragli 47/r · by appointment.",                      "est_delivery_days": "Whenever you like"},
            "fr": {"title": "Retrait à la bottega · Florence",   "description": "Via dei Serragli 47/r · sur rendez-vous.",                     "est_delivery_days": "Quand vous voulez"},
            "es": {"title": "Recogida en la bottega · Florencia","description": "Via dei Serragli 47/r · con cita.",                            "est_delivery_days": "Cuando quieras"},
            "ar": {"title": "الاستلام من البوتيغا · فلورنسا",    "description": "Via dei Serragli 47/r · بحجزٍ مسبق.",                           "est_delivery_days": "متى تشاء"},
        },
        "europe-4d": {
            "it": {"title": "Europa · 4 giorni",                 "description": "Spedizione tracciata in tutta l'UE.",                          "est_delivery_days": "4 giorni"},
            "en": {"title": "Europe · 4 days",                   "description": "Tracked shipping across the EU.",                              "est_delivery_days": "4 days"},
            "fr": {"title": "Europe · 4 jours",                  "description": "Livraison suivie dans toute l'UE.",                            "est_delivery_days": "4 jours"},
            "es": {"title": "Europa · 4 días",                   "description": "Envío con seguimiento por toda la UE.",                        "est_delivery_days": "4 días"},
            "ar": {"title": "أوروبا · 4 أيام",                   "description": "شحنٌ مع تتبّع في الاتحاد الأوروبي.",                            "est_delivery_days": "4 أيام"},
        },
    },
    "luxe-fashion-store": {
        "maison-milano": {
            "it": {"title": "Consegna maison · Milano",          "description": "Corriere dedicato, consegna in 24 ore.",                       "est_delivery_days": "24 ore"},
            "en": {"title": "Maison delivery · Milan",           "description": "Dedicated courier, 24h delivery.",                             "est_delivery_days": "24 hours"},
            "fr": {"title": "Livraison maison · Milan",          "description": "Transporteur dédié, livraison en 24 heures.",                  "est_delivery_days": "24 heures"},
            "es": {"title": "Entrega maison · Milán",            "description": "Mensajería dedicada, entrega en 24 horas.",                    "est_delivery_days": "24 horas"},
            "ar": {"title": "توصيلٌ من الميزون · ميلانو",       "description": "ناقلٌ مخصّص، التسليم خلال 24 ساعة.",                            "est_delivery_days": "24 ساعة"},
        },
        "maison-italia": {
            "it": {"title": "Consegna maison · Italia",         "description": "Corriere dedicato, consegna in 24–48 ore.",                    "est_delivery_days": "48 ore"},
            "en": {"title": "Maison delivery · Italy",          "description": "Dedicated courier, 24–48h delivery.",                          "est_delivery_days": "48 hours"},
            "fr": {"title": "Livraison maison · Italie",        "description": "Transporteur dédié, livraison en 24 à 48 heures.",             "est_delivery_days": "48 heures"},
            "es": {"title": "Entrega maison · Italia",          "description": "Mensajería dedicada, entrega en 24–48 horas.",                 "est_delivery_days": "48 horas"},
            "ar": {"title": "توصيلٌ من الميزون · إيطاليا",     "description": "ناقلٌ مخصّص، التسليم خلال 24–48 ساعة.",                          "est_delivery_days": "48 ساعة"},
        },
        "maison-europa": {
            "it": {"title": "Consegna maison · Europa",         "description": "DHL Express internazionale, assicurato alla totalità.",         "est_delivery_days": "3–5 giorni"},
            "en": {"title": "Maison delivery · Europe",         "description": "DHL Express international, fully insured.",                    "est_delivery_days": "3–5 days"},
            "fr": {"title": "Livraison maison · Europe",        "description": "DHL Express international, entièrement assuré.",               "est_delivery_days": "3 à 5 jours"},
            "es": {"title": "Entrega maison · Europa",          "description": "DHL Express internacional, asegurado al valor.",               "est_delivery_days": "3–5 días"},
            "ar": {"title": "توصيلٌ من الميزون · أوروبا",      "description": "DHL Express دولي، مؤمَّنٌ بكامل القيمة.",                       "est_delivery_days": "3–5 أيام"},
        },
        "private-appointment": {
            "it": {"title": "Consegna su appuntamento · showroom","description": "Ritiro nello showroom Brera con la direzione clienti.",        "est_delivery_days": "Quando vuoi"},
            "en": {"title": "Showroom appointment",              "description": "Pickup at the Brera showroom with the client director.",        "est_delivery_days": "Whenever you like"},
            "fr": {"title": "Rendez-vous showroom",              "description": "Retrait au showroom Brera avec la direction clientèle.",        "est_delivery_days": "Quand vous voulez"},
            "es": {"title": "Cita en el showroom",               "description": "Recogida en el showroom Brera con la dirección de clientes.",    "est_delivery_days": "Cuando quieras"},
            "ar": {"title": "موعدٌ في الشورُوم",                "description": "الاستلام من شورُوم بريرا مع إدارة العملاء.",                     "est_delivery_days": "متى تشاء"},
        },
    },
}


def _parse_price(raw: str) -> Decimal:
    """`€ 2.480` / `€ 95` → Decimal. Italian thousands separators."""
    s = raw.replace("€", "").replace("\xa0", "").strip()
    # Italian: thousands = ".", decimal = ","
    if "," in s:
        s = s.replace(".", "").replace(",", ".")
    else:
        # Digits only; "2.480" means 2480, not 2.480
        if s.count(".") == 1 and len(s.split(".")[1]) == 3:
            s = s.replace(".", "")
    return Decimal(s)


# ── Bottega seed data ──────────────────────────────────────────────

BOTTEGA_COLLECTIONS = [
    {"slug": "cuoio", "title": "Cuoio del Valdarno",
     "subtitle": "Concia vegetale, quaranta giorni in vasca",
     "description": "I pezzi in cuoio della bottega, conciati e cuciti a mano in Toscana.", "order": 1},
    {"slug": "ceramica", "title": "Ceramica di Montelupo",
     "subtitle": "Tornita a mano, cotta a legna",
     "description": "Argilla rossa, smalti a freddo e cottura lenta.", "order": 2},
    {"slug": "tessuti", "title": "Lino & tessuti",
     "subtitle": "Lino grezzo non sbiancato da Prato",
     "description": "Tessitura su telaio tradizionale a trama larga.", "order": 3},
    {"slug": "conserve", "title": "Conserve del mercato",
     "subtitle": "Greve in Chianti, cottura lenta",
     "description": "Pomodoro cuore di bue, fichi neri di settembre, olio EVO.", "order": 4},
]

BOTTEGA_PRODUCTS = [
    {
        "slug": "giubbotto-terra", "title": "Giubbotto Terra",
        "subtitle": "Cuoio conciato al vegetale · cucito a sella · tinto a mano",
        "collection": "cuoio",
        "price": "€ 420", "badge": "Pezzo unico", "edition": "3 / 8",
        "material": "Cuoio del Valdarno · concia vegetale",
        "made_in": "Santa Croce sull'Arno",
        "creator": "Severino Falchi",
        "sku_root": "BTG-GBT-042",
        "featured": True,
        "short": "Giubbotto corto in cuoio conciato al vegetale, tinto a mano terra di Siena.",
        "long": (
            "Un giubbotto corto in cuoio del Valdarno, conciato al vegetale per quaranta giorni "
            "con corteccia di castagno e mimosa. La tinta è data a mano con un panno di lino imbevuto "
            "di pigmento naturale terra di Siena: ogni pezzo prende il colore in modo leggermente diverso "
            "e nessuno è mai uguale al precedente."
        ),
        # Hero: black leather moto jacket (verified visually 2026-04-14,
        # Session 46). Original `1547949003-9792a18a2601` rendered a
        # backpack and was semantically wrong for a "giubbotto".
        "hero": "https://images.unsplash.com/photo-1551028719-00167b16eac5?w=1200&q=80&auto=format&fit=crop",
        "gallery": [
            "https://images.unsplash.com/photo-1521223890158-f9f7c3d5d504?w=1200&q=80&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1520975916090-3105956dac38?w=1200&q=80&auto=format&fit=crop",
        ],
        "info_rows": [
            {"label": "Materia", "value": "Cuoio del Valdarno · concia vegetale"},
            {"label": "Spessore", "value": "1,8 mm uniforme"},
            {"label": "Tinta", "value": "Terra di Siena · pigmento naturale"},
            {"label": "Cucitura", "value": "Punto sella, filo cerato"},
            {"label": "Fodera", "value": "Lino grezzo non sbiancato"},
            {"label": "Peso", "value": "780 g (taglia M)"},
            {"label": "Realizzazione", "value": "11 giorni di bottega"},
        ],
        "variants": [
            {"sku": "BTG-GBT-042-S", "option1": "Taglia S", "stock": 1},
            {"sku": "BTG-GBT-042-M", "option1": "Taglia M", "stock": 1},
            {"sku": "BTG-GBT-042-L", "option1": "Taglia L", "stock": 1},
        ],
    },
    {
        "slug": "borsa-cartolina", "title": "Borsa Cartolina",
        "subtitle": "Cuoio naturale · cucitura a sella",
        "collection": "cuoio",
        "price": "€ 280", "badge": "Pezzo unico", "edition": "2 / 12",
        "material": "Cuoio naturale",
        "made_in": "Santa Croce sull'Arno",
        "creator": "Severino Falchi",
        "sku_root": "BTG-BCA-056",
        "featured": True,
        "short": "Borsa rigida in cuoio naturale, formato cartolina.",
        "long": (
            "Una borsa rigida in cuoio naturale, formato cartolina. Cucita a sella, finita a cera "
            "d'api. Disponibile in due finiture: naturale e cognac."
        ),
        "hero": "https://images.unsplash.com/photo-1591561954557-26941169b49e?w=1200&q=80&auto=format&fit=crop",
        "gallery": [
            "https://images.unsplash.com/photo-1605518216938-7c31b7b14ad0?w=1200&q=80&auto=format&fit=crop",
        ],
        "info_rows": [
            {"label": "Materia", "value": "Cuoio naturale"},
            {"label": "Misure", "value": "22 × 15 × 6 cm"},
            {"label": "Finitura", "value": "Cera d'api · lucidata a mano"},
        ],
        "variants": [
            {"sku": "BTG-BCA-056-NAT", "option1": "Naturale", "stock": 3},
            {"sku": "BTG-BCA-056-COG", "option1": "Cognac", "stock": 2},
        ],
    },
    {
        "slug": "camicia-lino", "title": "Camicia di lino",
        "subtitle": "Lino grezzo non sbiancato",
        "collection": "tessuti",
        "price": "€ 95", "badge": "Fatto a mano", "edition": "1 / 6",
        "material": "Lino grezzo non sbiancato",
        "made_in": "Prato",
        "creator": "Bruno Ricci",
        "sku_root": "BTG-CAM-108",
        "featured": False,
        "short": "Camicia in lino grezzo, trama larga, bottoni di corno.",
        "long": (
            "Camicia in lino grezzo non sbiancato, tessuto su telaio a Prato. Bottoni di corno "
            "di bue, cuciti a mano. Ogni capo è unico per sfumatura del lino."
        ),
        "hero": "https://images.unsplash.com/photo-1620799140408-edc6dcb6d633?w=1200&q=80&auto=format&fit=crop",
        "gallery": [],
        "info_rows": [
            {"label": "Materia", "value": "Lino grezzo · trama larga"},
            {"label": "Bottoni", "value": "Corno di bue"},
            {"label": "Lavaggio", "value": "30°C · stiro a vapore"},
        ],
        "variants": [
            {"sku": "BTG-CAM-108-S", "option1": "Taglia S", "stock": 2},
            {"sku": "BTG-CAM-108-M", "option1": "Taglia M", "stock": 3},
            {"sku": "BTG-CAM-108-L", "option1": "Taglia L", "stock": 2},
            {"sku": "BTG-CAM-108-XL", "option1": "Taglia XL", "stock": 1},
        ],
    },
    {
        "slug": "tovaglia-armaiolo", "title": "Tovaglia Armaiolo",
        "subtitle": "Lino & cotone · trama larga",
        "collection": "tessuti",
        "price": "€ 165", "badge": "Edizione", "edition": "5 / 30",
        "material": "Lino & cotone · trama larga",
        "made_in": "Prato",
        "creator": "Bruno Ricci",
        "sku_root": "BTG-TOV-134",
        "featured": False,
        "short": "Tovaglia rettangolare per sei, lino & cotone.",
        "long": "Tessitura pesante, orli cuciti a mano. Adatta al quotidiano e alle feste.",
        "hero": "https://images.unsplash.com/photo-1583847268964-b28dc8f51f92?w=1200&q=80&auto=format&fit=crop",
        "gallery": [],
        "info_rows": [
            {"label": "Materia", "value": "Lino 60% · cotone 40%"},
            {"label": "Misure", "value": "180 × 140 cm"},
        ],
        "variants": [
            {"sku": "BTG-TOV-134-AVO", "option1": "Avorio", "stock": 4},
            {"sku": "BTG-TOV-134-TER", "option1": "Terracotta", "stock": 3},
        ],
    },
    {
        "slug": "set-cucina", "title": "Set da cucina",
        "subtitle": "Ceramica smaltata a freddo",
        "collection": "ceramica",
        "price": "€ 148", "badge": "Edizione", "edition": "7 / 24",
        "material": "Ceramica smaltata a freddo",
        "made_in": "Montelupo Fiorentino",
        "creator": "Caterina Lippi",
        "sku_root": "BTG-SET-213",
        "featured": True,
        "short": "Set di quattro pezzi: insalatiera, ciotola, due piatti.",
        "long": "Ceramica rossa di Montelupo, torniata e smaltata a freddo. Ogni pezzo è firmato.",
        "hero": "https://images.unsplash.com/photo-1565193566173-7a0ee3dbe261?w=1200&q=80&auto=format&fit=crop",
        "gallery": [],
        "info_rows": [
            {"label": "Materia", "value": "Argilla rossa locale"},
            {"label": "Smalto", "value": "Trasparente, cottura a freddo"},
            {"label": "Pezzi", "value": "4 (insalatiera, ciotola, 2 piatti)"},
        ],
        "variants": [
            {"sku": "BTG-SET-213-DEF", "option1": "Standard", "stock": 5},
        ],
    },
    {
        "slug": "tazze-tornite", "title": "Tazze Tornite",
        "subtitle": "Argilla rossa locale · cottura a legna",
        "collection": "ceramica",
        "price": "€ 78", "badge": "Edizione", "edition": "11 / 24",
        "material": "Argilla rossa · cottura a legna",
        "made_in": "Montelupo Fiorentino",
        "creator": "Caterina Lippi",
        "sku_root": "BTG-TAZ-219",
        "featured": False,
        "short": "Coppia di tazze da caffè, tornite a mano.",
        "long": "Argilla rossa locale, cottura lenta a legna. Due pezzi ogni set, firmati.",
        "hero": "https://images.unsplash.com/photo-1610701596007-11502861dcfa?w=1200&q=80&auto=format&fit=crop",
        "gallery": [],
        "info_rows": [
            {"label": "Materia", "value": "Argilla rossa locale"},
            {"label": "Cottura", "value": "Forno a legna · 12 ore"},
        ],
        "variants": [
            {"sku": "BTG-TAZ-219-DEF", "option1": "Coppia", "stock": 9},
        ],
    },
    {
        "slug": "vassoio-noce", "title": "Vassoio in noce",
        "subtitle": "Noce massello · finitura ad olio",
        "collection": "cuoio",  # reused grouping — falls under bottega's wood/leather register
        "price": "€ 210", "badge": "Lista d'attesa", "edition": "Esaurito",
        "material": "Noce massello · finitura ad olio",
        "made_in": "Pratovecchio",
        "creator": "Severino Falchi",
        "sku_root": "BTG-VAS-251",
        "featured": False,
        "short": "Vassoio ovale in noce massello, venatura centrale.",
        "long": "Lavorato a mano, finito con olio naturale. Prossima infornata a ottobre.",
        "hero": "https://images.unsplash.com/photo-1606112219348-204d7d8b94ee?w=1200&q=80&auto=format&fit=crop",
        "gallery": [],
        "info_rows": [
            {"label": "Materia", "value": "Noce massello"},
            {"label": "Misure", "value": "42 × 28 × 3,5 cm"},
        ],
        "variants": [
            {"sku": "BTG-VAS-251-DEF", "option1": "Unico", "stock": 0},
        ],
    },
    {
        "slug": "conserve-chianti", "title": "Conserve del mercato",
        "subtitle": "Pomodorini cuore di bue + olio EVO",
        "collection": "conserve",
        "price": "€ 18", "badge": "Stagione", "edition": "12 / 60",
        "material": "Pomodoro cuore di bue · olio EVO",
        "made_in": "Greve in Chianti",
        "creator": "Adele Pignatelli",
        "sku_root": "BTG-CON-317",
        "featured": False,
        "short": "Vasetto da 320g di pomodori sott'olio EVO.",
        "long": "Pomodori cuore di bue della valle del Chianti, cottura lenta a mano.",
        "hero": "https://images.unsplash.com/photo-1604908176997-125f25cc6f3d?w=1200&q=80&auto=format&fit=crop",
        "gallery": [],
        "info_rows": [
            {"label": "Peso", "value": "320 g"},
            {"label": "Scadenza", "value": "18 mesi dalla chiusura"},
        ],
        "variants": [
            {"sku": "BTG-CON-317-DEF", "option1": "Vasetto 320g", "stock": 48},
        ],
    },
    {
        "slug": "marmellata-fichi", "title": "Marmellata di fichi",
        "subtitle": "Fichi neri di settembre · cottura lenta",
        "collection": "conserve",
        "price": "€ 14", "badge": "Stagione", "edition": "21 / 80",
        "material": "Fichi neri · zucchero di canna",
        "made_in": "Greve in Chianti",
        "creator": "Adele Pignatelli",
        "sku_root": "BTG-MAR-322",
        "featured": False,
        "short": "Vasetto da 280g di marmellata di fichi neri.",
        "long": "Fichi neri maturi, cottura lenta in paiolo di rame. Senza conservanti.",
        # Typographic tile (artisan-workshop DNA-honest fallback) — no hero image,
        # the shop/product pages render an .is-empty stamp with the product initials.
        "hero": "",
        "gallery": [],
        "info_rows": [
            {"label": "Peso", "value": "280 g"},
            {"label": "Zucchero", "value": "Di canna · 45%"},
        ],
        "variants": [
            {"sku": "BTG-MAR-322-DEF", "option1": "Vasetto 280g", "stock": 59},
        ],
    },
]

BOTTEGA_SHIPPING = [
    {"code": "italy-48h", "title": "Italia · 48 ore",
     "description": "Corriere espresso, consegnato in 48 ore lavorative.",
     "price": "8.00", "eta": "48 ore"},
    {"code": "italy-pickup", "title": "Ritiro in bottega · Firenze",
     "description": "Via dei Serragli 47/r · su appuntamento.",
     "price": "0.00", "eta": "Quando vuoi"},
    {"code": "europe-4d", "title": "Europa · 4 giorni",
     "description": "Spedizione tracciata in tutta l'UE.",
     "price": "22.00", "eta": "4 giorni"},
]


# ── Luxe seed data ─────────────────────────────────────────────────

LUXE_COLLECTIONS = [
    {"slug": "drop-01-spring-26", "title": "Drop 01 · Spring 26",
     "subtitle": "La luce del mattino", "description": "Prima capsula della stagione.", "order": 1},
    {"slug": "drop-02-spring-26", "title": "Drop 02 · Spring 26",
     "subtitle": "L'ora del cocktail", "description": "Seconda uscita, silhouette serali.", "order": 2},
    {"slug": "drop-03-summer-26", "title": "Drop 03 · Summer 26",
     "subtitle": "Arriva il caldo", "description": "Capsula dell'estate lunga.", "order": 3},
    {"slug": "drop-04-summer-26", "title": "Drop 04 · Summer 26",
     "subtitle": "La luce di Como", "description": "Chiusura stagione, pezzi di alto atelier.", "order": 4},
    {"slug": "atelier", "title": "Atelier · archivio",
     "subtitle": "Riedizioni firmate", "description": "Pezzi d'archivio numerati.", "order": 5},
]

LUXE_PRODUCTS = [
    {
        "slug": "robe-manteau-grigio-perla", "title": "Robe-manteau Grigio Perla",
        "subtitle": "Cashmere alpaca doppio · Maglificio Lanifer Biella",
        "collection": "drop-01-spring-26",
        "price": "€ 2.840", "badge": "Lista d'attesa", "edition": "Look 03",
        "material": "Cashmere alpaca doppio", "made_in": "Biella",
        "creator": "Maglificio Lanifer Biella",
        "sku_root": "LUX-RM-03",
        "featured": True,
        "short": "Cappotto lungo, tessuto a doppio strato, allacciato in vita.",
        "long": (
            "Un robe-manteau in cashmere alpaca doppio, tessuto in esclusiva per la maison "
            "dal Maglificio Lanifer di Biella. Allacciato con cintura in cuoio nappa. Cuciture "
            "sellier a vista sulle revere. Numero 03 della serie primaverile."
        ),
        "hero": "https://images.unsplash.com/photo-1490481651871-ab68de25d43d?w=1400&q=80&auto=format&fit=crop",
        "gallery": [
            "https://images.unsplash.com/photo-1581338834647-b0fb40704e21?w=1400&q=80&auto=format&fit=crop",
        ],
        "info_rows": [
            {"label": "Atelier", "value": "Maglificio Lanifer · Biella"},
            {"label": "Materia", "value": "Cashmere 70% · alpaca 30%"},
            {"label": "Realizzazione", "value": "40 ore di atelier per pezzo"},
        ],
        "variants": [
            {"sku": "LUX-RM-03-38", "option1": "Taglia 38", "stock": 1},
            {"sku": "LUX-RM-03-40", "option1": "Taglia 40", "stock": 1},
            {"sku": "LUX-RM-03-42", "option1": "Taglia 42", "stock": 1},
        ],
    },
    {
        "slug": "tailleur-cady-bianco", "title": "Tailleur Cady Bianco",
        "subtitle": "Cady doppio strato · Setificio Tessitura Como",
        "collection": "drop-02-spring-26",
        "price": "€ 3.420", "badge": "In showroom", "edition": "Look 07",
        "material": "Cady doppio strato", "made_in": "Como",
        "creator": "Setificio Tessitura Como",
        "sku_root": "LUX-TAI-07",
        "featured": True,
        "short": "Giacca + pantalone avorio, cady doppio strato.",
        "long": "Tailleur serale in cady doppio strato, tessuto esclusivo per la maison.",
        "hero": "https://images.unsplash.com/photo-1581338834647-b0fb40704e21?w=1400&q=80&auto=format&fit=crop",
        "gallery": [],
        "info_rows": [
            {"label": "Atelier", "value": "Setificio Tessitura Como"},
            {"label": "Materia", "value": "Cady doppio strato · seta"},
        ],
        "variants": [
            {"sku": "LUX-TAI-07-38", "option1": "Taglia 38", "stock": 1},
            {"sku": "LUX-TAI-07-40", "option1": "Taglia 40", "stock": 1},
        ],
    },
    {
        "slug": "rack-atelier-nero", "title": "Rack Atelier Nero",
        "subtitle": "Cuoio nappa firenze · cucitura sellier",
        "collection": "drop-02-spring-26",
        "price": "€ 2.480", "badge": "Lista d'attesa", "edition": "Look 11 · Drop 02",
        "material": "Cuoio nappa firenze · concia vegetale", "made_in": "Sentier · Parigi",
        "creator": "Atelier Sentier",
        "sku_root": "LUX-RAC-11",
        "featured": True,
        "short": "Borsa giorno-sera in cuoio nappa, 12 esemplari numerati.",
        "long": (
            "Borsa giorno-sera in cuoio nappa di Firenze, cucita a mano nell'atelier di Sentier "
            "con cucitura sellier oro a tre lati. Profilo lucidato a cera d'api, fondo rinforzato "
            "in cuoio Vacchetta. Prodotta in dodici esemplari numerati."
        ),
        "hero": "https://images.unsplash.com/photo-1551803091-e20673f15770?w=1400&q=80&auto=format&fit=crop",
        "gallery": [
            "https://images.unsplash.com/photo-1605518216938-7c31b7b14ad0?w=1400&q=80&auto=format&fit=crop",
            "https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=1400&q=80&auto=format&fit=crop",
        ],
        "info_rows": [
            {"label": "Atelier", "value": "Sentier · Parigi"},
            {"label": "Materia", "value": "Nappa firenze · concia vegetale"},
            {"label": "Cucitura", "value": "Sellier oro a tre lati · filo cerato"},
            {"label": "Profilo", "value": "Cera d'api · lucidato a mano"},
            {"label": "Hardware", "value": "Ottone bagnato in oro 24K"},
            {"label": "Misure", "value": "32 × 24 × 12 cm · tracolla 105 cm"},
            {"label": "Realizzazione", "value": "21 ore di atelier per pezzo"},
        ],
        "variants": [
            {"sku": "LUX-RAC-11-DAY-NERO", "option1": "Day 32×24", "option2": "Nero notte", "stock": 1},
            {"sku": "LUX-RAC-11-DAY-BORDO", "option1": "Day 32×24", "option2": "Bordeaux Como", "stock": 1},
            {"sku": "LUX-RAC-11-EVE-NERO", "option1": "Evening 25×18", "option2": "Nero notte", "stock": 2},
            {"sku": "LUX-RAC-11-EVE-AVO", "option1": "Evening 25×18", "option2": "Avorio crema", "stock": 1},
        ],
    },
    {
        "slug": "bomber-siena", "title": "Bomber Siena",
        "subtitle": "Cady tinto a Siena · ricamo Atelier Sentier",
        "collection": "drop-03-summer-26",
        "price": "€ 1.290", "badge": "Capsula", "edition": "Look 14",
        "material": "Cady tinto a Siena · ricamo oro",
        "made_in": "Sentier · Parigi",
        "creator": "Atelier Sentier",
        "sku_root": "LUX-BOM-14",
        "featured": False,
        "short": "Bomber corto, cady siena, ricamo oro sul cuore.",
        "long": "Bomber estivo con ricamo oro Atelier Sentier.",
        "hero": "https://images.unsplash.com/photo-1495121605193-b116b5b9c5fe?w=1400&q=80&auto=format&fit=crop",
        "gallery": [],
        "info_rows": [
            {"label": "Materia", "value": "Cady tinto naturale · pigmento Siena"},
            {"label": "Ricamo", "value": "Atelier Sentier · filo oro"},
        ],
        "variants": [
            {"sku": "LUX-BOM-14-36", "option1": "Taglia 36", "stock": 1},
            {"sku": "LUX-BOM-14-38", "option1": "Taglia 38", "stock": 2},
            {"sku": "LUX-BOM-14-40", "option1": "Taglia 40", "stock": 2},
        ],
    },
    {
        "slug": "pantalone-wide-crepe", "title": "Pantalone Wide Crêpe",
        "subtitle": "Crêpe di seta Como · cintura sellier",
        "collection": "drop-03-summer-26",
        "price": "€ 1.180", "badge": "Lista d'attesa", "edition": "Look 16",
        "material": "Crêpe di seta", "made_in": "Como",
        "creator": "Setificio Tessitura Como",
        "sku_root": "LUX-PAN-16",
        "featured": False,
        "short": "Pantalone largo, crêpe di seta Como.",
        "long": "Taglio wide, cintura integrata in cuoio nappa.",
        "hero": "https://images.unsplash.com/photo-1559563458-527698bf5295?w=1400&q=80&auto=format&fit=crop",
        "gallery": [],
        "info_rows": [
            {"label": "Materia", "value": "Crêpe di seta · 100%"},
            {"label": "Cintura", "value": "Cuoio nappa · sellier"},
        ],
        "variants": [
            {"sku": "LUX-PAN-16-38", "option1": "Taglia 38", "stock": 2},
            {"sku": "LUX-PAN-16-40", "option1": "Taglia 40", "stock": 2},
            {"sku": "LUX-PAN-16-42", "option1": "Taglia 42", "stock": 1},
        ],
    },
    {
        "slug": "borsa-isola", "title": "Borsa Isola",
        "subtitle": "Cuoio Atelier Firenze · pochette giorno",
        "collection": "drop-03-summer-26",
        "price": "€ 860", "badge": "Atelier", "edition": "Look 18",
        "material": "Cuoio Atelier Firenze",
        "made_in": "Firenze",
        "creator": "Atelier Firenze",
        "sku_root": "LUX-ISO-18",
        "featured": False,
        "short": "Pochette giorno in cuoio, chiusura magnetica.",
        "long": "Pochette giorno in cuoio firenze, formato 22×13.",
        "hero": "https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=1400&q=80&auto=format&fit=crop",
        "gallery": [],
        "info_rows": [
            {"label": "Materia", "value": "Cuoio Atelier Firenze"},
            {"label": "Misure", "value": "22 × 13 × 4 cm"},
        ],
        "variants": [
            {"sku": "LUX-ISO-18-NERO", "option1": "Nero notte", "stock": 3},
            {"sku": "LUX-ISO-18-AVO", "option1": "Avorio crema", "stock": 2},
        ],
    },
    {
        "slug": "maglia-cashmere-corta", "title": "Maglia Cashmere Corta",
        "subtitle": "Cashmere a 12 fili · Maglificio Lanifer Biella",
        "collection": "drop-04-summer-26",
        "price": "€ 1.420", "badge": "Lista d'attesa", "edition": "Look 24",
        "material": "Cashmere a 12 fili", "made_in": "Biella",
        "creator": "Maglificio Lanifer Biella",
        "sku_root": "LUX-MGL-24",
        "featured": False,
        "short": "Maglia corta, cashmere 12 fili, collo alto.",
        "long": "Cashmere a 12 fili intrecciati, tessuto Lanifer Biella.",
        "hero": "https://images.unsplash.com/photo-1483985988355-763728e1935b?w=1400&q=80&auto=format&fit=crop",
        "gallery": [],
        "info_rows": [
            {"label": "Materia", "value": "Cashmere 12 fili"},
        ],
        "variants": [
            {"sku": "LUX-MGL-24-S", "option1": "Taglia S", "stock": 2},
            {"sku": "LUX-MGL-24-M", "option1": "Taglia M", "stock": 2},
            {"sku": "LUX-MGL-24-L", "option1": "Taglia L", "stock": 1},
        ],
    },
    {
        "slug": "sessione-vogue", "title": "Sessione Vogue",
        "subtitle": "Cappotto archivio · drop 2024 riedizione",
        "collection": "atelier",
        "price": "€ 1.940", "badge": "Archivio", "edition": "Look 26 · 2024",
        "material": "Lana cardata Biella", "made_in": "Biella",
        "creator": "Maglificio Lanifer Biella",
        "sku_root": "LUX-VOG-26",
        "featured": False,
        "short": "Cappotto d'archivio, riedizione limitata.",
        "long": "Drop 2024, riprodotto su richiesta in sei esemplari numerati.",
        "hero": "https://images.unsplash.com/photo-1611042553365-9b101441c135?w=1400&q=80&auto=format&fit=crop",
        "gallery": [],
        "info_rows": [
            {"label": "Atelier", "value": "Lanifer Biella"},
            {"label": "Edizione", "value": "6 esemplari numerati"},
        ],
        "variants": [
            {"sku": "LUX-VOG-26-38", "option1": "Taglia 38", "stock": 1},
            {"sku": "LUX-VOG-26-40", "option1": "Taglia 40", "stock": 1},
            {"sku": "LUX-VOG-26-42", "option1": "Taglia 42", "stock": 1},
        ],
    },
]

LUXE_SHIPPING = [
    {"code": "maison-milano", "title": "Consegna maison · Milano",
     "description": "Corriere maison in scatola firmata, consegnato su appuntamento.",
     "price": "0.00", "eta": "24 ore"},
    {"code": "maison-italia", "title": "Consegna maison · Italia",
     "description": "Corriere dedicato, consegna in 24–48 ore.",
     "price": "25.00", "eta": "48 ore"},
    {"code": "maison-europa", "title": "Consegna maison · Europa",
     "description": "DHL Express internazionale, assicurato alla totalità del valore.",
     "price": "60.00", "eta": "3–5 giorni"},
    {"code": "private-appointment", "title": "Consegna su appuntamento · showroom",
     "description": "Ritiro nello showroom Brera, su appuntamento con la direzione clienti.",
     "price": "0.00", "eta": "Quando vuoi"},
]


# ── Command ────────────────────────────────────────────────────────

class Command(BaseCommand):
    help = "Seed Commerce Foundation v1 data for Bottega + Luxe storefronts."

    def add_arguments(self, parser):
        parser.add_argument(
            "--reset", action="store_true",
            help="Wipe existing commerce data for the two storefronts before seeding.",
        )

    @transaction.atomic
    def handle(self, *args, **options):
        reset = options["reset"]
        self._seed_storefront(
            template_slug="bottega-shop-artigianale",
            skin=Storefront.Skin.ARTISAN_WORKSHOP,
            collections=BOTTEGA_COLLECTIONS,
            products=BOTTEGA_PRODUCTS,
            shipping_methods=BOTTEGA_SHIPPING,
            contact_phone="+39 055 234 11 90",
            contact_email="bottega@bottegadimartino.it",
            shipping_policy=(
                "Spedizione 48 ore in Italia, quattro giorni in Europa. "
                "Il ritiro in bottega a Firenze è gratuito e su appuntamento."
            ),
            return_policy=(
                "Resi entro 14 giorni dalla consegna. Le conserve e le edizioni numerate "
                "non rientrano nel diritto di recesso."
            ),
            payment_provider=Storefront.PaymentProvider.STUB,
            bank_transfer_instructions=(
                "La Bottega di Martino · IBAN IT47 X030 6909 6061 0000 0000 123 · "
                "BIC BCITITMM · causale: numero ordine."
            ),
            reset=reset,
        )
        self._seed_storefront(
            template_slug="luxe-fashion-store",
            skin=Storefront.Skin.FASHION_EDITORIAL,
            collections=LUXE_COLLECTIONS,
            products=LUXE_PRODUCTS,
            shipping_methods=LUXE_SHIPPING,
            contact_phone="+39 02 7600 1492",
            contact_email="direzione.clienti@maisonluxe.com",
            shipping_policy=(
                "Corriere maison in scatola firmata. Acconto del trenta per cento alla "
                "conferma per i pezzi di alta sartoria. Consegna entro 24 ore a Milano, "
                "48 ore nel resto d'Italia."
            ),
            return_policy=(
                "Cambi e resi solo su appuntamento con la direzione clienti entro sette "
                "giorni dalla consegna. I pezzi di archivio e le edizioni numerate non "
                "rientrano nel diritto di recesso."
            ),
            payment_provider=Storefront.PaymentProvider.STUB,
            bank_transfer_instructions=(
                "Maison Luxe S.r.l. · IBAN IT 89 A 01030 01600 000001234567 · "
                "BIC PASCITMMMIL · causale: numero ordine e cognome."
            ),
            reset=reset,
        )
        # Demo merchant accounts + storefront memberships.
        # Idempotent: re-running won't reset passwords or duplicate rows.
        self._seed_demo_merchants()

        self.stdout.write(self.style.SUCCESS("Commerce v2 seeded."))

    def _seed_demo_merchants(self):
        """Create one demo merchant per storefront, link via StorefrontMember.

        Usernames `bottega_owner` / `luxe_owner`, password `commerce-v2`.
        Used for dev login and to prove the merchant-scoped dashboard ACL
        in manual QA — production deployments should rotate these
        before exposing the dashboard publicly.
        """
        User = get_user_model()
        seed_specs = [
            ("bottega_owner", "bottega@bottegadimartino.it", "bottega-shop-artigianale"),
            ("luxe_owner",    "direzione.clienti@maisonluxe.com", "luxe-fashion-store"),
        ]
        for username, email, sf_slug in seed_specs:
            user, created = User.objects.get_or_create(
                username=username,
                defaults={"email": email, "is_staff": True},
            )
            if created:
                user.set_password("commerce-v2")
                user.save(update_fields=["password"])
                self.stdout.write(f"  user: {username} (created · pwd: commerce-v2)")
            sf = Storefront.objects.filter(template__slug=sf_slug).first()
            if sf is None:
                continue
            StorefrontMember.objects.get_or_create(
                storefront=sf, user=user,
                defaults={"role": StorefrontMember.Role.OWNER},
            )

    def _seed_storefront(
        self, *, template_slug: str, skin: str, collections: list[dict],
        products: list[dict], shipping_methods: list[dict],
        contact_phone: str, contact_email: str, shipping_policy: str,
        return_policy: str, payment_provider: str,
        bank_transfer_instructions: str, reset: bool,
    ):
        template = WebTemplate.objects.filter(slug=template_slug).first()
        if template is None:
            self.stdout.write(self.style.WARNING(
                f"Skipping {template_slug}: WebTemplate not found."
            ))
            return

        # Pull locale-keyed storefront text from apps/commerce/content.py.
        store_translations = commerce_content.STOREFRONT_CONTENT.get(template_slug) or {}

        sf, created = Storefront.objects.update_or_create(
            template=template,
            defaults={
                "skin": skin,
                "currency": "EUR",
                "currency_symbol": "€",
                "contact_phone": contact_phone,
                "contact_email": contact_email,
                "shipping_policy": shipping_policy,
                "return_policy": return_policy,
                "payment_provider": payment_provider,
                "bank_transfer_instructions": bank_transfer_instructions,
                "is_operational": True,
                "translations": store_translations,
            },
        )
        self.stdout.write(f"  storefront: {sf.slug} ({'created' if created else 'updated'})")

        if reset:
            sf.products.all().delete()
            sf.collections.all().delete()
            sf.shipping_methods.all().delete()

        # Collections
        coll_translations = commerce_content.COLLECTION_CONTENT.get(template_slug) or {}
        coll_by_slug: dict[str, Collection] = {}
        for c in collections:
            coll, _ = Collection.objects.update_or_create(
                storefront=sf, slug=c["slug"],
                defaults={
                    "title": c["title"], "subtitle": c.get("subtitle", ""),
                    "description": c.get("description", ""),
                    "order": c.get("order", 0), "is_active": True,
                    "translations": coll_translations.get(c["slug"], {}),
                },
            )
            coll_by_slug[c["slug"]] = coll

        # Shipping methods
        ship_translations = SHIPPING_TRANSLATIONS.get(template_slug) or {}
        for m in shipping_methods:
            ShippingMethod.objects.update_or_create(
                storefront=sf, code=m["code"],
                defaults={
                    "title": m["title"], "description": m.get("description", ""),
                    "price": Decimal(m["price"]),
                    "est_delivery_days": m.get("eta", ""),
                    "is_active": True,
                    "translations": ship_translations.get(m["code"], {}),
                },
            )

        # Products
        for order_idx, p in enumerate(products, start=1):
            prod, _ = Product.objects.update_or_create(
                storefront=sf, slug=p["slug"],
                defaults={
                    "title": p["title"],
                    "subtitle": p.get("subtitle", ""),
                    "short_description": p.get("short", ""),
                    "long_description": p.get("long", ""),
                    "sku_root": p.get("sku_root", ""),
                    "base_price": _parse_price(p["price"]),
                    "compare_at_price": None,
                    "badge": p.get("badge", ""),
                    "edition_number": p.get("edition", ""),
                    "material": p.get("material", ""),
                    "made_in": p.get("made_in", ""),
                    "creator_name": p.get("creator", ""),
                    "status": Product.Status.ACTIVE,
                    "featured": p.get("featured", False),
                    "order": order_idx,
                    "hero_image_url": p.get("hero", ""),
                    "info_rows": p.get("info_rows", []),
                    "collection": coll_by_slug.get(p.get("collection")),
                },
            )
            # Images
            prod.images.all().delete()
            for img_idx, url in enumerate(p.get("gallery", []), start=1):
                ProductImage.objects.create(
                    product=prod, image_url=url, alt_text=p["title"], order=img_idx,
                )
            # Variants
            existing_skus = {v["sku"] for v in p.get("variants", [])}
            for v_idx, v in enumerate(p.get("variants", []), start=1):
                ProductVariant.objects.update_or_create(
                    sku=v["sku"],
                    defaults={
                        "product": prod,
                        "option1": v.get("option1", ""),
                        "option2": v.get("option2", ""),
                        "option3": v.get("option3", ""),
                        "price_override": (
                            Decimal(v["price_override"]) if v.get("price_override") else None
                        ),
                        "stock": v.get("stock", 0),
                        "is_active": True,
                        "order": v_idx,
                    },
                )
            # Prune variants that no longer appear in the seed
            prod.variants.exclude(sku__in=existing_skus).delete()

        self.stdout.write(
            f"    · {sf.products.count()} products · "
            f"{sum(p.variants.count() for p in sf.products.all())} variants · "
            f"{sf.collections.count()} collections · "
            f"{sf.shipping_methods.count()} shipping methods"
        )
