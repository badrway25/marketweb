"""Sapori di Langa — Enoteca dei Vignaioli (artisan-workshop archetype) · ES.

Wave 1 Pass-10 (T54 · 2026-05-12). Spanish (peninsular) translation of
the IT template, mirroring `template_content_sapori.py` exactly: same
keys, same list lengths, same tuple arities, same image constants.

Voice contract (ES — Peninsular):
- Register: El País Gastro / Verema / Vinetur / Sobremesa · castellano
  peninsular cuidado · sumiller-pacato · terroir-curatorial.
- Treatment: `usted` formal throughout (cavista premium dirigiéndose
  a un coleccionista exigente · distinct from Bottega's `tú`).
- Voice anchor `vignaiolo indipendente` → `viticultor independiente`
  (plural `viticultores independientes`). Verbatim across all bands.
  This is the consecrated Spanish wine term for the same concept.
- Lexicon: "vino", "bodega", "añada", "crianza", "vendimia manual",
  "fermentación espontánea", "tonel grande de roble de Eslavonia",
  "sin barrica", "embotellado en luna menguante", "cata / vertical",
  "caja de seis", "sumiller" (Peninsular over "sommelier"), "añada
  cálida / añada fresca".
- Italian/Latin proper names preserved verbatim: brand Sapori di
  Langa · Enoteca dei Vignaioli, personas Pietro Brero · Federica
  Brero, cantine Brezza & Figli · Vajra · Boasso · Brovia, parcelas
  Cannubi · Bricco delle Viole · Gabutti · Villero · Bricco Sarmassa
  · Cannubi Muscatel · Rabajà, denominaciones Barolo · Barbaresco ·
  Roero · Langhe · Monferrato, vitigni Nebbiolo · Barbera · Dolcetto
  · Arneis, productos PDO/DOC Olio EVO · Castelmagno DOP · Nocciola
  Tonda Gentile · Tartufo Bianco. Order `Cavalier dell'Ordine dei
  Cavalieri del Tartufo e dei Vini di Alba` stays IT (glosado una vez
  como "Caballero de la Orden de los Caballeros de la Trufa y de los
  Vinos de Alba"). Press names (Slow Wine · Gambero Rosso Vini · Vitae
  AIS · I Vini di Veronelli · Doctor Wine) verbatim. Domaine Romanée-
  Conti verbatim.
- Headline anchor: `Vinos de <em>viticultor independiente</em> de las
  Langhe del Barolo.` — <em>...</em> tags preserved verbatim.

Shape parity guaranteed against SAPORI_CONTENT_IT: 179 leaf paths ·
zero missing · zero extra · same image URL constants.
"""
from __future__ import annotations

from typing import Any


# Imagery URLs from X.3 curator pack `wine-food-boutique.md`. All
# Pexels CC0 · commercial-safe. Re-declared verbatim from the IT file
# so the ES module is self-contained.
_VIGNAIOLO_PORTRAIT_PIETRO = (
    "https://images.pexels.com/photos/8472892/pexels-photo-8472892.jpeg"
    "?auto=compress&cs=tinysrgb&w=600&h=800&fit=crop"
)
_VIGNAIOLO_PORTRAIT_CARLO = (
    "https://images.pexels.com/photos/8472933/pexels-photo-8472933.jpeg"
    "?auto=compress&cs=tinysrgb&w=600&h=800&fit=crop"
)
_VIGNAIOLO_PORTRAIT_MARIA = (
    "https://images.pexels.com/photos/8472896/pexels-photo-8472896.jpeg"
    "?auto=compress&cs=tinysrgb&w=600&h=800&fit=crop"
)
_VIGNAIOLO_PORTRAIT_LUIGI = (
    "https://images.pexels.com/photos/5946081/pexels-photo-5946081.jpeg"
    "?auto=compress&cs=tinysrgb&w=600&h=800&fit=crop"
)
_FOUNDER_PORTRAIT = (
    "https://images.pexels.com/photos/8472944/pexels-photo-8472944.jpeg"
    "?auto=compress&cs=tinysrgb&w=800&h=1000&fit=crop"
)
_BOTTLE_BAROLO = (
    "https://images.pexels.com/photos/1407847/pexels-photo-1407847.jpeg"
    "?auto=compress&cs=tinysrgb&w=900&h=1200&fit=crop"
)
_BOTTLE_BARBERA = (
    "https://images.pexels.com/photos/1123260/pexels-photo-1123260.jpeg"
    "?auto=compress&cs=tinysrgb&w=900&h=1200&fit=crop"
)
_BOTTLE_OLIO = (
    "https://images.pexels.com/photos/33783/olive-oil-salad-dressing-cooking-olive.jpg"
    "?auto=compress&cs=tinysrgb&w=900&h=1200&fit=crop"
)
_BOTTLE_FORMAGGIO = (
    "https://images.pexels.com/photos/821365/pexels-photo-821365.jpeg"
    "?auto=compress&cs=tinysrgb&w=900&h=1200&fit=crop"
)


SAPORI_CONTENT_ES: dict[str, Any] = {
    "pages": [
        {"slug": "home",     "label": "Bodega",            "kind": "home"},
        {"slug": "shop",     "label": "Catálogo",          "kind": "shop"},
        {"slug": "product",  "label": "Botella",           "kind": "product"},
        {"slug": "atelier",  "label": "Los viticultores",  "kind": "about"},
        {"slug": "journal",  "label": "Diario",            "kind": "journal"},
        {"slug": "contatti", "label": "Visita & pedidos",  "kind": "contact"},
    ],

    "site": {
        "logo_initial": "S",
        "logo_word":    "Sapori di Langa",
        "tag":          "Enoteca de viticultores independientes · Alba · desde 1992",
        "phone":        "+39 0173 364 990",
        "whatsapp":     "0173 364 990",
        "whatsapp_link": "https://wa.me/390173364990",
        "email":        "enoteca@saporidilanga.it",
        "address":      "Via Vittorio Emanuele 38 · 12051 Alba CN",
        "hours_compact": "Mar – Sáb · 9:30 – 19:30 · Dom 10 – 13",
        "hours_footer_rows": [
            "Domingo · 10:00 – 13:00 (solo mañanas)",
            "Lunes · cerrado",
            "Feria de la Trufa · horario continuo Oct – Nov",
        ],
        "license":      "P.IVA 02814730042 · CCIAA Cuneo REA 263118",
        "footer_intro":
            "Enoteca de Alba fundada en 1992 por Pietro Brero. "
            "Treinta y dos viticultores independientes de las Langhe, del "
            "Roero y del Monferrato, cada uno con su propio número de lote, "
            "su firma al pie de la cuvée y su parcela vinificada en pureza. "
            "Envío refrigerado en 48 horas a toda Italia.",
        "nav_cta":      "Pida la caja del viticultor independiente",
        "nav_cta_kind": "case-order",

        "foot_studio":   "La enoteca",
        "foot_pages":    "Mapa del sitio",
        "foot_contact":  "Pedidos & visitas",
        "foot_stockists":"Restaurantes que nos eligen",
        "stockists_rows": [
            "Piazza Duomo · Alba · 3 estrellas Michelin",
            "La Ciau del Tornavento · Treiso",
            "Locanda del Pilone · Madonna di Como",
            "Antica Corona Reale · Cervere",
        ],

        "currency_symbol":  "€",
        "shop_filter_label": "Filtros",
        "shop_count_unit":   "botellas",
        "edition_label":     "Lote",
        "made_in_label":     "Vinificado en",
        "artisan_label":     "Viticultor",
        "material_label":    "Variedad",
        "shipping_label":    "Envío",
        "shipping_value":    "Refrigerado en 48 horas · seis botellas por caja",
        "guarantee_label":   "Garantía",
        "guarantee_value":   "Botella defectuosa sustituida sin coste",
    },

    # ─── HOME ──────────────────────────────────────────────────
    "home": {
        "eyebrow":  "Añada 2023 · treinta y dos viticultores independientes en bodega",
        "headline": "Vinos de <em>viticultor independiente</em> de las Langhe del Barolo.",
        "intro":
            "Vamos dos veces al año a la viña. Una para la vendimia y otra "
            "para catar las añadas en tonel. De cada bodega conocemos al "
            "enólogo por su nombre, la parcela vinificada y el lote "
            "embotellado. Ningún vino llega aquí desde un catálogo "
            "mayorista.",
        "primary_cta":   "Pida la caja del viticultor independiente",
        "primary_href":  "shop",
        "secondary_cta": "Visite la enoteca",
        "secondary_href":"contatti",

        # Stamp-aside data
        "stamp_label":  "Nuestra regla",
        "stamp_heading":"Dos viajes, <em>una botella.</em>",
        "stamp_rows": [
            ("Viticultores independientes", "32 bodegas"),
            ("Etiquetas",    "180 en carta"),
            ("Vendimia",     "Siempre manual"),
            ("Caja",         "6 botellas"),
        ],
        "stamp_footer": "Lote numerado · envío refrigerado",
        "stamp_corner_index": "01",
        "stamp_corner_word":  "LA ENOTECA",

        # Latest-arrived band — 4 bottles
        "latest_label":   "Recién entradas en carta",
        "latest_heading": "Las últimas añadas <em>de las Langhe.</em>",
        "latest_link_label": "Todo el catálogo",
        "latest_link_href":  "shop",
        "latest_items": [
            {
                "id":       "barolo-cannubi-2019",
                "n":        "Cuvée 2019",
                "edition":  "Lote 23 / 280",
                "name":     "Barolo Cannubi",
                "meta":     "Nebbiolo 100% · Barolo · La Morra",
                "price":    "58 €",
                "tag":      "Añada",
                "image":    _BOTTLE_BAROLO,
            },
            {
                "id":       "barbera-superiore-2021",
                "n":        "Cuvée 2021",
                "edition":  "Lote 87 / 1.200",
                "name":     "Barbera d'Alba Superiore",
                "meta":     "Barbera 100% · Roero",
                "price":    "22 €",
                "tag":      "Diario",
                "image":    _BOTTLE_BARBERA,
            },
            {
                "id":       "olio-evo-langhe",
                "n":        "Cosecha 2024",
                "edition":  "Lote 12 / 380",
                "name":     "Olio EVO Langhe DOP",
                "meta":     "Frantoio + Leccino · Diano d'Alba",
                "price":    "28 €",
                "tag":      "Temporada",
                "image":    _BOTTLE_OLIO,
            },
            {
                "id":       "castelmagno-stagionato",
                "n":        "Curación 18 meses",
                "edition":  "Pieza 04 / 22",
                "name":     "Castelmagno DOP d'Alpeggio",
                "meta":     "Leche de vaca · Castelmagno CN",
                "price":    "36 €",
                "tag":      "Despensa",
                "image":    _BOTTLE_FORMAGGIO,
            },
        ],

        # Vignaioli band — 4 named vintners
        "makers_label":   "Manos que vinifican",
        "makers_heading": "Treinta y dos bodegas, <em>una sola carta.</em>",
        "makers_intro":
            "Trabajamos únicamente con viticultores independientes — quien "
            "vinifica su propia uva en su propia parcela y firma de su "
            "puño cada lote en carta. Cada bodega ha sido visitada por "
            "Pietro al menos tres veces antes de entrar en el catálogo.",
        "makers": [
            {
                "name":   "Carlo Brezza",
                "craft":  "Viticultor independiente · Cannubi histórico",
                "place":  "Barolo (CN)",
                "since":  "Viñedo de 1885 · Brezza desde 1885",
                "quote":  "«El Barolo no se hace con prisa. Se hace con "
                          "silencio: dos años en tonel grande, y el oído "
                          "atento para escuchar si la madera canta o se "
                          "queja.»",
                "portrait": _VIGNAIOLO_PORTRAIT_CARLO,
            },
            {
                "name":   "Maria Vajra",
                "craft":  "Viticultora independiente · Bricco delle Viole",
                "place":  "Vergne · Barolo (CN)",
                "since":  "Bodega familiar desde 1972",
                "quote":  "«Vinificamos solo aquello que vemos crecer. Si "
                          "una parcela no rinde como debe, esa añada no la "
                          "embotellamos. La carta de los viticultores se "
                          "hace también con lo que no está.»",
                "portrait": _VIGNAIOLO_PORTRAIT_MARIA,
            },
            {
                "name":   "Luigi Boasso",
                "craft":  "Viticultor independiente · Gabutti Roccaforte",
                "place":  "Serralunga d'Alba (CN)",
                "since":  "Cuatro generaciones en la viña",
                "quote":  "«El Nebbiolo es una uva engañosa. Se convierte "
                          "en lo que le cuentas del suelo. Por eso no "
                          "trabajo otras parcelas: aprender un solo "
                          "terreno exige treinta años.»",
                "portrait": _VIGNAIOLO_PORTRAIT_LUIGI,
            },
            {
                "name":   "Anna Brovia",
                "craft":  "Viticultora independiente · Villero & Rocche dei Brovia",
                "place":  "Castiglione Falletto (CN)",
                "since":  "Bodega de los Brovia desde 1863",
                "quote":  "«No nos presentamos a concursos, no buscamos "
                          "puntuaciones. Hacemos Barolo como siempre se "
                          "ha hecho en Castiglione Falletto: largo, "
                          "austero, sin adornos. Quien busque lo fácil, "
                          "que vaya a otra parte.»",
                "portrait": _VIGNAIOLO_PORTRAIT_PIETRO,
            },
        ],

        # Provenance — terroir + filiera
        "provenance_label":   "De dónde viene",
        "provenance_heading": "Sesenta y cinco kilómetros, <em>tres denominaciones.</em>",
        "provenance_intro":
            "Todas las etiquetas en carta provienen de un radio de "
            "sesenta y cinco kilómetros alrededor de Alba. Tres "
            "denominaciones principales — Langhe, Roero, Monferrato — y "
            "una red de viticultores independientes que se han elegido "
            "los unos a los otros.",
        "provenance_items": [
            {
                "icon": "vine",
                "title": "Langhe DOCG",
                "desc":  "Barolo, Barbaresco, Dolcetto · once municipios "
                         "de producción · suelos calcáreos y margosos · "
                         "altitud 200-400 m s. n. m.",
                "place": "Alba · La Morra · Barolo · Castiglione",
            },
            {
                "icon": "hills",
                "title": "Roero DOCG",
                "desc":  "Nebbiolo Roero, Arneis, Favorita · al otro "
                         "lado del Tanaro · suelos arenosos · vinos más "
                         "ligeros y aromáticos · altitud 280-380 m s. n. m.",
                "place": "Canale · Vezza · Santo Stefano Roero",
            },
            {
                "icon": "cheese",
                "title": "Monferrato Casalese",
                "desc":  "Barbera Superiore, Grignolino, Ruchè · laderas "
                         "colinares · suelos calcáreo-arcillosos · vinos "
                         "diarios de carácter.",
                "place": "Casale · Vignale · Rosignano",
            },
            {
                "icon": "olive",
                "title": "Riviera ligure (50 km)",
                "desc":  "Olio EVO Taggiasco DOP · sal de Trapani al "
                         "carbón vegetal · caballa en aceite de La "
                         "Spezia. Proveedores históricos de la casa.",
                "place": "Imperia · La Spezia · Trapani",
            },
        ],

        # Care — wine handling guarantees
        "care_label":   "Cómo llega, cómo se conserva",
        "care_heading": "Cuatro promesas de caja.",
        "care_items": [
            ("Envío refrigerado",
             "Caja de seis botellas enviada en embalaje térmico con "
             "gel pack a 14 °C. Entrega en 48 horas a toda Italia · "
             "4 días a Europa Occidental."),
            ("Lote numerado al pie",
             "Cada botella lleva escrito a mano el número de lote, la "
             "añada de la cuvée y la firma del viticultor. Sin "
             "etiqueta industrial-tipográfica."),
            ("Sustitución de botella defectuosa",
             "TCA, oxidación, rotura en tránsito · sustitución sin "
             "coste dentro de los tres meses siguientes a la entrega · "
             "basta con prueba fotográfica del corcho o del nivel."),
            ("Consejos del sumiller",
             "Pietro o Federica le devolverán la llamada en 24 horas "
             "si necesita un maridaje para una velada, una vertical "
             "para un cumpleaños o una caja para un regalo de empresa."),
        ],

        # Press band — Italian wine press
        "press_label": "Reseñados en",
        "press_items": ["Slow Wine", "Gambero Rosso Vini", "Vitae AIS",
                        "I Vini di Veronelli", "Doctor Wine"],

        # Journal teaser
        "journal_teaser_label":   "Notas de diario",
        "journal_teaser_heading": "Cómo hemos construido la <em>carta de otoño 2026.</em>",
        "journal_teaser_link":    "Lea el diario",
        "journal_teaser_href":    "journal",

        # CTA section
        "cta_label":     "Pedidos · visitas · escríbanos",
        "cta_heading":   "Una caja de seis botellas, <em>elegida por Pietro.</em>",
        "cta_intro":
            "Las cajas seleccionadas cambian cada mes según las bodegas "
            "en reparto. Vino para el día a día, vinos para guarda, "
            "fórmulas mixtas con aceite y quesos. Se paga al retirar y "
            "se envía refrigerado en 48 horas.",
        "cta_primary":      "Pida la caja del mes",
        "cta_primary_href": "shop",
        "cta_secondary":    "Venga a la enoteca",
    },

    # ─── SHOP (catalog) ─────────────────────────────────────────
    "shop": {
        "eyebrow":  "Carta de la casa · añada 2023-2024",
        "headline": "Ciento ochenta etiquetas, <em>una sola firma.</em>",
        "intro":
            "Carta de vinos, aceites, quesos y conservas. Todas las "
            "etiquetas provienen de viticultores independientes visitados "
            "personalmente. Para cada vino se indica la cuvée, el lote, "
            "la añada y el viticultor independiente que firma.",

        "filter_section_label": "Filtros",
        "filter_groups": [
            {
                "label": "Denominación",
                "options": ["Barolo DOCG", "Barbaresco DOCG", "Roero DOCG",
                            "Langhe DOC", "Monferrato DOC", "Asti DOCG",
                            "Vino de mesa"],
            },
            {
                "label": "Variedad",
                "options": ["Nebbiolo", "Barbera", "Dolcetto", "Arneis",
                            "Favorita", "Grignolino"],
            },
            {
                "label": "Tipología",
                "options": ["Vinos tintos", "Vinos blancos", "Vinos dulces",
                            "Espumosos", "Aceites & condimentos", "Quesos",
                            "Embutidos & conservas"],
            },
        ],

        "sort_label": "Ordenar por",
        "sort_options": ["Más recientes", "Viticultor independiente", "Añada", "Precio"],

        "result_count": "180 botellas",
        "result_subtitle": "Actualizado el martes 8 de octubre de 2026",

        # Sample products — 8 cards (the shop shows more but this is the
        # featured slice)
        "products": [
            {
                "id":       "barolo-cannubi-2019",
                "n":        "01",
                "edition":  "Cuvée 2019 · Lote 23",
                "name":     "Barolo Cannubi · Brezza",
                "meta":     "Nebbiolo · Barolo · La Morra",
                "price":    "58 €",
                "tag":      "Añada",
                "image":    _BOTTLE_BAROLO,
            },
            {
                "id":       "barbaresco-rabaja-2018",
                "n":        "02",
                "edition":  "Cuvée 2018 · Lote 11",
                "name":     "Barbaresco Rabajà · Cortese",
                "meta":     "Nebbiolo · Barbaresco · Treiso",
                "price":    "64 €",
                "tag":      "Vertical",
                "image":    _BOTTLE_BAROLO,
            },
            {
                "id":       "barbera-superiore-2021",
                "n":        "03",
                "edition":  "Cuvée 2021 · Lote 87",
                "name":     "Barbera d'Alba Superiore · Vajra",
                "meta":     "Barbera · Roero · Canale",
                "price":    "22 €",
                "tag":      "Diario",
                "image":    _BOTTLE_BARBERA,
            },
            {
                "id":       "dolcetto-diano-2022",
                "n":        "04",
                "edition":  "Cuvée 2022 · Lote 42",
                "name":     "Dolcetto di Diano d'Alba · Boasso",
                "meta":     "Dolcetto · Diano d'Alba",
                "price":    "16 €",
                "tag":      "De mesa",
                "image":    _BOTTLE_BARBERA,
            },
            {
                "id":       "arneis-roero-2023",
                "n":        "05",
                "edition":  "Cuvée 2023 · Lote 56",
                "name":     "Roero Arneis · Brovia",
                "meta":     "Arneis · Vezza d'Alba",
                "price":    "18 €",
                "tag":      "Blanco",
                "image":    _BOTTLE_BARBERA,
            },
            {
                "id":       "olio-evo-langhe",
                "n":        "06",
                "edition":  "Cosecha 2024 · Lote 12",
                "name":     "Olio EVO Langhe DOP · Frantoio Anfossi",
                "meta":     "Frantoio + Leccino · Diano d'Alba",
                "price":    "28 €",
                "tag":      "Temporada",
                "image":    _BOTTLE_OLIO,
            },
            {
                "id":       "castelmagno-stagionato",
                "n":        "07",
                "edition":  "Curación 18 meses · Pieza 04",
                "name":     "Castelmagno DOP d'Alpeggio",
                "meta":     "Leche de vaca piamontesa",
                "price":    "36 €",
                "tag":      "Queso",
                "image":    _BOTTLE_FORMAGGIO,
            },
            {
                "id":       "salame-cuneo",
                "n":        "08",
                "edition":  "Curación 4 meses · Lote 08",
                "name":     "Salame Cuneo · Macelleria Cesare",
                "meta":     "Cerdo de Cuneo · pimienta negra · vino en el corte",
                "price":    "24 €",
                "tag":      "Chacinería",
                "image":    _BOTTLE_FORMAGGIO,
            },
        ],

        "featured_product_id": "barolo-cannubi-2019",

        "footer_note_label": "Envíos & recogidas",
        "footer_note":
            "Envío refrigerado en 48 horas a toda Italia · caja mínima "
            "de seis botellas · gastos de envío 12 € (gratuito a partir "
            "de 200 €). Recogida en la enoteca sin previo aviso. Para "
            "pedidos superiores a doce botellas, contacte directamente.",
    },

    # ─── PRODUCT ────────────────────────────────────────────────
    "product": {
        "id":       "barolo-cannubi-2019",
        "n":        "01",
        "edition":  "Cuvée 2019",
        "edition_note": "Lote 23 / 280 · embotellado en diciembre de 2022",
        "name":     "Barolo Cannubi · Brezza",
        "subtitle": "Nebbiolo 100% · vinificado en la colina histórica de Cannubi",
        "price":    "58 €",
        "vat_note": "IVA incluido · caja mínima de seis botellas",
        "intro":
            "Barolo de la bodega Brezza, parcela de Cannubi histórico "
            "(la colina más antigua del municipio de Barolo, vendimia "
            "documentada desde 1752). Vendimia manual, fermentación "
            "espontánea en depósitos de acero, crianza en tonel grande "
            "de roble de Eslavonia durante 30 meses, otros 12 meses en "
            "botella antes de la salida.",

        "gallery": [
            _BOTTLE_BAROLO,
            _BOTTLE_BAROLO,
            _BOTTLE_BAROLO,
        ],

        "info_label": "Ficha técnica",
        "info_rows": [
            ("Viticultor independiente", "Carlo Brezza · Brezza & Figli"),
            ("Denominación",  "Barolo DOCG"),
            ("Variedad",      "Nebbiolo 100%"),
            ("Municipio",     "Barolo (CN)"),
            ("Parcela",       "Cannubi histórico"),
            ("Altitud",       "260 m s. n. m. · orientación sureste"),
            ("Vendimia",      "Manual · segunda semana de octubre de 2019"),
            ("Crianza",       "30 meses en tonel grande + 12 en botella"),
            ("Graduación",    "14,5% vol"),
            ("Sulfitos",      "< 80 mg/l · viticultura ecológica certificada"),
        ],

        "size_label": "Formatos disponibles",
        "size_intro": "Disponible en botella individual, magnum, caja horizontal 2019 y caja vertical 2015 – 2019.",
        "size_options": ["750 ml", "1,5 L Magnum", "Caja 6 · 2019", "Caja 6 · vertical"],
        "size_chart_link": "Ver todos los formatos & verticales",
        "size_chart_href": "shop",

        "artisan_label":   "Viticultor independiente",
        "artisan_name":    "Carlo Brezza",
        "artisan_role":    "Cuarta generación · Brezza & Figli desde 1885",
        "artisan_bio":
            "Bodega familiar fundada por el bisabuelo de Carlo en 1885, "
            "transmitida en línea directa de padre a hijo. Carlo entró "
            "en la viña en 1997 tras los estudios de enología en Alba "
            "y tres vendimias en Domaine Romanée-Conti. Vinifica "
            "exclusivamente las parcelas de propiedad familiar (Cannubi "
            "histórico, Bricco Sarmassa, Cannubi Muscatel) — nunca con "
            "uva comprada.",
        "artisan_portrait": _VIGNAIOLO_PORTRAIT_CARLO,

        "buy_primary":   "Añadir a la caja",
        "buy_secondary": "Reserve en la enoteca",
        "buy_note":
            "Para pedidos superiores a 12 botellas · contacte "
            "directamente con la bodega. Disponibilidad verificada en "
            "el momento del pedido.",

        "care_label": "Conservación",
        "care_intro":
            "Barolo de guarda · requiere una conservación cuidadosa para "
            "expresar todo su potencial.",
        "care_items": [
            ("Temperatura",  "12-14 °C constantes · sin oscilaciones"),
            ("Posición",     "Horizontal · corcho siempre en contacto con el vino"),
            ("Humedad",      "Al menos 70% · ambiente oscuro"),
            ("Apertura",     "Abrir 2-3 horas antes · decantación recomendada"),
            ("Plateau",      "Listo para beber 2025-2040 · plateau de madurez 2028-2035"),
        ],

        "provenance_label":   "De Cannubi a la copa",
        "provenance_heading": "Cuatro pasos trazados.",
        "provenance_steps": [
            ("01", "Vendimia",       "Recogida manual en cajas de 18 kg · Cannubi a 260 m s. n. m. · segunda semana de octubre de 2019"),
            ("02", "Crianza",        "Tonel grande de roble de Eslavonia · 30 meses · nunca en barrica francesa · Bodega Brezza Barolo"),
            ("03", "Embotellado",    "Diciembre de 2022 · sin filtración · sin clarificación · lote 23 de 280"),
            ("04", "Envío",          "Caja de madera estampada · embalaje térmico con gel pack a 14 °C · 48 horas a toda Italia"),
        ],

        "related_label":   "Verticales y maridajes",
        "related_intro":
            "Cuvées de la misma bodega en añadas anteriores y vinos "
            "que Pietro recomienda como contraste.",
        "related_items": [
            {"id":"barolo-cannubi-2018",   "n":"N.º 088","name":"Barolo Cannubi · 2018",   "meta":"Añada fresca · Brezza",            "price":"62 €","image":_BOTTLE_BAROLO},
            {"id":"barolo-cannubi-2017",   "n":"N.º 074","name":"Barolo Cannubi · 2017",   "meta":"Añada cálida · Brezza",            "price":"68 €","image":_BOTTLE_BAROLO},
            {"id":"barbaresco-rabaja-2018","n":"N.º 142","name":"Barbaresco Rabajà · 2018","meta":"Contraste territorial",             "price":"64 €","image":_BOTTLE_BAROLO},
            {"id":"barbera-vajra",         "n":"N.º 211","name":"Barbera Superiore · 2021","meta":"Diario en la mesa · Vajra",         "price":"22 €","image":_BOTTLE_BARBERA},
        ],
    },

    # ─── ATELIER (about · "Los viticultores") ──────────────────
    "atelier": {
        "eyebrow":  "La enoteca",
        "headline": "Sapori di Langa: <em>treinta y dos viticultores independientes, una sola enseña.</em>",
        "intro":
            "Sapori di Langa es una enoteca independiente fundada en "
            "Alba en 1992. Trabajamos exclusivamente con viticultores "
            "independientes que vinifican por su cuenta · sin "
            "cooperativas · sin vinos industriales · sin etiquetas "
            "construidas sobre el papel. Para entrar en carta, la "
            "bodega de cada viticultor independiente es visitada al "
            "menos tres veces por Pietro.",

        "mission_label":   "Nuestra misión",
        "mission_heading": "Pagar al viticultor lo que es justo.",
        "mission_text":
            "La enoteca existe por una razón: devolver al viticultor "
            "independiente el precio que su trabajo merece. Margen "
            "acordado con transparencia, contratos anuales firmados a "
            "mano, anticipos sobre la uva en viña si hace falta. No "
            "vendemos «descuentos», porque quien hace Nebbiolo al 14% "
            "no puede descontar nada, y un viticultor independiente "
            "menos que nadie.",

        "process_label":   "Cómo elegimos las etiquetas",
        "process_heading": "Tres visitas, una carta.",
        "process_steps": [
            {"num": "01", "title": "Primera visita · primavera",
             "desc": "Pietro va a la viña en marzo o abril, observa la "
                     "poda, cata las últimas añadas desde los toneles y "
                     "habla con el viticultor independiente de cómo "
                     "fue el verano anterior."},
            {"num": "02", "title": "Segunda visita · vendimia",
             "desc": "Septiembre-octubre · presencia durante una jornada "
                     "de vendimia junto al viticultor independiente, al "
                     "menos tres cajas abiertas. Se observa a quién hay "
                     "en viña recogiendo y con qué cuidado."},
            {"num": "03", "title": "Tercera visita · cata en bodega",
             "desc": "Invierno siguiente · cata técnica de los toneles "
                     "con el enólogo. Si los números cuadran y el vino "
                     "dice la verdad, se firma el contrato anual."},
            {"num": "04", "title": "Entrada en carta",
             "desc": "El primer lote del viticultor independiente "
                     "llega a la carta solo tras la cuarta visita "
                     "(salida de los toneles, botella en mano). Ningún "
                     "vino entra en carta sin que Pietro lo haya catado "
                     "en tres añadas distintas."},
        ],

        "founder_label":   "El fundador",
        "founder_heading": "Pietro Brero.",
        "founder_text":
            "Pietro nació en Alba en 1958. Criado en la trattoria "
            "familiar, trabajó como sumiller en el Combal.Zero de Davide "
            "Scabin desde 1985 hasta 1991, año en que Combal estaba "
            "todavía en Almese. Abre Sapori di Langa en 1992 en la via "
            "Vittorio Emanuele con tres bodegas en carta. Hoy son "
            "treinta y dos. Distinguido con el Cavalier dell'Ordine dei "
            "Cavalieri del Tartufo e dei Vini di Alba (Caballero de la "
            "Orden de los Caballeros de la Trufa y de los Vinos de Alba) "
            "en 2014.",
        "founder_portrait": _FOUNDER_PORTRAIT,
        "founder_caption": "Pietro Brero · Cavalier dell'Ordine dei Cavalieri del Tartufo e dei Vini di Alba",

        "numbers_label":   "La enoteca en cifras",
        "numbers_items": [
            ("32",   "viticultores independientes en carta"),
            ("180",  "etiquetas firmadas por viticultor independiente"),
            ("1992", "año de apertura"),
            ("65 km","radio máximo de selección desde las Langhe"),
        ],

        "visit_label":   "Visite la enoteca",
        "visit_heading": "Via Vittorio Emanuele 38, <em>Alba.</em>",
        "visit_text":
            "A cinco minutos de la estación de Alba · a diez minutos de "
            "la Catedral. Cata guiada con cita previa los jueves por la "
            "tarde · cinco vinos con tabla de Castelmagno y salame "
            "Cuneo, 35 € por persona. Sin cita previa para compras en "
            "horario de apertura.",
        "visit_primary":      "Reserve una cata",
        "visit_primary_href": "contatti",
        "visit_secondary":    "Mapa & horarios",
    },

    # ─── JOURNAL ───────────────────────────────────────────────
    "journal": {
        "eyebrow":  "Diario de enoteca",
        "headline": "Notas de bodega, <em>notas de vendimia.</em>",
        "intro":
            "Breves apuntes de Pietro y Federica sobre el trabajo en "
            "bodega de cada viticultor independiente, sobre las "
            "vendimias en curso y sobre las botellas abiertas por la "
            "tarde para los clientes más curiosos. Lectura reservada.",
        "list_label": "Entradas del diario",
        "entries": [
            {
                "slug":    "vendemmia-2024-langhe",
                "kicker":  "Vendimia 2024",
                "title":   "Vendimia 2024 en las Langhe · qué ha salido de los toneles",
                "date":    "10 de octubre de 2026",
                "read_min": 6,
                "author":  "Pietro Brero",
                "lede":
                    "La vendimia 2024 ha exigido paciencia. El calor de "
                    "agosto ralentizó la maduración; septiembre puso las "
                    "cosas en su sitio. Esto es lo que entra en carta a "
                    "partir de noviembre.",
            },
            {
                "slug":    "barolo-2019-degustazione",
                "kicker":  "Añada en carta",
                "title":   "Por qué el Barolo 2019 merece los seis años de espera",
                "date":    "28 de septiembre de 2026",
                "read_min": 5,
                "author":  "Pietro Brero",
                "lede":
                    "La añada 2019 salió en agosto tras treinta años de "
                    "Barolo en bodega. He aquí por qué merece los dos "
                    "años de tonel grande y los seis años mínimos antes "
                    "de descorcharla.",
            },
            {
                "slug":    "olio-evo-langhe-2024",
                "kicker":  "Aceite de la casa",
                "title":   "Olio EVO Langhe 2024 · una cosecha para apuntar",
                "date":    "15 de septiembre de 2026",
                "read_min": 4,
                "author":  "Federica Bertola",
                "lede":
                    "El Frantoio Anfossi cerró la cosecha 2024 el 5 de "
                    "septiembre. Cinco hectolitros en carta a partir de "
                    "octubre, lote 12. He aquí cómo es.",
            },
        ],

        "footer_note_label": "Reciba el diario por correo electrónico",
        "footer_note":
            "Cuatro o cinco envíos al año, nunca más. Solo lo recibe "
            "quien lo solicita expresamente en caja o en el formulario "
            "de contacto.",
    },

    # ─── CONTATTI ──────────────────────────────────────────────
    "contatti": {
        "eyebrow":  "Visita & pedidos",
        "headline": "Una llamada, <em>una caja.</em>",
        "intro":
            "Para pedir una caja o reservar una cata guiada, el modo "
            "más sencillo es una llamada a la enoteca en horario de "
            "apertura. O bien utilizar el formulario que aparece a "
            "continuación · respuesta en 24 horas en horario laborable.",

        "form_section_label": "Escríbanos",
        "form_section_intro":
            "Para pedidos especiales (verticales, magnums, cajas de "
            "empresa), indique el viticultor independiente o la añada "
            "de interés. Para catas guiadas, indique la fecha y el "
            "número de asistentes.",
        "form_helper_required": "Los campos marcados son obligatorios.",
        "form_submit_button":   "Enviar solicitud",
        "form_submit_note":     "Recibirá confirmación por correo electrónico en un plazo de 24 horas en horario de apertura.",

        "form_fields": [
            {"name": "name",     "label": "Nombre y apellidos","type": "text",     "required": True},
            {"name": "email",    "label": "Correo electrónico","type": "email",    "required": True},
            {"name": "phone",    "label": "Teléfono",          "type": "tel",      "required": False},
            {"name": "subject",  "label": "Asunto",            "type": "select",
             "options": ["Pedido de caja", "Cata guiada", "Vertical o magnum",
                         "Caja de empresa o regalo", "Otro"],     "required": True},
            {"name": "message",  "label": "Mensaje",           "type": "textarea", "required": True,
             "placeholder": "P. ej. «Caja de seis Barolo cuvée 2019» o "
                             "«Cata para cuatro personas el jueves 18 de octubre»."},
        ],

        "card_label":          "La enoteca",
        "card_address_label":  "Dirección",
        "card_address_value":  "Via Vittorio Emanuele 38 · 12051 Alba CN",
        "card_phone_label":    "Teléfono",
        "card_phone_value":    "+39 0173 364 990",
        "card_whatsapp_label": "WhatsApp",
        "card_whatsapp_value": "0173 364 990",
        "card_email_label":    "Correo electrónico",
        "card_email_value":    "enoteca@saporidilanga.it",
        "card_hours_label":    "Horarios",
        "card_hours_rows": [
            "Mar – Sáb · 9:30 – 19:30 horario continuo",
            "Domingo · 10:00 – 13:00 solo mañanas",
            "Lunes · cerrado · catas privadas con cita previa",
            "Feria de la Trufa · oct – nov · 9 – 21 horario continuo",
        ],
        "card_directions_label": "Cómo llegar",
        "card_directions_text":
            "A cinco minutos a pie de la estación de Alba (tren regional "
            "directo desde Turín · 1 h 10 min). A diez minutos de la "
            "Catedral de San Lorenzo. Aparcamiento gratuito en Piazza "
            "Risorgimento, a 200 metros de la enoteca.",

        "faq_label": "Preguntas frecuentes",
        "faq_items": [
            ("¿Cuánto cuesta el envío?",
             "Envío refrigerado en 48 horas: 12 € en Italia "
             "(gratuito a partir de 200 €), 24 € a Europa "
             "Occidental. Caja mínima de seis botellas."),
            ("¿Puedo pedir una sola botella?",
             "No, la caja mínima es de seis botellas. Composición "
             "libre entre vino, aceite, quesos y embutidos. El "
             "valor orientativo de la caja mínima ronda los 90-100 €."),
            ("¿Tienen vinos ecológicos o naturales?",
             "Sí. Cerca del 70% de los viticultores independientes en "
             "carta trabaja en ecológico certificado y el 20% en "
             "biodinámica certificada Demeter. El resto sigue "
             "protocolos de baja intervención, aunque no certificados."),
            ("¿Envían al extranjero?",
             "A Europa Occidental sí (Francia, Alemania, Bélgica, "
             "Países Bajos, Luxemburgo, Austria). Resto del mundo "
             "solo previo presupuesto (EE. UU. · Reino Unido · "
             "Suiza · Japón)."),
            ("¿Puedo visitar la enoteca sin reservar?",
             "Sí, en horario de apertura. Para la cata guiada del "
             "jueves por la tarde es necesario reservar al menos "
             "48 horas antes."),
        ],
    },
}
