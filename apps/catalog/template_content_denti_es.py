"""Denti+Co — Estudio Dental · Spanish (ES) content tree.

Wave 1 Pass-2 (T46 · 2026-05-11) · workflow C multilingual rollout.
Mirrors `template_content_denti.py` (DENTI_CONTENT_IT) shape one-for-one:
identical top-level keys, nested keys, tuple arities, and list lengths.

Authoring workflow C: four sub-agent parallel translators (home / studio +
visite / medici + posts / contatti + richiedi-visita) merged into this
single locale file. Peninsular Spanish, `usted` formal register, El País
Sociedad editorial sobriety with warmth — no Latin American forms, no
bureaucratic stiffness.

Voice anchor: the IT noun-em italic on `<em>igiene</em>` translates to
`<em>higiene</em>` in the SAME surface locations. Verb-em on the side
quote follows the noun anchor. The anchor must appear verbatim-in-
translation (not stylistically rewritten) wherever IT had it.

Non-localizable data preserved verbatim from the IT tree: phone, email,
prices, doctor surnames (with ES "Dra." / "Dr." courtesy titles),
press-outlet titles in their original script, and all imagery URLs
(_CHIEF_PORTRAIT, _LEAD_IMAGE, the three inline doctor portraits, the
studio_image, service_image, map_fallback_image). Address localized only
on the city token: "Milano" → "Milán". Slugs stay Italian — URLs do
not change between locales, only labels do.

Tier stays `draft` until the EN/FR/AR siblings complete and the user
runs the public-flip handshake.
"""
from __future__ import annotations

from typing import Any


# Imagery URLs — verbatim from the IT tree (T46 Wave 1 Pass-2). Locale
# trees share the same dental imagery pack; do not divergerthe Pexels
# URLs across languages.
_CHIEF_PORTRAIT = (
    "https://images.pexels.com/photos/4269363/pexels-photo-4269363.jpeg"
    "?auto=compress&cs=tinysrgb&w=900&h=1200&fit=crop"
)
_LEAD_IMAGE = (
    "https://images.pexels.com/photos/9062525/pexels-photo-9062525.jpeg"
    "?auto=compress&cs=tinysrgb&w=1200&h=800&fit=crop"
)


DENTI_CONTENT_ES: dict[str, Any] = {
    "pages": [
        {"slug": "home",            "label": "Estudio",             "kind": "home"},
        {"slug": "studio",          "label": "El estudio",          "kind": "about"},
        {"slug": "visite",          "label": "Tratamientos",        "kind": "services"},
        {"slug": "medici",          "label": "Dentistas",           "kind": "team"},
        {"slug": "pubblicazioni",   "label": "Publicaciones",       "kind": "blog_list"},
        {"slug": "contatti",        "label": "Contacto",            "kind": "contact"},
        {"slug": "richiedi-visita", "label": "Reservar higiene",    "kind": "appointment"},
    ],

    "site": {
        "logo_initial": "D",
        "logo_word":    "Denti+Co",
        "tag":          "Estudio dental asociado · Milán Brera",
        "phone":        "+39 02 7770 4488",
        "email":        "studio@denticostudio.it",
        "address":      "Via Manzoni 18 · 20121 Milán",
        "hours_compact": "Lun – Vie · 8:30 – 19:30",
        "hours_footer_rows": [
            "Sábado · 9:00 – 13:00",
            "Domingo · cerrado",
        ],
        "license":      "Colegiación OMCeO Milán 03 / 18742 · Directora sanitaria Dra. C. Vespa",
        "footer_intro":
            "Estudio dental asociado de odontología conservadora, higiene "
            "profesional e implantología. Cuatro profesionales, una sola "
            "historia clínica para cada paciente.",
    },

    "home": {
        # Hero — editorial-magazine variant: portrait-driven, different
        # silhouette from Cardio's default split-consultive.
        "hero_variant": "editorial-magazine",
        "eyebrow":  "Odontología · Milán Brera",
        "headline": "La <em>higiene</em> no es un detalle. Es el primer capítulo.",
        "intro":
            "Higiene profesional, odontología conservadora, implantología y "
            "ortodoncia transparente. Cuatro dentistas asociados, una sola "
            "historia clínica, revisiones semestrales incluidas en el plan "
            "anual.",
        "primary_cta":   "Reservar higiene",
        "primary_href":  "richiedi-visita",
        "secondary_cta": "El estudio",
        "secondary_href":"studio",

        # Three-fact band — same arity as IT (3 tuples of 2).
        "facts": [
            ("12", "años de estudio asociado"),
            ("3.400", "higienes y revisiones / año"),
            ("4", "dentistas especialistas en la clínica"),
        ],

        # Manifesto with drop-cap.
        "manifesto_drop_cap": "L",
        "manifesto":
            "a salud bucal no se cuida dos veces al año: se sostiene cada "
            "día. Por eso Denti+Co trabaja a partir de la higiene "
            "—profesional, repetible, medible— y construye alrededor de "
            "ella la odontología conservadora, la implantología y la "
            "ortodoncia. Cuatro dentistas especialistas, una sola "
            "historia clínica compartida, una sola firma en el plan de "
            "tratamiento. Sin venta cruzada, sin tratamientos "
            "fragmentados: la higiene es el primer capítulo y la única "
            "verdadera puerta de entrada.",

        # Hero right sidebar.
        "hero_sidebar_top_label": "Dirección clínica",
        "hero_sidebar_quote":
            "«Una higiene profesional bien hecha <em>evita</em> el 70 % de "
            "los tratamientos invasivos. Para nosotros es clínica seria, "
            "no un servicio cosmético.»",
        "hero_sidebar_author": "— Dra. Chiara Vespa · Directora sanitaria",
        "hero_sidebar_pulse": [
            ("Estudio",     "Milán · Brera"),
            ("Desde",       "2013"),
            ("Referencia",  "Odontología asociada"),
        ],

        # Anchor subnav.
        "anchor_nav": [
            ("metodo",      "Método"),
            ("trattamenti", "Tratamientos"),
            ("percorso",    "Recorrido del paciente"),
            ("medico",      "Dirección clínica"),
            ("studio",      "Sede y contacto"),
        ],

        # Signature treatments — 4 entries of 3-tuple (num, title, desc).
        "signature_visits_label":   "Tratamientos y recorridos",
        "signature_visits_heading": "Cuatro recorridos clínicos, <em>una sola historia.</em>",
        "signature_visits_intro":
            "Las cuatro familias de tratamiento más solicitadas. "
            "El listado completo está en la página Tratamientos.",
        "signature_visits": [
            ("01", "Higiene profesional semestral",
             "Tartrectomía supra y subgingival, pulido por aire con "
             "bicarbonato sódico, índice de sangrado y registro PSR. "
             "Incluida en los planes anuales de mantenimiento."),
            ("02", "Odontología conservadora",
             "Obturaciones de composite estratificado, reconstrucciones "
             "estéticas y endodoncias con localizador apical. Dique de "
             "goma obligatorio en cada intervención conservadora."),
            ("03", "Implantología y regenerativa",
             "Implantes unitarios y rehabilitaciones completas con carga "
             "inmediata. Planificación asistida por ordenador y férula "
             "quirúrgica impresa en 3D en el laboratorio interno."),
            ("04", "Ortodoncia transparente",
             "Alineadores invisibles Invisalign y SmileLab para adultos, "
             "ortodoncia interceptiva en niños de 8 a 12 años con "
             "aparatos removibles. Revisión mensual incluida."),
        ],

        # Trattamenti tabs section — 4 tabs, each with items 4-tuple-ish.
        "trattamenti_tabs": {
            "label":   "Tarifa de tratamientos",
            "heading": "Lo que hacemos, con <em>qué criterio.</em>",
            "intro":
                "Cuatro categorías clínicas, cada una con un protocolo "
                "escrito y un precio declarado. No emitimos presupuesto "
                "personalizado para las prestaciones de rutina —solo "
                "para planes de tratamiento estructurados.",
            "tabs": [
                {
                    "id":      "igiene",
                    "label":   "Higiene",
                    "eyebrow": "Higiene profesional",
                    "heading": "Cuarenta y cinco minutos, no veinte.",
                    "body":
                        "La higiene no es una cita de rutina: es una visita "
                        "clínica de cuarenta y cinco minutos con registro "
                        "periodontal, índice de sangrado, pulido por aire "
                        "con bicarbonato y fotografías de control.",
                    "items": [
                        ("Higiene profesional individual", "45 min · € 95"),
                        ("Plan anual (2 higienes + 1 revisión)", "anual · € 220"),
                        ("Pulido por aire con bicarbonato", "incluido · gratuito"),
                        ("Sellado de fisuras (por diente)", "10 min · € 30"),
                    ],
                    "cta_label": "Todos los planes de higiene →",
                    "cta_href":  "visite",
                },
                {
                    "id":      "conservativa",
                    "label":   "Conservadora",
                    "eyebrow": "Odontología conservadora",
                    "heading": "Composite estratificado, siempre bajo dique.",
                    "body":
                        "Obturaciones de composite fotopolimerizado, "
                        "reconstrucciones estéticas y endodoncias con "
                        "localizador apical. Dique de goma obligatorio "
                        "en cada intervención conservadora. Ninguna "
                        "obturación de amalgama desde 2013.",
                    "items": [
                        ("Obturación simple (1 superficie)", "45 min · € 140"),
                        ("Obturación compuesta (2-3 superficies)", "60 min · € 220"),
                        ("Endodoncia unirradicular", "75 min · € 280"),
                        ("Endodoncia multirradicular", "120 min · € 420"),
                    ],
                    "cta_label": "Tarifa completa de conservadora →",
                    "cta_href":  "visite",
                },
                {
                    "id":      "implantologia",
                    "label":   "Implantología",
                    "eyebrow": "Implantología y regenerativa",
                    "heading": "Implantes italianos, garantía vitalicia sobre el fixture.",
                    "body":
                        "Implantes Sweden+Martina de procedencia italiana, "
                        "planificación asistida por ordenador con TAC de "
                        "haz cónico, férula quirúrgica impresa en 3D en "
                        "nuestro laboratorio interno. Carga inmediata "
                        "solo en casos seleccionados tras evaluación "
                        "clínica.",
                    "items": [
                        ("Implante unitario (fixture + corona de circonio)", "intervención · € 1.850"),
                        ("Mini elevación de seno maxilar", "intervención · € 950"),
                        ("Regenerativa ósea (zona única)", "intervención · € 480"),
                        ("Rehabilitación fija sobre 4 implantes", "plan · según presupuesto"),
                    ],
                    "cta_label": "Recorridos implantológicos →",
                    "cta_href":  "visite",
                },
                {
                    "id":      "ortodonzia",
                    "label":   "Ortodoncia",
                    "eyebrow": "Ortodoncia transparente e interceptiva",
                    "heading": "Alineadores para adultos, interceptiva para los niños.",
                    "body":
                        "Alineadores invisibles Invisalign y SmileLab con "
                        "escaneado intraoral iTero y plan simulado en 3D "
                        "antes de comenzar. Ortodoncia interceptiva de 8 "
                        "a 12 años con aparatos removibles. Revisión "
                        "mensual incluida en el plan.",
                    "items": [
                        ("Alineadores Invisalign – plan completo", "12-18 meses · € 3.200"),
                        ("Alineadores SmileLab – plan completo", "10-14 meses · € 2.400"),
                        ("Ortodoncia interceptiva infantil", "12-24 meses · € 1.600"),
                        ("Retenedor nocturno postratamiento", "permanente · € 220"),
                    ],
                    "cta_label": "Protocolos ortodóncicos →",
                    "cta_href":  "visite",
                },
            ],
        },

        "chief_label":   "Dirección clínica",
        "chief_heading": "Una sola firma <em>para cada historia clínica.</em>",
        "chief": {
            "name":  "Dra. Chiara Vespa",
            "role":  "Directora sanitaria · Odontología conservadora y endodoncia",
            "bio":
                "Especialista en odontología conservadora formada en la "
                "Università degli Studi di Milano y perfeccionada en la "
                "Loma Linda University, California. Miembro de la SIE "
                "(Sociedad Italiana de Endodoncia) y ponente en los "
                "cursos anuales de la Scuola Lombarda di Odontoiatria. "
                "Directora sanitaria del estudio desde 2013.",
            "portrait": _CHIEF_PORTRAIT,
        },

        # Patient journey — 5 steps.
        "percorso": {
            "label":   "Recorrido del paciente",
            "heading": "Qué esperar de la <em>primera visita.</em>",
            "intro":
                "La primera visita al estudio se dedica a construir la "
                "historia clínica: fotografías, índices, escaneado y "
                "plan de tratamiento por escrito. Nunca tratamiento en "
                "la primera sesión, salvo urgencias documentadas.",
            "steps": [
                {
                    "num": "01",
                    "icon": "clipboard",
                    "title": "Recepción y anamnesis",
                    "desc": "Secretaría, ficha de anamnesis con historial "
                            "médico y dental, radiografías previas o "
                            "panorámica reciente si las hubiera.",
                    "duration": "10 min",
                },
                {
                    "num": "02",
                    "icon": "book",
                    "title": "Exploración clínica completa",
                    "desc": "Registro periodontal, índice de placa, "
                            "índice de sangrado, exploración de los "
                            "tejidos blandos y de la mucosa oral.",
                    "duration": "20 min",
                },
                {
                    "num": "03",
                    "icon": "heart",
                    "title": "Fotografía y escaneado",
                    "desc": "Serie fotográfica estandarizada (8 tomas "
                            "intraorales + 4 extraorales) y escaneado "
                            "intraoral iTero para el archivo digital.",
                    "duration": "15 min",
                },
                {
                    "num": "04",
                    "icon": "chart",
                    "title": "Plan de tratamiento por escrito",
                    "desc": "Discusión en el sillón del plan clínico "
                            "con presupuesto detallado partida por "
                            "partida, entregado también en PDF.",
                    "duration": "15 min",
                },
                {
                    "num": "05",
                    "icon": "document",
                    "title": "Programación y seguimiento",
                    "desc": "Calendario de citas, recordatorio de la "
                            "higiene de mantenimiento y canal directo "
                            "por WhatsApp para urgencias.",
                    "duration": "5 min",
                },
            ],
        },

        # Press strip — outlets verbatim from IT (preserve titles).
        "press": ["Il Dentista Moderno", "Dental Tribune", "Bocca & Salute",
                  "Corriere Salute", "Vanity Fair Italia"],
        "press_label": "Publicado en",

        # FAQ — 5 items.
        "faq": {
            "label": "Preguntas frecuentes",
            "heading": "Las preguntas que <em>nos hacen más a menudo.</em>",
            "items": [
                ("¿Con qué frecuencia es necesaria una sesión de higiene?",
                 "Para los pacientes sin patología periodontal declarada la "
                 "cadencia es semestral. Para quienes presentan gingivitis, "
                 "periodontitis o llevan aparatos de ortodoncia, baja a "
                 "tres o cuatro meses. El plan se personaliza tras la "
                 "primera visita."),
                ("¿Las obturaciones de composite duran de verdad?",
                 "Sí, siempre que la cavidad se reconstruya bajo dique de "
                 "goma con composite estratificado y luz LED cualificada. "
                 "Nuestras obturaciones presentan una supervivencia media "
                 "de diez años con revisiones regulares. No utilizamos "
                 "amalgama desde 2013."),
                ("¿Cuánto cuesta realmente un implante?",
                 "El implante unitario (fixture de titanio Sweden+Martina "
                 "más corona de circonio) cuesta 1.850 €, IVA incluido. "
                 "Quedan excluidos los eventuales tratamientos "
                 "regenerativos previos (elevación de seno, GBR), que se "
                 "presupuestan solo tras el TAC de haz cónico."),
                ("¿La ortodoncia transparente funciona de verdad en adultos?",
                 "En el noventa por ciento de los casos clínicos en "
                 "adultos los alineadores transparentes (Invisalign o "
                 "SmileLab) son tan eficaces como la ortodoncia fija "
                 "tradicional. Los casos que aún requieren aparatos "
                 "fijos son las rotaciones graves de los premolares y "
                 "las extrusiones marcadas, y los hablamos abiertamente "
                 "en el plan."),
                ("¿Puedo traer a mis hijos al mismo estudio?",
                 "Sí. La Dra. Liccardi se ocupa de ortodoncia "
                 "interceptiva de 8 a 12 años con aparatos removibles. "
                 "La higiene pediátrica está incluida para los hijos de "
                 "los pacientes con plan anual activo."),
            ],
        },

        # Bottom CTA band.
        "cta_heading":
            "Cada plan de tratamiento queda <em>escrito, declarado, compartido.</em>",
        "cta_primary_label":   "Reservar higiene",
        "cta_secondary_label": "Contacto del estudio",

        # Sede / Location — Milán Brera.
        "location": {
            "label":   "Sede del estudio",
            "heading": "Via Manzoni 18, <em>Milán.</em>",
            "intro":
                "El estudio ocupa el piano nobile de un palacio histórico "
                "en el barrio de Brera, a ciento veinte metros de "
                "Montenapoleone. Cuatro consultas, sala radiológica con "
                "TAC de haz cónico y laboratorio de ortodoncia interno.",
            "map_image": "",
            "map_fallback_image":
                "https://images.pexels.com/photos/305567/pexels-photo-305567.jpeg"
                "?auto=compress&cs=tinysrgb&w=1200&h=800&fit=crop",
            "details": [
                ("Dirección",
                 "Via Manzoni 18\n20121 Milán"),
                ("Metro",
                 "M3 Montenapoleone\n3 minutos a pie"),
                ("Aparcamiento",
                 "Garaje concertado\nen Via Bigli, a 50 metros"),
                ("Accesibilidad",
                 "Entrada accesible con ascensor\nhasta el piano nobile"),
            ],
            "hours_short": [
                ("Lun – Vie", "8:30 – 19:30"),
                ("Sábado",    "9:00 – 13:00"),
                ("Domingo",   "Cerrado"),
            ],
            "cta_label": "Obtener indicaciones",
            "cta_href":  "contatti",
        },
    },

    # ─── STUDIO (about) ─────────────────────────────────────────────
    "studio": {
        "eyebrow":   "El estudio · Milán Brera",
        "headline":  "Cuatro dentistas, <em>una sola historia.</em>",
        "intro":
            "Denti+Co es un estudio asociado fundado en 2013 por cuatro "
            "profesionales que comparten la misma historia clínica y el "
            "mismo protocolo de trabajo: fotografías antes y después, "
            "dique de goma siempre, presupuesto por escrito entregado "
            "también en PDF y seguimiento programado.",
        # 5-row history timeline (year + 1-line description · 2-tuples).
        "history": [
            ("2013",
             "Fundación del estudio asociado en Via Manzoni con dos "
             "especialistas y una sala operativa."),
            ("2016",
             "Apertura del área de implantología con TAC de haz cónico "
             "Carestream CS 9600 y sala quirúrgica dedicada."),
            ("2019",
             "Adopción del escaneado intraoral iTero y de los planes "
             "ortodóncicos simulados en 3D antes del tratamiento."),
            ("2022",
             "Inauguración del laboratorio de ortodoncia interno con "
             "impresión 3D de férulas quirúrgicas y retenedores nocturnos."),
            ("2025",
             "El estudio cierra el año con cuatro asociados a jornada "
             "completa y un equipo de seis higienistas."),
        ],
        "studio_image":
            "https://images.pexels.com/photos/4269268/pexels-photo-4269268.jpeg"
            "?auto=compress&cs=tinysrgb&w=1400&h=600&fit=crop",
        "studio_image_caption": "Sala operativa · Via Manzoni 18",
        "method_title": "El método Denti+Co",
        "method_paragraphs": [
            "La higiene es el primer capítulo porque también es el más "
            "repetible. Casi nadie entra por primera vez al estudio con "
            "la boca en orden: para la mayoría de los pacientes hay que "
            "recomponer la base antes de hablar de estética, ortodoncia "
            "o implantología. Cuarenta minutos de higiene profesional "
            "bien hecha cambian la perspectiva sobre el presupuesto de "
            "todos los tratamientos posteriores.",
            "La historia clínica es una sola —la misma para los cuatro "
            "asociados— porque un paciente no es el paciente de un "
            "único dentista: es el paciente del estudio. Cuando la "
            "higienista detecta una recesión gingival durante una "
            "revisión, lo señala al periodoncista en el mismo documento "
            "clínico. Sin tratamientos fragmentados.",
            "Los precios están declarados para las prestaciones de "
            "rutina (higiene, conservadora, blanqueamiento, revisión). "
            "Para los planes más estructurados —implantología con "
            "regenerativa, ortodoncia compleja, rehabilitaciones "
            "totales— el presupuesto se personaliza tras una primera "
            "visita de setenta minutos, pero siempre se entrega por "
            "escrito y firmado al pie.",
        ],
        "values_label":   "Valores del estudio",
        "values_heading": "Cuatro compromisos, <em>escritos en la historia.</em>",
        "values": [
            ("Dique de goma siempre",
             "En cada intervención de conservadora, endodoncia y "
             "aplicación de composites. Sin excepciones."),
            ("Fotografías antes y después",
             "Serie fotográfica estandarizada entregada al paciente "
             "en formato digital al final de cada plan de tratamiento."),
            ("Presupuesto por escrito",
             "Nunca un coste comentado solo de palabra. PDF por correo "
             "o entregado en el estudio antes del inicio del trabajo."),
            ("Seguimiento programado",
             "Calendario de citas de mantenimiento enviado también por "
             "SMS o WhatsApp. Ningún paciente queda a su suerte tras "
             "la intervención."),
        ],
        "cta_heading":
            "El primer paso es siempre <em>una visita de setenta minutos.</em>",
        "cta_primary_label":   "Conoce a los dentistas",
        "cta_secondary_label": "Reservar la primera visita",
        "press_label": "Publicado en",
        "press": ["Il Dentista Moderno", "Dental Tribune",
                  "Bocca & Salute", "Corriere Salute"],
    },

    # ─── VISITE (services) ──────────────────────────────────────────
    "visite": {
        "eyebrow":  "Tratamientos · tarifa 2026",
        "headline": "Lo que hacemos, <em>lo que cuesta, lo que garantizamos.</em>",
        "intro":
            "La tarifa completa para las prestaciones de rutina. Los "
            "planes de tratamiento estructurados (implantología "
            "compleja, ortodoncia, rehabilitaciones totales) reciben "
            "siempre un presupuesto personalizado tras la primera visita.",
        "service_image":
            "https://images.pexels.com/photos/6502543/pexels-photo-6502543.jpeg"
            "?auto=compress&cs=tinysrgb&w=1400&h=600&fit=crop",
        "service_image_caption": "Sala operativa · instrumental y laboratorio interno",
        "treatments": [
            ("Higiene profesional individual",
             "45 min · sin necesidad de derivación médica",
             "Registro periodontal, índice de sangrado, pulido por aire "
             "con bicarbonato sódico y fotografías de control. Incluye el "
             "análisis de los hábitos de higiene domiciliaria con asignación "
             "—si procede— de cepillo sónico en prueba.",
             "€ 95"),
            ("Plan anual de mantenimiento",
             "anual · 2 higienes + 1 revisión + radiografías periapicales",
             "Dos higienes semestrales programadas, una visita de revisión "
             "con fotografías y radiografías periapicales cuando esté "
             "indicado. Canal directo por WhatsApp para las urgencias.",
             "€ 220"),
            ("Obturación conservadora (1 superficie)",
             "45 min · composite estratificado bajo dique de goma",
             "Composite de marca Tokuyama o 3M, siempre bajo dique de goma "
             "y con fotopolimerización LED cualificada. Garantía de "
             "estanqueidad de cinco años con revisiones regulares.",
             "€ 140"),
            ("Endodoncia unirradicular",
             "75 min · localizador apical + sellado termoplástico",
             "Endodoncia con localizador apical Morita, sellado "
             "tridimensional con gutapercha termoplástica y obturación "
             "coronal en composite. Seguimiento radiográfico a los seis y "
             "doce meses.",
             "€ 280"),
            ("Implante unitario (fixture + corona de circonio)",
             "intervención + 2 revisiones · garantía vitalicia sobre el fixture",
             "Implante italiano Sweden+Martina, pilar de circonio "
             "estabilizado y corona monolítica fresada en el laboratorio "
             "interno. TAC de haz cónico previo incluido.",
             "€ 1.850"),
            ("Alineadores Invisalign (plan completo)",
             "12-18 meses · escaneado iTero + plan 3D + retenedor",
             "Escaneado intraoral iTero y plan simulado en 3D entregado "
             "al paciente antes de empezar. Alineadores entregados por "
             "fases. Retenedor nocturno postratamiento incluido.",
             "€ 3.200"),
            ("Blanqueamiento profesional en sillón",
             "60 min · peróxido al 35 % + gel barrera gingival",
             "Una sesión de sesenta minutos con peróxido de hidrógeno al "
             "35 %, gel barrera gingival fotopolimerizado y control del "
             "pH en saliva antes y después del tratamiento.",
             "€ 380"),
            ("Primera visita (historia + plan)",
             "70 min · anamnesis + escaneado iTero + plan en PDF",
             "Anamnesis médica y dental, exploración clínica, registro "
             "periodontal, escaneado intraoral, fotografías y entrega "
             "del plan clínico en PDF. El coste se descuenta del primer "
             "tratamiento.",
             "€ 80"),
        ],
        "footnote_heading": "Qué NO está incluido en la tarifa",
        "footnote":
            "Las prestaciones de rutina anteriores están declaradas. Los "
            "planes de tratamiento estructurados (rehabilitaciones "
            "totales, implantología con regenerativa amplia, ortodoncia "
            "con cirugía ortognática) reciben un presupuesto "
            "personalizado tras la primera visita de setenta minutos. "
            "Ningún presupuesto se facilita por teléfono o por correo "
            "antes de una visita clínica.",
        "cta_heading":
            "El presupuesto siempre es <em>escrito, firmado, entregado en PDF.</em>",
        "cta_primary_label":   "Reservar la primera visita",
        "cta_secondary_label": "Escríbanos",
    },

    # ─── MEDICI (team) — 4 dental specialists ───────────────────────
    "medici": {
        "eyebrow":  "Los dentistas · equipo asociado",
        "headline": "Cuatro firmas, <em>una sola historia clínica.</em>",
        "intro":
            "Los cuatro asociados comparten la misma historia clínica y "
            "se consultan mutuamente sobre los planes complejos. Para "
            "cada paciente se indica el dentista de referencia, pero la "
            "higiene de mantenimiento puede realizarla cualquier "
            "miembro del equipo.",
        "doctors": [
            {
                "name":  "Dra. Chiara Vespa",
                "role":  "Directora sanitaria · Conservadora y endodoncia",
                "bio":
                    "Especialista en odontología conservadora formada en "
                    "la Università degli Studi di Milano y perfeccionada "
                    "en la Loma Linda University. Miembro de la SIE "
                    "(Sociedad Italiana de Endodoncia). Coordinadora "
                    "clínica del estudio desde 2013.",
                "portrait": _CHIEF_PORTRAIT,
            },
            {
                "name":  "Dr. Riccardo Berti",
                "role":  "Implantología y regenerativa",
                "bio":
                    "Implantólogo formado en la New York University "
                    "College of Dentistry y perfeccionado en Gnatología "
                    "Clínica en la Università di Pavia. Se ocupa de "
                    "implantología guiada por ordenador, rehabilitaciones "
                    "complejas y regenerativa ósea.",
                "portrait":
                    "https://images.pexels.com/photos/6627850/pexels-photo-6627850.jpeg"
                    "?auto=compress&cs=tinysrgb&w=900&h=1200&fit=crop",
            },
            {
                "name":  "Dra. Sofia Liccardi",
                "role":  "Ortodoncia y odontopediatría",
                "bio":
                    "Especialista en ortodoncia formada en la Università "
                    "Cattolica del Sacro Cuore. Certificada como "
                    "Invisalign Diamond Provider. Se ocupa de ortodoncia "
                    "en adultos, interceptiva infantil y atención al "
                    "paciente pediátrico hasta los dieciséis años.",
                "portrait":
                    "https://images.pexels.com/photos/4687404/pexels-photo-4687404.jpeg"
                    "?auto=compress&cs=tinysrgb&w=900&h=1200&fit=crop",
            },
            {
                "name":  "Dr. Andrea Carofiglio",
                "role":  "Periodoncia y medicina oral",
                "bio":
                    "Periodoncista formado en la Università degli Studi "
                    "di Bologna y perfeccionado en la Universidad de "
                    "Berna. Miembro de la SIdP (Sociedad Italiana de "
                    "Periodoncia e Implantología). Se ocupa de "
                    "periodontitis crónica y medicina oral.",
                "portrait":
                    "https://images.pexels.com/photos/6529057/pexels-photo-6529057.jpeg"
                    "?auto=compress&cs=tinysrgb&w=900&h=1200&fit=crop",
            },
        ],
        "portrait_city": "Milán · Brera",
    },

    # ─── PUBBLICAZIONI (blog_list) ──────────────────────────────────
    "pubblicazioni": {
        "eyebrow":  "Publicaciones y divulgación",
        "headline": "Lo que hemos escrito, <em>para quién.</em>",
        "intro":
            "Artículos divulgativos publicados en medios especializados "
            "y aportaciones clínicas a revistas científicas. Todos los "
            "contenidos los revisa personalmente la Dra. Vespa antes de "
            "su publicación.",
        "lead_image": _LEAD_IMAGE,
        "footer_strap": "Denti+Co · Estudio dental asociado · Milán",
        "empty_body_fallback_paragraphs": [
            "Artículo en preparación editorial. La publicación íntegra "
            "estará disponible en breve.",
            "Este marcador describe la voz del artículo: una nota "
            "clínica escrita por el médico, en tono directo y sin "
            "tecnicismos, pensada para pacientes que buscan información "
            "fiable sobre su salud bucal.",
        ],
    },

    # Posts list — TOP-LEVEL, sibling to `pubblicazioni`.
    "posts": [
        {
            "slug":     "igiene-professionale-perche-semestrale",
            "kicker":   "Higiene y prevención",
            "title":    "Higiene profesional: por qué la cadencia semestral es una decisión clínica",
            "date":     "12 de marzo de 2025",
            "read_min": 8,
            "author":   "Dra. Chiara Vespa",
            "lede":
                "La literatura clínica respalda una cadencia de higiene "
                "personalizada, pero la regla de los seis meses sigue "
                "siendo el mejor equilibrio entre coste, adhesión del "
                "paciente y resultado periodontal a largo plazo.",
        },
        {
            "slug":     "impianti-carico-immediato-quando",
            "kicker":   "Implantología",
            "title":    "Carga inmediata en implantología: cuándo está realmente indicada",
            "date":     "23 de enero de 2025",
            "read_min": 12,
            "author":   "Dr. Riccardo Berti",
            "lede":
                "La carga inmediata seduce por la reducción del tiempo "
                "de tratamiento, pero no es la solución universal. Los "
                "criterios de selección del paciente son restrictivos y "
                "deben explicarse abiertamente antes de la intervención.",
        },
        {
            "slug":     "allineatori-trasparenti-cosa-non-fanno",
            "kicker":   "Ortodoncia",
            "title":    "Alineadores transparentes: tres cosas que no hacen",
            "date":     "5 de noviembre de 2024",
            "read_min": 6,
            "author":   "Dra. Sofia Liccardi",
            "lede":
                "Son eficaces en la mayoría de los adultos, pero no lo "
                "resuelven todo. Tres límites clínicos honestos que "
                "todo paciente debería conocer antes de iniciar el plan.",
        },
        {
            "slug":     "parodontite-non-e-solo-gengivite",
            "kicker":   "Periodoncia",
            "title":    "La periodontitis no es solo «encías que sangran»",
            "date":     "18 de septiembre de 2024",
            "read_min": 5,
            "author":   "Dr. Andrea Carofiglio",
            "lede":
                "La periodontitis crónica afecta a uno de cada dos "
                "adultos a partir de los treinta y cinco años, pero se "
                "diagnostica tarde porque los signos iniciales son "
                "silentes. Tres índices periodontales que cualquier "
                "paciente puede pedir a su dentista.",
        },
    ],

    # ─── CONTATTI (contact) ─────────────────────────────────────────
    "contatti": {
        "eyebrow":  "Contacto y sede",
        "headline": "Escríbanos, <em>le llamamos en el día.</em>",
        "intro":
            "Para reservar una primera visita o una higiene de "
            "mantenimiento puede llamarnos, escribirnos por WhatsApp o "
            "rellenar el formulario que figura a continuación. "
            "Respondemos en el mismo día laborable.",
        # 4 info-blocks: (label, value, sub) 3-tuples.
        "blocks": [
            ("Sede",
             "Via Manzoni 18\n20121 Milán",
             "Piano nobile · entrada independiente"),
            ("Teléfono",
             "+39 02 7770 4488",
             "Respuesta en el día laborable"),
            ("Correo electrónico",
             "studio@denticostudio.it",
             "Para consultas no urgentes"),
            ("Horarios",
             "Lun – Vie · 8:30 – 19:30\nSáb · 9:00 – 13:00",
             "Domingo cerrado"),
        ],
        "form_title": "Escríbanos, le llamamos en el día.",
        "form_intro":
            "Formulario para consultas informativas o para concertar la "
            "primera visita. Para urgencias clínicas, llámenos "
            "directamente.",
        "form_placeholders": {
            "first_name": "María",
            "last_name":  "García",
            "email":      "maria.garcia@email.es",
            "phone":      "+34 612 34 56 78",
            "subject":    "Primera visita / higiene / urgencia",
            "message":    "Indique la franja horaria preferida y, si procede, el dentista de referencia.",
        },
        "form_helpers": {},
        "form_consent":
            "Consiento el tratamiento de mis datos personales con la "
            "única finalidad de que el estudio se ponga en contacto "
            "conmigo. RGPD Art. 6 · DPO localizable en "
            "dpo@denticostudio.it.",
        "form_submit_note":
            "Respuesta en el siguiente día laborable.",
        "hours_heading":    "Horario de apertura",
        # 3-tuples (day, am, pm).
        "hours": [
            ("Lunes",     "8:30 – 13:00", "14:00 – 19:30"),
            ("Martes",    "8:30 – 13:00", "14:00 – 19:30"),
            ("Miércoles", "8:30 – 13:00", "14:00 – 19:30"),
            ("Jueves",    "8:30 – 13:00", "14:00 – 19:30"),
            ("Viernes",   "8:30 – 13:00", "14:00 – 19:30"),
            ("Sábado",    "9:00 – 13:00", "—"),
            ("Domingo",   "—", "Cerrado"),
        ],
        "transport_heading": "Cómo llegar",
        # 2-tuples (label, text).
        "transport": [
            ("Metro",         "M3 Montenapoleone · 3 minutos a pie"),
            ("Tranvía",       "Línea 1 · parada Manzoni"),
            ("Tren",          "Estación Central · 12 minutos en M3"),
            ("Aparcamiento",  "Garaje Via Bigli · a 50 metros · concertado"),
        ],
    },

    # ─── RICHIEDI-VISITA (appointment) ──────────────────────────────
    "richiedi-visita": {
        "eyebrow":  "Reservar higiene · primera visita",
        "headline": "Reserve, <em>le contactamos en 24 horas.</em>",
        "intro":
            "Rellene el formulario: la secretaría fija la primera cita "
            "en el siguiente día laborable y se la confirma también por "
            "SMS o WhatsApp.",
        "process_label":   "El recorrido de reserva",
        "process_heading": "Del formulario a la primera <em>cita</em>, en cuatro pasos.",
        # 4 process steps (num, title, blurb) — 3-tuples.
        "process": [
            ("01", "Formulario y llamada",
             "La secretaría recibe el formulario, comprueba que estén "
             "todos los datos necesarios y le devuelve la llamada en el "
             "siguiente día laborable para fijar la cita."),
            ("02", "Confirmación y recordatorio",
             "Recibirá la confirmación por SMS o WhatsApp con fecha, "
             "hora, dentista de referencia, dirección del estudio e "
             "indicaciones para llegar."),
            ("03", "Primera visita de 70 minutos",
             "Anamnesis, exploración clínica completa, escaneado iTero, "
             "fotografías intraorales y extraorales, registro "
             "periodontal y entrega del plan clínico en PDF."),
            ("04", "Plan por escrito",
             "Discusión del plan en el sillón con presupuesto partida "
             "por partida. El coste de la primera visita se descuenta "
             "del primer tratamiento del plan."),
        ],
        "form_title": "Reservar la primera cita",
        "form_band_side_note":
            "Respuesta en 24 horas laborables. Para urgencias clínicas, "
            "llame directamente al +39 02 7770 4488.",
        "form_band_side_note_small":
            "Los datos recogidos se usan exclusivamente para devolverle la llamada · RGPD Art. 6.",
        "form_fields": [
            {"name": "first_name", "label": "Nombre",
             "type": "text",       "required": True,
             "placeholder": "María"},
            {"name": "last_name",  "label": "Apellidos",
             "type": "text",       "required": True,
             "placeholder": "García"},
            {"name": "email",      "label": "Correo electrónico",
             "type": "email",      "required": True,
             "placeholder": "maria.garcia@email.es"},
            {"name": "phone",      "label": "Teléfono",
             "type": "tel",        "required": True,
             "placeholder": "+34 612 34 56 78"},
            {"name": "service",    "label": "Tratamiento solicitado",
             "type": "select",     "required": True,
             "options": [
                 "Higiene profesional",
                 "Primera visita (historia + plan)",
                 "Urgencia odontológica",
                 "Visita de implantología",
                 "Visita de ortodoncia",
                 "Otro",
             ]},
            {"name": "preferred",  "label": "Franja horaria preferida",
             "type": "select",     "required": False,
             "options": [
                 "Mañana (8:30 – 13:00)",
                 "Tarde (14:00 – 19:30)",
                 "Sábado por la mañana",
                 "Indiferente",
             ]},
            {"name": "notes",      "label": "Notas (opcionales)",
             "type": "textarea",   "required": False,
             "full_width": True,
             "placeholder": "Indique alergias a medicamentos, pruebas previas o el dentista de referencia, si procede."},
        ],
        "submit_label": "Reservar cita",
        "consent":
            "Consiento el tratamiento de los datos personales con la "
            "única finalidad de que el estudio se ponga en contacto "
            "conmigo. RGPD Art. 6 · DPO localizable en "
            "dpo@denticostudio.it.",
        "footnote":
            "Los datos recogidos se usan exclusivamente para devolverle "
            "la llamada en relación con su consulta. Cumplimiento del "
            "RGPD Art. 6 · DPO localizable en dpo@denticostudio.it.",
    },
}
