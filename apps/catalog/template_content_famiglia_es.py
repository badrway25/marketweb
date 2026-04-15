"""FAMIGLIA_CONTENT_ES — native pediatric warm-family translation.

Voice: Guía Infantil / Mi Bebé y Yo / El País Mamás Papás register.
Español peninsular, usted cercano con los padres pero formal. "Su hijo o
hija", "seguimiento pediátrico", "los primeros años". Sin diminutivos
cursis, sin "tu pequeño/a".
"""
from __future__ import annotations

from typing import Any


FAMIGLIA_CONTENT_ES: dict[str, Any] = {
    "pages": [
        {"slug": "home",     "label": "Inicio",        "kind": "home"},
        {"slug": "studio",   "label": "La consulta",   "kind": "about"},
        {"slug": "visite",   "label": "Consultas",     "kind": "services"},
        {"slug": "crescita", "label": "Crecer",        "kind": "faq"},
        {"slug": "pediatre", "label": "Las pediatras", "kind": "team"},
        {"slug": "contatti", "label": "Contacto",      "kind": "contact"},
    ],

    # ─── SITE-WIDE CHROME ────────────────────────────────────────
    "site": {
        "logo_initial": "P",
        "logo_word":    "Pediatria Famiglia Plus",
        "tag":          "Consulta pediátrica · Turín, barrio Crocetta",
        "phone":        "011 549 21 88",
        "phone_tel":    "+390115492188",
        "whatsapp":     "+39 349 123 4567",
        "whatsapp_link": "https://wa.me/393491234567",
        "nav_cta_wa":   "WhatsApp",
        "email":        "studio@crocettapediatria.it",
        "address":      "Corso Galileo Ferraris 140 · 10129 Turín",
        "emergency_tel": "+393491234567",

        "hours_compact": "Lun – Vie · 8:30 – 12:30 · 15:00 – 19:00",
        "hours_footer_rows": [
            "Sábado · 9:00 – 12:00 · solo urgencias",
            "Domingo · guardia telefónica",
        ],
        "license":
            "CIF 11234120014 · Colegio de Médicos de Turín 08/5412",
        "footer_intro":
            "Consulta pediátrica privada en el barrio de Crocetta, en "
            "Turín. Cuatro pediatras, una neonatóloga y una enfermera "
            "dedicada. Consultas de treinta minutos, guardia "
            "telefónica los domingos y festivos, y una escucha real "
            "de los niños y sus familias.",
    },

    # ─── HOME ────────────────────────────────────────────────────
    "home": {
        "eyebrow":       "Consulta pediátrica · Turín, Crocetta",
        "headline":      "Crecemos <em>junto a</em> sus hijos.",
        "subhead":
            "Cuatro pediatras, una psicomotricista infantil y una "
            "enfermera dedicada. Consultas sin prisa, con tiempo "
            "para escuchar de verdad — porque cada familia merece "
            "un punto de referencia, no un número de ventanilla.",
        "primary_cta":   "Llamar a la consulta",
        "secondary_cta": "Escribirnos por WhatsApp",

        "hero_image":
            "https://images.pexels.com/photos/7447009/pexels-photo-7447009.jpeg"
            "?auto=compress&cs=tinysrgb&w=1000&h=1250&fit=crop",
        "hero_image_alt":
            "Pediatra durante una revisión pediátrica con una niña "
            "en la sala luminosa de la consulta del barrio Crocetta",
        "hero_ribbon":   "Concertada con el SSN (sanidad pública italiana)",
        "hero_stamp_initial": "E",
        "hero_stamp_name":    "Dra. Rambaldi",
        "hero_stamp_meta":    "hoy en consulta · 8:30 – 13:00",

        "trust_items": [
            {"icon": "clock",  "label": "Consultas de treinta minutos, nunca diez"},
            {"icon": "shield", "label": "Guardia 24 horas para pacientes en seguimiento"},
            {"icon": "people", "label": "Una consulta a medida de familia desde 1998"},
        ],

        # ── Intro trio · franjas de edad ──
        "age_groups": [
            {
                "icon":  "baby",
                "range": "0 – 2 años",
                "title": "Recién nacido y primer año",
                "blurb":
                    "El camino que empieza la primera semana de "
                    "vida: lactancia, sueño, revisiones "
                    "pediátricas, alta del Sant'Anna o del "
                    "Mauriziano. La Dra. Conti se ocupa "
                    "personalmente del seguimiento hasta los dos "
                    "años cumplidos.",
                "items": [
                    "Primera consulta dentro de los siete días",
                    "Revisiones al 1.º, 3.º, 6.º, 9.º y 12.º mes",
                    "Apoyo en lactancia y sueño",
                ],
            },
            {
                "icon":  "child",
                "range": "3 – 10 años",
                "title": "Infancia y edad escolar",
                "blurb":
                    "Los años de la guardería y la primaria: "
                    "vacunas, certificados deportivos, "
                    "seguimiento del crecimiento, pequeños "
                    "imprevistos y todas esas preguntas que un "
                    "padre o una madre suele guardar para sí.",
                "items": [
                    "Revisiones pediátricas anuales",
                    "Calendario vacunal completo",
                    "Certificados deportivos no federativos",
                ],
            },
            {
                "icon":  "teen",
                "range": "11 – 18 años",
                "title": "Adolescencia",
                "blurb":
                    "La etapa más delicada, cuando los "
                    "adolescentes prefieren hablar sin los "
                    "padres en la sala. Consultas dedicadas, "
                    "escucha confidencial y un canal de "
                    "WhatsApp para esas preguntas que no se "
                    "hacen en voz alta.",
                "items": [
                    "Revisión anual en solitario",
                    "Endocrinología, crecimiento, pubertad",
                    "Canal reservado para el adolescente",
                ],
            },
        ],

        # ── Le pediatre · portrait stack ──
        "team_label":   "Las pediatras de la consulta",
        "team_heading": "Cuatro firmas, <em>una sola historia clínica familiar.</em>",
        "team_intro":
            "La consulta reúne a cuatro pediatras que comparten "
            "historias clínicas, protocolos y estándar de "
            "revisión. Cada niño, sin embargo, tiene siempre una "
            "pediatra de referencia: la misma persona desde las "
            "primeras revisiones hasta la adolescencia.",

        "doctors": [
            {
                "name":  "Dr.ssa Elisa Rambaldi",
                "role":  "Pediatra de familia",
                "spec":  "Nutrición infantil",
                "wa_label": "Escribir por WhatsApp",
                "portrait":
                    "https://images.pexels.com/photos/7447002/pexels-photo-7447002.jpeg"
                    "?auto=compress&cs=tinysrgb&w=600&h=800&fit=crop",
            },
            {
                "name":  "Dr.ssa Marta Greco",
                "role":  "Pediatra alergóloga",
                "spec":  "Asma y dermatitis atópica",
                "wa_label": "Escribir por WhatsApp",
                "portrait":
                    "https://images.pexels.com/photos/3875229/pexels-photo-3875229.jpeg"
                    "?auto=compress&cs=tinysrgb&w=600&h=800&fit=crop",
            },
            {
                "name":  "Dr.ssa Lucia Sferra",
                "role":  "Pediatra endocrinóloga",
                "spec":  "Crecimiento y pubertad",
                "wa_label": "Escribir por WhatsApp",
                "portrait":
                    "https://images.pexels.com/photos/8460043/pexels-photo-8460043.jpeg"
                    "?auto=compress&cs=tinysrgb&w=600&h=800&fit=crop",
            },
            {
                "name":  "Dr.ssa Beatrice Conti",
                "role":  "Pediatra neonatóloga",
                "spec":  "Sueño y lactancia",
                "wa_label": "Escribir por WhatsApp",
                "portrait":
                    "https://images.pexels.com/photos/19357678/pexels-photo-19357678.jpeg"
                    "?auto=compress&cs=tinysrgb&w=600&h=800&fit=crop",
            },
        ],

        "team_note":
            "El equipo clínico se completa con Luisa Ferraro, "
            "enfermera pediátrica con quince años de experiencia "
            "en el hospital infantil Regina Margherita, y Giada "
            "Porro, psicomotricista especializada en trastornos "
            "del desarrollo de 0 a 6 años.",

        # ── Percorso della crescita · milestone timeline ──
        "journey_label":   "El camino del crecimiento",
        "journey_heading": "De las primeras semanas <em>hasta el bachillerato</em>.",
        "journey_intro":
            "Un niño ve a la misma pediatra al menos doce veces "
            "antes de cumplir los dieciocho. Cada encuentro es "
            "una revisión, no una urgencia. Estas son las cinco "
            "etapas que marcan más el camino.",

        "journey_steps": [
            {
                "age":   "1 mes",
                "title": "Primera revisión",
                "desc":  "La pediatra recibe al recién nacido en "
                         "la consulta dentro de los cuarenta "
                         "días: peso, reflejos, lactancia, sueño "
                         "y primeras tranquilizaciones para los "
                         "padres.",
            },
            {
                "age":   "6 meses",
                "title": "Alimentación complementaria",
                "desc":  "Consejos prácticos sobre la "
                         "introducción de los primeros alimentos "
                         "sólidos, seguimiento de la curva de "
                         "crecimiento y primera parte del "
                         "calendario vacunal.",
            },
            {
                "age":   "1 año",
                "title": "Primer cumpleaños",
                "desc":  "Revisión completa al final del primer "
                         "año: motricidad, lenguaje, primeras "
                         "interacciones sociales. Se asientan "
                         "los ritmos de la familia.",
            },
            {
                "age":   "3 años",
                "title": "Entrada en la guardería",
                "desc":  "El paso a la escuela infantil: "
                         "certificado médico, revisiones "
                         "visuales y auditivas, valoración de "
                         "autonomías y ritmos de sueño.",
            },
            {
                "age":   "6 años",
                "title": "Edad escolar",
                "desc":  "Revisión antes de primaria: postura, "
                         "alimentación, primeros controles de "
                         "la vista y recomendaciones sobre "
                         "actividad física.",
            },
        ],

        # ── FAQ accordion padres ──
        "faq_label":   "Preguntas de los padres",
        "faq_heading": "Las preguntas que <em>nos llegan</em> más a menudo.",
        "faq_intro":
            "Hemos reunido las ocho preguntas más frecuentes "
            "que los padres nos hacen por teléfono o en la sala "
            "de espera. Si la suya no está aquí, puede "
            "encontrarnos en el número de la consulta o en "
            "WhatsApp.",

        "faq": [
            (
                "¿Cuándo debo llamar a la pediatra?",
                "De inmediato en caso de fiebre superior a "
                "38,5 °C en los tres primeros meses de vida, "
                "llanto inconsolable, rechazo total del "
                "alimento o de la leche durante más de 12 "
                "horas, diarrea con sangre o lesiones "
                "cutáneas extensas. Para todo lo demás — una "
                "fiebre moderada, una tos nocturna, una "
                "quemadura solar — se puede esperar al "
                "horario de mañana y llamar con calma. En la "
                "consulta se contesta en persona.",
            ),
            (
                "¿Cómo reservo una primera consulta?",
                "Basta con llamar al 011 549 21 88 de lunes "
                "a viernes: la recepción, a cargo de Silvia "
                "Pairetto, toma el nombre del niño, la edad "
                "y el motivo de la visita. También se puede "
                "escribir al número de WhatsApp dedicado, "
                "incluso fuera de horario. No hay agenda "
                "online: preferimos hablar primero con "
                "ustedes.",
            ),
            (
                "¿Qué debo llevar a la primera consulta?",
                "La cartilla sanitaria del niño, el informe "
                "de alta del hospital si lo hay, el "
                "calendario de vacunas ya puestas y — si el "
                "niño tiene más de un año — el diario de la "
                "alimentación complementaria. No hace falta "
                "traer pruebas recientes: la pediatra pide "
                "solo lo que realmente necesita.",
            ),
            (
                "¿La consulta es accesible con carrito?",
                "Sí. La entrada está en la planta baja "
                "elevada del nº 140 del Corso Galileo "
                "Ferraris, con dos escalones y una rampa "
                "lateral. Dentro hay un rincón para carritos "
                "en la sala de espera y el baño está "
                "equipado con cambiador. Todas las salas de "
                "consulta están en la planta baja.",
            ),
            (
                "¿Qué ocurre por la tarde o el fin de semana?",
                "La Dra. Rambaldi y la Dra. Greco se turnan "
                "en la guardia telefónica para los pacientes "
                "en seguimiento: tardes entre semana, noche, "
                "sábado por la tarde y domingo. El número "
                "dedicado se facilita tras la primera "
                "consulta. Para urgencias reales sigue "
                "estando el 118 o el hospital infantil "
                "Regina Margherita.",
            ),
            (
                "¿Qué vacunas son obligatorias?",
                "El decreto Lorenzin de 2017 establece diez "
                "vacunas obligatorias para la matriculación "
                "en la enseñanza obligatoria en Italia. La "
                "consulta sigue el calendario nacional de la "
                "Región del Piamonte y ofrece un itinerario "
                "vacunal privado, sin colas del ASL, con la "
                "opción de espaciar las dosis si los padres "
                "lo piden.",
            ),
            (
                "¿Cuánto dura una revisión de seguimiento?",
                "Una revisión pediátrica en la consulta "
                "dura siempre treinta minutos, incluso "
                "cuando el niño está perfectamente. Es el "
                "tiempo mínimo para hacer la exploración "
                "clínica, pesar y medir sin prisa, "
                "actualizar la cartilla y contestar a las "
                "preguntas de los padres sin que nadie se "
                "sienta apurado.",
            ),
            (
                "¿Cuánto cuesta una consulta pediátrica privada?",
                "La primera consulta cuesta 90 euros, las "
                "revisiones siguientes 70 euros y las "
                "consultas de control 60 euros. Las "
                "familias con dos o más hijos en "
                "seguimiento tienen un 15 % de descuento. "
                "Todos los pagos son deducibles como "
                "gastos sanitarios en Italia, con recibo "
                "emitido el mismo día.",
            ),
        ],

        # ── Studio child-friendly gallery ──
        "gallery_label":   "La consulta",
        "gallery_heading": "Una casa, <em>no una planta hospitalaria.</em>",
        "gallery_intro":
            "Hemos pensado cada sala para que el niño no tenga "
            "miedo de entrar. Desde la sala de espera con "
            "libros hasta el cambiador climatizado, pasando por "
            "las mesitas bajas con juguetes y las salas de "
            "consulta de colores.",
        "gallery": [
            {
                "src": "https://images.pexels.com/photos/8460043/pexels-photo-8460043.jpeg"
                       "?auto=compress&cs=tinysrgb&w=1000&h=800&fit=crop",
                "cap": "Sala de consulta · planta baja",
            },
            {
                "src": "https://images.pexels.com/photos/7447002/pexels-photo-7447002.jpeg"
                       "?auto=compress&cs=tinysrgb&w=800&h=600&fit=crop",
                "cap": "Rincón del estetoscopio",
            },
            {
                "src": "https://images.pexels.com/photos/3875229/pexels-photo-3875229.jpeg"
                       "?auto=compress&cs=tinysrgb&w=800&h=600&fit=crop",
                "cap": "Sala de lactancia",
            },
            {
                "src": "https://images.pexels.com/photos/19357678/pexels-photo-19357678.jpeg"
                       "?auto=compress&cs=tinysrgb&w=800&h=600&fit=crop",
                "cap": "Sala de revisiones del recién nacido",
            },
            {
                "src": "https://images.pexels.com/photos/5867700/pexels-photo-5867700.jpeg"
                       "?auto=compress&cs=tinysrgb&w=800&h=600&fit=crop",
                "cap": "Entrada · Corso Galileo Ferraris",
            },
        ],

        # ── Orari band ──
        "hours_heading": "Horario de apertura",
        "hours": [
            ("Lun – Vie",  "8:30 – 12:30  ·  15:00 – 19:00"),
            ("Sábado",     "9:00 – 12:00  ·  solo urgencias"),
            ("Domingo",    "Guardia telefónica"),
            ("Festivos",   "Línea dedicada para pacientes en seguimiento"),
        ],
        "urgency_label": "Urgencias nocturnas",
        "urgency_title": "Estamos cerca también fuera de horario.",
        "urgency_text":
            "Los pacientes en seguimiento cuentan con un "
            "número dedicado de guardia nocturna y festiva, "
            "abierto todos los días de 19:30 a 8:00. Para "
            "urgencias reales, sigue estando el 118 o el "
            "hospital infantil Regina Margherita.",
        "urgency_phone": "+39 349 123 4567",

        # ── Bottom CTA band ──
        "cta_heading":     "¿Nos <em>necesita</em>?",
        "cta_lead":
            "Llamar a la consulta es la forma más sencilla y más "
            "humana de empezar. Contestamos en persona, sin "
            "menús telefónicos y sin tiempos de espera. Si lo "
            "prefiere, también estamos en WhatsApp.",
        "cta_phone_label": "Teléfono de la consulta",
        "cta_or":          "o bien",
        "cta_wa_label":    "Escríbanos por WhatsApp",
    },

    # ─── LO STUDIO (about) ───────────────────────────────────────
    "studio": {
        "eyebrow":  "La consulta",
        "headline": "Desde 1998, <em>una casa</em> para las familias de Crocetta.",
        "intro":
            "Nacimos como consulta pediátrica de barrio en 1998, "
            "por iniciativa de la Dra. Rambaldi. En veintisiete "
            "años hemos acompañado a más de tres mil niños, "
            "muchos de los cuales hoy son ya padres que nos "
            "traen a sus propios hijos. Es el mejor cumplido que "
            "podríamos recibir.",

        "values": [
            {
                "icon":  "clock",
                "title": "Tiempo sin prisa",
                "desc":  "Treinta minutos por consulta, nunca "
                         "menos. El tiempo es la única "
                         "herramienta que de verdad marca la "
                         "diferencia entre un diagnóstico "
                         "acertado y uno equivocado.",
            },
            {
                "icon":  "ear",
                "title": "Escucha real",
                "desc":  "Escuchamos primero a los padres, "
                         "después a los niños, después a los "
                         "adolescentes. Cada uno con su espacio "
                         "y su voz.",
            },
            {
                "icon":  "home",
                "title": "Ambiente de casa",
                "desc":  "Salas con color pero sin "
                         "infantilismos, luz natural, olores "
                         "acogedores. Una consulta debe parecer "
                         "una casa, no una planta de hospital.",
            },
            {
                "icon":  "people",
                "title": "Continuidad",
                "desc":  "Cada niño tiene su pediatra de "
                         "referencia, la misma desde las "
                         "primeras revisiones hasta los "
                         "dieciocho años. Compartimos las "
                         "historias, no las personas.",
            },
        ],

        "studio_image":
            "https://images.pexels.com/photos/5867700/pexels-photo-5867700.jpeg"
            "?auto=compress&cs=tinysrgb&w=1600&h=700&fit=crop",
        "studio_image_caption":
            "Consulta pediátrica · Corso Galileo Ferraris 140, Turín",

        "history_label":   "Veintisiete años de consulta",
        "history_heading": "Cuatro hitos, <em>tres generaciones</em> de niños.",
        "history_intro":
            "La consulta ha cambiado de dirección tres veces en "
            "la misma calle, ha ampliado el equipo de una a "
            "cinco profesionales y ha atravesado tres reformas "
            "del sistema sanitario italiano. Una cosa no ha "
            "cambiado nunca: la consulta dura treinta minutos.",

        "history": [
            (
                "1998",
                "La Dra. Elisa Rambaldi abre la primera "
                "consulta pediátrica en Via Morgari, con dos "
                "salas y una recepcionista. Las primeras "
                "quince familias siguen hoy en seguimiento.",
            ),
            (
                "2008",
                "Traslado al nº 140 del Corso Galileo "
                "Ferraris, planta baja accesible con "
                "carrito. Se incorpora la Dra. Marta Greco "
                "como pediatra alergóloga y Silvia Pairetto "
                "como recepcionista clínica.",
            ),
            (
                "2016",
                "Ampliación del equipo con la Dra. Lucia "
                "Sferra (endocrinología pediátrica) y puesta "
                "en marcha de la consulta de psicomotricidad "
                "para los trastornos del desarrollo, con "
                "Giada Porro.",
            ),
            (
                "2026",
                "La consulta alcanza cinco profesionales con "
                "la incorporación de la Dra. Beatrice Conti "
                "(neonatología) e inaugura el canal de "
                "WhatsApp reservado a la adolescencia.",
            ),
        ],

        "cta_heading":
            "¿Quiere conocer a las pediatras <em>antes</em> de reservar?",
        "cta_lead":
            "Puede leer sus trayectorias, ver sus rostros y "
            "elegir a quien prefiera para la primera consulta. "
            "Si duda, llámenos: le ayudamos a encontrar a la "
            "persona adecuada para su hijo o hija.",
        "cta_primary_label":   "Llamar a la consulta",
        "cta_secondary_label": "Las cuatro pediatras",
    },

    # ─── VISITE (services) ───────────────────────────────────────
    "visite": {
        "eyebrow":  "Las consultas",
        "headline": "Ocho tipos de consulta, <em>una sola manera</em> de hacer pediatría.",
        "intro":
            "Cada consulta tiene un tiempo, un motivo y un "
            "precio claros. Llámenos para reservar: elegimos "
            "juntos la consulta adecuada para la edad y el "
            "motivo del niño.",

        "visits": [
            {
                "icon":     "baby",
                "title":    "Revisión del recién nacido",
                "duration": "45 min · 0 – 12 meses",
                "desc":
                    "La primera evaluación completa tras el "
                    "nacimiento: peso, longitud, reflejos "
                    "arcaicos, exploración de caderas, apoyo "
                    "a la lactancia y al sueño. Se repite al "
                    "1.º, 3.º, 6.º, 9.º y 12.º mes.",
                "bring_label": "Qué traer",
                "bring":    "Cartilla sanitaria, informe de "
                            "alta del hospital y cualquier "
                            "prueba neonatal.",
                "cta_label": "Reservar por teléfono",
            },
            {
                "icon":     "child",
                "title":    "Revisión pediátrica",
                "duration": "30 min · 1 – 10 años",
                "desc":
                    "Control anual del crecimiento, valoración "
                    "de autonomías, postura, alimentación y "
                    "desarrollo psicomotor. Es la revisión más "
                    "solicitada en la consulta.",
                "bring_label": "Qué traer",
                "bring":    "Cartilla sanitaria actualizada y, "
                            "a ser posible, un diario "
                            "alimentario de una semana.",
                "cta_label": "Reservar por teléfono",
            },
            {
                "icon":     "vaccine",
                "title":    "Vacunaciones",
                "duration": "20 min · todas las edades",
                "desc":
                    "El calendario vacunal de la Región del "
                    "Piamonte se realiza en la consulta, sin "
                    "colas del ASL. Es posible espaciar las "
                    "dosis y acordar un itinerario "
                    "personalizado en caso de dudas "
                    "vacunales.",
                "bring_label": "Qué traer",
                "bring":    "Cartilla de vacunación y DNI del "
                            "progenitor acompañante.",
                "cta_label": "Reservar por teléfono",
            },
            {
                "icon":     "sport",
                "title":    "Revisión deportiva",
                "duration": "30 min · 6 – 18 años",
                "desc":
                    "Certificado médico no federativo para la "
                    "escuela y las actividades deportivas "
                    "amateurs. Incluye exploración clínica, "
                    "medición de tensión y ECG en reposo "
                    "cuando está indicado.",
                "bring_label": "Qué traer",
                "bring":    "Impreso del club deportivo y la "
                            "cartilla sanitaria.",
                "cta_label": "Reservar por teléfono",
            },
            {
                "icon":     "moon",
                "title":    "Consulta del sueño",
                "duration": "45 min · 0 – 4 años",
                "desc":
                    "Para padres agotados y niños que no "
                    "duermen. Análisis del contexto familiar, "
                    "plan de normalización del ritmo "
                    "sueño-vigilia y seguimiento telefónico "
                    "semanal durante un mes.",
                "bring_label": "Qué traer",
                "bring":    "Un diario del sueño del niño "
                            "rellenado durante siete días.",
                "cta_label": "Reservar por teléfono",
            },
            {
                "icon":     "leaf",
                "title":    "Consulta de alergología",
                "duration": "45 min · 2 – 18 años",
                "desc":
                    "Valoración alergológica pediátrica: "
                    "historia clínica detallada, prueba "
                    "cutánea prick, orientaciones sobre asma, "
                    "dermatitis atópica y alergias "
                    "alimentarias. A cargo de la Dra. Greco.",
                "bring_label": "Qué traer",
                "bring":    "Análisis de sangre recientes y "
                            "diario de síntomas.",
                "cta_label": "Reservar por teléfono",
            },
            {
                "icon":     "skin",
                "title":    "Dermatología pediátrica",
                "duration": "30 min · todas las edades",
                "desc":
                    "Para dermatitis, eritemas, pequeñas "
                    "lesiones cutáneas y nevos en cambio. A "
                    "cargo de la Dra. Greco, con seguimiento "
                    "fotográfico para comparar la evolución "
                    "en el tiempo.",
                "bring_label": "Qué traer",
                "bring":    "Fotografías fechadas de la lesión "
                            "si se dispone de ellas y lista de "
                            "los productos utilizados.",
                "cta_label": "Reservar por teléfono",
            },
            {
                "icon":     "apple",
                "title":    "Consulta de nutrición",
                "duration": "45 min · 6 meses – 18 años",
                "desc":
                    "Para una alimentación complementaria "
                    "difícil, selectividad alimentaria, "
                    "sobrepeso, bajo peso o simplemente "
                    "inseguridad de los padres. A cargo de la "
                    "Dra. Rambaldi, con un plan escrito "
                    "personalizado.",
                "bring_label": "Qué traer",
                "bring":    "Diario alimentario de siete días "
                            "y curvas de crecimiento de la "
                            "cartilla sanitaria.",
                "cta_label": "Reservar por teléfono",
            },
        ],

        "tips_label":   "Tres consejos para los padres",
        "tips_heading": "Cosas que nos gustaría que <em>supieran</em> antes de llamarnos.",
        "tips_intro":
            "Algunas recomendaciones valen más que una "
            "consulta. Las recogemos aquí porque creemos que un "
            "padre o una madre informados son más serenos — y "
            "un niño más sereno.",

        "tips": [
            {
                "title": "La fiebre no es el enemigo",
                "text":
                    "La fiebre es un mecanismo de defensa, no "
                    "un número que haya que bajar de "
                    "inmediato. Fíjese más en cómo se "
                    "comporta su hijo — si come, si bebe, si "
                    "juega — que en el dato del termómetro.",
            },
            {
                "title": "Cinco minutos bastan",
                "text":
                    "Cada noche, antes de dormir, pregúntele "
                    "a su hijo cómo le ha ido el día. No a "
                    "la hora de cenar, ni mientras cocina. "
                    "En su habitación, con él o ella. Cinco "
                    "minutos lo cambian todo.",
            },
            {
                "title": "Llámenos sin miedo",
                "text":
                    "Ninguna pregunta es tonta en pediatría. "
                    "La consulta contesta al teléfono de "
                    "lunes a viernes: llamar antes de "
                    "preocuparse es siempre la decisión "
                    "correcta.",
            },
        ],

        "cta_heading":
            "La forma más sencilla de reservar consulta sigue siendo <em>llamarnos</em>.",
        "cta_primary_label":   "Llamar a la consulta",
        "cta_secondary_label": "Escribir por WhatsApp",
    },

    # ─── CRESCITA (faq) ──────────────────────────────────────────
    "crescita": {
        "eyebrow":  "Crecer & tranquilizar",
        "headline": "Las preguntas que <em>acompañan</em> los primeros dieciocho años.",
        "intro":
            "Hemos reunido aquí las preguntas que más nos "
            "hacen los padres, agrupadas por temas. Es una "
            "primera lectura: para todo lo demás, háblelo con "
            "su pediatra de referencia.",

        "topics": [
            {
                "icon":  "apple",
                "meta":  "Tema 01",
                "title": "Nutrición y alimentación",
                "intro":
                    "De la subida de la leche a la "
                    "adolescencia, la alimentación es el "
                    "terreno donde padres y pediatras más "
                    "conversan. Cuatro preguntas que nos "
                    "llegan cada semana.",
                "items": [
                    (
                        "¿A qué edad empiezo la alimentación complementaria?",
                        "Las guías actuales señalan el sexto "
                        "mes cumplido como momento óptimo "
                        "para empezar, cuando el bebé se "
                        "mantiene sentado, ha perdido el "
                        "reflejo de extrusión y muestra "
                        "interés por la comida de los "
                        "adultos. No hay un día mágico: se "
                        "empieza cuando el niño está listo, "
                        "no cuando lo dice el calendario.",
                    ),
                    (
                        "¿Mi hijo está demasiado delgado?",
                        "El peso por sí solo no dice nada. "
                        "Siempre hay que leer juntos tres "
                        "valores: peso, talla e índice de "
                        "masa corporal en relación con la "
                        "curva de crecimiento personal del "
                        "niño. Un niño que crece con "
                        "regularidad por su percentil — "
                        "aunque sea el décimo — está "
                        "perfectamente.",
                    ),
                    (
                        "¿Cómo gestiono a un niño selectivo?",
                        "La selectividad alimentaria entre "
                        "los 2 y los 5 años es fisiológica. "
                        "Nada de batallas en la mesa, nada "
                        "de chantajes y nada de platos "
                        "especiales: se ofrece, se vuelve a "
                        "ofrecer, se espera. Si después de "
                        "los seis años la selectividad "
                        "persiste sobre grupos enteros de "
                        "alimentos, llame a la consulta.",
                    ),
                    (
                        "¿Sirven de verdad los suplementos?",
                        "En la inmensa mayoría de los "
                        "casos, no. Un niño que come "
                        "variado no necesita suplementos, "
                        "salvo la vitamina D en los primeros "
                        "años y la vitamina K en el recién "
                        "nacido. Todo lo demás es "
                        "marketing, no pediatría.",
                    ),
                ],
            },
            {
                "icon":  "moon",
                "meta":  "Tema 02",
                "title": "Sueño y descanso",
                "intro":
                    "El sueño es el tema que más agota a los "
                    "padres en los tres primeros años. Cuatro "
                    "tranquilizaciones basadas en la práctica "
                    "clínica, no en los libros.",
                "items": [
                    (
                        "¿Cuántas horas tiene que dormir un niño?",
                        "De 0 a 3 meses: 14–17 horas al "
                        "día, repartidas. De 4 a 11 meses: "
                        "12–15 horas. De 1 a 2 años: 11–14 "
                        "horas. De 3 a 5 años: 10–13 horas. "
                        "Cada niño tiene su propio ritmo: "
                        "variaciones de dos horas son "
                        "normales.",
                    ),
                    (
                        "¿Es normal que se despierte cada dos horas?",
                        "Durante los primeros seis meses, "
                        "sí, es fisiológico: el estómago "
                        "del lactante es pequeño y el "
                        "ritmo circadiano todavía no es "
                        "maduro. Después de los seis meses, "
                        "si los despertares frecuentes "
                        "continúan, podemos diseñar juntos "
                        "un plan de normalización.",
                    ),
                    (
                        "¿Puedo dormirlo a mi lado?",
                        "El colecho en la misma habitación "
                        "(pero no en la misma cama) se "
                        "recomienda hasta los 12 meses. "
                        "Después depende de los hábitos de "
                        "la familia: ningún enfoque es "
                        "erróneo si funciona para padres e "
                        "hijo.",
                    ),
                    (
                        "¿Cuándo le quito el pañal de noche?",
                        "El control nocturno del esfínter "
                        "llega de media entre los 3 y los 5 "
                        "años. No es una carrera: algunos "
                        "niños están listos a los dos años "
                        "y medio, otros a los seis. Si a "
                        "los 7 persisten las enuresis "
                        "frecuentes, hablemos.",
                    ),
                ],
            },
            {
                "icon":  "vaccine",
                "meta":  "Tema 03",
                "title": "Vacunaciones y enfermedades comunes",
                "intro":
                    "El escenario vacunal italiano cambió en "
                    "2017 con el decreto Lorenzin. Aquí "
                    "respondemos a las cuatro preguntas más "
                    "frecuentes — con paciencia y con los "
                    "datos.",
                "items": [
                    (
                        "¿Qué vacunas son obligatorias?",
                        "Son diez: difteria, tétanos, "
                        "tos ferina, hepatitis B, "
                        "poliomielitis, Hib, sarampión, "
                        "rubéola, parotiditis y varicela. "
                        "La obligación afecta a la "
                        "matriculación en la enseñanza "
                        "obligatoria (0-16 años) y está "
                        "regulada por el decreto Lorenzin "
                        "de 2017.",
                    ),
                    (
                        "¿Puedo espaciar las dosis?",
                        "Sí. La consulta ofrece itinerarios "
                        "personalizados para las familias "
                        "que prefieren repartir las "
                        "vacunas en varias citas en lugar "
                        "de administrar tres en una sola "
                        "sesión. Lo hablamos juntos en la "
                        "primera revisión.",
                    ),
                    (
                        "¿Cómo gestiono la sexta enfermedad?",
                        "La sexta enfermedad (roseola "
                        "infantum) afecta a los niños de "
                        "entre 6 meses y 2 años: tres "
                        "días de fiebre alta repentina "
                        "seguidos de una erupción cutánea "
                        "rosa. Se maneja con antipiréticos "
                        "y paciencia. Llámenos solo si la "
                        "fiebre supera los 40 °C o dura "
                        "más de cuatro días.",
                    ),
                    (
                        "¿Debo preocuparme por la tos?",
                        "Una tos de hasta tres semanas "
                        "tras un resfriado es normal: las "
                        "vías aéreas del niño son más "
                        "reactivas. Llámenos si la tos se "
                        "acompaña de una fiebre que no "
                        "baja en cinco días, de sibilancias "
                        "o de retracciones intercostales "
                        "visibles.",
                    ),
                ],
            },
            {
                "icon":  "comp",
                "meta":  "Tema 04",
                "title": "Comportamiento y desarrollo",
                "intro":
                    "Las preguntas menos médicas son a "
                    "menudo las más importantes. Aquí "
                    "respondemos sobre desarrollo "
                    "psicomotor, rabietas y adolescencia.",
                "items": [
                    (
                        "¿A qué edad habla un niño?",
                        "Las primeras palabras llegan entre "
                        "los 10 y los 18 meses, las "
                        "primeras frases entre los 18 y "
                        "los 24 meses. Si a los 24 meses "
                        "el niño no combina dos palabras, "
                        "es razonable pedir una valoración "
                        "psicomotora — que realizamos en "
                        "la consulta con Giada Porro.",
                    ),
                    (
                        "¿Las rabietas son normales?",
                        "Sí, son fisiológicas y decisivas: "
                        "es la forma en que el niño "
                        "experimenta con la autonomía y "
                        "los límites. No se castigan, se "
                        "contienen. Se convierten en un "
                        "problema cuando implican "
                        "agresividad física habitual o "
                        "autolesiones.",
                    ),
                    (
                        "¿Cuánto tiempo delante de una pantalla?",
                        "Las recomendaciones de la OMS "
                        "indican: nada de pantalla antes "
                        "de los 2 años, máximo 1 hora al "
                        "día entre los 2 y los 5, máximo "
                        "2 horas a partir de los 5. "
                        "Televisión, tableta y móvil son "
                        "todos pantallas: cuente también "
                        "los dibujos de la mañana.",
                    ),
                    (
                        "¿Cómo hablo con mi hijo adolescente?",
                        "Menos de lo que querría y con "
                        "más escucha de lo que cree. Las "
                        "preguntas abiertas funcionan "
                        "siempre mejor que las cerradas: "
                        "«¿Qué tal el día?» le gana a "
                        "«¿Has estudiado?» diez a cero. Y "
                        "recuerde: el silencio no es "
                        "rechazo, es pensamiento.",
                    ),
                ],
            },
        ],

        "materials_label":   "Materiales útiles",
        "materials_heading": "Tres guías <em>descargables</em>.",
        "materials_intro":
            "Hemos preparado tres vademécum en PDF para que "
            "los padres puedan descargarlos y consultarlos en "
            "casa. Están escritos por las pediatras de la "
            "consulta y actualizados a 2026.",

        "materials": [
            {
                "title":    "Vademécum del recién nacido",
                "desc":
                    "Veintiocho páginas sobre los tres "
                    "primeros meses de vida: lactancia, "
                    "sueño, baño, primeras vacunas y "
                    "cuándo llamar a la consulta.",
                "size":     "PDF · 2,4 MB",
                "dl_label": "Descargar",
            },
            {
                "title":    "Calendario vacunal 2026",
                "desc":
                    "El calendario vacunal actualizado de "
                    "la Región del Piamonte en versión "
                    "resumida, con fechas recomendadas y "
                    "opcionales.",
                "size":     "PDF · 1,1 MB",
                "dl_label": "Descargar",
            },
            {
                "title":    "Guía de la alimentación complementaria",
                "desc":
                    "Del sexto mes al primer cumpleaños: "
                    "qué alimentos introducir, en qué "
                    "orden y con qué precauciones. Con "
                    "recetas de la Dra. Rambaldi.",
                "size":     "PDF · 3,1 MB",
                "dl_label": "Descargar",
            },
        ],

        "cta_heading":
            "¿No ha encontrado <em>su</em> pregunta?",
        "cta_lead":
            "Llámenos o escríbanos por WhatsApp: contestamos "
            "en persona durante la jornada. Ninguna pregunta "
            "es tonta en pediatría.",
        "cta_primary_label":   "Llamar a la consulta",
        "cta_secondary_label": "Escribir por WhatsApp",
    },

    # ─── PEDIATRE (team) ─────────────────────────────────────────
    "pediatre": {
        "eyebrow":  "Las pediatras",
        "headline": "Cuatro firmas, <em>una sola historia clínica</em> familiar.",
        "intro":
            "Somos cuatro pediatras con formaciones distintas "
            "y una sola manera de trabajar: treinta minutos "
            "por consulta, historias clínicas compartidas "
            "entre colegas, continuidad de la relación con "
            "cada niño desde el nacimiento hasta los "
            "dieciocho años.",

        "doctors": [
            {
                "name":  "Dr.ssa Elisa Rambaldi",
                "role":  "Fundadora · Pediatra de familia",
                "tag":   "Fundadora",
                "specs": ["Nutrición infantil", "Alimentación complementaria", "Edad escolar"],
                "bio":
                    "Licenciatura en Medicina por la "
                    "Universidad de Turín y especialidad en "
                    "Pediatría en el hospital infantil Regina "
                    "Margherita. Abre la consulta en 1998 con "
                    "el objetivo de devolver a la pediatría de "
                    "cabecera su dimensión de tiempo largo. "
                    "Autora del libro «Crescere insieme» "
                    "(Crecer juntos), Einaudi Ragazzi, 2019.",
                "exp_label": "Experiencia",
                "exp_value": "28 años · más de 3.000 historias activas",
                "wa_label":  "Escribir por WhatsApp",
                "portrait":
                    "https://images.pexels.com/photos/7447002/pexels-photo-7447002.jpeg"
                    "?auto=compress&cs=tinysrgb&w=800&h=1050&fit=crop",
            },
            {
                "name":  "Dr.ssa Marta Greco",
                "role":  "Pediatra · Alergología y dermatología",
                "tag":   "Alergología",
                "specs": ["Asma pediátrica", "Dermatitis atópica", "Alergias alimentarias"],
                "bio":
                    "Licenciatura y especialidad en Pediatría "
                    "por la Universidad de Pavía, máster en "
                    "Alergología Pediátrica en el San "
                    "Raffaele de Milán. En la consulta de "
                    "Crocetta desde 2008, donde dirige el "
                    "itinerario alergológico y dermatológico "
                    "pediátrico. Referente para el hospital "
                    "infantil Gaslini de Génova en "
                    "consultas territoriales.",
                "exp_label": "Experiencia",
                "exp_value": "22 años · alergología pediátrica desde 2006",
                "wa_label":  "Escribir por WhatsApp",
                "portrait":
                    "https://images.pexels.com/photos/3875229/pexels-photo-3875229.jpeg"
                    "?auto=compress&cs=tinysrgb&w=800&h=1050&fit=crop",
            },
            {
                "name":  "Dr.ssa Lucia Sferra",
                "role":  "Pediatra · Endocrinología",
                "tag":   "Endocrinología",
                "specs": ["Crecimiento", "Pubertad precoz", "Tiroides pediátrica"],
                "bio":
                    "Licenciatura por la Universidad "
                    "Federico II de Nápoles, especialidad "
                    "en Pediatría por la Universidad de "
                    "Bolonia y fellowship en Endocrinología "
                    "Pediátrica en el Boston Children's "
                    "Hospital. En la consulta desde 2016, "
                    "se ocupa del crecimiento, la pubertad "
                    "y los trastornos endocrinos entre los "
                    "8 y los 18 años.",
                "exp_label": "Experiencia",
                "exp_value": "18 años · endocrinología pediátrica",
                "wa_label":  "Escribir por WhatsApp",
                "portrait":
                    "https://images.pexels.com/photos/8460043/pexels-photo-8460043.jpeg"
                    "?auto=compress&cs=tinysrgb&w=800&h=1050&fit=crop",
            },
            {
                "name":  "Dr.ssa Beatrice Conti",
                "role":  "Pediatra · Neonatología",
                "tag":   "Neonatología",
                "specs": ["Lactancia", "Sueño 0-3 años", "Prematuridad"],
                "bio":
                    "Licenciatura y especialidad en la "
                    "Universidad de Turín. Quince años en "
                    "la unidad de neonatología del Sant'Anna, "
                    "donde atendió a más de dos mil recién "
                    "nacidos prematuros y a término. "
                    "Consultora IBCLC en lactancia. Se "
                    "incorpora a la consulta en 2026 para "
                    "ocuparse del primer año de vida y del "
                    "apoyo a las madres recientes.",
                "exp_label": "Experiencia",
                "exp_value": "15 años · Sant'Anna · IBCLC desde 2014",
                "wa_label":  "Escribir por WhatsApp",
                "portrait":
                    "https://images.pexels.com/photos/19357678/pexels-photo-19357678.jpeg"
                    "?auto=compress&cs=tinysrgb&w=800&h=1050&fit=crop",
            },
        ],

        "extra_title": "El equipo clínico se completa con dos profesionales más.",
        "extra_text":
            "Luisa Ferraro, enfermera pediátrica con quince "
            "años en la planta del hospital infantil Regina "
            "Margherita, se ocupa de las vacunaciones y las "
            "extracciones en la consulta. Giada Porro, "
            "psicomotricista especializada en trastornos del "
            "desarrollo de 0 a 6 años, atiende los martes y "
            "jueves con cita previa.",
    },

    # ─── CONTATTI (contact) ──────────────────────────────────────
    "contatti": {
        "eyebrow":  "Contacto & acceso",
        "headline": "Un <em>número</em>, una persona, una respuesta.",
        "intro":
            "Silvia Pairetto contesta personalmente el "
            "teléfono de lunes a viernes. Conoce cada "
            "historia clínica, cada nombre y cada madre de "
            "esta consulta. Para las peticiones no urgentes, "
            "también puede escribirnos por WhatsApp o a "
            "través del formulario que encontrará a "
            "continuación.",

        "address_label": "Dónde estamos",
        "address_line":  "Corso Galileo Ferraris 140",
        "address_sub":   "10129 Turín · Barrio Crocetta · planta baja elevada",
        "phone_label":   "Teléfono",
        "email_label":   "Correo electrónico",

        "map_image":
            "https://images.pexels.com/photos/5867700/pexels-photo-5867700.jpeg"
            "?auto=compress&cs=tinysrgb&w=1000&h=750&fit=crop",

        "travel_heading": "Cómo llegar",
        "travel": [
            {
                "icon":  "metro",
                "title": "Metro",
                "text":  "Línea 1 · estación Re Umberto, 4 minutos a pie hasta Corso Galileo Ferraris.",
            },
            {
                "icon":  "car",
                "title": "Coche y aparcamiento",
                "text":  "Aparcamiento concertado Q-Park Crocetta en Via Governolo 22, a 80 metros de la consulta.",
            },
            {
                "icon":  "walk",
                "title": "A pie",
                "text":  "A cinco minutos del Parco del Valentino y a 15 de la estación de Porta Nuova.",
            },
        ],

        "hours_heading": "Horario de apertura",
        "hours": [
            ("Lun – Vie",  "8:30 – 12:30 · 15:00 – 19:00"),
            ("Sábado",     "9:00 – 12:00 · solo urgencias"),
            ("Domingo",    "Guardia telefónica"),
            ("Festivos",   "Línea dedicada"),
        ],

        "form_title": "Escribir a la consulta",
        "form_intro":
            "Para peticiones no urgentes — tarifas, "
            "horarios, documentos, primera consulta — "
            "escríbanos aquí. Contestamos durante la jornada "
            "laborable. Para urgencias, llame.",

        "label_parent_name": "Nombre del progenitor",
        "label_child_age":   "Edad del niño",
        "label_reason":      "Motivo del contacto",

        "reason_options": [
            "Primera consulta",
            "Revisión de rutina",
            "Vacunaciones",
            "Consulta sobre un problema concreto",
            "Información administrativa",
            "Otro",
        ],

        "form_placeholders": {
            "parent_name": "Giulia Bianchi",
            "email":       "giulia.bianchi@email.it",
            "phone":       "+39 333 …",
            "child_age":   "4 años y medio",
            "message":
                "Escriba aquí su petición. "
                "Contestamos durante la jornada laborable.",
        },
        "form_helpers": {
            "parent_name": "Indique el nombre del progenitor que escribe.",
            "email":       "Le contestaremos aquí durante la jornada.",
            "phone":       "Opcional — útil si prefiere que le llamemos.",
            "child_age":   "Edad y, si lo desea, nombre del niño.",
            "reason":      "Si tiene dudas, elija «Otro».",
            "message":
                "Unas pocas líneas bastan — para lo demás "
                "se habla mejor por teléfono.",
        },
        "form_consent":
            "Acepto el tratamiento de mis datos personales "
            "según la política de privacidad de la consulta "
            "y el Reglamento UE 679/2016 (RGPD). Los datos "
            "de los niños los custodia la consulta y no se "
            "comunican a terceros.",
        "form_submit_note":
            "Respuesta durante la jornada laborable · para "
            "urgencias, llame directamente a la consulta.",
    },
}
__all__ = ["FAMIGLIA_CONTENT_ES"]
