"""Sapore — Trattoria Da Nonna Rosa (trattoria-warm archetype) — Spanish (ES).

Phase 2g3.6 — Restaurant live-completion (Session 48, 2026-04-15).

Voice contract (ES — peninsular, El País Gastro / 7 Caníbales register):
- Native peninsular Spanish, registro cálido de reportaje gastronómico
  español al escribir sobre una trattoria familiar del Trastevere. Nada de
  marketing, nada de formalismo cortado a cuchillo: se habla como quien
  cuenta una cena real.
- ``tú`` form throughout — la trattoria habla como una familia amiga,
  nunca ``usted``. Gusto ES guarda el ``usted`` (registro Michelin) y
  Brace ES tira de imperativo street-food. Sapore ES se queda entre los
  dos, en el centro cordial.
- Spanish punctuation: « » comillas latinas editoriales, apertura ¿ y ¡
  donde toque, guiones largos — como se usan en prensa gastro española.
- Nombres propios y platos italianos se dejan en italiano: Trattoria Da
  Nonna Rosa, Rosa / Marco / Giulia Trezzi, Trastevere, Roma, Via dei
  Salumi, Cacio e pepe, Carbonara, Bucatini all'amatriciana, Coda alla
  vaccinara, Margherita Verace, Cesanese del Lazio, Amatrice, Agerola.
- Monedas: 12,00 € (formato peninsular, coma decimal, espacio antes del
  símbolo). Convertido desde IT « € 12,00 ».
- Días y horarios: ``Mar – Sáb``, ``Lunes``, ``Domingo``.
- Vocabulario peninsular: ``tú``, ``vosotros``, ``coger`` (no ``agarrar``),
  ``vino``, ``mesa``, ``reservar`` (no ``apartar``). Nada de latinoamericano.

Differentiation guard vs Gusto ES (fine-dining) & Brace ES (street-food):
- Sapore ES = reportaje cálido de trattoria romana con ``tú``.
- Gusto ES = registro Michelin editorial, ``usted``, vocabulario concierge.
- Brace ES = street-food boloñés brutalist, imperativo corto, tono pop.
- Si aparece ``usted``, menú degustación, concierge, sumiller firma,
  palabra ``maison`` o frases tipo ``pídelo ya`` / ``llévatelo`` / ``rápido``
  — STOP, ha pillado el registro equivocado.
"""
from __future__ import annotations

from typing import Any


SAPORE_CONTENT_ES: dict[str, Any] = {
    "pages": [
        {"slug": "home",     "label": "Inicio",                    "kind": "home"},
        {"slug": "menu",     "label": "Carta",                     "kind": "menu"},
        {"slug": "storia",   "label": "Nuestra historia",          "kind": "about"},
        {"slug": "forno",    "label": "Horno de leña",             "kind": "signature"},
        {"slug": "eventi",   "label": "Mesas largas y eventos",    "kind": "events"},
        {"slug": "contatti", "label": "Encuéntranos y reserva",    "kind": "contact"},
    ],

    # ─── SITE-WIDE CHROME ────────────────────────────────────────
    "site": {
        "logo_initial": "R",
        "logo_word":    "Trattoria Da Nonna Rosa",
        "tag":          "Trattoria de familia · Trastevere · desde 1987",
        "phone":        "06 581 4488",
        "phone_tel":    "+390658144880",
        "whatsapp":     "06 581 4488",
        "whatsapp_link": "https://wa.me/390658144880",
        "email":        "ciao@trattoriadanonnarosa.it",
        "address":      "Via dei Salumi 16/a · 00153 Roma · Trastevere",
        "hours_compact": "Mar – Sáb · 12:30 – 15:00 · 19:00 – 23:30",
        "hours_footer_rows": [
            "Domingo · solo comidas · 12:30 – 15:00",
            "Lunes · día de descanso",
        ],
        "license":      "NIF IT 07634211006 · CCIAA Roma REA 1138992",
        "footer_intro":
            "Trattoria familiar abierta en 1987 por Rosa Trezzi. Pasta estirada "
            "al rodillo cada mañana, pizza del horno de leña por la noche, vino "
            "de la casa invitado a quien vuelve por segunda vez. Sesenta "
            "cubiertos, dos salas, tres generaciones en la cocina.",
        "nav_cta":      "Reservar mesa",
        "nav_cta_href": "contatti",
        "nav_phone_cta": "Llama: 06 581 4488",
        "star_line":    "Trattoria de familia · desde 1987",
        "copyright":    "© 2026 Trattoria Da Nonna Rosa · NIF IT 07634211006",

        # Mirror the fine-dining _base.html footer keys used by the chrome
        "footer_hours_1": "Mar – Sáb · comida y cena",
        "footer_hours_2": "Domingo · solo comidas",
    },

    # ─── HOME ────────────────────────────────────────────────────
    "home": {
        "eyebrow":  "Trattoria de familia · Trastevere · desde 1987",
        "headline": "En casa de Nonna Rosa, <em>como en casa.</em>",
        "intro":
            "Pasta estirada al rodillo cada mañana, pizza del horno de leña por la "
            "noche, y una copa de vino de la casa invitada a quien vuelve por "
            "segunda vez. Sesenta cubiertos, dos salas, tres generaciones en la cocina.",
        "primary_cta":   "Reservar mesa",
        "primary_href":  "contatti",
        "secondary_cta": "Escríbenos por WhatsApp",
        "secondary_href_is_whatsapp": True,

        # Hero photo-frame
        "hero_image":   "https://images.unsplash.com/photo-1481931098730-318b6f776db0?w=1600&q=80&auto=format&fit=crop",
        "hero_caption": "Cacio e pepe del martes · tonnarelli estirados al rodillo",
        "hero_stamp":   "Desde 1987",

        # Facts band — 3 numbers/claims
        "facts": [
            ("1987", "el año en que Rosa abrió la cocina"),
            ("60",   "cubiertos en dos salas · no aceptamos reservas de más de veinte"),
            ("3",    "generaciones de familia en la cocina"),
        ],

        # Chalkboard — 5 daily specials lun → ven
        "chalkboard_label":   "La pizarra de la semana",
        "chalkboard_heading": "Plato del día, <em>escrito a mano.</em>",
        "chalkboard_intro":
            "Cada mañana Nonna Rosa escribe la pizarra con la tiza, decidiendo "
            "en la barra qué vamos a cocinar hoy. Esta semana la cosa va así.",
        "chalkboard_buongiorno": "¡Buen provecho!",
        "chalkboard_days": [
            ("Lun", "Cacio e pepe",              "tonnarelli estirados a mano",                   "10,00 €"),
            ("Mar", "Bucatini all'amatriciana",  "guanciale de Amatrice de Sarnelli",             "11,00 €"),
            ("Mié", "Coda alla vaccinara",       "receta de Nonna Rosa, igual que en 1987",       "14,00 €"),
            ("Jue", "Gnocchi al sugo d'arrosto", "hechos por la mañana con patatas viejas",       "11,00 €"),
            ("Vie", "Bacalao en tempura",        "tomatitos confitados y alcachofa romana",       "13,00 €"),
        ],

        # Family strip — 3 portraits with personal blurbs
        "family_label":   "La familia en la cocina",
        "family_heading": "Tres generaciones, <em>una sola mesa.</em>",
        "family": [
            {
                "name":   "Rosa Trezzi",
                "role":   "Pasta fresca desde 1987",
                "blurb":
                    "Nonna Rosa abre la trattoria el 3 de septiembre de 1987 con un "
                    "sueño y dos rodillos. Hoy tiene ochenta y dos años y sigue "
                    "estirando la pasta cada mañana desde las siete. Su lema es "
                    "sencillo: «la pasta buena se nota bajo las manos, la balanza "
                    "no hace falta».",
                "portrait": "https://images.pexels.com/photos/2050990/pexels-photo-2050990.jpeg?auto=compress&cs=tinysrgb&w=600&h=750&fit=crop",
            },
            {
                "name":   "Marco Trezzi",
                "role":   "Pizzero · horno de leña desde 2003",
                "blurb":
                    "Hijo de Rosa, criado entre harina y ladrillos. Enciende el "
                    "horno cada tarde a las cuatro —roble del Cimino, nunca otra "
                    "cosa— y lo mantiene vivo hasta medianoche. Su Margherita "
                    "Verace la aprendió con Peppe Guida en Vico Equense, en 2008.",
                "portrait": "https://images.unsplash.com/photo-1607631568010-a87245c0daf8?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":   "Giulia Trezzi",
                "role":   "Sala y dulces caseros",
                "blurb":
                    "Nieta de Rosa, treinta años, se encarga de la sala y de los "
                    "dulces. Tiramisú con mascarpone de Sarnelli, tarta de "
                    "guindas cuando la temporada acompaña, maritozzi con nata "
                    "solo el sábado por la mañana. Te recibe con una sonrisa y "
                    "una jarra de agua con gas.",
                "portrait": "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?w=600&q=80&auto=format&fit=crop",
            },
        ],

        # Forno teaser band
        "forno_label":   "El horno de leña",
        "forno_heading": "Encendido cada tarde, <em>a las cuatro en punto.</em>",
        "forno_text":
            "El horno de cúpula de Marco es de ladrillos del Viterbese, levantado a "
            "mano por el pizzero Gennaro Esposito en 2003. Quema solo roble del "
            "Cimino, alcanza los 420 °C y saca la pizza en sesenta segundos. De "
            "martes a sábado, solo por la noche, cuando la primera sala se vacía "
            "del servicio de comidas.",
        "forno_image":    "https://images.unsplash.com/photo-1593504049359-74330189a345?w=1200&q=80&auto=format&fit=crop",
        "forno_caption":  "Margherita Verace · 420 °C · sesenta segundos",
        "forno_cta":      "Descubre pizza y pasta",
        "forno_cta_href": "forno",

        # Reviews band — 2–3 quotes
        "reviews_label": "Lo que dicen de nosotros",
        "reviews": [
            {
                "quote":  "Me he sentido en la cocina de la abuela que nunca tuve.",
                "author": "Gambero Rosso · Tre Spicchi 2024",
            },
            {
                "quote":  "Una de las últimas trattorie de verdad del Trastevere. Ve andando, por la noche, y pide la coda.",
                "author": "Corriere della Sera · Cook",
            },
            {
                "quote":  "La carbonara de Rosa hace callar a todos, incluso a los de Testaccio.",
                "author": "Puntarella Rossa · 2025",
            },
        ],

        # Hours strip — 3 rows under reviews
        "hours_label":  "Cuándo estamos abiertos",
        "hours_rows": [
            ("Mar – Sáb", "12:30 – 15:00", "comidas"),
            ("Mar – Sáb", "19:00 – 23:30", "cenas · horno de leña"),
            ("Domingo",   "12:30 – 15:00", "solo comidas · cerramos a las 16:00"),
        ],
        "hours_note": "Lunes descanso semanal · abierto todos los festivos salvo Navidad",

        # Tavolata band — group experience teaser
        "tavolata_label":   "La mesa larga",
        "tavolata_heading": "Doce amigos, <em>una sola mesa.</em>",
        "tavolata_text":
            "La mesa larga es nuestro tablón de doce plazas en la sala de la "
            "chimenea. Menú fijo a treinta y dos euros, vino de la casa incluido, "
            "dulces de Giulia para cerrar. Para cumpleaños, comuniones, cenas de "
            "promoción o, sencillamente, porque hoy es un buen día para estar "
            "juntos.",
        "tavolata_cta":      "Organiza una mesa larga",
        "tavolata_cta_href": "eventi",
        "tavolata_image":    "https://images.unsplash.com/photo-1547573854-74d2a71d0826?w=1200&q=80&auto=format&fit=crop",

        # Final CTA band
        "cta_label":    "Pásate a vernos",
        "cta_heading":  "Via dei Salumi dieciséis, <em>llama fuerte.</em>",
        "cta_intro":
            "Estamos en Via dei Salumi, a dos pasos del lungotevere. La puerta es "
            "de madera verde, el timbre hace ruido: no tengas reparo, llama "
            "fuerte. Te encontramos una copa de Cesanese fresco y una porción "
            "de pizza rossa recién salida del horno.",
        "cta_primary":      "Reservar mesa",
        "cta_primary_href": "contatti",
        "cta_secondary":    "Escribir por WhatsApp",
    },

    # ─── MENU ────────────────────────────────────────────────────
    "menu": {
        "eyebrow":  "La carta · temporada otoño '26",
        "headline": "Pasta estirada a mano, pizza al horno de leña, <em>dulces de la casa.</em>",
        "intro":
            "La carta cambia poco porque los platos de la casa son los que son: "
            "Cacio e pepe, amatriciana, carbonara, coda, saltimbocca. Las pizzas "
            "rotan según la temporada. Lo demás lo decide Nonna Rosa en la barra, "
            "por la mañana.",

        "wine_house_label":   "Vino de la casa",
        "wine_house_heading": "Cesanese del Lazio, <em>a granel, 18,00 € el litro.</em>",
        "wine_house_text":
            "El vino de la casa viene de Olevano Romano, de la bodega Proietti "
            "Riccardi, que lo hace desde hace cuarenta años. Lo servimos en jarra "
            "de litro, medio o cuartillo. Blanco: Malvasia Puntinata dei "
            "Castelli, Cantina Ribelà, también a granel.",

        "allergen_note":
            "Los platos marcados con (G) contienen gluten, (L) lactosa y "
            "(P) pescado. Si tienes alguna alergia particular, avisa en la "
            "barra antes de pedir: Rosa hizo el curso de APPCC en 2019 y se "
            "lo sabe de memoria.",

        "sections": [
            {
                "label": "Entrantes de la casa",
                "heading": "Del huerto y de la barra",
                "dishes": [
                    ("Bruschetta de tomate",            "tomatitos del Piennolo, albahaca, AOVE Sabina DOP",             "7,00 €"),
                    ("Carciofo alla giudia",            "alcachofa romana frita dos veces, limón de Amalfi",             "9,00 €"),
                    ("Supplì clásico",                  "arroz, mozzarella fundente, ragú de carne de la casa",          "4,00 €"),
                    ("Flores de calabacín fritas",      "rellenas de mozzarella y anchoa, rebozado ligero",              "8,00 €"),
                    ("Puntarelle alla romana",          "anchoas del Cantábrico, ajo, vinagre tinto",                    "8,00 €"),
                    ("Tabla de embutidos y quesos",     "guanciale de Amatrice, pecorino di Pienza, aceitunas",          "14,00 €"),
                    ("Albóndigas de Nonna Rosa",        "salsa de tomate, pan casero al lado",                           "10,00 €"),
                ],
            },
            {
                "label": "Primeros de pasta estirada a mano",
                "heading": "Del rodillo de la mañana",
                "dishes": [
                    ("Cacio e pepe",                    "tonnarelli estirados al rodillo, pecorino di Pienza",           "12,00 €"),
                    ("Carbonara clásica",               "guanciale de Amatrice, pecorino romano, cinco yemas",           "13,00 €"),
                    ("Bucatini all'amatriciana",        "guanciale, tomate San Marzano, pecorino",                       "12,00 €"),
                    ("Gnocchi al sugo d'arrosto",       "hechos por la mañana, salsa del jueves de Rosa",                "11,00 €"),
                    ("Fettuccine alla papalina",        "jamón curado, guisantes frescos, huevo, parmesano",             "13,00 €"),
                    ("Rigatoni con la pajata",          "intestino de ternera lechal, salsa de tomate",                  "15,00 €"),
                    ("Tonnarelli al cacio e tartufo",   "trufa negra de Norcia, pecorino, pimienta",                     "18,00 €"),
                ],
            },
            {
                "label": "Pizza del horno de leña",
                "heading": "Solo por la noche · martes → sábado",
                "dishes": [
                    ("Margherita Verace",               "tomate San Marzano, fiordilatte, albahaca",                     "9,00 €"),
                    ("Capricciosa de Nonna Rosa",       "alcachofas, champiñones, jamón cocido, huevo",                  "12,00 €"),
                    ("Diavola al guanciale",            "tomate, fiordilatte, salami picante, guanciale",                "11,00 €"),
                    ("Blanca al cacio e pepe",          "fiordilatte, pecorino, pimienta negra de Pondicherry",          "10,00 €"),
                    ("Nonna Rosa (firma)",              "stracciatella de Andria, tomatitos semisecos, albahaca",        "13,00 €"),
                    ("Calabaza y salsiccia",            "crema de calabaza, salsiccia de Norcia, romero",                "12,00 €"),
                ],
            },
            {
                "label": "Segundos de la barra",
                "heading": "De la cocina del domingo",
                "dishes": [
                    ("Saltimbocca alla romana",         "ternera, jamón curado, salvia, vino blanco",                    "16,00 €"),
                    ("Coda alla vaccinara",             "rabo de buey, apio, cacao, piñones, pasas",                     "17,00 €"),
                    ("Abbacchio a scottadito",          "costillitas de cordero, romero, limón",                         "19,00 €"),
                    ("Trippa alla romana",              "callos, salsa de tomate, menta, pecorino",                      "14,00 €"),
                    ("Bacalao en tempura",              "bacalao desalado, rebozado ligero, tomatitos",                  "14,00 €"),
                ],
            },
            {
                "label": "Dulces caseros",
                "heading": "Las manos de Giulia",
                "dishes": [
                    ("Tiramisú de Giulia",              "mascarpone de Sarnelli, savoiardi, café de la italiana",        "6,00 €"),
                    ("Panna cotta de vainilla",         "con guindas de Nonna Rosa",                                     "5,00 €"),
                    ("Tarta de guindas",                "masa quebrada de la casa, guindas del 2025",                    "6,00 €"),
                    ("Maritozzo con nata",              "solo el sábado por la mañana · nata fresca de Valentini",       "4,00 €"),
                    ("Helado del abuelo",               "tres sabores · fior di latte, avellana, chocolate",             "5,00 €"),
                ],
            },
        ],
    },

    # ─── STORIA (about) ──────────────────────────────────────────
    "storia": {
        "eyebrow":  "Nuestra historia · desde 1987",
        "headline": "Cuarenta años de pasta estirada <em>al rodillo.</em>",
        "intro":
            "Trattoria Da Nonna Rosa abre el 3 de septiembre de 1987 en dos "
            "habitaciones de Via dei Salumi, heredadas de la madre de Rosa "
            "Trezzi. Treinta años después seguimos aquí, en la misma cocina, "
            "con un horno más y tres generaciones de familia turnándose en la "
            "barra.",

        "story": [
            "Rosa Trezzi nace en Roma en 1944, hija de un tabernero de "
            "Testaccio. Crece entre ollas, rodillos y el bullicio del "
            "mercadillo de Porta Portese. A los quince años se casa con "
            "Marino, que era panadero, y con él abre una primera osteria "
            "en Via dei Foraggi. Dura seis años, hasta 1987, cuando el "
            "padre de Marino deja en herencia dos habitaciones en Via dei "
            "Salumi, en el Trastevere.",

            "El 3 de septiembre de 1987 la trattoria abre en el número "
            "dieciséis/a, con doce cubiertos, un horno de gas y una "
            "nevera empotrada. La carta de la primera noche está escrita "
            "a bolígrafo sobre una hoja de papel encerado: Cacio e pepe, "
            "amatriciana, Coda alla vaccinara y un tiramisú hecho con el "
            "mascarpone del lechero de abajo. Coste total de la cena: "
            "cuatro mil liras.",

            "En 2003 el hijo Marco se queda con la segunda sala —el "
            "taller de un carpintero que había cerrado— y construye el "
            "horno de leña con el pizzero Gennaro Esposito, que había "
            "venido a Roma para una boda. Desde aquel verano, la pizza "
            "entra en la carta solo por la noche, martes y sábado. "
            "Luego todas las noches, a partir de 2005.",

            "En 2024 Giulia, nieta de Rosa, vuelve de Barcelona, donde "
            "trabajaba en pastelería, y se hace cargo de la sala y de "
            "los dulces. Hoy la trattoria tiene sesenta cubiertos, tres "
            "generaciones, un horno de leña, un camarero histórico —"
            "Beppe, desde 1996— y el cartel de siempre en la puerta: a "
            "quien vuelve por segunda vez, el vino de la casa se lo "
            "invita la familia.",
        ],

        # Timeline — 3 steps
        "timeline_label":   "Tres fechas",
        "timeline": [
            {
                "year":  "1987",
                "title": "Rosa abre en el dieciséis/a",
                "desc":  "Tres de septiembre, doce cubiertos, cuatro mil liras por cabeza. La primera carta se escribe a bolígrafo sobre papel encerado.",
            },
            {
                "year":  "2003",
                "title": "Llega el horno de leña",
                "desc":  "Marco se queda con la segunda sala y levanta el horno con Gennaro Esposito. Primera Margherita: veintidós de junio.",
            },
            {
                "year":  "2024",
                "title": "Giulia vuelve a casa",
                "desc":  "Giulia regresa de Barcelona y se pone al frente de la sala. Primer maritozzo del sábado: veintiséis de octubre.",
            },
        ],

        # Family portraits (reused shape from home but with longer blurbs)
        "family_label":   "Las manos que te atienden",
        "family": [
            {
                "name":   "Rosa Trezzi",
                "role":   "Fundadora · pasta fresca desde 1987",
                "blurb":
                    "Ochenta y dos años, un nieto para cada dedo de la mano y "
                    "un rodillo que conoce de memoria. Estira la pasta cada "
                    "mañana de siete a diez, luego pasa a escribir la pizarra "
                    "del día. La carbonara la hace solo ella: es un ritual "
                    "celoso.",
                "portrait": "https://images.pexels.com/photos/2050990/pexels-photo-2050990.jpeg?auto=compress&cs=tinysrgb&w=600&h=750&fit=crop",
            },
            {
                "name":   "Marco Trezzi",
                "role":   "Pizzero · horno de leña desde 2003",
                "blurb":
                    "Criado en la trattoria, carpintero durante tres años y "
                    "después pizzero durante veintidós. Enciende el horno a "
                    "las dieciséis, hace crepitar el roble del Cimino y amasa "
                    "a mano con masa madre del 2008. La Margherita la mete "
                    "con los ojos cerrados, en sesenta segundos.",
                "portrait": "https://images.unsplash.com/photo-1607631568010-a87245c0daf8?w=600&q=80&auto=format&fit=crop",
            },
            {
                "name":   "Giulia Trezzi",
                "role":   "Sala y dulces · desde 2024",
                "blurb":
                    "Dos años con Josep Maria en una pastelería de Barcelona, "
                    "y luego la vuelta a casa. Se encarga de la sala con el "
                    "camarero Beppe, prepara los dulces del día y decide la "
                    "carta de vinos. Hace el mejor maritozzo al oeste del "
                    "Tíber, pero solo el sábado por la mañana.",
                "portrait": "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?w=600&q=80&auto=format&fit=crop",
            },
        ],

        # Valori grid — 4 cards
        "values_label":   "Nuestras reglas",
        "values_heading": "Cuatro cosas <em>que no cambian.</em>",
        "values": [
            {
                "title": "La masa de la pasta",
                "desc":
                    "Harina del Molino Paolo Mariani, agua de Roma, yemas de "
                    "Paolo Parisi. Estirada al rodillo cada mañana desde las "
                    "siete. Nunca seca, nunca congelada, nunca del día "
                    "anterior.",
            },
            {
                "title": "El horno de leña",
                "desc":
                    "Solo roble del Cimino, cortado en Vitorchiano. Encendido "
                    "cada tarde a las cuatro en punto. Si el horno no pilla "
                    "los 420 °C, esa noche la pizza no sale — así de claro.",
            },
            {
                "title": "Vino de la casa",
                "desc":
                    "Cesanese de Olevano Romano de Proietti Riccardi, "
                    "Malvasia dei Castelli de Cantina Ribelà. A granel en "
                    "jarra. Dieciocho euros el litro, la misma cifra desde "
                    "2019.",
            },
            {
                "title": "La regla de la copa",
                "desc":
                    "A quien vuelve por segunda vez, el vino de la casa se "
                    "lo invita la casa. Está escrito en la pizarra, lleva "
                    "ahí desde el primer día, no lo hemos cambiado nunca. "
                    "Aunque te reconozcamos, pídelo igual.",
            },
        ],

        "photo_image":   "https://images.unsplash.com/photo-1488477181946-6428a0291777?w=1600&q=80&auto=format&fit=crop",
        "photo_caption": "La sala de la chimenea · cena del sábado · noviembre de 2025",
    },

    # ─── FORNO (signature · pizza & pasta) ────────────────────────
    "forno": {
        "eyebrow":  "Pizza y pasta · las firmas de la casa",
        "headline": "Cuatro pizzas y cuatro pastas <em>escritas a mano.</em>",
        "intro":
            "Nuestras firmas son ocho — cuatro del horno, cuatro del rodillo. "
            "No cambian, no se adelgazan, no rotan. Son los platos que Nonna "
            "Rosa decidió en 1987 y sobre los que la familia se juega la "
            "reputación desde hace cuarenta años.",

        # Pizza section
        "pizza_label":   "Del horno de leña",
        "pizza_heading": "Cuatro pizzas <em>de autor de la casa.</em>",
        "pizza_intro":
            "El horno de leña de Marco quema solo roble del Cimino, alcanza "
            "los 420 °C y saca la pizza en sesenta segundos. Masa con 24 "
            "horas de fermentación y masa madre del 2008. Tomate San "
            "Marzano DOP, fiordilatte de Agerola de Caseificio Sorrentina.",
        "pizza_signatures": [
            {
                "n":     "I",
                "name":  "Margherita Verace",
                "desc":  "Tomate San Marzano DOP, fiordilatte de Agerola, albahaca genovesa DOP, AOVE Sabina en frío.",
                "price": "9,00 €",
            },
            {
                "n":     "II",
                "name":  "Capricciosa de Nonna Rosa",
                "desc":  "Alcachofas romanas salteadas, champiñones, jamón cocido de Prato, huevo ecológico de Parisi al centro.",
                "price": "12,00 €",
            },
            {
                "n":     "III",
                "name":  "Diavola al guanciale",
                "desc":  "Tomate, fiordilatte, salami picante de Amatrice, guanciale de Sarnelli, guindilla de Diamante.",
                "price": "11,00 €",
            },
            {
                "n":     "IV",
                "name":  "Nonna Rosa (firma de la casa)",
                "desc":  "Stracciatella de Andria en crudo, tomatitos semisecos, albahaca, AOVE Sabina, ralladura de limón de Amalfi.",
                "price": "13,00 €",
            },
        ],

        # Pasta section
        "pasta_label":   "Del rodillo",
        "pasta_heading": "Cuatro pastas <em>estiradas a mano desde las siete.</em>",
        "pasta_intro":
            "Pasta estirada al rodillo cada mañana de siete a diez. Harina "
            "del Molino Paolo Mariani, agua de Roma, yemas de Paolo Parisi. "
            "Nunca seca, nunca congelada, nunca del día anterior.",
        "pasta_signatures": [
            {
                "n":     "I",
                "name":  "Cacio e pepe",
                "desc":  "Tonnarelli estirados al rodillo, pecorino di Pienza DOP, pimienta negra de Pondicherry molida al momento.",
                "price": "12,00 €",
            },
            {
                "n":     "II",
                "name":  "Carbonara clásica",
                "desc":  "Spaghetti, guanciale de Amatrice, pecorino romano, cinco yemas de Parisi, pimienta negra. Nunca nata.",
                "price": "13,00 €",
            },
            {
                "n":     "III",
                "name":  "Bucatini all'amatriciana",
                "desc":  "Bucatini del molino, guanciale de Amatrice crujiente, San Marzano, pecorino romano rallado al plato.",
                "price": "12,00 €",
            },
            {
                "n":     "IV",
                "name":  "Fettuccine alla papalina",
                "desc":  "Fettuccine, jamón curado San Daniele, guisantes frescos, huevos, parmesano reggiano 36 meses.",
                "price": "13,00 €",
            },
        ],

        # Forno story
        "forno_story_label":   "El horno de leña",
        "forno_story_heading": "Cuatrocientos veinte grados, <em>sesenta segundos.</em>",
        "forno_story_text_1":
            "El horno de cúpula de Marco lo construyó a mano en 2003 el "
            "pizzero Gennaro Esposito, ladrillo a ladrillo, con tierra "
            "refractaria de Viterbo. Mide dos metros y diez de diámetro, "
            "cuece seis pizzas a la vez y alcanza los 420 grados con una "
            "cesta de roble del Cimino cortado en Vitorchiano.",
        "forno_story_text_2":
            "Encendido cada tarde a las cuatro en punto. Si a las seis "
            "aún no ha cogido la temperatura, esa noche la pizza no sale "
            "— ha pasado tres veces en veintidós años, la última en "
            "febrero de 2024 con la nevada gorda, y esa noche hicimos "
            "todos pasta.",
        "forno_story_image":
            "https://images.unsplash.com/photo-1571997478779-2adcbbe9ab2f?w=1600&q=80&auto=format&fit=crop",
        "forno_story_caption": "Roble del Cimino · horno a 420 °C · julio de 2025",

        # Ingredients/producers band
        "producers_label":   "Cinco manos que firman",
        "producers_heading": "De dónde vienen, <em>y de quién.</em>",
        "producers": [
            {
                "name":       "Sarnelli Guanciale",
                "place":      "Amatrice · Lazio",
                "ingredient": "Guanciale de cerdo negro casertano · curación 90 días",
            },
            {
                "name":       "Molino Paolo Mariani",
                "place":      "Barchi · Marche",
                "ingredient": "Harina tipo 0 y 00 · trigo Senatore Cappelli · molida a la piedra",
            },
            {
                "name":       "Proietti Riccardi",
                "place":      "Olevano Romano · Lazio",
                "ingredient": "Cesanese del Lazio a granel · viñas en vaso · cosecha 2024",
            },
            {
                "name":       "Caseificio Sorrentina",
                "place":      "Agerola · Campania",
                "ingredient": "Fiordilatte de búfala campana · entrega diaria",
            },
            {
                "name":       "Paolo Parisi",
                "place":      "Usigliano di Lari · Toscana",
                "ingredient": "Huevos de gallina alimentada con leche de cabra · yema anaranjada",
            },
        ],

        # Dough photo
        "dough_image":   "https://images.unsplash.com/photo-1473093295043-cdd812d0e601?w=1600&q=80&auto=format&fit=crop",
        "dough_caption": "Masa con 24 horas · masa madre del 2008",
    },

    # ─── EVENTI (events & tavolate) ──────────────────────────────
    "eventi": {
        "eyebrow":  "Mesas largas y eventos · grupos de doce a sesenta",
        "headline": "Una mesa larga, <em>todos juntitos.</em>",
        "intro":
            "La sala de la chimenea se abre para mesas largas de doce plazas en "
            "adelante. Menú fijo, vino de la casa incluido, dulces de Giulia "
            "para cerrar. Para cumpleaños, comuniones, cenas de promoción, "
            "despedidas de soltero, cenas de empresa — o, sencillamente, "
            "porque estar juntos sienta bien.",

        # 3 group experiences
        "experiences_label":   "Tres fórmulas",
        "meta_menu_label":     "Menú",
        "meta_wine_label":     "Vinos",
        "experiences": [
            {
                "n":       "01",
                "title":   "Mesa larga",
                "persons": "de 12 a 20 personas",
                "menu":    "Entrante variado, dos primeros a elegir, segundo, postre · 32,00 €",
                "wine":    "Cesanese de la casa y agua incluidos",
                "desc":
                    "La fórmula histórica: tablón largo en la sala de la "
                    "chimenea, platos para compartir, tiempos tranquilos. "
                    "Perfecta para cumpleaños, cenas de promoción, "
                    "despedidas de soltero. Se reserva con cuatro días "
                    "de antelación.",
            },
            {
                "n":       "02",
                "title":   "Comunión y bautizo",
                "persons": "de 20 a 40 personas",
                "menu":    "Bufet de entrantes, dos primeros, dos segundos, tarta · 48,00 €",
                "wine":    "Cesanese + Malvasia + refrescos incluidos · burbujas aparte",
                "desc":
                    "Dos salas abiertas a medida, niños bienvenidos, tarta "
                    "de Giulia incluida en el menú (eliges entre tres: "
                    "ricotta y guindas, chocolate y peras, milhojas de "
                    "vainilla). Se reserva con dos semanas de antelación.",
            },
            {
                "n":       "03",
                "title":   "Cena de empresa",
                "persons": "de 25 a 60 personas",
                "menu":    "Menú degustación de cinco platos · 62,00 €",
                "wine":    "Maridaje del sumiller de la casa · cuatro copas",
                "desc":
                    "Privatización completa de la trattoria, una noche "
                    "entre semana (mar–jue). Menú en tres idiomas si hace "
                    "falta, proyector para presentaciones, wifi libre. Se "
                    "reserva con un mes de antelación.",
            },
        ],

        # Birthday/celebration block
        "birthday_label":   "Cumpleaños y aniversarios",
        "birthday_heading": "Tarta de Giulia, velas <em>y un brindis con Nonna Rosa.</em>",
        "birthday_text":
            "Para cada cumpleaños, Giulia prepara una tarta a medida (avisa con "
            "dos días de antelación del sabor preferido). La sacamos con las "
            "velas encendidas, Nonna Rosa sale de la cocina para el brindis "
            "y, si tienes suerte, hasta te canta una estrofa de Roma nun fa' "
            "la stupida stasera — pero solo si se lo pides tú, porque con "
            "nosotros no lo hace nunca.",
        "birthday_image":   "https://images.unsplash.com/photo-1540189549336-e6e99c3679fe?w=1200&q=80&auto=format&fit=crop",
        "birthday_caption": "Tarta de ricotta y guindas · sesenta cumpleaños de Beppe",

        # Contact card specific to events
        "contact_label":    "Para organizar una mesa larga",
        "contact_heading":  "Habla directamente <em>con Giulia.</em>",
        "contact_text":
            "Las mesas largas y los eventos los lleva Giulia en persona. Llámala "
            "entre las diez y las doce de la mañana (es la hora en la que "
            "todavía no está en sala) o escríbele por WhatsApp: te responde por "
            "la tarde. Si el correo te resulta más cómodo, también vale.",
        "contact_phone":    "06 581 4488",
        "contact_whatsapp": "06 581 4488",
        "contact_email":    "eventi@trattoriadanonnarosa.it",
        "contact_cta":      "Escribe a Giulia",
        "contact_cta_href": "contatti",
    },

    # ─── CONTATTI (reservations + find us) ────────────────────────
    "contatti": {
        "eyebrow":  "Encuéntranos y reserva · Via dei Salumi 16/a",
        "headline": "Reserva una mesa, <em>o pásate sin más.</em>",
        "intro":
            "Estamos en Via dei Salumi, en el Trastevere, a cinco minutos "
            "andando del lungotevere. Si venís dos o tres, no hace falta "
            "reservar: entras y te encontramos una mesa. A partir de cuatro, "
            "mejor una llamada el día antes. Para grupos de más de doce, pasa "
            "a la página de mesas largas.",

        # Address card
        "address_label":   "Dónde estamos",
        "address_heading": "Via dei Salumi 16/a",
        "address_text":
            "En el Trastevere, entre Piazza dei Mercanti y el lungotevere "
            "Ripa. La puerta es de madera verde, el timbre hace ruido. "
            "Metro línea B parada Circo Massimo (diez minutos a pie), "
            "tranvía 8 parada Belli (cuatro minutos), autobús H parada "
            "Sonnino.",
        "address_city":    "00153 Roma · Trastevere",

        # Hours table — 4 rows
        "hours_label":   "Horario de apertura",
        "hours_heading": "Comida y cena, <em>lunes descanso.</em>",
        "hours_table": [
            ("Martes – sábado", "12:30 – 15:00", "comidas"),
            ("Martes – sábado", "19:00 – 23:30", "cenas · horno de leña encendido"),
            ("Domingo",         "12:30 – 15:00", "solo comidas · cerramos a las 16:00"),
            ("Lunes",           "cerrado",       "descanso semanal"),
        ],

        # Phone/WhatsApp/email card
        "contact_label":     "Habla con nosotros",
        "contact_heading":   "Tres formas, <em>todas buenas.</em>",
        "contact_phone_label":    "Llama a la barra",
        "contact_phone_value":    "06 581 4488",
        "contact_phone_hours":    "Te atiende Giulia de 10 a 23",
        "contact_whatsapp_label": "Escribe por WhatsApp",
        "contact_whatsapp_value": "06 581 4488",
        "contact_whatsapp_hours": "Te respondemos en menos de una hora",
        "contact_email_label":    "Mándanos un correo",
        "contact_email_value":    "ciao@trattoriadanonnarosa.it",
        "contact_email_hours":    "Respondemos al día siguiente",

        # Reservation form
        "form_label":    "Reserva online",
        "form_heading":  "Reserva una mesa, <em>ya la apuntamos en la pizarra.</em>",
        "form_intro":
            "Rellena el formulario de aquí abajo. Recibirás la confirmación por "
            "SMS o WhatsApp en menos de dos horas (estamos en la cocina, pero "
            "los teléfonos los miramos). Para grupos de más de doce, escríbenos "
            "directamente por WhatsApp.",

        "form_sections": [
            {
                "num":   "01",
                "title": "Quién eres",
                "meta":  "Para confirmarte la mesa",
                "fields": ["name", "email", "phone"],
            },
            {
                "num":   "02",
                "title": "Cuándo vienes",
                "meta":  "Fecha, hora y cuántos sois",
                "fields": ["date", "time", "people"],
            },
            {
                "num":   "03",
                "title": "Notas",
                "meta":  "Ocasión, alergias, preferencias",
                "fields": ["occasion", "notes"],
            },
        ],

        "form_fields": [
            {
                "name":     "name",
                "label":    "Nombre y apellidos",
                "type":     "text",
                "placeholder": "Cómo te llamamos en la mesa",
                "required": True,
                "helper":   "Lo apuntamos en la pizarra de las reservas.",
            },
            {
                "name":     "email",
                "label":    "Correo electrónico",
                "type":     "email",
                "placeholder": "nombre@ejemplo.es",
                "required": True,
                "helper":   "Te mandamos la confirmación aquí.",
            },
            {
                "name":     "phone",
                "label":    "Teléfono o WhatsApp",
                "type":     "tel",
                "placeholder": "+34 612 34 56 78",
                "required": True,
                "helper":   "Te llamamos aquí solo si surge algún imprevisto.",
            },
            {
                "name":     "date",
                "label":    "Fecha",
                "type":     "date",
                "placeholder": "dd/mm/aaaa",
                "required": True,
                "helper":   "Los lunes estamos cerrados.",
            },
            {
                "name":     "time",
                "label":    "Hora",
                "type":     "time",
                "placeholder": "ej. 20:30",
                "required": True,
                "helper":   "Comidas 12:30–14:30 · cenas 19:00–22:30.",
            },
            {
                "name":     "people",
                "label":    "Cuántos sois",
                "type":     "number",
                "placeholder": "número de cubiertos",
                "required": True,
                "helper":   "A partir de doce, escríbenos directamente por WhatsApp.",
            },
            {
                "name":     "occasion",
                "label":    "Ocasión",
                "type":     "select",
                "placeholder": "",
                "required": False,
                "full_width": True,
                "helper":   "Si es un cumpleaños, preparamos la tarta de Giulia.",
            },
            {
                "name":     "notes",
                "label":    "Notas para la cocina",
                "type":     "textarea",
                "placeholder": "Alergias, platos preferidos, peticiones particulares…",
                "required": False,
                "full_width": True,
                "helper":   "Nonna Rosa hizo el curso de APPCC en 2019: dilo y listo.",
            },
        ],

        "occasion_options": [
            "Cena normal",
            "Cumpleaños",
            "Aniversario",
            "Cena de trabajo",
            "Primera vez con nosotros",
            "Mesa larga (12+)",
            "Otro",
        ],

        "consent":
            "Acepto el tratamiento de los datos para gestionar la reserva "
            "(sin boletín, sin publicidad, nunca).",
        "form_submit":      "Reservar la mesa",
        "form_submit_note": "Te confirmamos en menos de dos horas, por SMS o WhatsApp.",

        # Map
        "map_label":    "En el mapa",
        "map_heading":  "Via dei Salumi 16/a · Trastevere",
        "map_embed":
            "https://www.openstreetmap.org/export/embed.html"
            "?bbox=12.4660%2C41.8880%2C12.4720%2C41.8910"
            "&layer=mapnik&marker=41.8893%2C12.4690",
        "map_link":     "Abrir en OpenStreetMap",
        "map_link_href":"https://www.openstreetmap.org/?mlat=41.8893&mlon=12.4690#map=17/41.8893/12.4690",

        # Getting-here notes
        "transport_label":   "Cómo llegar",
        "transport_heading": "Tres maneras, <em>todas andando desde el centro.</em>",
        "transport": [
            {
                "mode":  "Metro",
                "line":  "B · parada Circo Massimo",
                "note":  "Diez minutos a pie por via di Monte Savello y el lungotevere Ripa.",
            },
            {
                "mode":  "Tranvía",
                "line":  "8 · parada Belli",
                "note":  "Cuatro minutos a pie, cruzando Piazza Trilussa hacia Via dei Salumi.",
            },
            {
                "mode":  "Autobús",
                "line":  "H · parada Sonnino",
                "note":  "Seis minutos a pie, pasando por Piazza in Piscinula.",
            },
            {
                "mode":  "Andando desde el centro",
                "line":  "Ponte Sisto · quince minutos",
                "note":  "Desde Piazza Navona, cruzando Campo de' Fiori y el ponte Sisto.",
            },
        ],
    },

    # No blog
    "posts": [],
}
