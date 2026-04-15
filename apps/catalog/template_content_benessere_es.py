"""BENESSERE_CONTENT_ES — native wellness-premium translation.

Registro editorial: Mía Wellness / El País Sección Wellness / Six Senses.
Usted peninsular cálido, escritura sensorial, literaria. Nombres propios
italianos (Studio Armonia, Bergamo Alta, Via Arena 15, Sara Conti, Davide
Lai, Yara Bonomi, Elena Rossi, Miguel Ferrari, Chiara Bonomi) preservados
en forma original.
"""
from __future__ import annotations

from typing import Any

from apps.catalog.template_content_benessere import (
    _AMBIENT_CANDLES,
    _AMBIENT_MASSAGE,
    _AMBIENT_RITUAL,
    _AMBIENT_TEA,
    _AMBIENT_YOGA,
    _HERO_IMG,
    _MAP_IMG,
    _PORTRAIT_DAVIDE,
    _PORTRAIT_ELENA,
    _PORTRAIT_MIGUEL,
    _PORTRAIT_SARA,
    _PORTRAIT_YARA,
    _ROOM_GARDEN,
    _ROOM_HAMMAM,
    _ROOM_MEDITATION,
    _ROOM_RECEPTION,
    _ROOM_TISANERIA,
    _ROOM_WATER,
)


BENESSERE_CONTENT_ES: dict[str, Any] = {
    "pages": [
        {"slug": "home",           "label": "Inicio",          "kind": "home"},
        {"slug": "filosofia",      "label": "Filosofía",       "kind": "about"},
        {"slug": "rituali",        "label": "Rituales",        "kind": "services"},
        {"slug": "ambienti",       "label": "Espacios",        "kind": "gallery"},
        {"slug": "professionisti", "label": "Profesionales",   "kind": "team"},
        {"slug": "contatti",       "label": "Contacto",        "kind": "contact"},
        {"slug": "prenota",        "label": "Reservar",        "kind": "appointment"},
    ],

    "site": {
        "logo_initial":  "A",
        "logo_word":     "Studio Armonia",
        "tag":           "Casa holística · Bergamo Alta · 800 m sobre el nivel del mar",
        "nav_cta":       "Reservar un ritual",
        "phone":         "+39 035 412 998",
        "email":         "ritual@studioarmonia.it",
        "address":       "Via Arena 15 · 24129 Bergamo Alta",
        "hours_compact": "Lun – Sáb · con cita previa",
        "hours_footer_rows": [
            "Lun – Vie · 9:00 – 20:00",
            "Sábado · 9:00 – 18:00",
            "Domingo · jornada del silencio",
        ],
        "license":       "Profesionales acreditados por FIF y SIAF (federaciones italianas)",
        "footer_intro":
            "Studio Armonia es una casa holística independiente, nacida "
            "en 2011 dentro de los muros de piedra de Bergamo Alta. "
            "Rituales a medida, profesionales acreditados, tiempo sin "
            "prisa — para quien busca un respiro, no una prestación.",
        "socials": [
            ("Instagram", "#"),
            ("Journal",   "#"),
            ("Telegram",  "#"),
        ],
    },

    # ───────────────────────── HOME ─────────────────────────
    "home": {
        "hero_image":  _HERO_IMG,
        "eyebrow":     "Casa holística · Bergamo Alta",
        "headline":    'Un respiro es la medida de <em>nuestro tiempo</em>',
        "subhead":
            "Rituales a medida inspirados en las tradiciones mediterráneas "
            "y orientales, en un refugio de piedra al margen del tiempo, a "
            "ochocientos metros sobre el nivel del mar.",
        "primary_cta":   "Reserve su ritual",
        "secondary_cta": "Consultar los tratamientos",
        "hero_meta": [
            "Bergamo Alta",
            "Desde 2011",
            "Cinco profesionales acreditados",
            "Silencio los domingos",
        ],

        "manifesto_label": "Manifiesto · Studio Armonia",
        "manifesto":
            "A Armonia no se viene para añadir — se viene para dejar. "
            "Dejar la prisa, la voz interior que reprende, la postura "
            "cansada de quien sostiene tres pensamientos a la vez. "
            "Nuestros rituales están hechos de tiempo pausado, aceites "
            "tibios, aguas de manantial y silencios escogidos. No somos "
            "un spa de hotel: somos un taller de presencia, abierto "
            "desde hace quince años entre los muros altos de Bérgamo.",
        "manifesto_signature": "— Chiara Bonomi, fundadora",

        "rituali_label": "Rituales destacados",
        "rituali_heading": 'Cuatro <em>medidas del tiempo</em> para elegir',
        "rituali_intro":
            "El listado completo de diez rituales está en su página "
            "dedicada. Aquí los más solicitados por quienes nos visitan "
            "por primera vez.",
        "rituali": [
            ("Masaje Mediterráneo",
             "55 minutos · aceite de oliva y cítricos de Sorrento",
             "85 €"),
            ("Ritual Hammam",
             "90 minutos · vapor, sal gruesa, arcilla roja",
             "120 €"),
            ("Reequilibrio energético",
             "60 minutos · pranoterapia y respiración guiada",
             "95 €"),
            ("Ayurveda Abhyanga",
             "90 minutos · aceites tibios, a cuatro manos",
             "135 €"),
        ],

        "benefits_label": "Lo que uno se lleva",
        "benefits_heading": 'Tres <em>palabras</em>, no tres promesas',
        "benefits_intro":
            "No prometemos transformaciones radicales en noventa "
            "minutos. Prometemos una desaceleración mesurada y repetible.",
        "benefits": [
            ("Equilibrio",
             "Un sistema nervioso que se afloja, una postura que se "
             "reencuentra, un ritmo respiratorio que deja de perseguir "
             "los plazos."),
            ("Respiración",
             "La práctica respiratoria es el hilo conductor de cada "
             "ritual. Uno se marcha sabiendo dónde está su diafragma — y "
             "dónde se había detenido."),
            ("Arraigo",
             "Contacto con el propio peso, con la piedra antigua bajo "
             "los pies, con este territorio. No se medita en el vacío: "
             "se medita en casa."),
        ],

        "ambients_label": "Espacios · Studio Armonia",
        "ambients_heading": 'Un edificio del <em>siglo XVII</em>, restaurado con mesura',
        "ambients_intro":
            "Palazzo Bonomi Suardi, Via Arena 15. Cuatro salas, un "
            "claustro con hierbas oficinales, una tisanería abierta a "
            "todos los huéspedes.",
        "ambients": [
            (_AMBIENT_MASSAGE, "Sala del Masaje",       "luz rasante desde las vidrieras a toda altura"),
            (_AMBIENT_TEA,     "Tisanería de Hierbas",  "recogidas en el claustro · servidas en porcelana"),
            (_AMBIENT_CANDLES, "Sala del Ritual",       "velas de cera de abeja · toallas tibias"),
            (_AMBIENT_YOGA,    "Estudio del Aliento",   "parqué antiguo · alfombras de lana cruda"),
        ],

        "therapists_label": "Profesionales",
        "therapists_heading": 'Cinco <em>manos</em> que conocen el nombre de cada huésped',
        "therapists_intro":
            "Cada ritual lo conduce personalmente un profesional "
            "acreditado. El listado completo, con biografías extendidas, "
            "se encuentra en la página Profesionales.",
        "therapists_trio": [
            {
                "name": "Sara Conti",
                "role": "Naturópata · Cofundadora",
                "bio":
                    "Doce años de práctica, formada en el Istituto Riza "
                    "de Milán. Se ocupa de fitoterapia, hidroterapia "
                    "alpina y del programa estacional de depuración.",
                "portrait": _PORTRAIT_SARA,
            },
            {
                "name": "Davide Lai",
                "role": "Osteópata D.O.",
                "bio":
                    "Diplomado en la Scuola Superiore di Osteopatia "
                    "Italiana, especializado en técnicas craneosacrales "
                    "y viscerales. Recibe los martes y los jueves.",
                "portrait": _PORTRAIT_DAVIDE,
            },
            {
                "name": "Yara Bonomi",
                "role": "Profesional de ayurveda",
                "bio":
                    "Formada en Varkala (India) y acreditada por la "
                    "Sociedad Italiana de Ayurveda (S.I.A.). Conduce los "
                    "rituales Abhyanga y el Lomi-Lomi hawaiano, siempre "
                    "a cuatro manos junto con una segunda profesional.",
                "portrait": _PORTRAIT_YARA,
            },
        ],

        "journey_label": "Cómo se desarrolla la visita",
        "journey_heading": 'La <em>visita</em>, paso a paso',
        "journey_intro":
            "Cada ritual sigue la misma liturgia: acogida silenciosa, "
            "tratamiento, pausa con infusión, respiración. No hay "
            "altavoces ni música impuesta — el tiempo se mide solo.",
        "journey": [
            {
                "num": "01",
                "title": "Acogida",
                "body":
                    "En el umbral deja calzado, teléfono y prisa. Se "
                    "le ofrece una infusión tibia de temporada, una "
                    "hoja de papel reciclado para anotar peticiones y "
                    "atenciones, diez minutos de silencio antes de "
                    "entrar en sala.",
            },
            {
                "num": "02",
                "title": "Ritual del cuerpo",
                "body":
                    "El tratamiento que ha elegido — masaje, hammam, "
                    "shiatsu — lo conduce su profesional con aceites "
                    "preparados en la propia casa y lienzos de lino "
                    "natural. No hay esperas dentro de la sala.",
            },
            {
                "num": "03",
                "title": "Pausa con infusión",
                "body":
                    "Tras el ritual, quince minutos en la tisanería con "
                    "una mezcla ajustada a la estación y a su "
                    "constitución: ortiga en primavera, melisa en "
                    "verano, jengibre en invierno.",
            },
            {
                "num": "04",
                "title": "Respiración de cierre",
                "body":
                    "Tres minutos de respiración guiada antes de "
                    "devolverle teléfono y calzado. Es la parte más "
                    "breve de la liturgia — y la que se lleva a casa.",
            },
        ],

        "calendar_label": "Próxima disponibilidad",
        "calendar_heading": 'Elija su <em>momento</em>',
        "calendar_intro":
            "Una selección de las franjas abiertas esta semana. Para "
            "la agenda completa y las peticiones especiales, utilice el "
            "formulario de la página Reservar.",
        "calendar": [
            {"day": "Lun", "num": "14", "month": "Abr",
             "slots": ["10:00", "14:30", "17:00"], "has_slots": True, "soldout": False},
            {"day": "Mar", "num": "15", "month": "Abr",
             "slots": ["09:30", "15:00"],         "has_slots": True, "soldout": False},
            {"day": "Mié", "num": "16", "month": "Abr",
             "slots": ["11:00", "16:30"],         "has_slots": True, "soldout": False},
            {"day": "Jue", "num": "17", "month": "Abr",
             "slots": ["completo"],               "has_slots": False, "soldout": True},
            {"day": "Vie", "num": "18", "month": "Abr",
             "slots": ["10:30", "14:00", "18:00"], "has_slots": True, "soldout": False},
            {"day": "Sáb", "num": "19", "month": "Abr",
             "slots": ["completo"],               "has_slots": False, "soldout": True},
            {"day": "Dom", "num": "20", "month": "Abr",
             "slots": ["silencio"],               "has_slots": False, "soldout": True},
        ],
        "calendar_cta": "Abrir el formulario de reserva",

        "press_label": "Hablan de nosotros en",
        "press": [
            "Vogue Italia Living",
            "Marie Claire",
            "Io Donna",
            "Natural Style",
            "Corriere della Sera · Salute",
        ],
    },

    # ──────────────────── FILOSOFIA (about) ────────────────────
    "filosofia": {
        "eyebrow":  "Nuestra filosofía",
        "headline": "Tres palabras, <em>ninguna promesa</em>",
        "intro":
            "Studio Armonia nació en 2011 a partir de una idea sencilla: "
            "una casa holística que no venda transformaciones, sino que "
            "devuelva tiempo. Tres pilares — Aliento, Ritual, Naturaleza — "
            "inspiran cada elección, desde la carta de tratamientos hasta "
            "las hierbas de la tisanería.",

        "pillars": [
            {
                "init":  "A",
                "title": "Aliento",
                "body":
                    "El aliento es el hilo conductor de cada ritual. "
                    "Cada tratamiento comienza y termina con tres "
                    "minutos de práctica respiratoria — lo llamamos "
                    "el ritmo del regreso.",
            },
            {
                "init":  "R",
                "title": "Ritual",
                "body":
                    "Ni sesiones, ni paquetes: rituales. Cada uno con "
                    "una liturgia precisa, repetible, que no depende "
                    "del humor del profesional ni de la agenda de la "
                    "semana.",
            },
            {
                "init":  "N",
                "title": "Naturaleza",
                "body":
                    "Nuestras materias proceden del territorio: aceite "
                    "de oliva de Apulia, sal del Adriático, arcillas de "
                    "las colinas emilianas, hierbas recogidas en el "
                    "claustro de marzo a octubre.",
            },
        ],

        "photo_image": _AMBIENT_RITUAL,
        "photo_caption":
            "Sala del Ritual · Palazzo Bonomi Suardi, Bergamo Alta",
        "photo_sub": "Restauración conservadora · 2011",

        "timeline_label": "Nuestra historia",
        "timeline_heading": "Quince años de <em>trabajo silencioso</em>",
        "timeline": [
            {
                "year":  "2011",
                "title": "La primera sala en Via Arena",
                "body":
                    "Chiara Bonomi y Sara Conti abren el primer "
                    "espacio en la planta baja del Palazzo Bonomi "
                    "Suardi. Dos salas, una sala de espera, una "
                    "tisanería de cuatro metros cuadrados.",
            },
            {
                "year":  "2014",
                "title": "El claustro de las hierbas oficinales",
                "body":
                    "Se restaura el claustro interior y se planta el "
                    "primer jardín de hierbas oficinales: melisa, "
                    "lavanda, salvia esclarea, hipérico, ortiga, menta "
                    "piperita.",
            },
            {
                "year":  "2018",
                "title": "El hammam y la sala del vapor",
                "body":
                    "Se añade la sala hammam con bóveda de cañón de "
                    "ladrillo recuperado, diseñada por la arquitecta "
                    "Valeria Cipolli en diálogo con la Soprintendenza.",
            },
            {
                "year":  "2022",
                "title": "El Estudio del Aliento",
                "body":
                    "Apertura del Estudio del Aliento en la primera "
                    "planta, sobre parqué antiguo restaurado, dedicado "
                    "al yoga, la meditación y las prácticas somáticas "
                    "en grupo (máximo seis personas).",
            },
        ],

        "cta_label": "El siguiente paso",
        "cta_heading": 'Conocer <em>Studio Armonia</em> en persona',
        "cta_sub":
            "El umbral no se cruza en línea. Reserve un ritual breve "
            "— sesenta y cinco minutos — y deje que el espacio haga "
            "el resto.",
        "cta_primary":   "Reservar un ritual",
        "cta_secondary": "Consultar los rituales",
    },

    # ──────────────────── RITUALI (services) ────────────────────
    "rituali": {
        "eyebrow":  "Carta de rituales",
        "headline": "Diez rituales, <em>ningún carril rápido</em>",
        "intro":
            "Cada ritual tiene una duración precisa, un profesional "
            "dedicado, una liturgia que se ha ido asentando con los "
            "años. Los precios son definitivos — no hay recargos de "
            "fin de semana ni suplementos ocultos.",

        "treatments": [
            {
                "name":  "Masaje Mediterráneo",
                "meta":  "55 min · aceite de oliva de Sorrento y cítricos",
                "desc":
                    "Presiones largas, aceite tibio extraído en frío, "
                    "esencias de bergamota y limón de Sorrento. "
                    "Indicado para la primera visita o para quien "
                    "busca un ritual introductorio no invasivo.",
                "price": "85 €",
            },
            {
                "name":  "Ritual Hammam",
                "meta":  "90 min · vapor, sal gruesa, arcilla roja",
                "desc":
                    "Veinticuatro minutos en sala de vapor con aceites "
                    "esenciales de eucalipto, exfoliación con sal "
                    "gruesa del Adriático, mascarilla de arcilla roja "
                    "de las colinas boloñesas, ducha de manantial, "
                    "infusión de cierre. A cuatro manos.",
                "price": "120 €",
            },
            {
                "name":  "Reequilibrio energético",
                "meta":  "60 min · pranoterapia y respiración guiada",
                "desc":
                    "Sesión sin contacto de pranoterapia conducida "
                    "por Chiara Bonomi, con práctica respiratoria "
                    "guiada en los primeros y últimos diez minutos. "
                    "Apta también durante el embarazo a partir del "
                    "segundo trimestre.",
                "price": "95 €",
            },
            {
                "name":  "Hidroterapia alpina",
                "meta":  "75 min · aguas de manantial del Monte Resegone",
                "desc":
                    "Circuito de tres piscinas a temperatura creciente "
                    "con aguas de manantial embotelladas en origen, "
                    "alternadas con chorros fríos. Lo conduce Davide "
                    "Lai.",
                "price": "110 €",
            },
            {
                "name":  "Piedras Calientes",
                "meta":  "75 min · basalto volcánico · aceite de almendras",
                "desc":
                    "Doce piedras de basalto calentadas a 48 °C "
                    "colocadas sobre los puntos Shu de la espalda, "
                    "masaje de desbloqueo con aceite de almendras "
                    "dulces y aceite esencial de incienso.",
                "price": "105 €",
            },
            {
                "name":  "Ayurveda Abhyanga",
                "meta":  "90 min · aceites tibios medicinales · dos profesionales",
                "desc":
                    "Ritual ayurvédico clásico conducido por Yara "
                    "Bonomi junto a una segunda profesional. Aceites "
                    "medicinales elegidos según la constitución (Vata, "
                    "Pitta, Kapha) detectada en la consulta previa.",
                "price": "135 €",
            },
            {
                "name":  "Shiatsu",
                "meta":  "60 min · presiones en los meridianos · futón",
                "desc":
                    "Sesión tradicional de shiatsu conducida por "
                    "Miguel Ferrari sobre futón japonés. El huésped "
                    "permanece vestido con ropa cómoda facilitada por "
                    "el estudio.",
                "price": "90 €",
            },
            {
                "name":  "Lomi-Lomi",
                "meta":  "75 min · masaje hawaiano de olas largas",
                "desc":
                    "Olas largas con antebrazo y palma de la mano, "
                    "aceites tropicales de coco y monoi. Lo conduce "
                    "Yara Bonomi, acreditada por la Hawaiian Lomi-"
                    "Lomi School de Kauai.",
                "price": "115 €",
            },
            {
                "name":  "Craneosacral",
                "meta":  "55 min · tacto leve · fluidos cefalorraquídeos",
                "desc":
                    "Sesión osteopática craneosacral conducida por "
                    "Davide Lai. Presiones muy ligeras (por debajo de "
                    "los cinco gramos) para escuchar y acompañar el "
                    "ritmo de los fluidos. Compatible con el embarazo.",
                "price": "95 €",
            },
            {
                "name":  "Ritual Madre-Tierra",
                "meta":  "105 min · ritual completo de temporada",
                "desc":
                    "Nuestro ritual más extenso, pensado para los "
                    "cambios de estación: hidroterapia breve, "
                    "exfoliación corporal, masaje con aceites de "
                    "temporada, rito de cierre con cuenco tibetano y "
                    "tisana de rosa canina.",
                "price": "150 €",
            },
        ],
        "reserve_label": "Reservar",

        "advice_label":   "Antes del tratamiento",
        "advice_heading": "Tres <em>atenciones</em> que aconsejamos",
        "advice": [
            {
                "title": "Llegue quince minutos antes",
                "body":
                    "La transición no es un lujo: forma parte del "
                    "ritual. Un cuarto de hora en la sala de espera, "
                    "con una infusión tibia, permite que el sistema "
                    "nervioso se alinee con el espacio.",
            },
            {
                "title": "Evite el café en las dos horas previas",
                "body":
                    "La cafeína vuelve el cuerpo más reactivo a las "
                    "presiones y acorta la ventana de relajación. Una "
                    "infusión, un vaso de agua templada, una "
                    "manzanilla: mucho mejor.",
            },
            {
                "title": "Comunique cada atención",
                "body":
                    "Embarazo, ciclo menstrual, intolerancias "
                    "olfativas, lesiones recientes, medicación: deben "
                    "comunicarse siempre al reservar. Nada resulta "
                    "incómodo — todo es útil para su profesional.",
            },
        ],

        "packages_label":   "Paquetes · fines de semana largos",
        "packages_heading": 'Dos <em>estancias</em> pensadas como paréntesis',
        "packages_intro":
            "Dos propuestas cosidas con hoteles asociados en Bergamo "
            "Alta para quien desea una estancia breve de recuperación.",
        "packages": [
            {
                "tag":       "Jornada única",
                "title":     "Aliento",
                "duration":  "1 día · 3 rituales · infusiones ilimitadas",
                "desc":
                    "Una jornada completa en el estudio con tres "
                    "rituales encadenados, acceso a la tisanería de "
                    "diez de la mañana a seis de la tarde, comida "
                    "ligera in-house a cargo del chef Matteo Riva.",
                "includes": [
                    "Entrada a las 10:00, salida antes de las 18:00",
                    "Reequilibrio energético (60 min)",
                    "Masaje Mediterráneo (55 min)",
                    "Ritual Madre-Tierra breve (75 min)",
                    "Comida ligera · tisanería ilimitada",
                ],
                "price": "340 €",
                "cta":   "Reservar Aliento",
            },
            {
                "tag":       "Tres días",
                "title":     "Detox tres días",
                "duration":  "3 jornadas · 5 rituales · tisanería estacional",
                "desc":
                    "Tres jornadas cosidas con el Hotel Gombit cuatro "
                    "estrellas (habitación doble incluida), cinco "
                    "rituales repartidos en los tres días, plan "
                    "alimentario vegetariano acordado con la naturópata.",
                "includes": [
                    "2 noches · Hotel Gombit 4★",
                    "Cinco rituales en tres jornadas",
                    "Plan alimentario vegetariano a cargo de la naturópata",
                    "Acceso libre al claustro y al Estudio del Aliento",
                    "Kit estacional para llevar a casa · valor 85 €",
                ],
                "price": "920 €",
                "cta":   "Reservar los tres días",
            },
        ],

        "cta_label": "El siguiente paso",
        "cta_heading": 'Un único <em>umbral</em> que cruzar',
        "cta_sub":
            "Reserve el ritual que más le atrae. Si no está seguro "
            "de cuál elegir, escríbanos: le orientamos nosotros.",
        "cta_primary":   "Abrir el formulario de reserva",
        "cta_secondary": "Pedir consejo",
    },

    # ──────────────────── AMBIENTI (gallery) ────────────────────
    "ambienti": {
        "eyebrow":  "Palazzo Bonomi Suardi",
        "headline": 'Ocho <em>salas</em>, un claustro, una tisanería',
        "intro":
            "Cada espacio ha sido restaurado en diálogo con la "
            "Soprintendenza ai Beni Architettonici de Bérgamo. Ladrillo "
            "visto, parqué antiguo, vidrieras que abren al claustro de "
            "las hierbas oficinales.",
        "rooms": [
            {
                "span":  "a",
                "image": _ROOM_HAMMAM,
                "tag":   "Sala I · Hammam",
                "title": "Hammam abovedado",
                "sub":
                    "Bóveda de cañón en ladrillo recuperado durante "
                    "la restauración, gradas a dos niveles, "
                    "exfoliación con sal gruesa y chorro de agua de "
                    "manantial fría.",
            },
            {
                "span":  "b",
                "image": _AMBIENT_MASSAGE,
                "tag":   "Sala II · Masajes",
                "title": "Sala del Sol",
                "sub":
                    "Dos camillas paralelas para rituales a cuatro "
                    "manos. Luz rasante del sureste.",
            },
            {
                "span":  "c",
                "image": _ROOM_WATER,
                "tag":   "Sala III · Agua",
                "title": "Sala del Ritual del Agua",
                "sub":
                    "Bañera de hidroterapia en cobre martillado, "
                    "recorrido de tres temperaturas. Agua de "
                    "manantial del Resegone.",
            },
            {
                "span":  "d",
                "image": _ROOM_TISANERIA,
                "tag":   "Tisanería",
                "title": "Tisanería de Hierbas",
                "sub":
                    "Mezclas de temporada recogidas en nuestro propio "
                    "claustro. Servidas en porcelana blanca de Limoges.",
            },
            {
                "span":  "e",
                "image": _ROOM_GARDEN,
                "tag":   "Claustro",
                "title": "Jardín oficinal",
                "sub":
                    "Melisa, lavanda, salvia esclarea, hipérico, "
                    "ortiga. Accesible a todos los huéspedes.",
            },
            {
                "span":  "f",
                "image": _AMBIENT_YOGA,
                "tag":   "Estudio del Aliento",
                "title": "Estudio del Aliento",
                "sub":
                    "Parqué antiguo restaurado, alfombras de lana "
                    "cruda, máximo seis personas por sesión colectiva.",
            },
            {
                "span":  "g",
                "image": _ROOM_MEDITATION,
                "tag":   "Sala IV · Meditación",
                "title": "Cámara del Silencio",
                "sub":
                    "Seis tatamis de algodón orgánico, cuenco "
                    "tibetano de época, luz de velas de cera de abeja.",
            },
            {
                "span":  "h",
                "image": _ROOM_RECEPTION,
                "tag":   "Entrada",
                "title": "Umbral · Recepción",
                "sub":
                    "Suelo original del siglo XVII, libro de "
                    "huéspedes, primera infusión tibia tras cruzar "
                    "el umbral.",
            },
        ],

        "cta_label": "El siguiente paso",
        "cta_heading": 'Cruce <em>el umbral</em>',
        "cta_sub":
            "Los espacios se habitan, no se fotografían. La mejor "
            "manera de conocerlos es un ritual breve de sesenta minutos.",
        "cta_primary":   "Reservar un ritual",
        "cta_secondary": "Elegir un tratamiento",
    },

    # ──────────────────── PROFESSIONISTI (team) ────────────────────
    "professionisti": {
        "eyebrow":  "Los profesionales",
        "headline": 'Cinco <em>firmas</em>, un único libro de huéspedes',
        "intro":
            "Cada profesional tiene una formación específica, un "
            "calendario propio y una firma de tratamiento distinta. "
            "Quien le recibe en el umbral es también quien le acompaña "
            "al ritual.",

        "people": [
            {
                "name":     "Sara Conti",
                "role":     "Naturópata · Cofundadora",
                "portrait": _PORTRAIT_SARA,
                "tags":     ["Fitoterapia", "Hidroterapia", "Programa estacional"],
                "bio":
                    "Diplomada en Naturopatía en el Istituto Riza de "
                    "Milán en 2009 y acreditada por FIF (Federación "
                    "italiana de fitoterapia). Tras cinco años en Spa "
                    "du Château en Annecy, regresa a Bérgamo y cofunda "
                    "Studio Armonia con Chiara Bonomi. Dirige el "
                    "programa estacional de depuración y el jardín "
                    "oficinal del claustro.",
                "quote":
                    "«No existe una dieta depurativa. Existe una "
                    "atención repetida a cómo come, cuándo respira, "
                    "cuánto duerme.»",
            },
            {
                "name":     "Davide Lai",
                "role":     "Osteópata D.O.",
                "portrait": _PORTRAIT_DAVIDE,
                "tags":     ["Craneosacral", "Visceral", "Estructural"],
                "bio":
                    "Diplomado en la Scuola Superiore di Osteopatia "
                    "Italiana (S.S.O.I.) en 2014, se especializó en "
                    "técnicas craneosacrales y viscerales. Recibe los "
                    "martes y los jueves con cita previa, y es la "
                    "referencia del estudio para posparto y dolor "
                    "crónico.",
                "quote":
                    "«El cuerpo ya sabe cómo curarse — mi trabajo es "
                    "escuchar dónde ha dejado de hacerlo.»",
            },
            {
                "name":     "Yara Bonomi",
                "role":     "Profesional de ayurveda",
                "portrait": _PORTRAIT_YARA,
                "tags":     ["Abhyanga", "Lomi-Lomi", "Shirodhara"],
                "bio":
                    "Formada en Varkala (Kerala, India) en la Kerala "
                    "Ayurveda Academy en 2016, acreditada por la "
                    "Società Italiana di Ayurveda (S.I.A.). Conduce "
                    "los rituales Abhyanga y Shirodhara — siempre a "
                    "cuatro manos — así como el Lomi-Lomi hawaiano.",
                "quote":
                    "«El abhyanga no es un masaje: es una "
                    "conversación con la piel, hecha de aceite y de "
                    "tiempo.»",
            },
            {
                "name":     "Elena Rossi",
                "role":     "Maestra de yoga acreditada RYT-500",
                "portrait": _PORTRAIT_ELENA,
                "tags":     ["Hatha", "Yin", "Respiración somática"],
                "bio":
                    "Acreditada RYT-500 por la Yoga Alliance tras "
                    "cuatro años de práctica en Rishikesh y dos años "
                    "de estudio con Judith Hanson Lasater en San "
                    "Francisco. Conduce las sesiones colectivas en el "
                    "Estudio del Aliento los miércoles, viernes y "
                    "sábados por la mañana.",
                "quote":
                    "«El yoga que enseño aquí no es una gimnasia "
                    "exótica: es una manera de recordar dónde "
                    "descansan los hombros.»",
            },
            {
                "name":     "Miguel Ferrari",
                "role":     "Profesional de shiatsu · FISIEO",
                "portrait": _PORTRAIT_MIGUEL,
                "tags":     ["Shiatsu Namikoshi", "Do-in", "Medicina china"],
                "bio":
                    "Diplomado en la Scuola Europea di Shiatsu de "
                    "Milán en 2018 e inscrito en la FISIEO (Federación "
                    "italiana de profesionales de shiatsu). Recibe los "
                    "lunes, miércoles y viernes, y firma una columna "
                    "mensual sobre las estaciones del cuerpo según la "
                    "medicina tradicional china.",
                "quote":
                    "«La presión no es la técnica: la técnica es "
                    "dónde escucho antes de apretar.»",
            },
        ],

        "philo_label": "La filosofía de los profesionales",
        "philo_quote":
            "«Un ritual bien conducido no <em>añade</em> nada a quien "
            "lo recibe: solo le recuerda lo que ya sabía.»",
        "philo_attr": "— Manifiesto de los profesionales · 2015",

        "cta_label":   "El siguiente paso",
        "cta_heading": 'Reserve su <em>primer encuentro</em>',
        "cta_primary": "Abrir el formulario de reserva",
    },

    # ──────────────────── CONTATTI (contact) ────────────────────
    "contatti": {
        "eyebrow":  "Cómo encontrar el estudio",
        "headline": 'Via Arena 15, <em>Bergamo Alta</em>',
        "intro":
            "Estamos en el corazón de la ciudad alta medieval, a unos "
            "pasos de la Piazza Vecchia y de la Basílica de Santa "
            "Maria Maggiore. La entrada la señala una placa de latón "
            "satinado.",

        "map_image": _MAP_IMG,

        "blocks": [
            {"label": "Dirección",
             "value": "Via Arena 15",
             "sub":   "24129 Bergamo Alta · Palazzo Bonomi Suardi"},
            {"label": "Teléfono",
             "value": "+39 035 412 998",
             "sub":   "Línea directa 9:00 – 19:00"},
            {"label": "Correo electrónico",
             "value": "ritual@studioarmonia.it",
             "sub":   "Respuesta en el mismo día"},
            {"label": "Peticiones especiales",
             "value": "+39 346 772 4108",
             "sub":   "WhatsApp · activo 9:00 – 18:00"},
        ],

        "access_label": "Cómo llegar",
        "access": [
            {"mode": "En coche",
             "text": "Aparcamiento Monterosso (Via Fara) y cinco "
                     "minutos andando hasta la Via Arena."},
            {"mode": "Funicular",
             "text": "Funicular de Bergamo Alta desde el Viale "
                     "Vittorio Emanuele, descenso en Mercato delle "
                     "Scarpe, dos minutos a pie."},
            {"mode": "A pie",
             "text": "Desde la estación de tren de Bergamo Bassa, "
                     "autobús línea 1 (15 minutos), o bien 35 "
                     "minutos de paseo urbano."},
        ],

        "form_title": "Escríbanos",
        "form_intro":
            "Para consultas sobre rituales, regalos rituales o "
            "paquetes de estancia, utilice el formulario siguiente. "
            "Respondemos siempre antes del cierre del día laborable "
            "siguiente.",

        "form_placeholders": {
            "name":    "Chiara Ferrari",
            "email":   "chiara@email.es",
            "phone":   "+39 333 ...",
            "message":
                "Me gustaría reservar un ritual como regalo, "
                "preferiblemente un viernes por la tarde.",
        },
        "form_helpers": {
            "name":     "Cómo prefiere que le llamemos.",
            "email":    "Solo usamos el correo para responderle.",
            "phone":    "Si prefiere que le llamemos, indíquelo aquí.",
            "interest": "En caso de duda, elija Consulta inicial.",
            "message":  "Bastan unas líneas — sabemos responder a "
                        "preguntas concretas.",
        },
        "form_fields": {
            "interest_label": "Ritual de interés",
            "interest_options": [
                "Consulta inicial",
                "Masaje Mediterráneo",
                "Ritual Hammam",
                "Reequilibrio energético",
                "Ayurveda Abhyanga",
                "Paquete Aliento",
                "Paquete Detox tres días",
                "Regalo ritual",
                "Otro",
            ],
        },
        "form_consent":
            "Consiento el tratamiento de datos personales según el "
            "Regl. UE 679/2016. Los datos se conservan en Studio "
            "Armonia y no se ceden a terceros.",
        "form_submit_note":
            "Respuesta antes del cierre del día laborable siguiente.",

        "hours_label":   "Horario",
        "hours_heading": 'Abiertos <em>seis días</em> a la semana',
        "hours_note":
            "Los domingos Studio Armonia observa su jornada del "
            "silencio. Para urgencias, los huéspedes en curso pueden "
            "escribir a ritual@studioarmonia.it — respuesta "
            "garantizada en tres horas.",
        "hours": [
            {"day": "Lunes",     "value": "9:00 – 20:00"},
            {"day": "Martes",    "value": "9:00 – 20:00"},
            {"day": "Miércoles", "value": "9:00 – 20:00"},
            {"day": "Jueves",    "value": "9:00 – 20:00"},
            {"day": "Viernes",   "value": "9:00 – 20:00"},
            {"day": "Sábado",    "value": "9:00 – 18:00"},
            {"day": "Domingo",   "value": "Jornada del silencio"},
        ],
    },

    # ──────────────────── PRENOTA (appointment) ────────────────────
    "prenota": {
        "eyebrow":  "Reserva",
        "headline": 'El ritual comienza en cuanto usted <em>cruza el umbral</em>',
        "intro":
            "La reserva es el primer gesto del ritual. Elija la "
            "jornada que más le atraiga, complete el formulario "
            "siguiente: le contestamos en un plazo de dos horas "
            "laborables para confirmar.",

        "calendar_heading": 'Siete días de <em>próxima disponibilidad</em>',
        "calendar_hint":    "Indicativo · confirmación por correo",
        "calendar": [
            {"day": "Lun", "num": "14", "month": "Abr",
             "slots": ["10:00", "14:30", "17:00"], "has_slots": True, "soldout": False},
            {"day": "Mar", "num": "15", "month": "Abr",
             "slots": ["09:30", "13:00", "15:00"], "has_slots": True, "soldout": False},
            {"day": "Mié", "num": "16", "month": "Abr",
             "slots": ["11:00", "16:30"],          "has_slots": True, "soldout": False},
            {"day": "Jue", "num": "17", "month": "Abr",
             "slots": ["completo"],                "has_slots": False, "soldout": True},
            {"day": "Vie", "num": "18", "month": "Abr",
             "slots": ["10:30", "14:00", "18:00"], "has_slots": True, "soldout": False},
            {"day": "Sáb", "num": "19", "month": "Abr",
             "slots": ["completo"],                "has_slots": False, "soldout": True},
            {"day": "Dom", "num": "20", "month": "Abr",
             "slots": ["silencio"],                "has_slots": False, "soldout": True},
        ],

        "form_title":
            'Formulario de <em>reserva</em>',
        "form_side_note":
            "Reserve cinco minutos para completarlo con cuidado. "
            "Cuantos más detalles nos deje, más coherente con usted "
            "será el ritual que le propongamos.",
        "form_side_small": "↓ Formulario privado",

        "why_label": "Por qué reservar en línea",
        "why": [
            "Confirmación por correo en un plazo de dos horas laborables.",
            "Cancelación cortés hasta 24 horas antes, sin coste.",
            "Intolerancias y atenciones leídas con antelación por el profesional.",
            "Su franja queda bloqueada hasta que confirmemos.",
        ],

        "form_fields": [
            {"name": "name", "label": "Nombre y apellidos",
             "placeholder": "Chiara Ferrari",
             "type": "text", "required": True, "full_width": False,
             "helper": "Cómo prefiere que le llamemos."},
            {"name": "email", "label": "Correo electrónico",
             "placeholder": "chiara@email.es",
             "type": "email", "required": True, "full_width": False,
             "helper": "La confirmación llega aquí."},
            {"name": "phone", "label": "Teléfono",
             "placeholder": "+39 333 ...",
             "type": "tel", "required": True, "full_width": False,
             "helper": "Solo lo usamos en caso de necesidad."},
            {"name": "ritual", "label": "Ritual",
             "type": "select", "required": True, "full_width": False,
             "options": [
                 "Masaje Mediterráneo (55 min · 85 €)",
                 "Ritual Hammam (90 min · 120 €)",
                 "Reequilibrio energético (60 min · 95 €)",
                 "Hidroterapia alpina (75 min · 110 €)",
                 "Piedras Calientes (75 min · 105 €)",
                 "Ayurveda Abhyanga (90 min · 135 €)",
                 "Shiatsu (60 min · 90 €)",
                 "Lomi-Lomi (75 min · 115 €)",
                 "Craneosacral (55 min · 95 €)",
                 "Ritual Madre-Tierra (105 min · 150 €)",
                 "Paquete Aliento (1 día · 340 €)",
                 "Paquete Detox tres días (920 €)",
             ],
             "helper": "En caso de duda, elija el Masaje "
                       "Mediterráneo: es la introducción más suave "
                       "a nuestro trabajo."},
            {"name": "duration", "label": "Duración preferida",
             "type": "select", "required": False, "full_width": False,
             "options": [
                 "55 minutos",
                 "60 minutos",
                 "75 minutos",
                 "90 minutos",
                 "105 minutos",
             ],
             "helper": "Opcional · coherente con el ritual elegido."},
            {"name": "therapist", "label": "Profesional preferido",
             "type": "select", "required": False, "full_width": False,
             "options": [
                 "Indiferente",
                 "Sara Conti (naturópata)",
                 "Davide Lai (osteópata)",
                 "Yara Bonomi (ayurveda)",
                 "Elena Rossi (yoga)",
                 "Miguel Ferrari (shiatsu)",
             ],
             "helper": "Si prefiere un profesional concreto, indíquelo aquí."},
            {"name": "date", "label": "Fecha preferida",
             "placeholder": "14 de abril de 2026",
             "type": "date", "required": True, "full_width": False,
             "helper": "Indique su primera opción; propondremos "
                       "alternativas si no hay disponibilidad."},
            {"name": "slot", "label": "Franja horaria",
             "type": "select", "required": True, "full_width": False,
             "options": [
                 "Mañana (9:00 – 12:30)",
                 "Primera tarde (13:00 – 15:30)",
                 "Tarde (15:30 – 18:00)",
                 "Final de tarde (18:00 – 20:00)",
             ],
             "helper": "Las franjas son indicativas; confirmamos la "
                       "hora exacta."},
            {"name": "notes", "label": "Atenciones e intolerancias",
             "placeholder":
                 "¿Embarazo? ¿Intolerancias olfativas? ¿Lesiones "
                 "recientes? ¿Algo que su profesional deba saber? "
                 "Aquí lo leemos.",
             "type": "textarea", "required": False, "full_width": True,
             "helper": "Nada es demasiado pequeño. Embarazo, ciclo, "
                       "medicación, ansiedades: lo leemos todo con "
                       "antelación."},
        ],

        "form_sections": [
            {"num": "01", "title": "Quién es usted",
             "meta": "Sus coordenadas básicas.",
             "fields": ["name", "email", "phone"]},
            {"num": "02", "title": "El ritual que desea",
             "meta": "Si tiene dudas, elija «indiferente» — le orientamos nosotros.",
             "fields": ["ritual", "duration", "therapist"]},
            {"num": "03", "title": "Cuándo",
             "meta": "Indíquenos una primera opción · confirmamos por correo.",
             "fields": ["date", "slot"]},
            {"num": "04", "title": "Atenciones",
             "meta": "Todo lo que su profesional deba saber antes.",
             "fields": ["notes"]},
        ],

        "consent":
            "Consiento el tratamiento de datos personales según la "
            "política de privacidad (Regl. UE 679/2016). Los datos "
            "clínicos y las atenciones comunicadas permanecen en el "
            "archivo interno reservado.",

        "submit_label": "Reserve su momento",
        "form_submit_note":
            "Confirmamos la disponibilidad en un plazo de dos "
            "horas laborables.",

        "footnote":
            "La reserva solo queda confirmada tras nuestro correo "
            "de respuesta. La cancelación cortés es posible sin "
            "coste hasta veinticuatro horas antes del ritual — a "
            "partir de ese plazo, retenemos el 50 % del valor como "
            "salvaguarda del profesional.",
    },
}

__all__ = ["BENESSERE_CONTENT_ES"]
