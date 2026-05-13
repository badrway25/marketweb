"""Podere Le Querce — agriturismo familiar toscano (artisan-workshop · ES).

T60 · Wave 2 Pass-4 (2026-05-13) · Spanish (Peninsular) translation of
PODERE_CONTENT_IT. Shape parity strict: exactly 218 leaf paths · zero
missing · zero extra (per factory/standards/artisan-workshop-shape-
contract.md).

Voice contract (ES Peninsular):
- Editorial-rural register: El Pais Viajero · National Geographic
  Traveler Espana · Conde Nast Traveler Espana · Vogue Espana (Viajes)
  · Sobremesa. Calidez familiar; usted formal singular y ustedes plural
  (donde IT usa `voi`); registro reposado, sin marketing turistico.
- Voice anchor `ospitalita contadina` -> `hospitalidad campesina`
  (uso editorial consagrado en El Pais Viajero y NGT-Espana). Aparece
  >= 15 veces en superficies clave: home headline + home care heading,
  famiglia mission heading + intro, soggiorno intro + faq, footer
  intro, prodotto provenance, etc.
- Vocabolario: podere (prestamo) · agriturismo (prestamo) · familia ·
  campesino · vendimia · cosecha · olivar · vina · huerta · horno ·
  establo · bodega · cocina · hospitalidad · mesa larga. Nunca:
  resort · `all inclusive` · spa cinco estrellas · `check-in
  automatico` · `booking engine`.
- Concreto: Greve in Chianti · Chianti Classico DOCG · Cinta Senese ·
  cosecha de aceitunas en noviembre · vendimia en septiembre ·
  Antinori (propiedad historica · escritura de compraventa de 1934 a
  los bisabuelos Pasquinelli archivada en el ayuntamiento) ·
  familia Pasquinelli (Maria, 1962, matriarca · Carlo, marido ·
  Giovanni, 35, cocinero · Anna, 32, huerta y hospitalidad) ·
  8 productos del podere en la dispensa.

Italianismos preservados (convencion editorial ES):
- `podere`, `agriturismo`, `dispensa`, `tavolata` (cuando rotula
  pagina, p. ej. "Visiten la dispensa"), `Vin Santo`, `pecorino`,
  `ribollita`, `bruschetta`, `cantucci`, `Sangiovese`, `Canaiolo`,
  `Colorino`, `Cinta Senese`, `Senatore Cappelli`, `Pecorino Toscano
  DOP`, `Chianti Classico`, nombres propios italianos verbatim
  (Maria, Carlo, Giovanni, Anna, Mario, Annetta, Maddalena, Andrea
  Falleri, Famiglia Bartoletti, Davide Pieri, Suore di San Vivaldo,
  Antinori, Pasquinelli). Toponimos: Greve in Chianti, Lamole,
  Roccastrada, Castelfiorentino, Montaione, Vinci, Zeri, Florencia
  (para Firenze), Toscana, Chianti, Pratomagno, Maremma, Le Querce.

Digitos en arabigo latino: 1934, 1985, 2025, 2026, EUR 28, EUR 22,
EUR 75 (mantenidos verbatim del IT, con simbolo `€`).
"""
from __future__ import annotations

from typing import Any


# Interim Unsplash CC0 imagery pool · matches IT verbatim.
_PODERE_HERO = "https://images.unsplash.com/photo-1602941525521-46f6f1ab39ce?w=1600&q=80&auto=format&fit=crop"
_OLIVETO = "https://images.unsplash.com/photo-1567416661576-d8b6e92e63d2?w=1200&q=80&auto=format&fit=crop"
_VIGNA_CHIANTI = "https://images.unsplash.com/photo-1547595628-c61a29f496f0?w=1200&q=80&auto=format&fit=crop"
_TAVOLATA = "https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=1200&q=80&auto=format&fit=crop"
_CUCINA_CONTADINA = "https://images.unsplash.com/photo-1567620905732-2d1ec7ab7445?w=1200&q=80&auto=format&fit=crop"
_FAMIGLIA_PORTRAIT = "https://images.unsplash.com/photo-1573497019418-b400bb3ab074?w=1200&q=80&auto=format&fit=crop"
_OLIO_BOTTLE = "https://images.unsplash.com/photo-1474979266404-7eaacbcd87c5?w=1200&q=80&auto=format&fit=crop"
_VINO_BOTTLE = "https://images.unsplash.com/photo-1474722883778-792e7990302f?w=1200&q=80&auto=format&fit=crop"
_VINSANTO = "https://images.unsplash.com/photo-1547595628-c61a29f496f0?w=1200&q=80&auto=format&fit=crop"
_MIELE = "https://images.unsplash.com/photo-1587049352846-4a222e784d38?w=1200&q=80&auto=format&fit=crop"
_MARMELLATA = "https://images.unsplash.com/photo-1535990379313-50d1f6fc0c4f?w=1200&q=80&auto=format&fit=crop"
_PECORINO = "https://images.unsplash.com/photo-1452195100486-9cc805987862?w=1200&q=80&auto=format&fit=crop"
_SALAME = "https://images.unsplash.com/photo-1599379892470-bbe1eb01ea75?w=1200&q=80&auto=format&fit=crop"
_CANTUCCI = "https://images.unsplash.com/photo-1488477181946-6428a0291777?w=1200&q=80&auto=format&fit=crop"
_PORTRAIT_MARIA = "https://images.unsplash.com/photo-1559963110-71b394e7494d?w=900&q=80&auto=format&fit=crop"
_PORTRAIT_CARLO = "https://images.unsplash.com/photo-1545167622-3a6ac756afa4?w=900&q=80&auto=format&fit=crop"
_PORTRAIT_GIOVANNI = "https://images.unsplash.com/photo-1583394293214-28ded15ee548?w=900&q=80&auto=format&fit=crop"
_PORTRAIT_ANNA = "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=900&q=80&auto=format&fit=crop"
_PORTRAIT_PRODUCER = "https://images.unsplash.com/photo-1580489944761-15a19d654956?w=900&q=80&auto=format&fit=crop"


PODERE_CONTENT_ES: dict[str, Any] = {
    "pages": [
        {"slug": "home",      "label": "El podere",         "kind": "home"},
        {"slug": "dispensa",  "label": "La dispensa",       "kind": "shop"},
        {"slug": "prodotto",  "label": "El producto",       "kind": "product"},
        {"slug": "famiglia",  "label": "La familia",        "kind": "about"},
        {"slug": "diario",    "label": "Diario de campo",   "kind": "journal"},
        {"slug": "soggiorno", "label": "Estancia",          "kind": "contact"},
    ],

    # ─── SITE CHROME ───────────────────────────────────────────
    "site": {
        "logo_initial":    "Q",
        "logo_word":       "Podere Le Querce",
        "tag":             "Agriturismo de familia · hospitalidad campesina · Greve in Chianti · desde 1934",
        "phone":           "+39 055 853 261",
        "whatsapp":        "+39 339 458 1126",
        "whatsapp_link":   "https://wa.me/393394581126",
        "email":           "famiglia@podereleQuerce.it",
        "address":         "Località Le Querce 14 · 50022 Greve in Chianti · Florencia",
        "hours_compact":   "Abierto todo el año · cocina con reserva 12:30 y 19:30",
        "hours_footer_rows": [
            "Recepción de huéspedes 8-22 · Maria en la cocina desde las 7",
            "Dispensa abierta todos los días 9-19 · domingo cerrado",
        ],
        "license":         "Código CITRA 048-029-001 · Inscr. CCIAA Florencia 354210 · Az. Agricola Pasquinelli S.S.",
        "footer_intro":
            "Podere Le Querce es una explotación agrícola familiar en Greve in "
            "Chianti · 13 hectáreas de terreno con olivar histórico, viña de "
            "Sangiovese, huerta, establo de Cinta Senese, bodega y cuatro "
            "habitaciones de hospitalidad campesina. Lo elaboramos todo en "
            "casa: aceite, vino, miel, embutidos, pasta, cantucci. La familia "
            "Pasquinelli vive aquí desde 1934. Cuando ustedes vienen como "
            "huéspedes, comen en nuestra mesa.",

        # Nav CTA — sabor agriturismo
        "nav_cta":         "Reserven su estancia",
        "nav_cta_kind":    "appointment",

        # Footer labels
        "foot_studio":     "El podere",
        "foot_pages":      "Mapa",
        "foot_contact":    "Estancia",
        "foot_stockists":  "Dónde nos encuentran",
        "stockists_rows": [
            "Mercato della Terra · Greve in Chianti · domingo por la mañana",
            "Slow Food Florencia · puesto mensual",
            "Envío a domicilio · Italia 24-48h · Europa 4-6 días",
            "Dispensa en el podere · abierta al público todos los días 9-19",
        ],

        # Currency + product labels
        "currency_symbol":   "€",
        "shop_filter_label": "Afinen la dispensa",
        "shop_count_unit":   "productos del podere",
        "edition_label":     "Añada",
        "made_in_label":     "Elaborado en",
        "artisan_label":     "Manos de",
        "material_label":    "Materia prima",
        "shipping_label":    "Envío",
        "shipping_value":    "24-48h en Italia · envío refrigerado en verano",
        "guarantee_label":   "Garantía del podere",
        "guarantee_value":   "Sustituimos sin coste cualquier botella rota o defectuosa · en un plazo de 30 días",
    },

    # ─── HOME ──────────────────────────────────────────────────
    "home": {
        "eyebrow":  "Agriturismo · hospitalidad campesina · Greve in Chianti · desde 1934",
        "headline": "Cuatro generaciones en un podere toscano. <em>Hospitalidad campesina</em>, todo el año.",
        "intro":
            "Podere Le Querce es la casa de la familia Pasquinelli desde 1934, "
            "cuando los bisabuelos Mario y Annetta lo compraron a la familia "
            "Antinori con una escritura de compraventa conservada en el "
            "ayuntamiento. Hoy es un agriturismo de hospitalidad campesina "
            "con cuatro habitaciones, una cocina familiar con mesa larga "
            "bajo reserva y una dispensa campesina con nuestros ocho "
            "productos.",

        "primary_cta":          "Reserven su estancia de hospitalidad campesina",
        "primary_href":         "soggiorno",
        "secondary_cta":        "Visiten la dispensa",
        "secondary_href":       "dispensa",

        # Stamp panel — list[4] of tuple[2]
        "stamp_label":   "El podere en cuatro líneas",
        "stamp_heading": "Cuatro generaciones · una sola mesa larga.",
        "stamp_rows": [
            ("Año",          "1934 · escritura de compraventa Antinori → Pasquinelli"),
            ("Familia",      "Maria + Carlo + Giovanni + Anna · 4 al frente"),
            ("Hectáreas",    "13 hectáreas · olivar + viña + huerta + establo"),
            ("Habitaciones", "4 habitaciones · hospitalidad campesina abierta todo el año"),
        ],
        "stamp_footer":      "Mercato della Terra Greve · Slow Food Florencia · Envío a domicilio Italia 24-48h",
        "stamp_corner_index": "Temporada",
        "stamp_corner_word":  "2026",

        # Latest items — list[4] of dict[8 keys=edition,id,image,meta,n,name,price,tag]
        "latest_label":       "En la dispensa",
        "latest_heading":     "Ocho productos del podere, siempre disponibles.",
        "latest_link_label":  "Todos los productos",
        "latest_link_href":   "dispensa",
        "latest_items": [
            {
                "id":      "olio-evo-podere-2025",
                "n":       "N.º 01",
                "image":   _OLIO_BOTTLE,
                "edition": "Cosecha 2025",
                "name":    "Aceite de oliva virgen extra del Podere",
                "meta":    "Moraiolo + Frantoio + Leccino · 2.400 olivos",
                "price":   "€ 28 / 500 ml",
                "tag":     "Nuevo · cosecha de noviembre",
            },
            {
                "id":      "chianti-classico-2022",
                "n":       "N.º 02",
                "image":   _VINO_BOTTLE,
                "edition": "Vendimia 2022",
                "name":    "Chianti Classico DOCG",
                "meta":    "Sangiovese 95 % · 1,8 ha de viña",
                "price":   "€ 22 / botella",
                "tag":     "Bodega del podere",
            },
            {
                "id":      "miele-millefiori",
                "n":       "N.º 04",
                "image":   _MIELE,
                "edition": "Extracción julio 2025",
                "name":    "Miel de mil flores",
                "meta":    "12 colmenas · claro de castaños",
                "price":   "€ 14 / 250 g",
                "tag":     "Cien por cien del podere",
            },
            {
                "id":      "salame-cinta-senese",
                "n":       "N.º 07",
                "image":   _SALAME,
                "edition": "Curación 9 meses",
                "name":    "Salame de Cinta Senese",
                "meta":    "Cerdos negros criados en semilibertad",
                "price":   "€ 38 / pieza entera",
                "tag":     "8 cabezas en el establo",
            },
        ],

        # Makers — list[4] of dict[6 keys=craft,name,place,portrait,quote,since]
        "makers_label":   "Los productores del territorio",
        "makers_heading": "Cuatro manos que completan nuestra mesa.",
        "makers_intro":
            "Los productos del podere no alcanzan para la mesa de todos los "
            "huéspedes · desde hace cuatro generaciones la familia "
            "Pasquinelli se apoya en los mismos productores del territorio. "
            "Todos a menos de treinta kilómetros. Son parte de la "
            "hospitalidad campesina que ustedes encuentran en la mesa.",
        "makers": [
            {
                "craft":    "Pastor · pecorino de leche cruda",
                "name":     "Andrea Falleri",
                "place":    "Lamole · a 4 km del podere",
                "since":    "Cliente de la familia desde 1987",
                "portrait": _PORTRAIT_PRODUCER,
                "quote":
                    "Los Pasquinelli me compran el pecorino de Lamole desde "
                    "que yo era un muchacho. Mi abuelo se lo daba a su padre, "
                    "y ahora yo se lo doy a Maria. Es la manera en que las "
                    "cosas se transmiten aquí.",
            },
            {
                "craft":    "Molinero · trigo duro Maremma",
                "name":     "Famiglia Bartoletti",
                "place":    "Roccastrada · a 28 km del podere",
                "since":    "Molino de la familia desde 1820",
                "portrait": _PORTRAIT_PRODUCER,
                "quote":
                    "Molemos el trigo duro Senatore Cappelli a la piedra · "
                    "Maria hace con él la pasta de la mesa larga del "
                    "domingo. El sabor de la harina antigua es el sabor de "
                    "su pasta.",
            },
            {
                "craft":    "Norcino · embutidos de Cinta Senese",
                "name":     "Davide Pieri",
                "place":    "Castelfiorentino · a 22 km del podere",
                "since":    "Charcutería de familia desde 1958",
                "portrait": _PORTRAIT_PRODUCER,
                "quote":
                    "El padre de Maria me enseñó a despiezar el cerdo como "
                    "Dios manda en 1972. Ahora que Maria cría los Cinta "
                    "Senese del podere, los embutidos se los elaboro yo.",
            },
            {
                "craft":    "Monasterio · dulce de membrillo",
                "name":     "Suore di San Vivaldo",
                "place":    "Montaione · a 18 km del podere",
                "since":    "Monasterio activo desde el siglo XV",
                "portrait": _PORTRAIT_PRODUCER,
                "quote":
                    "Las hermanas del monasterio elaboran el dulce de "
                    "membrillo como se hacía en el Quattrocento · cinco "
                    "horas de cocción a fuego lento. Maria lo lleva a la "
                    "mesa con el pecorino.",
            },
        ],

        # Provenance items — list[4] of dict[4 keys=icon,title,desc,place]
        "provenance_label":   "El podere",
        "provenance_heading": "Trece hectáreas, cuatro producciones.",
        "provenance_intro":
            "El podere cuenta con 13 hectáreas trabajadas directamente por "
            "la familia Pasquinelli. Cuatro producciones históricas · olivar, "
            "viña, huerta, establo · siguen gobernándose con los ritmos que "
            "Maria aprendió de su padre.",
        "provenance_items": [
            {
                "icon":  "🌿",
                "title": "Olivar histórico",
                "desc": "2.400 olivos de moraiolo, frantoio y leccino · algunos árboles superan los 200 años · cosecha a mano en noviembre · prensado en frío en menos de 8 horas.",
                "place": "8 hectáreas en la ladera sureste del podere",
            },
            {
                "icon":  "🍇",
                "title": "Viña de Sangiovese",
                "desc": "1,8 hectáreas de Sangiovese (95 %) con pequeñas proporciones de Canaiolo y Colorino · vendimia manual a finales de septiembre · vinificación en la bodega de la familia · embotellado antes de mayo.",
                "place": "1,8 hectáreas en la ladera oeste · 380 m s. n. m.",
            },
            {
                "icon":  "🥕",
                "title": "Huerta de la cocina",
                "desc": "1 hectárea de huerta estacional · tomates San Marzano, fagioli zolfini, azafrán, hierbas aromáticas · nada de producto comprado para la mesa de Maria salvo los limones en invierno.",
                "place": "1 hectárea junto a la casa colona",
            },
            {
                "icon":  "🐖",
                "title": "Establo de Cinta Senese",
                "desc": "8 cabezas de Cinta Senese (cerdo negro) criadas en semilibertad · alimentación con bellota del bosque del podere y farro de la huerta · sacrificio local dos veces al año.",
                "place": "2,2 hectáreas de bosque con establo cubierto",
            },
        ],

        # Care items — list[4] of tuple[2]
        "care_label":   "Las cuatro promesas de la casa",
        "care_heading": "Hospitalidad campesina: pocas reglas, siempre respetadas.",
        "care_items": [
            ("Mesa larga siempre con Maria",
             "Cada cena la prepara y la sirve Maria. Cuando se sienta con "
             "ustedes, es porque ha terminado de servir — no para "
             "entretenerlos."),
            ("Nada de registro automático",
             "Carlo o Giovanni los reciben en el portón y los acompañan a la "
             "habitación. La llave es una llave de verdad, de hierro, con "
             "el nombre de la habitación. Nada de tarjetas magnéticas."),
            ("Desayuno hasta las 10:30",
             "Pan de Lorenzini caliente del horno del podere · mermeladas de "
             "las hermanas de San Vivaldo · miel de la colmena · huevos de "
             "las gallinas · café de la mezcla histórica del podere."),
            ("Envío a domicilio tras la estancia",
             "Cuando se marchan, la dispensa les prepara una caja de "
             "madera con seis productos del podere a su elección. Lo "
             "enviamos a casa en una semana · solo se paga el transporte."),
        ],

        # Press strip — list[5] of scalar str
        "press_label":   "Han hablado de la hospitalidad campesina del podere",
        "press_items": [
            "Slow Food Florencia",
            "Bell'Italia · Toscana rural",
            "Touring Club Italiano",
            "Gambero Rosso · Agriturismos 2025",
            "Vie del Gusto · Chianti Classico",
        ],

        # Journal teaser
        "journal_teaser_label":   "Del diario de campo",
        "journal_teaser_heading": "Tres voces desde Greve in Chianti.",
        "journal_teaser_link":    "Leer el diario",
        "journal_teaser_href":    "diario",

        # Final CTA
        "cta_label":          "Para reservar la mesa larga · hospitalidad campesina",
        "cta_heading":        "<em>Cuatro habitaciones</em>, una sola mesa larga, una sola familia.",
        "cta_intro":
            "Las cuatro habitaciones del podere se reservan directamente con "
            "Maria por WhatsApp o por teléfono. La mesa larga de la cena se "
            "reserva a la llegada · cocinamos para los que sean ustedes.",
        "cta_primary":        "Escriban a Maria por WhatsApp",
        "cta_primary_href":   "soggiorno",
        "cta_secondary":      "Teléfono directo en la cocina",
    },

    # ─── DISPENSA (shop · 8 farm products) ─────────────────────
    "dispensa": {
        "eyebrow":             "La dispensa campesina",
        "headline":            "Ocho productos del podere · envío a domicilio en Italia 24-48h.",
        "intro":
            "La dispensa es la prolongación natural de la cocina de Maria: "
            "los productos que ustedes comen en la mesa cuando son "
            "huéspedes, los encuentran aquí para llevárselos a casa. "
            "Envío refrigerado en verano y caja de madera con el sello "
            "del podere.",
        "filter_section_label": "Afinen la dispensa",
        "filter_groups": [
            {
                "label":   "Producción",
                "options": ["Aceite de oliva virgen extra", "Vino", "Conservas", "Embutidos", "Pasta · pan · dulces"],
            },
            {
                "label":   "Temporada",
                "options": ["Cosecha 2025", "Vendimias 2022-2024", "Extracción de julio", "Curación larga", "Siempre disponibles"],
            },
            {
                "label":   "Caja de madera",
                "options": ["Caja de 6 productos · elección libre", "Caja aceite + vino", "Caja desayuno (miel + mermelada + cantucci)", "Caja de embutidos"],
            },
        ],
        "sort_label":      "Ordenar",
        "sort_options": [
            "Por producción",
            "Por temporada",
            "Por curación",
            "Por disponibilidad",
        ],
        "result_count":    "8 productos del podere en la dispensa",
        "result_subtitle": "Seis con la marca del podere + dos de los productores del territorio · envío a domicilio en Italia 24-48h.",
        "featured_product_id": "olio-evo-podere-2025",

        # 8 products — full dict shape (11 keys per contract)
        "products": [
            {
                "id":         "olio-evo-podere-2025",
                "n":          "N.º 01",
                "image":      _OLIO_BOTTLE,
                "edition":    "Cosecha 2025",
                "name":       "Aceite de oliva virgen extra del Podere",
                "meta":       "Moraiolo 60 % + Frantoio 25 % + Leccino 15 % · prensado en frío en menos de 8 horas tras la recolección",
                "place":      "Greve in Chianti",
                "artisan":    "Maria + Carlo Pasquinelli",
                "price":      "€ 28 / 500 ml",
                "tag":        "Cosecha de noviembre",
                "available":  True,
            },
            {
                "id":         "chianti-classico-2022",
                "n":          "N.º 02",
                "image":      _VINO_BOTTLE,
                "edition":    "Vendimia 2022",
                "name":       "Chianti Classico DOCG",
                "meta":       "Sangiovese 95 % · Canaiolo 4 % · Colorino 1 % · barrica grande + 6 meses de botella",
                "place":      "Viña del podere · 1,8 ha · 380 m s. n. m.",
                "artisan":    "Giovanni Pasquinelli · enólogo del podere",
                "price":      "€ 22 / 750 ml",
                "tag":        "Bodega del podere",
                "available":  True,
            },
            {
                "id":         "vin-santo-2018",
                "n":          "N.º 03",
                "image":      _VINSANTO,
                "edition":    "Añada 2018 · crianza de 7 años",
                "name":       "Vin Santo del Chianti",
                "meta":       "Malvasia blanca + Trebbiano · pasificación 4 meses · caratelli de roble de 50 litros",
                "place":      "Desván del podere · caratelli históricos",
                "artisan":    "Carlo Pasquinelli · bodeguero",
                "price":      "€ 32 / 375 ml",
                "tag":        "Media botella",
                "available":  True,
            },
            {
                "id":         "miele-millefiori",
                "n":          "N.º 04",
                "image":      _MIELE,
                "edition":    "Extracción julio 2025",
                "name":       "Miel de mil flores",
                "meta":       "12 colmenas en claro de castaños · recolección de julio · ningún tratamiento químico · ninguna alimentación invernal",
                "place":      "Bosque del podere",
                "artisan":    "Anna Pasquinelli · apicultora",
                "price":      "€ 14 / 250 g",
                "tag":        "Cien por cien del podere",
                "available":  True,
            },
            {
                "id":         "marmellata-susine",
                "n":          "N.º 05",
                "image":      _MARMELLATA,
                "edition":    "Lote de agosto 2025",
                "name":       "Mermelada de ciruelas",
                "meta":       "Ciruelas claudia amarillas · azúcar 38 % · sin pectina añadida · cocción a fuego lento durante 4 horas",
                "place":      "Huerta del podere · 3 árboles históricos",
                "artisan":    "Maria Pasquinelli · cocina",
                "price":      "€ 9 / 280 g",
                "tag":        "Lote pequeño",
                "available":  True,
            },
            {
                "id":         "pecorino-toscano-dop",
                "n":          "N.º 06",
                "image":      _PECORINO,
                "edition":    "Curación 6 meses",
                "name":       "Pecorino Toscano DOP",
                "meta":       "Leche cruda de oveja · cuajo natural · curado en cueva · cepillado con aceite virgen extra del podere",
                "place":      "Lamole · a 4 km del podere",
                "artisan":    "Andrea Falleri · pastor",
                "price":      "€ 24 / pieza pequeña 600 g",
                "tag":        "Manos de Andrea",
                "available":  True,
            },
            {
                "id":         "salame-cinta-senese",
                "n":          "N.º 07",
                "image":      _SALAME,
                "edition":    "Curación 9 meses",
                "name":       "Salame de Cinta Senese",
                "meta":       "Cerdos Cinta Senese del podere · cría en semilibertad · sacrificio local · curación en bodega de piedra",
                "place":      "Establo del podere + charcutería Pieri en Castelfiorentino",
                "artisan":    "Davide Pieri · norcino",
                "price":      "€ 38 / pieza entera 700 g",
                "tag":        "8 cabezas en el establo",
                "available":  True,
            },
            {
                "id":         "cantucci-mandorle",
                "n":          "N.º 08",
                "image":      _CANTUCCI,
                "edition":    "Horneado semanal",
                "name":       "Cantucci de almendras",
                "meta":       "Almendras sin pelar · huevos del podere · azúcar de caña · receta de la abuela Annetta de 1948",
                "place":      "Horno del podere · cocina de Maria",
                "artisan":    "Maria Pasquinelli · cocina",
                "price":      "€ 12 / bolsa 250 g",
                "tag":        "Receta de la abuela Annetta",
                "available":  True,
            },
        ],

        "footer_note_label": "Envío y caja de madera",
        "footer_note":
            "Todos los productos se envían en caja de madera con el sello "
            "del podere · pedidos por encima de € 80 con envío gratuito en "
            "Italia · si no, € 12 fijos. La caja vuelve a su discreción · "
            "o bien se queda en casa como objeto de cocina.",
    },

    # ─── PRODOTTO (product page · featured = Aceite de oliva 2025) ───
    "prodotto": {
        "id":           "olio-evo-podere-2025",
        "n":            "N.º 01",
        "edition":      "Cosecha de noviembre 2025",
        "edition_note": "Añada 2025 limitada a 1.800 botellas · lote 23/01",
        "name":         "Aceite de oliva virgen extra del Podere",
        "subtitle":     "Moraiolo + Frantoio + Leccino · prensado en frío en menos de 8 horas",
        "price":        "€ 28 / botella 500 ml",
        "vat_note":     "IVA incluido · envío 24-48h en Italia",
        "intro":
            "El aceite de Podere Le Querce es el producto histórico de la "
            "casa · la familia Pasquinelli ha vendido siempre su propio "
            "aceite de oliva virgen extra de manera directa, desde los "
            "bisabuelos Mario y Annetta. La cosecha de 2025 la hicieron a "
            "mano una decena de personas (la familia más cuatro temporeros) "
            "entre el 6 y el 19 de noviembre · prensado en frío en menos de "
            "ocho horas. Hospitalidad campesina también en la botella.",

        # Gallery — list of scalar URL strings
        "gallery": [
            _OLIO_BOTTLE,
            _OLIVETO,
            _CUCINA_CONTADINA,
        ],

        "info_label": "Ficha técnica",
        # info_rows — list[10] of tuple[2]
        "info_rows": [
            ("Variedades",    "Moraiolo 60 % · Frantoio 25 % · Leccino 15 %"),
            ("Recolección",   "Manual · 6-19 de noviembre 2025"),
            ("Prensado",      "En frío · en menos de 8 horas · 27 °C máximo"),
            ("Acidez",        "0,18 % · por debajo del umbral de excelencia"),
            ("Polifenoles",   "412 mg/kg · valor alto"),
            ("Botella",       "Vidrio oscuro 500 ml · tapón de rosca metálico"),
            ("Lote",          "23/01 de 36 · etiqueta numerada a mano"),
            ("Conservación",  "Lugar fresco · al abrigo de la luz · antes de 18 meses"),
            ("Premios",       "Slow Food Presidio · Gambero Rosso 2 hojas 2025"),
            ("Disponibilidad", "1.800 botellas · disponibles hasta agotar existencias"),
        ],

        "size_label":      "Formatos disponibles",
        "size_intro":      "Botella individual de 500 ml, caja de 6 botellas con un descuento del 12 %, o lata de 3 litros para quienes cocinan mucho.",
        # size_options — list[4] of SCALAR strings
        "size_options": [
            "Botella 500 ml",
            "Caja de 6 botellas · 500 ml",
            "Lata 3 litros",
            "Bolsa regalo · 2 botellas + cantucci",
        ],
        "size_chart_link":   "Todos los formatos de la dispensa",
        "size_chart_href":   "dispensa",

        "artisan_label":     "Manos de",
        "artisan_name":      "Maria + Carlo Pasquinelli",
        "artisan_role":      "Cuarta generación · en el podere desde 1985",
        "artisan_bio":
            "Maria Pasquinelli (nacida en 1962) y Carlo Pasquinelli (nacido "
            "en 1960) tomaron las riendas del podere en 1985 tras la muerte "
            "de Mario, padre de Maria. Desde entonces cuidan el olivar en "
            "pareja · Carlo dirige la recolección a mano y Maria supervisa "
            "el prensado en la almazara cooperativa del Chianti. La familia "
            "no ha usado nunca pesticidas en el olivar.",
        "artisan_portrait":  _PORTRAIT_MARIA,

        "buy_primary":       "Añadir a la caja",
        "buy_secondary":     "Escriban a Maria por WhatsApp",
        "buy_note":
            "Para pedidos superiores a 12 botellas escriban directamente a "
            "la familia · les preparamos una caja especial y les calculamos "
            "el descuento. Pago contra reembolso en Italia, transferencia "
            "bancaria para Europa.",

        "care_label":  "Conservación y uso",
        "care_intro":
            "El aceite del podere es un aceite para consumir en crudo · sobre "
            "pan caliente, judías, ribollita, bruschetta toscana. "
            "Desaconsejado para frituras.",
        # care_items — list[5] of tuple[2]
        "care_items": [
            ("Temperatura", "Conservar a 14-18 °C · nada de nevera · nada de cocina caliente"),
            ("Luz",         "Botella de vidrio oscuro · proteger igualmente de la luz directa"),
            ("Consumo",     "Una vez abierta · terminarla en 4 meses · luego el sabor se atenúa"),
            ("Carácter",    "Verde, amargo y picante en equilibrio · afrutado medio-intenso"),
            ("Maridaje",    "Fagioli zolfini · pan sin sal · ribollita · bruschetta toscana"),
        ],

        "provenance_label":   "Del olivar a la botella",
        "provenance_heading": "Cuatro pasos a mano.",
        # provenance_steps — list[4] of 3-TUPLE (n, t, p)
        "provenance_steps": [
            ("01", "Recolección manual",       "Del 6 al 19 de noviembre de 2025 · 10 personas · 6 semanas de recolección a mano · cajas de plástico perforado"),
            ("02", "Transporte a la almazara", "El mismo día · en menos de 8 horas · 12 km hasta la almazara cooperativa del Chianti"),
            ("03", "Prensado en frío",         "27 °C máximo · extracción mecánica · sin añadir agua · sin calor"),
            ("04", "Embotellado",              "Marzo de 2026 · en el podere · botella de vidrio oscuro 500 ml · lote numerado a mano"),
        ],

        "related_label": "Otros productos del podere",
        "related_intro": "Los productos de la misma temporada que completan la caja.",
        # related_items — list[4] of dict[6 keys including n]
        "related_items": [
            {
                "id":    "chianti-classico-2022",
                "n":     "N.º 02",
                "image": _VINO_BOTTLE,
                "name":  "Chianti Classico DOCG · 2022",
                "meta":  "Vino de la misma añada histórica · perfecto con la caja de aceite",
                "price": "€ 22",
            },
            {
                "id":    "miele-millefiori",
                "n":     "N.º 04",
                "image": _MIELE,
                "name":  "Miel de mil flores",
                "meta":  "12 colmenas · claro de castaños · extracción de julio",
                "price": "€ 14",
            },
            {
                "id":    "marmellata-susine",
                "n":     "N.º 05",
                "image": _MARMELLATA,
                "name":  "Mermelada de ciruelas",
                "meta":  "Ciruelas claudia · lote de agosto · cocción lenta 4 horas",
                "price": "€ 9",
            },
            {
                "id":    "cantucci-mandorle",
                "n":     "N.º 08",
                "image": _CANTUCCI,
                "name":  "Cantucci de almendras",
                "meta":  "Receta de la abuela Annetta · horno semanal del podere",
                "price": "€ 12",
            },
        ],
    },

    # ─── FAMIGLIA (about · La familia Pasquinelli) ───────────
    "famiglia": {
        "eyebrow":  "La familia Pasquinelli",
        "headline": "Cuatro generaciones en Le Querce.",
        "intro":
            "El Podere Le Querce es la casa de la familia Pasquinelli desde "
            "noviembre de 1934. Los bisabuelos Mario y Annetta lo compraron "
            "a la familia Antinori con una escritura de compraventa "
            "conservada en el ayuntamiento. Desde entonces cuatro "
            "generaciones se han sucedido en el podere · hoy al timón están "
            "Maria y Carlo con sus hijos Giovanni y Anna.",

        "mission_label":   "Nuestra misión",
        "mission_heading": "Hospitalidad campesina, como la tienen ustedes en mente.",
        "mission_text":
            "Cocinamos para nuestros huéspedes la misma cocina que hacemos "
            "para nosotros · nada de menú de restaurante, nada de carro de "
            "quesos, nada de sumiller. Está Maria, que lleva a la mesa la "
            "ribollita que ha hecho esta mañana; Giovanni, que abre el vino "
            "que embotelló en primavera; Anna, que corta el pan que sacó "
            "del horno al alba.",

        "process_label":   "El calendario de la familia",
        "process_heading": "Cuatro estaciones, cuatro tiempos del podere.",
        # process_steps — list[4] of DICT[5 keys=n,title,place,desc,duration]
        "process_steps": [
            {
                "n":        "01",
                "title":    "Primavera · injerto y floración",
                "place":    "Olivar + viña + huerta",
                "desc":
                    "De marzo a mayo · injerto de las viñas, poda del olivar, "
                    "siembra de la huerta · las cuatro habitaciones reabren "
                    "tras el cierre técnico de enero. Mesa larga de Pascua "
                    "con cordero de Zeri.",
                "duration": "Tres meses · de marzo a mayo",
            },
            {
                "n":        "02",
                "title":    "Verano · cosecha y hospitalidad plena",
                "place":    "Todo el podere",
                "desc":
                    "De junio a agosto · plenitud de la temporada de "
                    "hospitalidad · mesas largas diarias de 12-16 huéspedes "
                    "· cosecha de la miel · siega del trigo · elaboración de "
                    "las conservas de verano (tomates, ciruelas, moras, "
                    "higos).",
                "duration": "Tres meses · de junio a agosto",
            },
            {
                "n":        "03",
                "title":    "Septiembre · vendimia",
                "place":    "Viña + bodega",
                "desc":
                    "Septiembre · vendimia manual del Sangiovese · "
                    "dieciocho días de trabajo continuo en la viña · "
                    "bodega cerrada al público durante las dos semanas "
                    "de vinificación · mesa larga de cierre de vendimia "
                    "con toda la familia y los temporeros.",
                "duration": "Un mes · septiembre",
            },
            {
                "n":        "04",
                "title":    "Otoño-invierno · aceite y cerdo",
                "place":    "Olivar + establo + cocina",
                "desc":
                    "Noviembre · recolección de aceitunas (seis semanas) · "
                    "diciembre, sacrificio de los Cinta Senese · enero, "
                    "elaboración de embutidos con el norcino Pieri · "
                    "febrero, cierre técnico del podere · marzo, "
                    "reapertura.",
                "duration": "Cinco meses · de noviembre a marzo",
            },
        ],

        "founder_label":    "La matriarca",
        "founder_heading":  "Maria Pasquinelli · en el podere desde 1985.",
        "founder_text":
            "Maria Pasquinelli (nacida en 1962) es la tercera generación del "
            "podere · hija de Giovanni y Maddalena Pasquinelli, nieta de los "
            "bisabuelos Mario y Annetta que compraron el podere a los "
            "Antinori. Tomó las riendas de la explotación en 1985 tras la "
            "muerte de su padre · casada con Carlo (de un podere vecino) "
            "desde 1987 · dos hijos, Giovanni (1990) y Anna (1993), que "
            "trabajan el podere a tiempo completo desde 2015. En la cocina "
            "desde las siete de la mañana, en la mesa larga de la noche con "
            "los huéspedes.",
        "founder_portrait":  _PORTRAIT_MARIA,
        "founder_caption":   "Maria Pasquinelli en la mesa larga del domingo · fotografía de Paolo Codeluppi · verano de 2024",

        "numbers_label": "El podere en cifras",
        # numbers_items — list[4] of tuple[2]
        "numbers_items": [
            ("92",  "Años de la familia Pasquinelli en el podere · desde 1934"),
            ("13",  "Hectáreas trabajadas directamente · olivar + viña + huerta + bosque"),
            ("4",   "Habitaciones de hospitalidad · toda la familia entre los fogones"),
            ("8",   "Productos de la dispensa · seis con la marca del podere + dos de los productores del territorio"),
        ],

        "visit_label":          "Para visitar el podere",
        "visit_heading":        "Mesa larga bajo reserva · o bien visita guiada.",
        "visit_text":
            "Visitas guiadas al podere bajo reserva · martes y jueves por la "
            "tarde (16 h) para huéspedes no residentes. Mesa larga de la "
            "noche (12-16 personas) bajo reserva con al menos 48 horas de "
            "antelación. Las cuatro habitaciones se reservan directamente "
            "con Maria · hospitalidad campesina sin intermediarios.",
        "visit_primary":         "Reserven la mesa larga",
        "visit_primary_href":    "soggiorno",
        "visit_secondary":       "WhatsApp directo a Maria",
    },

    # ─── DIARIO (journal · 3 entries) ─────────────────────────
    "diario": {
        "eyebrow":     "Diario de campo",
        "headline":    "Tres voces desde Greve in Chianti.",
        "intro":
            "El diario del podere recoge las voces de la familia · Maria "
            "escribe una vez al mes desde enero de 2018 · Giovanni y Anna "
            "añaden notas de temporada. Anotaciones de trabajo · no "
            "crónicas turísticas.",
        "list_label":  "Tres notas recientes",
        # entries — list[3] of dict[5 keys=n,title,place,excerpt,minutes]
        "entries": [
            {
                "n":       "001",
                "title":   "Vendimia 2025 · el día de la lluvia",
                "place":   "Viña · 14 de septiembre de 2025",
                "excerpt":
                    "La lluvia llegó la tarde del décimo día · seguimos "
                    "trabajando igualmente · solo tres hileras por terminar. "
                    "Giovanni metió la tinaja grande bajo la pérgola · "
                    "Maria abrió la cocina · a las diez de la noche "
                    "estábamos todos dentro con la sopa de col negra.",
                "minutes": "4 minutos de lectura",
            },
            {
                "n":       "002",
                "title":   "Cosecha de aceitunas 2025 · los árboles más ancianos",
                "place":   "Olivar · 12 de noviembre de 2025",
                "excerpt":
                    "Los árboles de más de doscientos años dieron este año "
                    "mucho menos · el calor de agosto los castigó. Carlo "
                    "dice que el árbol número 47 (el más anciano, con más "
                    "de 350 años según el cuaderno de 1923) dio solo 4 kg "
                    "este año frente a los 28 del año pasado. Seguiremos "
                    "cuidándolo.",
                "minutes": "3 minutos de lectura",
            },
            {
                "n":       "003",
                "title":   "Anna empieza con la apicultura · las primeras tres colmenas",
                "place":   "Bosque del podere · 22 de abril de 2025",
                "excerpt":
                    "Anna trajo a casa las primeras tres colmenas del curso "
                    "de apicultura de Vinci. Las colocó en el bosque del "
                    "podere, donde hay un claro de castaños. Maria dice que "
                    "su padre había tenido abejas hasta 1972 · luego ya no "
                    "hubo nadie. Veremos si pasan el invierno.",
                "minutes": "5 minutos de lectura",
            },
        ],
        "footer_note_label": "Para recibir el diario",
        "footer_note":
            "El diario no tiene boletín automático · si quieren recibirlo, "
            "escriban a Maria. Enviamos una edición impresa a final de año "
            "a los huéspedes que nos la piden.",
    },

    # ─── SOGGIORNO (contact · reserva de estancia) ────────────
    "soggiorno": {
        "eyebrow":  "Estancia · reserva directa",
        "headline": "Cuatro habitaciones, una sola mesa larga.",
        "intro":
            "Las cuatro habitaciones del podere se reservan directamente con "
            "la familia Pasquinelli · sin plataforma externa, sin comisiones "
            "intermediarias. Escriban a Maria · responde personalmente en el "
            "día, normalmente entre pausa y pausa de la cocina. Hospitalidad "
            "campesina desde el primer mensaje.",

        "form_section_label":   "Solicitud de estancia",
        "form_section_intro":
            "Indiquen las fechas deseadas, el número de huéspedes y "
            "cualquier petición especial · alergias, intolerancias, "
            "niños, animales. Maria responde desde la cocina en 24 horas.",
        "form_helper_required": "Los campos con · son obligatorios",
        "form_submit_button":   "Envíen a Maria",
        "form_submit_note":
            "Confirmación definitiva mediante señal del 30 % por "
            "transferencia bancaria · saldo a la llegada en la recepción "
            "del podere.",

        # form_fields — list[7] of dict[5 keys=label,name,type,required,placeholder] (+ optional rows)
        "form_fields": [
            {
                "label":       "Nombre y apellidos",
                "name":        "name",
                "type":        "text",
                "required":    True,
                "placeholder": "Cómo se presentan · Maria los llamará por su nombre",
            },
            {
                "label":       "Correo electrónico directo",
                "name":        "email",
                "type":        "email",
                "required":    True,
                "placeholder": "Maria responde desde famiglia@podereleQuerce.it",
            },
            {
                "label":       "WhatsApp · o teléfono",
                "name":        "phone",
                "type":        "tel",
                "required":    False,
                "placeholder": "+39 339 458 1126 · Maria responde también por WhatsApp",
            },
            {
                "label":       "Fecha de llegada",
                "name":        "arrival",
                "type":        "date",
                "required":    True,
                "placeholder": "",
            },
            {
                "label":       "Fecha de salida",
                "name":        "departure",
                "type":        "date",
                "required":    True,
                "placeholder": "",
            },
            {
                "label":       "Número de huéspedes",
                "name":        "guests",
                "type":        "number",
                "required":    True,
                "placeholder": "Adultos + niños",
            },
            {
                "label":       "Alergias, intolerancias, animales",
                "name":        "notes",
                "type":        "textarea",
                "required":    False,
                "placeholder": "Maria adapta la cocina · cuéntennoslo aquí",
                "rows":        5,
            },
        ],

        # Contact card
        "card_label":            "Para respuestas rápidas",
        "card_address_label":    "Dónde estamos",
        "card_address_value":    "Località Le Querce 14 · 50022 Greve in Chianti · Florencia",
        "card_phone_label":      "Cocina · Maria",
        "card_phone_value":      "+39 055 853 261",
        "card_whatsapp_label":   "WhatsApp directo",
        "card_whatsapp_value":   "+39 339 458 1126 · Maria",
        "card_email_label":      "Correo electrónico",
        "card_email_value":      "famiglia@podereleQuerce.it",
        "card_hours_label":      "Horarios",
        # card_hours_rows — list of SCALAR strings
        "card_hours_rows": [
            "Cocina abierta todo el año · comida 12:30 · cena 19:30",
            "Recepción de huéspedes 8-22 · Maria en la cocina desde las 7",
            "Dispensa 9-19 · domingo cerrado (mercado de Greve)",
            "Cierre técnico · del 1 al 28 de febrero",
        ],
        "card_directions_label": "Cómo llegar",
        "card_directions_text":
            "Desde Florencia, 28 km · salida de la autopista A1 Florencia "
            "Sur · seguir la Chiantigiana · 12 km después de Greve in "
            "Chianti girar a la derecha hacia Lamole · 1,4 km desde el "
            "cruce. Portón de madera con el rótulo «Podere Le Querce» "
            "hecho a mano · llamen al timbre.",

        "faq_label": "Preguntas desde la cocina",
        # faq_items — list[5] of DICT[2 keys=q,a]
        "faq_items": [
            {
                "q": "¿Se paga la mesa larga aunque seamos huéspedes de las habitaciones?",
                "a":
                    "Sí · la cocina y el alojamiento son dos cosas "
                    "distintas · las habitaciones se pagan por noche y la "
                    "mesa larga se paga aparte · 35 € por persona para "
                    "cena, 28 € para comida (vino del podere incluido). El "
                    "desayuno, en cambio, está incluido en el precio de la "
                    "habitación. Es nuestra forma de hospitalidad "
                    "campesina, sin sorpresas.",
            },
            {
                "q": "¿Se admiten niños y animales?",
                "a":
                    "Los niños son bienvenidos · tenemos cunas para los "
                    "más pequeños y tronas para los más grandes · Anna se "
                    "encarga a menudo de llevarlos al establo a ver los "
                    "Cinta Senese. Los perros pequeños se admiten en las "
                    "habitaciones de la planta baja (suplemento de 15 € "
                    "por noche) · los grandes, en el patio y en el bosque, "
                    "pero no en habitación ni en cocina.",
            },
            {
                "q": "¿Se puede visitar el podere sin dormir aquí?",
                "a":
                    "Sí · martes y jueves por la tarde (16 h, duración 90 "
                    "minutos, bajo reserva con al menos 24 horas de "
                    "antelación) Carlo lleva a los visitantes al olivar y "
                    "a la bodega · 20 € por persona · cata de aceite + "
                    "vino + miel incluida. Sin reserva, la dispensa está "
                    "abierta de todas formas todos los días de 9 a 19.",
            },
            {
                "q": "¿Se puede reservar el podere entero para bodas u otros eventos?",
                "a":
                    "Sí, para bodas íntimas · un máximo de 36 invitados · "
                    "ceremonia civil en el jardín bajo la pérgola de "
                    "glicinas · mesa larga bajo el henar restaurado · "
                    "escriban a Maria con al menos ocho meses de "
                    "antelación. No organizamos bodas con más de 36 "
                    "invitados ni eventos de empresa.",
            },
            {
                "q": "¿Se pueden comprar los productos sin venir al podere?",
                "a":
                    "Sí · la dispensa envía a toda Italia (24-48 horas, "
                    "envío gratuito por encima de € 80) y a Europa (4-6 "
                    "días). Caja de madera con el sello del podere · "
                    "vuelve a su discreción · para pedidos por encima de "
                    "12 botellas escriban directamente a Maria por un "
                    "descuento.",
            },
        ],
    },
}
