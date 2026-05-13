"""Content tree · `madou-pasticceria` · T50 multilingual rollout (ES).

Spanish (Peninsular) translation of `MADOU_CONTENT_IT`. Built for the
marketweb T50 multilingual pass (IT → EN/FR/ES/AR · AAA walk · public
flip). Shape parity contract enforced against
`template_content_madou.py`:

  * Same top-level keys, same nested keys at every depth.
  * Same list lengths (5 lievitati signature courses, 8 menu courses,
    4 produttori, 4 atmosphere images, 4 riconoscimenti, etc.).
  * Same tuple positions for tuple-typed values.
  * Same `pages[].slug` values (labels translated, slugs preserved).
  * Same `posts[].slug` values, same `page kind`.

Voice anchor — `fermentación lenta` (peninsular pastelería register
· El País Sociedad gastronómico / Iban Yarza / Xavier Barriga /
Christian Escribà artisan-pastry-craft idiom) carries the IT
`lievitazione lenta` load-bearing promise across the same surfaces
(hero H1 with `<em>` italic emphasis, manifesto, cta_heading, forno
headline/values, pasticceria intro, ordina, produttori + signature
courses copy). The variant `larga fermentación` is used sparingly
where the same noun-em would feel repetitive. Register is
Peninsular `usted` (formal · institutional pastelería de autor —
NOT Latin American `usted`). Italian/French heritage proper names
(Torino, Borgo Po, Pierre Marchais, Famiglia Brero, Olivier Domori,
Anna Negroni, Carla Madou, Tommaso Rinaldi, Iginio Massari, Pierre
Hermé, Cristian Beduschi, Cuneo IGP, Val Susa, Isigny-sur-Mer,
Sambirano, Mortara, Domori Criollo, Marrone IGP, Nocciola Piemonte
IGP, Gambero Rosso Pasticcerie, AMPI, Coppa del Mondo Pasticceria,
Identità di Pasticceria, Dissapore, Cook Corriere, Vogue Cibo,
Erbaluce passito Cieck, Caffè Vergnano, Damman, Inalpi, Caffè Al
Bicerin) preserved verbatim. Brand name `Madou · Pasticceria
Atelier` preserved. Pastry product names (Croissant viennoise,
Maritozzo, Millefoglie, Bignè, Saint Honoré, Mont-Blanc, Tarte au
chocolat, Macarons, Pasta sfoglia, Bicerin) kept as
Italian/French loanwords. Currency in Peninsular convention
(`18 € / ración`), decimal comma (`pH 4,2`), and the feminine
`la pastelera` for Carla Madou throughout.
"""

from typing import Any


MADOU_CONTENT_ES: dict[str, Any] = {
    "pages": [
        {"slug": "home",         "label": "Inicio",           "kind": "home"},
        {"slug": "forno",        "label": "El obrador",       "kind": "about"},
        {"slug": "pasticceria",  "label": "Pastelería",       "kind": "menu"},
        {"slug": "vetrina",      "label": "Escaparate",       "kind": "gallery"},
        {"slug": "diario",       "label": "Diario",           "kind": "blog_list"},
        {"slug": "ordina",       "label": "Pedidos",          "kind": "reservations"},
    ],

    "site": {
        "logo_initial":  "MD",
        "logo_word":     "Madou",
        "tag":           "Pasticceria Atelier · Torino Borgo Po · desde 2011",
        "phone":         "+39 011 8195 770",
        "email":         "atelier@madou-pasticceria.it",
        "address":       "Via Sant'Ottavio 36 · 10124 Torino",
        "hours_compact": "Mar – Sáb · 7:30 – 19:30 · Dom 7:30 – 13:00",
        "star_line":     "★ Tre Torte · Gambero Rosso · 2023 · 2024 · 2025",
        "footer_intro":
            "Quince años de fermentación lenta. Un obrador a la vista, "
            "un escaparate de masa cruda, dos hornos de solera refractaria. "
            "Sin premezclas industriales, sin congelados, sin prisa.",
        "footer_hours_1": "Mar – Sáb · 7:30 – 19:30",
        "footer_hours_2": "Dom · 7:30 – 13:00 · Lun · cerrado",
        "copyright": "© 2026 Madou Atelier S.r.l. · NIF 11237680016",
    },

    # ─── HOME ──────────────────────────────────────────────────
    "home": {
        # T49: hero plate URL threaded into the fine-dining template via
        # page_data so Madou swaps Gusto's plated-dish hero for the
        # pasticceria vetrina without forking home.html. URL from X.3
        # curator pack `bakery-pasticceria.md` (Pexels CC0-compatible).
        "hero_plate_url":
            "https://images.pexels.com/photos/19288569/pexels-photo-19288569.jpeg"
            "?auto=compress&cs=tinysrgb&w=1600",
        "eyebrow":  "Pasticceria Atelier · Torino Borgo Po · desde 2011",
        "headline": "Doce horas de <em>fermentación lenta,</em> un hojaldre que se deja escuchar.",
        "intro":
            "Hojaldres laminados en frío, fermentación natural con masa "
            "madre refrescada cada doce horas, cremas montadas al momento. "
            "El escaparate cambia cada día según lo que ha salido del horno "
            "al amanecer.",
        "primary_cta":   "Reserve el hojaldre del sábado",
        "primary_href":  "ordina",
        "secondary_cta": "La pastelera",
        "secondary_href":"forno",

        # Repurposed labels (Gusto's "chef" → Madou's "pasticciera")
        "chef_label":    "La pastelera",
        "star_tag":      "★ Tre Torte · Gambero Rosso 2025",
        "photo_label":   "Fotografía",
        "cuisine_label": "Pastelera",

        "facts": [
            ("12 h", "fermentación mínima · pasta sfoglia"),
            ("3",    "masas madre vivas en el obrador · desde 2011"),
            ("0",    "premezclas industriales · 0 congelados · 0 preparados"),
        ],

        "manifesto_drop_cap": "C",
        "manifesto":
            "uando entra un hojaldre en el horno, en Madou se interrumpe el "
            "trabajo durante cuatro minutos y se escucha. El sonido del "
            "hojaldre que sube — las burbujas de aire que se liberan entre "
            "las 64 capas de masa laminada — es el primer indicador de si "
            "ese lote se venderá el sábado por la mañana o se quedará para "
            "la brigada. Sin cronómetro, sin termómetro: solo el oído.",

        # Pasticceria signature — 5 "lievitati" (vs Gusto 5 "atti")
        "signature_courses": [
            ("I",    "Croissant viennoise",         "12 horas de fermentación lenta · 64 capas · mantequilla normanda de Isigny", "Café monoorigen Etiopía Sidamo"),
            ("II",   "Maritozzo con nata",          "fermentación natural de 24 horas · nata fresca montada al momento",          "Chocolate caliente Madagascar 72 %"),
            ("III",  "Millefoglie de avellana",     "tres capas de hojaldre caramelizado · crema chantilly de avellana IGP",      "Bicerin tradicional torinés"),
            ("IV",   "Bignè con chocolate Domori",  "pasta choux de la casa · ganache negra Criollo 80 %",                        "Té negro Darjeeling First Flush"),
            ("V",    "Saint Honoré de marroni",     "temporada de otoño · marroni de Cuneo IGP · crema muselina",                 "Vino dulce Erbaluce passito"),
        ],

        # Persona — pasticciera Carla Madou
        "chef": {
            "name":  "Carla Madou",
            "role":  "Pastelera del atelier · promoción de 1979",
            "bio":
                "Torinesa, nacida en 1979. Aprendizaje de cuatro años con "
                "Iginio Massari en Brescia, después dos años con Pierre "
                "Hermé en París y, por último, dos con Cristian Beduschi en "
                "Ginebra. Abre Madou en 2011 en una antigua imprenta de "
                "Borgo Po, con una sola intuición: trabajar solo con masas "
                "madre vivas y refrescadas cada doce horas.",
        },

        "courses_label": "Cinco fermentados de la semana · octubre de '26",
        "courses_footline": "Escaparate vivo — lo que ven ha salido esta mañana del horno",
        "courses_full_cta": "Toda la pastelería",
        "chef_link_filosofia": "El obrador y las manos",
        "chef_link_diario": "El diario de harina",

        "press_label": "Publicada en",
        "press": ["GAMBERO ROSSO PASTICCERIE", "DISSAPORE", "COOK CORRIERE",
                  "IDENTITÀ DI PASTICCERIA", "VOGUE CIBO"],

        # Ingredients/sourcing editorial band — pasticceria-specific
        "ingredienti": {
            "label":   "Materia prima",
            "heading": "Dieciséis proveedores, <em>todos por su nombre.</em>",
            "text":
                "La cadena de suministro de Madou es corta y trazable línea "
                "por línea. La mantequilla llega de una lechería normanda de "
                "Isigny-sur-Mer · los huevos de una granja a sesenta "
                "kilómetros de Torino · las harinas de un molino de piedra "
                "en Val Susa · el cacao de tres plantaciones single-origin "
                "(Madagascar, Venezuela, República Dominicana) seleccionadas "
                "sobre el terreno en 2019.",
            "image":
                "https://images.pexels.com/photos/28183472/pexels-photo-28183472.jpeg"
                "?auto=compress&cs=tinysrgb&w=1000",
            "image_caption":
                "Masa laminada sobre el mármol refrigerado · turno de las 5:30 de la mañana",
        },

        # Atmosphere teaser — pasticceria-specific imagery
        "atmosphere_teaser": {
            "label": "El escaparate vivo",
            "images": [
                ("https://images.pexels.com/photos/19288569/pexels-photo-19288569.jpeg"
                 "?auto=compress&cs=tinysrgb&w=600",
                 "El escaparate del sábado por la mañana"),
                ("https://images.pexels.com/photos/16140003/pexels-photo-16140003.jpeg"
                 "?auto=compress&cs=tinysrgb&w=600",
                 "Decoración a mano · tarta por encargo"),
                ("https://images.pexels.com/photos/30853716/pexels-photo-30853716.jpeg"
                 "?auto=compress&cs=tinysrgb&w=600",
                 "Croissant viennoise recién horneados"),
                ("https://images.pexels.com/photos/31000323/pexels-photo-31000323.jpeg"
                 "?auto=compress&cs=tinysrgb&w=600",
                 "Macarons de temporada · octubre de '26"),
            ],
            "link_label": "Entre en el escaparate",
            "link_href":  "vetrina",
        },

        # Awards/recognition — pastry awards (not Michelin)
        "riconoscimenti": {
            "label": "Reconocimientos",
            "items": [
                ("★★★", "Tre Torte · Gambero Rosso", "Premio anual · 2023 · 2024 · 2025"),
                ("AMPI", "Accademia Maestri Pasticceri", "Miembro desde 2017 · sede de Brescia"),
                ("CMP",  "Coppa del Mondo Pasticceria", "Selección Italia · suplente 2022 · 4.º puesto en Lyon"),
                ("DIS",  "Dissapore · 50 Pasticcerie", "Primera posición en Piemonte 2024 · top 5 Italia 2025"),
            ],
        },

        # CTA section
        "cta_heading": "Solo fermentación lenta, <em>solo lo que sale del horno por la mañana.</em>",
        "cta_primary":  "Reserve el hojaldre del sábado",
        "cta_secondary": "Descubra toda la pastelería",

        # Seasonal highlight card — pasticceria seasonal
        "stagione": {
            "label":     "En el escaparate ahora",
            "title":     "Pastelería de otoño '26",
            "subtitle":  "Marroni, caqui, chocolate monoorigen · desde el 6 de octubre",
            "text":
                "La carta de otoño se abre el 6 de octubre con el Saint "
                "Honoré de marroni de Cuneo IGP, la millefoglie de caqui "
                "astringente del Bel Paese y el Mont-Blanc 2026 en versión "
                "monoporción. Toda la pastelería de otoño permanece en el "
                "escaparate hasta el 30 de noviembre; después se pasa a "
                "la Navidad.",
            "cta_label": "Descubra toda la carta de otoño →",
            "cta_href":  "pasticceria",
        },

        # Producer showcase — pastry supply chain (vs Gusto wine producers)
        "produttori": {
            "label":   "Los proveedores",
            "heading": "Dieciséis manos, <em>un solo escaparate.</em>",
            "intro":
                "Cada materia prima de Madou tiene un proveedor con nombre, "
                "dirección y número de teléfono. Mantequilla, leche, huevos, "
                "harinas, cacao, fruta, miel — nada llega de catálogo. "
                "Todos los proveedores han sido visitados personalmente por "
                "Carla al menos una vez.",
            "items": [
                {
                    "portrait":
                        "https://images.pexels.com/photos/8477754/pexels-photo-8477754.jpeg"
                        "?auto=compress&cs=tinysrgb&w=800",
                    "name": "Pierre Marchais",
                    "role": "Mantequilla normanda AOP",
                    "area": "Isigny-sur-Mer · Normandía",
                    "blurb":
                        "La mantequilla Isigny AOP llega cada miércoles en "
                        "carga refrigerada a 4 °C. Lechería familiar desde "
                        "1932, cuatro vacas normandas por hectárea.",
                },
                {
                    "portrait":
                        "https://images.pexels.com/photos/8188937/pexels-photo-8188937.jpeg"
                        "?auto=compress&cs=tinysrgb&w=800",
                    "name": "Famiglia Brero",
                    "role": "Molino de piedra Val Susa",
                    "area": "Bussoleno · Piemonte",
                    "blurb":
                        "Molienda en piedra en tres pasadas · trigo blando "
                        "Bologna 100 % local · sin refinado. Tres tipos de "
                        "harina, una al mes en exclusiva.",
                },
                {
                    "portrait":
                        "https://images.pexels.com/photos/11869895/pexels-photo-11869895.jpeg"
                        "?auto=compress&cs=tinysrgb&w=800",
                    "name": "Olivier Domori",
                    "role": "Cacao single-origin",
                    "area": "Sambirano · Madagascar",
                    "blurb":
                        "Tres plantaciones seleccionadas sobre el terreno "
                        "por Carla en 2019. Cacao Criollo trinitario al "
                        "80 %, tostado en frío en Italia · partida trazada "
                        "por lote.",
                },
                {
                    "portrait":
                        "https://images.pexels.com/photos/29198586/pexels-photo-29198586.jpeg"
                        "?auto=compress&cs=tinysrgb&w=800",
                    "name": "Anna Negroni",
                    "role": "Fruta de temporada Cuneo",
                    "area": "Lagnasco · Piemonte",
                    "blurb":
                        "Melocotones de Cuneo IGP en junio · marroni IGP "
                        "en octubre · caquis astringentes en noviembre. "
                        "Ocho hectáreas, recogida a mano, sin cámara.",
                },
            ],
        },

        # Repurposed `private_dining` → `eventi su misura` / cake design
        "private_dining": {
            "label":   "Eventos a medida",
            "heading": "Cake design y <em>encargos privados.</em>",
            "intro":
                "En Madou pueden encargarse tartas ceremoniales, wedding "
                "cakes y pequeñas producciones privadas para eventos. Tres "
                "vías de entrada, cada una con plazos y precios distintos.",
            "experiences": [
                {
                    "icon": "fork",
                    "title": "Tarta por encargo",
                    "meta":  "Mín. 8 raciones · desde 18 € / ración",
                    "desc":
                        "Diseño personalizado a partir de tres encuentros "
                        "preliminares con Carla. Plazo de entrega: dos "
                        "semanas mínimo. Decoramos solo a mano, sin moldes "
                        "industriales.",
                },
                {
                    "icon": "door",
                    "title": "Wedding cake",
                    "meta":  "Desde 40 raciones · desde 22 € / ración",
                    "desc":
                        "Cuatro meses de trabajo a cuatro manos con la "
                        "pareja. Tres pruebas de sabor incluidas en el "
                        "servicio. Recogida en el atelier o transporte "
                        "refrigerado a cargo de Madou en el Piemonte central.",
                },
                {
                    "icon": "wine",
                    "title": "Bufé privado",
                    "meta":  "20 – 60 invitados · desde 38 € / invitado",
                    "desc":
                        "Solo pastelería mignon · 8 referencias, 150 "
                        "piezas mínimas. Cocción el mismo día del evento, "
                        "entrega refrigerada. La tarde del sábado la "
                        "dejamos libre.",
                },
            ],
            "cta_label": "Escriba a la pastelera",
            "cta_href":  "ordina",
        },

        # Repurposed `wine_program` → `lieviti madre` collection
        "wine_program": {
            "label":   "El archivo de las masas madre",
            "heading": "Tres masas madre vivas, <em>una sola pastelería.</em>",
            "intro":
                "El atelier conserva tres masas madre activas, cada una "
                "con su firma de acidez y su rendimiento. Cada fermentado "
                "de Madou se asocia a la madre que le corresponde — sin "
                "levadura de cerveza, sin mejorantes.",
            "sommelier": {
                "name": "Tommaso Rinaldi",
                "role": "Maestro panadero · responsable de la masa madre",
                "bio":
                    "Aprendiz de Carla desde 2014, responsable del "
                    "refresco de las tres masas madre desde 2018. Refresca "
                    "cada doce horas, a las 5:30 y a las 17:30. Conserva la "
                    "memoria de harina de cada partida.",
            },
            "pairings": [
                ("01", "Madre M-1 · hojaldre laminado",
                 "Masa activa desde 2011 · acidez láctica dominante · "
                 "pH 4,2 · pliegues rápidos, reposo largo. Usada para "
                 "croissants, kouign-amann, brioche col tuppo.",
                 "12 – 16 h"),
                ("02", "Madre M-2 · panettoni y fermentados altos",
                 "Madre nacida en 2014 de un refresco a triple. Acidez "
                 "mixta acética-láctica, pH 4,5 · desarrollo vertical "
                 "agresivo. Solo panettone, colomba y veneziana.",
                 "36 – 48 h"),
                ("03", "Madre M-3 · pan brioche y laminados dulces",
                 "Madre refrescada con miel de castaño · acidez "
                 "contenida, pH 4,7 · aroma a avellana tostada. "
                 "Maritozzi, brioches redondas, trenza de chocolate.",
                 "8 – 12 h"),
            ],
            "cellar_facts": [
                ("3",   "masas madre vivas"),
                ("12h", "frecuencia de refresco fija"),
                ("2011", "año de la primera madre · M-1"),
            ],
        },
    },

    # ─── FORNO (about) — Gusto's "filosofia" page ────────────
    "forno": {
        "eyebrow":  "El obrador",
        "headline": "Quince años de obrador, <em>una sola promesa de hojaldre.</em>",
        "intro":
            "Madou nace en 2011 en una antigua imprenta de Borgo Po, en "
            "Torino. El atelier tiene un solo obrador a la vista de la "
            "calle y dos hornos de solera refractaria. La promesa es "
            "siempre la misma: cero premezclas, cero congelados, cero "
            "preparados industriales. Solo fermentación lenta, solo "
            "materia prima trazada.",

        "history": [
            ("2011",
             "Carla Madou abre el atelier en via Sant'Ottavio tras ocho "
             "años entre Brescia (Massari), París (Hermé) y Ginebra "
             "(Beduschi). Cuatro plazas en la barra, dos referencias de "
             "pastelería, una sola madre — M-1, fundada con harina del "
             "molino Brero."),
            ("2014",
             "Tommaso Rinaldi entra como aprendiz y en tres años se "
             "convierte en responsable de las masas madre. Nace M-2, la "
             "madre de los panettoni, de un refresco a triple de M-1."),
            ("2017",
             "Carla es admitida en la Accademia Maestri Pasticceri Italiani "
             "(AMPI), segunda mujer piemontesa en entrar tras Sonia Balacchi."),
            ("2021",
             "Traslado del atelier a via Sant'Ottavio 36, la antigua "
             "imprenta completamente rehabilitada. Tres hornos, dos "
             "laminadoras, un escaparate de quince metros lineales abierto "
             "a la calle."),
            ("2023",
             "Gambero Rosso le concede las Tre Torte (máximo reconocimiento "
             "pastelero) y se las confirma en 2024 y 2025. Madou se "
             "convierte en parada fija del circuito de pastelerías de "
             "autor italianas."),
        ],

        "filosofia_image":
            "https://images.pexels.com/photos/30918889/pexels-photo-30918889.jpeg"
            "?auto=compress&cs=tinysrgb&w=1400",
        "filosofia_image_caption": "El obrador · Carla Madou en la laminadora",

        "method_title": "Método",
        "method_paragraphs": [
            "Toda la pastelería de Madou parte del refresco de la madre. "
            "A las 5:30 de la mañana, Tommaso refresca las tres masas "
            "madre y separa las cantidades para los amasados del día · a "
            "las 17:30 refresca de nuevo para los amasados nocturnos. Es "
            "un horario fijo, independiente de Navidad, Pascua o "
            "ferragosto.",
            "Los hojaldres laminados se preparan la víspera y reposan en "
            "cámara a 4 °C durante doce horas mínimo, dieciséis horas "
            "para los lotes del sábado. La mantequilla se golpea en frío "
            "· la sal de Mothia se añade en escamas · los pliegues son "
            "siempre cuatro, nunca tres · el ciclo final de laminado "
            "produce 64 capas de masa visibles al corte.",
            "Las cremas se preparan a la vista, montadas al momento. "
            "Ninguna pieza de pastelería de Madou sale del mostrador con "
            "una crema preparada hace más de dos horas · las pastas "
            "quebradas se cortan a mano · las ganaches se emulsionan con "
            "varilla en el pase siguiente. Trabajar al momento es la "
            "razón por la que no vendemos cake design sin aviso.",
        ],

        "values_label": "Lo que garantizamos",
        "values_heading": "Cuatro promesas <em>innegociables</em>.",
        "values": [
            ("Tiempo",        "Doce horas mínimas de fermentación lenta · dieciséis para el sábado."),
            ("Cadena",        "Dieciséis proveedores, todos visitados en persona al menos una vez."),
            ("Transparencia", "Sin preparados, sin mejorantes, sin congelados."),
            ("Mano",          "Decoración a mano · cremas montadas al momento · sin molde industrial."),
        ],

        "cta_heading": "¿Quiere ver la <em>pastelería de la semana en curso?</em>",
        "cta_menu": "Cinco fermentados de octubre de '26",
        "cta_prenota": "Reserve el hojaldre del sábado",
    },

    # ─── PASTICCERIA (menu) — Gusto's "menu" page ────────────
    "pasticceria": {
        "eyebrow":  "La carta de la semana",
        "headline": "Escaparate vivo — <em>otoño '26</em>",
        "intro":
            "La pastelería de Madou cambia cada semana según el horno de "
            "la noche del lunes. Lo que sigue es la carta en vigor del 6 "
            "al 12 de octubre de 2026 · escaparate abierto del martes al "
            "sábado, domingo solo por la mañana, lunes cerrado.",
        "courses_label": "Cinco fermentados · octubre de '26",

        "courses": [
            ("I",     "Croissant viennoise",
             "Pasta sfoglia fermentada 12 horas · mantequilla normanda AOP "
             "de Isigny · 64 capas visibles al corte · pincelada de yema de "
             "huevo entero · azúcar glas de Mothia espolvoreada a la salida "
             "del horno.",
             "Café monoorigen Etiopía Sidamo · Caffè Vergnano para Madou"),
            ("II",    "Maritozzo con nata",
             "Masa brioche fermentada 24 horas con M-3 · nata fresca de la "
             "lechería Inalpi montada al momento · vainilla Tahitian entera "
             "de Madagascar · azúcar hilado en corona.",
             "Chocolate caliente Madagascar Domori 72 %"),
            ("III",   "Millefoglie de avellana",
             "Tres capas de hojaldre caramelizado · crema chantilly de "
             "avellana Piemonte IGP del molino Brero · granillo de avellana "
             "tostado sobre la solera refractaria.",
             "Bicerin tradicional torinés · receta histórica del Caffè Al Bicerin"),
            ("IV",    "Bignè con chocolate Domori",
             "Pasta choux de la casa · ganache negra de cacao Criollo "
             "Domori 80 % · brillo con jarabe de glucosa · acabado a "
             "manga · azúcar glas al gusto.",
             "Té negro Darjeeling First Flush · selección Damman 2026"),
            ("V",     "Saint Honoré de marroni",
             "Solo otoño · bignès rellenos de crema muselina al marrón · "
             "marroni IGP de Cuneo del campo de Anna Negroni · pasta "
             "sfoglia en la base · azúcar hilado en corona dorada.",
             "Erbaluce di Caluso passito · selección Cieck · 50 cl por copa"),
            ("VI",    "Mont-Blanc 2026",
             "Vermicelli de castañas IGP de Mortara · crema chantilly de "
             "vainilla · corazón de merengue francés cocido a 90 °C "
             "durante cuatro horas · acabado a mano alzada.",
             "Café turco al cardamomo verde · servido en cafetera de cobre"),
            ("VII",   "Tarte au chocolat Sambirano",
             "Pasta quebrada al cacao 22 % · ganache negra Madagascar "
             "Sambirano 72 % · sal de Mothia en escamas · acabado con "
             "aceite de oliva virgen extra de Taggia.",
             "—"),
            ("VIII",  "Macarons de temporada",
             "Seis macarons de temporada · azafrán de los Abruzzos, "
             "frambuesa del Roero, castaña de Cuneo, chocolate Sambirano, "
             "vainilla Tahitian, oliva taggiasca · cocción a 165 °C "
             "durante 12 minutos.",
             "Té blanco Pai Mu Tan · selección Damman"),
        ],

        # Wine_program → repurposed as caffè & tisaneria
        "wine_intro_title": "Cafetería y tetería",
        "wine_intro":
            "En Madou se marida cada fermentado con un café monoorigen "
            "tostado en Torino por Vergnano o con una infusión seleccionada "
            "por Damman. La carta de tés y cafés es completa, los "
            "maridajes quedan a criterio del mostrador — pregunte a "
            "Tommaso al pasar por caja.",

        "wine_highlights": [
            ("Café monoorigen",       "8 orígenes · Etiopía, Brasil, Colombia, Guatemala, Vietnam, Sambirano"),
            ("Tés negros y verdes",   "22 selecciones Damman · Darjeeling, Ceylon, Sencha, Genmaicha"),
            ("Chocolates calientes",  "6 orígenes · Madagascar, Venezuela, Ecuador, Dominicana, Tanzania, Ghana"),
            ("Bebidas tradicionales", "Bicerin · vin brulé con canela · ponche de mandarina · zabaione"),
        ],

        "footer":
            "Escaparate abierto de martes a sábado · reserva del sábado "
            "recomendada a partir del miércoles. El hojaldre del sábado se "
            "agota regularmente antes de las 11:00. Para pedidos "
            "superiores a 12 piezas, escriba a atelier@madou-pasticceria.it "
            "al menos 48 horas antes.",
    },

    # ─── VETRINA (gallery) — Gusto's "atmosfera" ─────────────
    "vetrina": {
        "eyebrow":  "El escaparate",
        "headline": "Quince metros de escaparate, <em>un solo escaparate.</em>",
        "intro":
            "Madou ocupa una antigua imprenta de Via Sant'Ottavio · el "
            "escaparate está abierto a la calle a lo largo de quince "
            "metros lineales y deja ver todo el obrador. Sin pared entre "
            "el horno y la acera de Borgo Po.",

        "rooms": [
            ("El escaparate de calle",
             "Quince metros de escaparate a lo largo de Via Sant'Ottavio · "
             "exposición a doble altura · refrigeración a +4 °C para las "
             "cremas · vitrina seca a +18 °C para los fermentados."),
            ("El obrador a la vista",
             "El atelier de verdad — cuatro puestos: laminado, "
             "fermentados, cremas, decoración. Toda la pastelería se ve en "
             "tiempo real desde el escaparate · sin cocina oculta."),
            ("La sala de cata",
             "Ocho plazas en la barra, frente a la laminadora. Abierta "
             "solo para las catas guiadas del jueves por la tarde · tres "
             "horas con Carla, seis fermentados, tres cafés monoorigen."),
            ("El patio de la antigua imprenta",
             "De mayo a septiembre, cuatro mesas al aire libre bajo la "
             "glicinia de la antigua imprenta. Abiertas solo para el "
             "desayuno · menú fijo del lunes, croissant + bicerin."),
        ],

        "captions": [
            "El escaparate del sábado por la mañana · exposición de las 7:30.",
            "Decoración a mano · wedding cake de otoño '26.",
            "Los croissants viennoise recién horneados a las 6:00.",
            "Los macarons de octubre de '26 · seis sabores de temporada.",
            "Carla Madou en la laminadora · pasta sfoglia de las 5:30.",
            "El mostrador al paso del primer cliente · martes 7:30.",
        ],

        "cta_quote": "«Sin pared entre el horno y la acera de Borgo Po.»",
        "cta_desc": "Escaparate abierto Mar – Sáb · 7:30 – 19:30 · Dom 7:30 – 13:00 · Lun cerrado.",
        "cta_primary": "Reserve el hojaldre del sábado",
        "cta_secondary": "Vea toda la pastelería",
    },

    # ─── DIARIO (blog list / detail) ──────────────────────────
    "diario": {
        "eyebrow":  "El diario de harina",
        "headline": "Notas de obrador, <em>de levadura,</em> de laboratorio.",
        "intro":
            "Breves apuntes de Carla Madou y Tommaso Rinaldi sobre las "
            "fermentaciones en curso, sobre las materias primas de "
            "temporada, sobre los pasteles más bonitos y sobre lo que no "
            "está funcionando en la pastelería de semana en semana.",
        "read_article": "Leer el artículo",
        "min_label": "min",
        "min_read_label": "min de lectura",
        "crumb_label": "Diario",
        "back_link": "← Todo el diario",
        "footer_label": "Madou Pasticceria Atelier · El diario de harina",
        "empty_body": [
            "Artículo en preparación editorial. La publicación íntegra "
            "estará disponible en breve, escrita personalmente por la "
            "pastelera o por el maestro panadero.",
            "Este marcador describe la voz del Diario de Harina: breves "
            "notas de trabajo, reflexiones sobre las masas madre, "
            "relatos de fermentaciones que salen mal. Nunca más de dos "
            "mil palabras, nunca menos de quinientas.",
        ],
    },

    "posts": [
        {
            "slug":     "vetrina-autunno-26",
            "kicker":   "Escaparate en curso",
            "title":    "Las cinco ideas del escaparate de otoño '26",
            "date":     "6 de octubre de 2026",
            "read_min": 5,
            "author":   "Carla Madou",
            "lede":
                "La nueva carta entró en el escaparate anoche. Cinco "
                "fermentados, dos relecturas de clásicos de la pastelería "
                "torinesa y un hojaldre que he perseguido durante tres "
                "años.",
            "body": [
                ("p", "Construir un escaparate otoñal es menos una "
                      "cuestión de recetas y más una cuestión de tiempos "
                      "de fermentación lenta. La temperatura de la cámara "
                      "baja, las levaduras se ralentizan · las madres "
                      "responden más despacio. Para la carta de otoño '26 "
                      "hemos trabajado dos semanas solo en los tiempos de "
                      "reposo del Saint Honoré de marroni."),
                ("h2", "Las cinco ideas nuevas"),
                ("p", "El primer fermentado, el Saint Honoré de marroni "
                      "de Cuneo, es una relectura del Saint Honoré "
                      "clásico francés hecha sobre tres materias primas "
                      "piemontesas: marroni de Cuneo IGP del campo de "
                      "Anna Negroni, nata fresca de la lechería Inalpi y "
                      "pasta sfoglia con mantequilla normanda. Tenía "
                      "ganas desde 2022, desde que pasé por Lyon y probé "
                      "el de Cyril Lignac · pero quería una versión "
                      "torinesa, no parisina."),
                ("h2", "Las relecturas"),
                ("p", "El Mont-Blanc 2026 y el maritozzo con nata son "
                      "dos dulces en los que llevo trabajando siete años "
                      "· ninguno de los dos nace en octubre, pero es en "
                      "octubre cuando sus respectivas materias primas "
                      "entran en su mejor momento: los marroni de Mortara "
                      "para el primero, la nata otoñal para el segundo. "
                      "El maritozzo, en particular, lo he cambiado siete "
                      "veces en doce meses. Ahora está como debe."),
                ("h2", "Un hojaldre"),
                ("p", "El croissant viennoise es la pieza de la que más "
                      "orgullosa estoy de esta carta. Es un hojaldre "
                      "fermentado 12 horas en cámara a +4 °C, con "
                      "mantequilla Isigny AOP golpeada en frío y harina "
                      "del molino Brero. Sesenta y cuatro capas visibles "
                      "al corte, una burbuja de aire cada 0,4 milímetros "
                      "de masa. Es el fermentado al que he llegado tras "
                      "ocho años de intentos, y la única razón por la "
                      "que estoy aquí."),
                ("h2", "Qué sale el sábado"),
                ("p", "El sábado Madou produce 220 croissants viennoise "
                      "que se agotan regularmente antes de las 11:00. La "
                      "reserva desde el jueves es, por tanto, "
                      "calurosamente recomendable — sobre todo a partir "
                      "de octubre, cuando la demanda vuelve a subir con "
                      "el primer frío."),
            ],
        },
        {
            "slug":     "lievito-madre-m2",
            "kicker":   "Masa madre",
            "title":    "Por qué esperamos siete años antes de hacer el panettone",
            "date":     "28 de septiembre de 2026",
            "read_min": 6,
            "author":   "Tommaso Rinaldi",
            "lede":
                "Madou puso el panettone en la carta solo en 2018, siete "
                "años después de abrir. La razón es una sola: la madre "
                "M-2 no estaba lista. Aquí está el motivo.",
            "body": [
                ("p", "El panettone exige una madre de madres · muchos "
                      "pasteleros se hacen la madre cuando abren la "
                      "pastelería, pero para el panettone de alta gama "
                      "hace falta una madre que haya trabajado al menos "
                      "tres años, desarrollado su perfil acético, "
                      "encontrado su equilibrio. La M-1 de Madou — "
                      "fundada en 2011 — era una madre láctica, perfecta "
                      "para el hojaldre pero poco agresiva para el "
                      "panettone."),
                ("h2", "Cómo nace la M-2"),
                ("p", "En 2014 cogí un trozo de 200 gramos de M-1 y la "
                      "refresqué a triple durante cuarenta días · cada "
                      "doce horas, siempre. Así es como se \"vira\" una "
                      "madre láctica hacia un perfil mixto · es un "
                      "proceso que aprendí de Achille Zoia. Tras los "
                      "cuarenta días, la madre se había vuelto bastante "
                      "acética para el panettone, pero aún demasiado "
                      "joven."),
                ("h2", "Cuatro años de espera"),
                ("p", "De 2014 a 2018 refresqué la M-2 cada doce horas "
                      "sin saltarme una sola vez · ni en Navidad, ni en "
                      "agosto. Carla la llamaba \"la madre del futuro\" "
                      "porque no la usábamos nunca. En noviembre de "
                      "2018, en la séptima prueba, el panettone salió "
                      "como tenía que salir. Desde entonces la M-2 "
                      "produce solo panettone, colomba y veneziana, "
                      "nada más."),
            ],
        },
    ],

    # ─── ORDINA (reservations) — Gusto's "prenota" ────────────
    "ordina": {
        "eyebrow":      "Pedidos y encargos",
        "headline":     "Reserve el hojaldre del sábado.",
        "intro":
            "El escaparate del sábado se agota regularmente antes de las "
            "11:00. Para asegurarse los fermentados, conviene reservar "
            "desde el miércoles · recogida en el mostrador de 7:30 a "
            "13:00. Para tartas por encargo y wedding cakes, escriba a "
            "atelier@madou-pasticceria.it al menos dos semanas antes.",
        "primary_label":   "¿Qué desea reservar?",
        "primary_placeholder": "Sábado 18 de octubre · 12 croissants viennoise + 4 maritozzi · recogida a las 9:30",
        "name_label":      "Nombre y apellidos",
        "phone_label":     "Teléfono",
        "email_label":     "Correo electrónico",
        "submit_label":    "Enviar la reserva",
        "submit_note":     "Recibirá confirmación del mostrador en un plazo de 24 h. La reserva se paga en la recogida.",

        "contact_block": {
            "address_label": "Atelier",
            "address":       "Via Sant'Ottavio 36 · 10124 Torino · Borgo Po",
            "phone_label":   "Mostrador",
            "phone":         "+39 011 8195 770",
            "email_label":   "Correo electrónico",
            "email":         "atelier@madou-pasticceria.it",
            "hours_label":   "Horario",
            "hours_list": [
                "Mar – Sáb · 7:30 – 19:30",
                "Dom · 7:30 – 13:00",
                "Lun · cerrado",
            ],
        },

        "policy_label": "Notas sobre la reserva",
        "policy_paragraphs": [
            "La reserva del sábado se cierra el viernes a las 18:00. "
            "Después de esa hora, aceptamos solo si la producción del día "
            "lo permite.",
            "Para pedidos superiores a 12 piezas, contacten con el "
            "mostrador directamente. Para las wedding cakes, dos semanas "
            "mínimas de antelación · para el cake design, tres semanas.",
            "Las materias primas trazadas (mantequilla Isigny, cacao "
            "Sambirano, marroni IGP, avellanas IGP) siguen el calendario "
            "estacional. En caso de rotura de stock, le proponemos una "
            "variante coherente.",
        ],

        "small_print":
            "Madou Atelier S.r.l. · NIF 11237680016 · Via Sant'Ottavio 36, "
            "10124 Torino · Pasticceria Atelier desde 2011.",
    },
}
