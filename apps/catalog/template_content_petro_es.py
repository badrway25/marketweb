"""Petro · Estudio Veterinario Perro Gato Exóticos · Spanish (ES) content tree.

T52 multilingual rollout pass. Peninsular Spanish (`usted` register ·
formal · institutional) translation of `PETRO_CONTENT_IT`. Built for the
marketweb T52 multilingual workflow (IT → EN/FR/ES/AR · AAA walk ·
public flip). Shape parity contract enforced against
`template_content_petro.py`:

  * Same top-level keys, same nested keys at every depth.
  * Same list lengths (4 signature visits, 8 treatments, 3 doctors,
    2 posts, 5 history entries, 5 percorso steps, 5 FAQ items, etc.).
  * Same tuple positions for tuple-typed values:
      - `home.signature_visits` 3-tuples (num, title, desc)
      - `visite.treatments` 4-tuples (name, meta, desc, price)
      - `contatti.blocks` 3-tuples (label, value, sub)
      - `contatti.hours` 3-tuples (day, am, pm)
      - `contatti.transport` 2-tuples (label, text)
      - `richiedi-visita.process` 3-tuples (num, title, blurb)
  * Same `pages[].slug` values (labels translated, slugs preserved).
  * Same `posts[].slug` values, same page `kind`.

Voice anchor — `medicina preventiva` (peninsular veterinary register ·
Colegio Oficial de Veterinarios de Madrid register · AVEPA
[Asociación Veterinaria Española de Especialistas en Pequeños Animales]
professional press · authoritative pet-care idiom) carries the IT
`cura preventiva` load-bearing clinical promise across the same
surfaces (hero H1 with `<em>` italic emphasis, manifesto, cta_heading,
studio.values, visite, signature_visits, doctor bios). The variant
`revisión preventiva` is used as the bookable noun ("Reserve una
revisión preventiva") where the act of booking is foregrounded.
Register is Peninsular `usted` (formal · institutional · NOT Latin
American). Italian heritage proper names (Padova, Borgo Trento, Via
Belzoni 71, Università di Padova, Royal Veterinary College London,
Cornell University Vet School, Ospedale Veterinario di Legnaro,
SCIVAC, ANMVI, AAEMV, Esaote MyLab Omega, Carestream, Mortara,
Cuneo IGP) preserved verbatim. Veterinary technical vocabulary
(WSAVA, DA2PPi-L, FRCP+FeLV, RHDV1+2, Mixoma, BCS, laparoscopia)
preserved. Currency in Peninsular convention (`75 €`, after number),
decimal comma (`pH 4,2`, `0,4 mm`), `¿…?` `¡…!` opening marks,
masculine `el veterinario` for Marco Petro, feminine `la
veterinaria` for Anna Bressan.
"""
from __future__ import annotations

from typing import Any


# Imagery URLs from the X.3 curator pack
# `docs/content-factory/imagery/packs/veterinary.md`. All URLs
# Pexels License (CC0-compatible · commercial use OK).
_CHIEF_PORTRAIT = (
    # Veterinarian with white coat examining a small dog · matches
    # Dr. Petro "veterinario direttore" hands-on persona
    "https://images.pexels.com/photos/6235648/pexels-photo-6235648.jpeg"
    "?auto=compress&cs=tinysrgb&w=900&h=1200&fit=crop"
)
_STUDIO_IMAGE = (
    # Veterinary clinic interior — exam table + bright clinical
    "https://images.pexels.com/photos/7468978/pexels-photo-7468978.jpeg"
    "?auto=compress&cs=tinysrgb&w=1400&h=600&fit=crop"
)
_LEAD_IMAGE = (
    # Bright veterinary clinic consultation · used as blog_list lead
    "https://images.pexels.com/photos/6235244/pexels-photo-6235244.jpeg"
    "?auto=compress&cs=tinysrgb&w=1200&h=800&fit=crop"
)
_MAP_FALLBACK = (
    # Modern veterinary clinic reception · map-fallback when Mapbox
    # tile fails to load
    "https://images.pexels.com/photos/6235241/pexels-photo-6235241.jpeg"
    "?auto=compress&cs=tinysrgb&w=1200&h=800&fit=crop"
)
_SERVICE_IMAGE = (
    # Vet auscultating cat patient close-up — visite page hero
    "https://images.pexels.com/photos/7470779/pexels-photo-7470779.jpeg"
    "?auto=compress&cs=tinysrgb&w=1400&h=900&fit=crop"
)


PETRO_CONTENT_ES: dict[str, Any] = {
    "pages": [
        {"slug": "home",            "label": "Estudio",                 "kind": "home"},
        {"slug": "studio",          "label": "El Estudio",              "kind": "about"},
        {"slug": "visite",          "label": "Consultas",               "kind": "services"},
        {"slug": "medici",          "label": "Veterinarios",            "kind": "team"},
        {"slug": "pubblicazioni",   "label": "Diario clínico",          "kind": "blog_list"},
        {"slug": "contatti",        "label": "Contacto",                "kind": "contact"},
        {"slug": "richiedi-visita", "label": "Reservar una consulta",   "kind": "appointment"},
    ],

    "site": {
        "logo_initial": "P",
        "logo_word":    "Petro",
        "tag":          "Estudio veterinario · Padova Borgo Trento · perro gato exóticos",
        "phone":        "+39 049 6731 220",
        "email":        "studio@studiopetro.it",
        "address":      "Via Belzoni 71 · 35121 Padova",
        "hours_compact": "Lun – Vie · 8:00 – 20:00 · Sáb 9:00 – 13:00",
        "hours_footer_rows": [
            "Domingo · solo urgencias bajo llamada",
            "Disponibilidad nocturna 24/7 · +39 333 410 7726",
        ],
        "license":      "Inscripción Colegio de Veterinarios de Padova n.º 1428 · Director sanitario Dr. M. Petro",
        "footer_intro":
            "Estudio veterinario independiente de medicina preventiva, "
            "cirugía de tejidos blandos y cuidado geriátrico para perro, "
            "gato y pequeños animales exóticos. Tres veterinarios, una "
            "sola historia clínica por animal, disponibilidad nocturna "
            "bajo llamada.",
    },

    "home": {
        "hero_variant": "split-consultive",
        "eyebrow":  "Medicina veterinaria · Padova Borgo Trento",
        "headline": "Los animales no hablan. La <em>medicina preventiva</em> escucha primero.",
        "intro":
            "Revisiones preventivas anuales, vacunaciones según "
            "calendario, diagnóstico por imagen y cirugía de tejidos "
            "blandos para perro, gato y pequeños animales exóticos. "
            "Tres veterinarios asociados, disponibilidad nocturna bajo "
            "llamada, una sola historia clínica compartida por cada "
            "paciente.",
        "primary_cta":   "Reserve una revisión preventiva",
        "primary_href":  "richiedi-visita",
        "secondary_cta": "Los veterinarios",
        "secondary_href":"medici",

        "facts": [
            ("17",    "años de estudio veterinario independiente"),
            ("4.200", "animales atendidos cada año"),
            ("3",     "veterinarios asociados en la sede"),
        ],

        "manifesto_drop_cap": "L",
        "manifesto":
            "os animales no describen el dolor: lo esconden. El gato "
            "se refugia, el perro come menos, el conejo deja de "
            "moverse. Por eso en Petro la medicina preventiva no es "
            "un servicio adicional — revisión anual completa, "
            "cribado geriátrico semestral a partir de los siete "
            "años, control dental cada dos, vacunaciones según "
            "calendario. Cuando el animal llega al estudio con "
            "síntomas visibles, a menudo estamos ya en la mitad "
            "del problema. Nuestra historia clínica existe para "
            "llegar antes.",

        "hero_sidebar_top_label": "Dirección clínica",
        "hero_sidebar_quote":
            "«Los animales no dicen dónde les duele. La revisión "
            "preventiva es el único modo honesto de practicar la "
            "medicina veterinaria — el resto es solo urgencia.»",
        "hero_sidebar_author": "— Dr. Marco Petro · Director sanitario · Inscripción OMV Padova 1428",
        "hero_sidebar_pulse": [
            ("Estudio",     "Padova · Borgo Trento"),
            ("Desde",       "2008"),
            ("Referencia",  "Perro gato exóticos"),
        ],

        "anchor_nav": [
            ("metodo",        "Método clínico"),
            ("visite",        "Revisiones preventivas"),
            ("percorso",      "Recorrido del paciente"),
            ("medico",        "Dirección clínica"),
            ("studio",        "Sede y contacto"),
        ],

        "signature_visits_label":   "Cuatro familias de intervención",
        "signature_visits_heading": "Cuatro recorridos clínicos, <em>una sola historia por cada animal.</em>",
        "signature_visits_intro":
            "Las cuatro familias de medicina preventiva más "
            "solicitadas de la veterinaria de pequeños animales. "
            "La lista completa está en la página Consultas.",
        "signature_visits": [
            ("01", "Revisión preventiva anual",
             "El pilar de la medicina preventiva: examen físico "
             "completo, peso y BCS, auscultación cardiopulmonar, "
             "palpación abdominal, control dental, anamnesis "
             "vacunal y profilaxis antiparasitaria. Cuarenta "
             "minutos, con cita previa."),
            ("02", "Vacunaciones y profilaxis",
             "Vacunas perro (DA2PPi-L) y gato (FRCP-FeLV) según "
             "calendario WSAVA. Profilaxis filaria, leishmania, "
             "garrapatas. Vacunas conejo (RHDV-Mixoma) y hurón. "
             "Cartilla sanitaria actualizada en la sede."),
            ("03", "Cirugía de tejidos blandos",
             "Esterilización de perra y gata por laparoscopia "
             "(mínimamente invasiva, tiempos de recuperación "
             "reducidos), extirpación de neoformaciones cutáneas, "
             "cirugía oncológica con estudio histológico, suturas "
             "estéticas."),
            ("04", "Diagnóstico por imagen",
             "Ecografía abdominal y cardíaca en sede, radiografía "
             "digital con imágenes entregadas al propietario, "
             "citología por punción-aspiración leída en 24 horas en "
             "el laboratorio asociado de la Università di Padova."),
        ],

        "trattamenti_tabs": {
            "label":   "Tarifa de consultas e intervenciones",
            "heading": "Qué hacemos, con <em>qué criterio.</em>",
            "intro":
                "Cuatro familias clínicas, cada una con un protocolo "
                "escrito y un coste declarado. Sin presupuestos "
                "personalizados para los conceptos de rutina — solo "
                "para planes de cuidado estructurados (cirugía "
                "compleja, terapia oncológica, rehabilitación).",
            "tabs": [
                {
                    "id":      "preventiva",
                    "label":   "Preventiva",
                    "eyebrow": "Medicina preventiva",
                    "heading": "Cuarenta minutos, una vez al año.",
                    "body":
                        "La revisión preventiva anual no es un control "
                        "rápido: es una valoración clínica completa de "
                        "cuarenta minutos con anamnesis, examen físico "
                        "sistemático, control dental, peso/BCS, "
                        "auscultación y palpación. A partir de los "
                        "siete años se añade el cribado geriátrico "
                        "semestral.",
                    "items": [
                        ("Revisión preventiva anual perro/gato", "40 min · 65 €"),
                        ("Cribado geriátrico (≥ 7 años)", "60 min · 95 €"),
                        ("Revisión preventiva exóticos (conejo/hurón)", "45 min · 75 €"),
                        ("Anamnesis pre-adopción cachorro/gatito", "30 min · 50 €"),
                    ],
                    "cta_label": "Todos los protocolos preventivos →",
                    "cta_href":  "visite",
                },
                {
                    "id":      "vaccinazioni",
                    "label":   "Vacunaciones",
                    "eyebrow": "Vacunas y profilaxis antiparasitaria",
                    "heading": "Protocolo WSAVA, cartilla en la sede.",
                    "body":
                        "Las vacunas siguen las directrices WSAVA "
                        "(perro DA2PPi-L core anual, gato FRCP-FeLV "
                        "core trienal tras refuerzo). La cartilla "
                        "sanitaria se entrega en la sede, también "
                        "electrónica mediante app. Profilaxis "
                        "antiparasitaria mensual o trimestral según "
                        "raza y entorno.",
                    "items": [
                        ("Vacuna perro DA2PPi-L (anual)", "cita previa · 45 €"),
                        ("Vacuna gato FRCP + FeLV", "cita previa · 55 €"),
                        ("Vacuna conejo RHDV1+2 / Mixoma", "cita previa · 50 €"),
                        ("Profilaxis filaria + garrapatas (12 meses)", "plan · 95 €"),
                    ],
                    "cta_label": "Calendario vacunal completo →",
                    "cta_href":  "visite",
                },
                {
                    "id":      "chirurgia",
                    "label":   "Cirugía",
                    "eyebrow": "Cirugía de tejidos blandos",
                    "heading": "Laparoscopia mínimamente invasiva siempre que sea posible.",
                    "body":
                        "Esterilización de perra y gata por "
                        "laparoscopia (tres pequeños accesos · "
                        "ingreso diurno · dolor postoperatorio "
                        "reducido). Extirpación de neoformaciones "
                        "cutáneas con estudio histológico en el "
                        "laboratorio de Anatomía Patológica de la "
                        "Università di Padova. Suturas estéticas "
                        "subcuticulares reabsorbibles.",
                    "items": [
                        ("Esterilización gata (laparoscopia)", "intervención · 320 €"),
                        ("Esterilización perra < 20 kg", "intervención · 480 €"),
                        ("Esterilización perra > 20 kg", "intervención · 620 €"),
                        ("Extirpación neoformación cutánea + histología", "intervención · 220 €"),
                    ],
                    "cta_label": "Recorridos quirúrgicos completos →",
                    "cta_href":  "visite",
                },
                {
                    "id":      "diagnostica",
                    "label":   "Diagnóstico",
                    "eyebrow": "Diagnóstico por imagen y laboratorio",
                    "heading": "Eco, radiografía digital, citología en 24 horas.",
                    "body":
                        "Ecografía abdominal y cardíaca en sede con "
                        "Esaote MyLab Omega · radiografía digital "
                        "Carestream con entrega de imágenes al "
                        "propietario por la nube · citología por "
                        "punción-aspiración leída en 24 horas en el "
                        "laboratorio de Anatomía Patológica de la "
                        "Università di Padova. Análisis hemato"
                        "químicos procesados en sede en 30 minutos.",
                    "items": [
                        ("Ecografía abdominal completa", "30 min · 95 €"),
                        ("Ecografía cardíaca (ecocardio)", "45 min · 130 €"),
                        ("Radiografía digital (2 proyecciones)", "20 min · 75 €"),
                        ("Análisis hematoquímicos completos en sede", "30 min · 85 €"),
                    ],
                    "cta_label": "Protocolos diagnósticos →",
                    "cta_href":  "visite",
                },
            ],
        },

        "chief_label":   "Dirección clínica",
        "chief_heading": "Un solo veterinario <em>firma cada historia.</em>",
        "chief": {
            "name":  "Dr. Marco Petro",
            "role":  "Director sanitario · Medicina interna y cirugía de tejidos blandos",
            "bio":
                "Licenciado en Medicina Veterinaria por la Università "
                "di Padova en 2000, perfeccionamiento en el Royal "
                "Veterinary College London (2002-2004) en pequeños "
                "animales y medicina preventiva, estancia de "
                "especialización en la Cornell University Vet School "
                "(NY, EE. UU.) en 2006. Miembro SCIVAC (Società "
                "Culturale Italiana Veterinari Animali Compagnia) y "
                "ANMVI (Associazione Nazionale Medici Veterinari "
                "Italiani). Inscripción Colegio de Veterinarios de "
                "Padova n.º 1428 desde 2001. Director sanitario del "
                "estudio desde 2008.",
            "portrait": _CHIEF_PORTRAIT,
        },

        "percorso": {
            "label":   "Recorrido del paciente",
            "heading": "Qué esperar de la <em>primera consulta.</em>",
            "intro":
                "La primera consulta en el estudio dura una hora y "
                "está dedicada a la construcción de la historia "
                "clínica completa: anamnesis, examen físico, "
                "eventual ecografía abdominal de base, plan de "
                "cuidado escrito. Nunca intervenciones no urgentes "
                "en la primera consulta.",
            "steps": [
                {
                    "num": "01",
                    "icon": "clipboard",
                    "title": "Recepción y anamnesis",
                    "desc": "Secretaría, ficha anamnésica completa "
                            "(raza, edad, alimentación, entorno, "
                            "convivencia con otros animales), "
                            "eventuales pruebas previas del "
                            "veterinario anterior.",
                    "duration": "10 min",
                },
                {
                    "num": "02",
                    "icon": "book",
                    "title": "Examen físico completo",
                    "desc": "Peso y Body Condition Score, "
                            "auscultación cardiopulmonar, palpación "
                            "abdominal, inspección de la cavidad "
                            "oral, control de piel y pelaje, "
                            "palpación de ganglios linfáticos.",
                    "duration": "20 min",
                },
                {
                    "num": "03",
                    "icon": "heart",
                    "title": "Diagnóstico de base",
                    "desc": "Ecografía abdominal orientativa (si "
                            "está indicada), eventuales extracciones "
                            "para análisis hematoquímicos procesados "
                            "en sede en treinta minutos. Radiografía "
                            "si hay sospecha de traumatismo.",
                    "duration": "15 min",
                },
                {
                    "num": "04",
                    "icon": "chart",
                    "title": "Plan de cuidado escrito",
                    "desc": "Conversación con el propietario sobre "
                            "el plan preventivo o terapéutico, "
                            "presupuesto detallado concepto por "
                            "concepto, entregado también por correo "
                            "en formato PDF.",
                    "duration": "10 min",
                },
                {
                    "num": "05",
                    "icon": "document",
                    "title": "Programación y seguimiento",
                    "desc": "Calendario de revisiones de control, "
                            "recordatorios por WhatsApp para vacunas "
                            "y profilaxis, canal directo con la "
                            "secretaría para dudas no urgentes.",
                    "duration": "5 min",
                },
            ],
        },

        "press": ["Veterinaria Italiana", "SCIVAC Bulletin", "Il Mondo del Cane",
                  "QuattroZampe Mondadori", "Corriere Animali"],
        "press_label": "Publicado en",

        "faq": {
            "label": "Preguntas frecuentes",
            "heading": "Las preguntas que <em>los propietarios nos hacen más a menudo.</em>",
            "items": [
                ("¿Cada cuánto hace falta una revisión preventiva?",
                 "Para perro y gato adultos sanos la frecuencia es "
                 "anual. A partir de los siete años (animales "
                 "geriátricos) se añade una revisión de cribado "
                 "semestral con análisis hematoquímicos. Para "
                 "conejo y hurón la frecuencia es semestral desde "
                 "la primera consulta porque la esperanza de vida "
                 "es más corta."),
                ("¿Practican la esterilización por laparoscopia?",
                 "Sí, en gata y perra de hasta 35 kg. La "
                 "esterilización por laparoscopia supone tres "
                 "pequeños accesos abdominales de 5 mm en lugar de "
                 "la incisión tradicional, ingreso diurno, dolor "
                 "postoperatorio reducido y vuelta a la normalidad "
                 "en 48 horas. En tallas superiores a 35 kg se "
                 "valora caso por caso."),
                ("¿Atienden también a conejos, hurones, aves y reptiles?",
                 "Conejo, hurón y cobaya sí, en todos los "
                 "recorridos (preventiva, vacunaciones, cirugía, "
                 "diagnóstico). Aves y reptiles solo para "
                 "consultas básicas — para patologías complejas "
                 "derivamos a colegas especialistas en animales "
                 "exóticos de las clínicas universitarias."),
                ("¿Tienen servicio de disponibilidad nocturna?",
                 "Sí, el doctor Petro está disponible 24/7 para "
                 "sus propios pacientes en el número "
                 "+39 333 410 7726. Para urgencias en animales no "
                 "registrados en historia derivamos al Ospedale "
                 "Veterinario de la Università di Padova (Legnaro, "
                 "abierto 24 h) o a la Clinica San Marco de "
                 "Veggiano."),
                ("¿Cómo funciona el plan de prevención anual?",
                 "Incluye revisión preventiva, vacunas perro "
                 "DA2PPi-L o gato FRCP, profilaxis mensual filaria "
                 "y garrapatas, cribado hematoquímico anual, un "
                 "refuerzo semestral gratuito. Coste 245 €/año "
                 "para perro, 195 €/año para gato. Descuento del "
                 "15 % sobre las intervenciones quirúrgicas "
                 "programadas en los doce meses siguientes."),
            ],
        },

        "cta_heading":
            "Cada plan de medicina preventiva es <em>escrito, declarado, compartido con el propietario.</em>",
        "cta_primary_label":   "Reserve una revisión preventiva",
        "cta_secondary_label": "Contacto del estudio",

        "location": {
            "label":   "Sede del estudio",
            "heading": "Via Belzoni 71, <em>Padova.</em>",
            "intro":
                "El estudio ocupa la planta baja de un edificio "
                "decimonónico en la zona de Borgo Trento, a "
                "cuatrocientos metros de la Estación Central y a "
                "diez minutos a pie de la Facultad de Medicina "
                "Veterinaria. Tres salas de consulta separadas "
                "perro/gato/exóticos, sala quirúrgica, sala de "
                "diagnóstico con ecógrafo y Rx digital, área de "
                "hospitalización diurna.",
            "map_image": "",
            "map_fallback_image": _MAP_FALLBACK,
            "details": [
                ("Dirección",
                 "Via Belzoni 71\n35121 Padova"),
                ("Estación",
                 "Padova Centrale\n6 minutos a pie"),
                ("Aparcamiento",
                 "Aparcamiento Borgo Trento gratuito\n80 metros del estudio"),
                ("Accesibilidad",
                 "Entrada en planta baja sin escalones\naccesible para sillas de ruedas y transportines grandes"),
            ],
            "hours_short": [
                ("Lun – Vie", "8:00 – 20:00"),
                ("Sábado",    "9:00 – 13:00"),
                ("Domingo",   "Solo urgencias bajo llamada"),
            ],
            "cta_label": "Obtener indicaciones para llegar",
            "cta_href":  "contatti",
        },
    },

    # ─── STUDIO (about) ────────────────────────────────────────
    "studio": {
        "eyebrow":   "El estudio · Padova Borgo Trento",
        "headline":  "Tres veterinarios, <em>una historia por cada animal.</em>",
        "intro":
            "Studio Veterinario Petro es un estudio asociado "
            "fundado en 2008 por Marco Petro junto con dos colegas "
            "formados en la Università di Padova. Tres veterinarios, "
            "una sola historia clínica compartida por cada paciente, "
            "una sola firma al pie de cada plan de cuidado. "
            "Disponibilidad nocturna bajo llamada para los pacientes "
            "registrados en historia.",
        "history": [
            ("2008",
             "Marco Petro abre el estudio en Via Belzoni con un "
             "solo consultorio y una asistente. Setenta y cinco "
             "animales en historia en el primer año."),
            ("2012",
             "Incorporación de la Dra. Anna Bressan como segunda "
             "veterinaria asociada · especialización en animales "
             "exóticos (conejo, hurón, cobaya, pequeños reptiles)."),
            ("2015",
             "Apertura de la sala quirúrgica con anestesia "
             "inhalatoria de isoflurano y monitorización "
             "multiparamétrica. Puesta en marcha de la cirugía "
             "laparoscópica para las esterilizaciones."),
            ("2018",
             "Adquisición del ecógrafo Esaote MyLab Omega y del Rx "
             "digital Carestream. Todo el diagnóstico por imagen "
             "pasa a realizarse en la sede."),
            ("2023",
             "Incorporación del Dr. Tommaso Zen como tercer "
             "asociado · especialización en oncología veterinaria y "
             "cirugía reconstructiva. El estudio cierra el año con "
             "4.200 animales en historia."),
        ],
        "studio_image": _STUDIO_IMAGE,
        "studio_image_caption": "Sala de consulta · Via Belzoni 71 · Padova",
        "method_title": "El método Petro",
        "method_paragraphs": [
            "La medicina veterinaria de pequeños animales no se "
            "parece a la medicina humana por una razón: el paciente "
            "no habla. El gato que empieza a beber el triple de lo "
            "normal ya tiene una insuficiencia renal a mitad de "
            "camino. El perro que cojea en días alternos ya tiene "
            "una artrosis avanzada. Por eso en Petro la medicina "
            "preventiva no es un servicio adicional: es el primer "
            "capítulo de toda historia clínica y, para muchos "
            "pacientes, también el único que realmente hace falta.",
            "La historia clínica es una sola — la misma para los "
            "tres asociados — porque un animal no es el paciente de "
            "un solo veterinario, es el paciente del estudio. "
            "Cuando Anna detecta una neoformación cutánea "
            "sospechosa durante la vacunación, lo señala a Tommaso "
            "para la extirpación quirúrgica en el mismo documento "
            "clínico. Sin cuidados fragmentados, sin informes que "
            "se pierden entre colegas.",
            "Los costes están declarados para los conceptos de "
            "rutina (revisión preventiva, vacunas, esterilización, "
            "ecografía, diagnóstico de base). Para los planes "
            "estructurados — terapia oncológica, rehabilitación "
            "postraumática, cirugía ortopédica compleja — el "
            "presupuesto se personaliza tras una valoración clínica "
            "completa, pero siempre se entrega por escrito y "
            "firmado al pie.",
        ],
        "values_label":   "Valores del estudio",
        "values_heading": "Cuatro compromisos, <em>escritos en la historia.</em>",
        "values": [
            ("Medicina preventiva siempre",
             "La revisión preventiva anual es el punto de partida "
             "de toda relación con el paciente. Nunca una "
             "intervención no urgente sin anamnesis completa."),
            ("Una sola historia",
             "Tres veterinarios comparten la misma historia "
             "clínica por cada animal. Ningún informe perdido, "
             "ningún seguimiento omitido entre colegas."),
            ("Costes declarados",
             "Tarifas escritas para los conceptos de rutina. "
             "Presupuesto en PDF firmado para cada plan complejo "
             "antes del inicio de los tratamientos."),
            ("Disponibilidad para los propios pacientes",
             "Disponibilidad nocturna 24/7 en el número directo "
             "del doctor Petro para los animales ya registrados en "
             "historia. Ningún paciente abandonado a su suerte."),
        ],
        "cta_heading":
            "El primer paso es siempre <em>una revisión preventiva de una hora.</em>",
        "cta_primary_label":   "Conozca a los veterinarios",
        "cta_secondary_label": "Reserve la primera consulta",
        "press_label": "Publicado en",
        "press": ["Veterinaria Italiana", "SCIVAC Bulletin", "Il Mondo del Cane",
                  "QuattroZampe Mondadori", "Corriere Animali"],
    },

    # ─── VISITE (services) ─────────────────────────────────────
    "visite": {
        "eyebrow":  "Consultas e intervenciones",
        "headline": "Cuatro familias de intervención, <em>una sola historia por animal.</em>",
        "intro":
            "El listado completo de los recorridos de medicina "
            "preventiva y clínica disponibles en la sede. Los "
            "costes indicados corresponden a los conceptos de "
            "rutina; para planes estructurados el presupuesto se "
            "redacta tras una valoración clínica completa.",
        "service_image": _SERVICE_IMAGE,
        "service_image_caption": "Auscultación cardiopulmonar · revisión preventiva",
        # Treatments — 4-tuples (name, meta, desc, price) per
        # specialist services.html:121 unpacking contract.
        "treatments": [
            ("Revisión preventiva anual perro/gato",
             "40 min · con cita previa",
             "Anamnesis completa, peso y Body Condition Score, "
             "auscultación cardiopulmonar, palpación abdominal, "
             "control de la cavidad oral, inspección de piel y "
             "pelaje, palpación de ganglios linfáticos, "
             "verificación del calendario vacunal y "
             "antiparasitario.",
             "65 €"),
            ("Cribado geriátrico (≥ 7 años)",
             "60 min · semestral",
             "Revisión completa + análisis hematoquímicos "
             "(hemograma, función renal y hepática, electrolitos, "
             "T4 en el gato), presión arterial, ecografía "
             "abdominal orientativa. Indicado para perro y gato a "
             "partir de los siete años.",
             "95 €"),
            ("Vacuna perro DA2PPi-L (anual)",
             "cita previa · 30 min",
             "Vacuna combinada moquillo, adenovirus, parvovirus, "
             "parainfluenza, leptospirosis cuatro cepas (L4). "
             "Calendario WSAVA, cartilla sanitaria actualizada en "
             "la sede.",
             "45 €"),
            ("Vacuna gato FRCP + FeLV",
             "cita previa · 30 min",
             "Vacuna combinada rinotraqueítis, calicivirus, "
             "panleucopenia + vacuna leucemia felina (FeLV). Para "
             "gatos que viven en casa solo FRCP trienal tras "
             "refuerzo, coste 40 €.",
             "55 €"),
            ("Esterilización gata por laparoscopia",
             "intervención · ingreso diurno",
             "Ovariectomía mínimamente invasiva con tres accesos "
             "de 5 mm, anestesia inhalatoria de isoflurano, "
             "monitorización multiparamétrica, suturas "
             "subcuticulares reabsorbibles. Alta en el mismo día.",
             "320 €"),
            ("Esterilización perra < 20 kg (laparoscopia)",
             "intervención · ingreso diurno",
             "Ovariectomía por laparoscopia con tres accesos "
             "abdominales, anestesia inhalatoria, analgesia "
             "multimodal postoperatoria, alta en el mismo día.",
             "480 €"),
            ("Ecografía abdominal completa",
             "30 min · con cita previa",
             "Esaote MyLab Omega · valoración de hígado, bazo, "
             "riñones, vejiga, paredes gastrointestinales, "
             "ganglios mesentéricos, próstata. Informe entregado "
             "en el día.",
             "95 €"),
            ("Ecocardiografía",
             "45 min · con cita previa",
             "Estudio ecográfico de las cámaras cardíacas, "
             "valoración de las válvulas, medición de la fracción "
             "de eyección y la contractilidad. Indicado pre"
             "anestesia en pacientes geriátricos o razas "
             "predispuestas (Cavalier King Charles, Boxer, Maine "
             "Coon).",
             "130 €"),
        ],
        "footnote_heading": "Lo que no hacemos en la sede",
        "footnote":
            "Cardiología intervencionista, neurocirugía, "
            "ortopedia reconstructiva compleja, obstetricia "
            "equina. Para estos casos derivamos al Ospedale "
            "Veterinario de la Università di Padova (Legnaro), "
            "con el que tenemos un convenio directo y una vía "
            "preferente para nuestros pacientes.",
        "cta_heading":
            "¿Desea reservar una <em>revisión preventiva o un control?</em>",
        "cta_primary_label":   "Reservar una consulta",
        "cta_secondary_label": "Conozca a los veterinarios",
    },

    # ─── MEDICI (team) ─────────────────────────────────────────
    "medici": {
        "eyebrow":  "Los veterinarios",
        "headline": "Tres veterinarios asociados, <em>tres especializaciones complementarias.</em>",
        "intro":
            "Tres veterinarios comparten el estudio desde 2008 "
            "(Marco), 2012 (Anna) y 2023 (Tommaso). Tres "
            "especializaciones complementarias cubren medicina "
            "preventiva e interna, animales exóticos y cirugía "
            "reconstructiva. Una sola historia clínica por cada "
            "paciente.",
        "doctors": [
            {
                "name":  "Dr. Marco Petro",
                "role":  "Director sanitario",
                "specialty": "Medicina interna · cirugía de tejidos blandos",
                "bio":
                    "Licenciatura Università di Padova 2000. "
                    "Royal Veterinary College London 2002-2004. "
                    "Cornell University Vet School (NY, EE. UU.) "
                    "estancia 2006. Inscripción OMV Padova 1428 "
                    "desde 2001. Director sanitario desde 2008. "
                    "Miembro SCIVAC y ANMVI.",
                "portrait": _CHIEF_PORTRAIT,
                "year_label": "Desde",
                "year": "2008",
            },
            {
                "name":  "Dra. Anna Bressan",
                "role":  "Veterinaria asociada",
                "specialty": "Animales exóticos · conejo, hurón, cobaya, reptiles",
                "bio":
                    "Licenciatura Università di Padova 2010. "
                    "Máster en Medicina de los Animales Exóticos "
                    "en Cremona (Università di Milano) 2011-2012. "
                    "Miembro AAEMV (Associazione Italiana "
                    "Veterinari per Animali Esotici). Dirige la "
                    "sección de exóticos del estudio desde 2012, "
                    "con foco en medicina preventiva de pequeños "
                    "animales exóticos.",
                "portrait":
                    "https://images.pexels.com/photos/6235113/pexels-photo-6235113.jpeg"
                    "?auto=compress&cs=tinysrgb&w=900&h=1200&fit=crop",
                "year_label": "Desde",
                "year": "2012",
            },
            {
                "name":  "Dr. Tommaso Zen",
                "role":  "Veterinario asociado",
                "specialty": "Oncología veterinaria · cirugía reconstructiva",
                "bio":
                    "Licenciatura Università di Bologna 2014. "
                    "Especialización en Oncología Veterinaria en "
                    "la Universidad de Madrid 2017-2019. "
                    "Publicaciones en Journal of Small Animal "
                    "Practice (2018) y Veterinary Surgery (2020). "
                    "Dirige la sección de cirugía oncológica del "
                    "estudio desde 2023.",
                "portrait":
                    "https://images.pexels.com/photos/6234600/pexels-photo-6234600.jpeg"
                    "?auto=compress&cs=tinysrgb&w=900&h=1200&fit=crop",
                "year_label": "Desde",
                "year": "2023",
            },
        ],
        "portrait_city": "Padova · Borgo Trento",
    },

    # ─── PUBBLICAZIONI (blog_list) ─────────────────────────────
    "pubblicazioni": {
        "eyebrow":  "Diario clínico del estudio",
        "headline": "Notas de trabajo <em>desde la sala de consulta.</em>",
        "intro":
            "Breves apuntes de los tres veterinarios sobre los "
            "protocolos clínicos en uso, sobre los casos más "
            "representativos del año, sobre las vacunas y las "
            "profilaxis de temporada. Lectura reservada a los "
            "propietarios de pacientes en historia y a los colegas.",
        "lead_image": _LEAD_IMAGE,
        "footer_strap": "Studio Veterinario Petro · El diario clínico",
        "empty_body_fallback_paragraphs": [
            "Artículo en preparación editorial. La publicación "
            "íntegra estará disponible en breve, escrita "
            "personalmente por uno de los tres veterinarios "
            "asociados.",
            "Este marcador describe la voz del Diario Clínico: "
            "breves notas de trabajo, reflexiones sobre los "
            "protocolos preventivos, relatos de casos clínicos "
            "representativos. Nunca más de dos mil palabras, nunca "
            "menos de quinientas.",
        ],
    },

    "posts": [
        {
            "slug":     "calendario-vaccinale-2026",
            "kicker":   "Vacunaciones en curso",
            "title":    "El calendario vacunal del estudio · actualización 2026",
            "date":     "8 de octubre de 2026",
            "read_min": 4,
            "author":   "Dr. Marco Petro",
            "cover_image": _LEAD_IMAGE,
            "lede":
                "WSAVA publicó en septiembre las nuevas directrices "
                "sobre las vacunas core para perro y gato. Qué "
                "cambia desde octubre de 2026 en el calendario de "
                "refuerzo de nuestros pacientes.",
            "body": [
                ("p", "Las directrices WSAVA 2026 confirman la "
                      "frecuencia anual para las vacunas core perro "
                      "(DA2PPi-L) y consolidan el paso a trienal "
                      "tras refuerzo para las vacunas core gato "
                      "(FRCP) en los gatos que viven en ambiente "
                      "doméstico cerrado. Para los gatos con acceso "
                      "al exterior la frecuencia sigue siendo anual "
                      "también para FRCP."),
                ("h2", "Qué cambia en la profilaxis"),
                ("p", "La leptospirosis cuatro cepas (L4) sigue "
                      "siendo core anual para el perro en el "
                      "ambiente urbano padovano — la incidencia en "
                      "las últimas temporadas se ha mantenido "
                      "estable pero no en descenso. Para el gato "
                      "en ambiente doméstico recalibramos a trienal "
                      "el FeLV tras el refuerzo del primer año, "
                      "mientras que para los gatos free-roaming el "
                      "FeLV sigue siendo anual."),
                ("h2", "Qué hacemos desde octubre"),
                ("p", "Los propietarios de los pacientes en "
                      "historia recibirán por WhatsApp el plan "
                      "vacunal actualizado. Para los nuevos "
                      "pacientes el calendario se construye en la "
                      "primera revisión preventiva sobre la base de "
                      "raza, edad, entorno de vida y contacto con "
                      "otros animales."),
            ],
        },
        {
            "slug":     "sterilizzazione-laparoscopia-perche",
            "kicker":   "Cirugía",
            "title":    "Por qué preferimos la laparoscopia para la esterilización",
            "date":     "25 de septiembre de 2026",
            "read_min": 5,
            "author":   "Dr. Tommaso Zen",
            "cover_image":
                "https://images.pexels.com/photos/7470769/pexels-photo-7470769.jpeg"
                "?auto=compress&cs=tinysrgb&w=1200&h=800&fit=crop",
            "lede":
                "Desde 2015 el estudio realiza la esterilización de "
                "gatas y perras por laparoscopia mínimamente "
                "invasiva. He aquí por qué es nuestro estándar y "
                "cuándo seguimos haciendo la intervención "
                "tradicional.",
            "body": [
                ("p", "La esterilización por laparoscopia supone "
                      "tres accesos abdominales de 5 mm en lugar de "
                      "la incisión tradicional de 4-7 cm. La "
                      "diferencia no es estética: es ante todo "
                      "fisiológica. Dolor postoperatorio reducido, "
                      "vuelta a la normalidad en 48 horas, riesgo "
                      "de complicaciones infecciosas reducido, "
                      "ingreso diurno en lugar de una noche."),
                ("h2", "Cuándo seguimos haciendo la cirugía tradicional"),
                ("p", "Tres situaciones clínicas. Primera: perras "
                      "por encima de los 35 kg, en las que el "
                      "acceso laparoscópico se vuelve técnicamente "
                      "complejo (el ovario es profundo, el espacio "
                      "operatorio limitado). Segunda: piómetra "
                      "(infección uterina) — el útero debe "
                      "extraerse íntegro y el acceso abierto "
                      "también es válido. Tercera: tumores "
                      "ováricos, por la misma razón."),
                ("h2", "Las cifras del estudio"),
                ("p", "Desde 2015 hasta hoy hemos realizado unas "
                      "1.400 esterilizaciones por laparoscopia. "
                      "Tasa de complicaciones mayores por debajo "
                      "del 1 %. Tasa de complicaciones menores "
                      "(seromas, edemas locales) en torno al 3 %. "
                      "Índice de satisfacción del propietario "
                      "(cuestionario de seguimiento a siete días) "
                      "por encima del 95 %."),
            ],
        },
    ],

    # ─── CONTATTI ──────────────────────────────────────────────
    "contatti": {
        "eyebrow":  "Contacto y sede",
        "headline": "Tres canales, <em>una sola secretaría.</em>",
        "intro":
            "Para citas de rutina se reserva desde el formulario "
            "en línea o por teléfono en horario de apertura. Para "
            "urgencias, el número de disponibilidad está activo "
            "24/7 para los pacientes en historia.",
        # Blocks — 3-tuples (label, value, sub) per specialist
        # contact.html:105 unpacking contract.
        "blocks": [
            ("Secretaría",
             "+39 049 6731 220",
             "Lun – Vie · 8:00 – 20:00 · Sáb 9:00 – 13:00"),
            ("Disponibilidad nocturna",
             "+39 333 410 7726",
             "24/7 · solo para pacientes ya registrados en historia"),
            ("Correo electrónico",
             "studio@studiopetro.it",
             "Respuesta en un plazo de 24 h en horario de apertura"),
            ("Sede",
             "Via Belzoni 71 · 35121 Padova",
             "Borgo Trento · 6 minutos desde la Estación Central"),
        ],
        "form_title": "Escríbanos",
        "form_intro":
            "Para citas de rutina utilice el formulario Reservar "
            "una consulta. Este formulario está pensado para "
            "consultas generales, solicitud de copia de la historia "
            "clínica, segunda opinión o preguntas sobre los "
            "protocolos.",
        "form_placeholders": {
            "name":    "Nombre y apellidos",
            "email":   "Correo electrónico",
            "phone":   "Teléfono",
            "subject": "Asunto",
            "message": "¿En qué podemos ayudarle? Indique también el nombre y la especie del animal.",
        },
        "form_helpers": {
            "name":    "Se utilizará para encabezar la eventual respuesta.",
            "email":   "Responderemos en un plazo de 24 horas en horario de apertura.",
            "phone":   "Solo para solicitar llamadas de vuelta.",
            "subject": "Ejemplo: «solicitud de segunda opinión» o «copia de historia clínica».",
        },
        "form_consent":
            "Acepto el tratamiento de los datos conforme al RGPD. Política de privacidad disponible en la sede.",
        "form_submit_note":
            "Para urgencias clínicas en pacientes registrados en "
            "historia, llame al número de disponibilidad 24/7. "
            "Este formulario no se monitoriza fuera del horario de "
            "apertura.",
        "hours_heading": "Horario de apertura",
        # hours — 3-tuples (day, am, pm) per specialist contact.html:175.
        "hours": [
            ("Lun – Vie", "8:00 – 13:00", "14:30 – 20:00"),
            ("Sábado",    "9:00 – 13:00", "cerrado"),
            ("Domingo",   "cerrado",      "disponibilidad bajo llamada"),
        ],
        "transport_heading": "Cómo llegar",
        "transport": [
            ("Tren",         "Estación Central de Padova · 6 minutos a pie"),
            ("Coche",        "Salida Padova Est · 12 minutos en coche"),
            ("Tranvía",      "SIR1 parada Borgo Trento · 2 minutos a pie"),
            ("Aparcamiento", "Aparcamiento Borgo Trento gratuito · 80 metros del estudio"),
        ],
    },

    # ─── RICHIEDI-VISITA (appointment) ─────────────────────────
    "richiedi-visita": {
        "eyebrow":  "Reservar una consulta",
        "headline": "Una revisión preventiva, <em>cuarenta minutos.</em>",
        "intro":
            "Reserve en línea la primera revisión preventiva de "
            "su animal. La secretaría confirma la cita en un plazo "
            "de 24 horas en horario de apertura. Para urgencias "
            "llame al número de disponibilidad.",
        "process_label": "Cómo funciona",
        "process_heading": "Tres pasos, <em>una sola consulta.</em>",
        # process — 3-tuples (num, title, blurb) per specialist
        # appointment.html:97 unpacking contract.
        "process": [
            ("01", "Rellene el formulario",
             "Indique el nombre del animal, la especie, la raza, "
             "la edad, el motivo de la consulta. Las eventuales "
             "pruebas previas pueden adjuntarse o llevarse al "
             "estudio."),
            ("02", "Confirmación en 24 horas",
             "La secretaría se pone en contacto en un plazo de "
             "24 horas para confirmar fecha y hora. Para consultas "
             "urgentes (cojera repentina, inapetencia, vómitos "
             "recurrentes) llame directamente a la secretaría."),
            ("03", "Primera consulta de 60 minutos",
             "Anamnesis, examen físico completo, diagnóstico de "
             "base si está indicado, plan de cuidado escrito. El "
             "presupuesto se entrega también en PDF."),
        ],
        "form_title": "Formulario de reserva",
        "form_band_side_note":
            "Revisión preventiva — 40 minutos — 65 € (perro/gato), "
            "75 € (exóticos).",
        "form_band_side_note_small":
            "Los costes están declarados para los conceptos de "
            "rutina. Para planes estructurados el presupuesto se "
            "redacta tras la primera consulta.",
        "form_fields": [
            {
                "name":    "owner_name",
                "label":   "Nombre del propietario",
                "type":    "text",
                "required": True,
                "placeholder": "Nombre y apellidos del propietario",
            },
            {
                "name":    "email",
                "label":   "Correo electrónico",
                "type":    "email",
                "required": True,
                "placeholder": "Para la confirmación de la cita",
            },
            {
                "name":    "phone",
                "label":   "Teléfono",
                "type":    "tel",
                "required": True,
                "placeholder": "Para eventuales contactos rápidos",
            },
            {
                "name":    "pet_name",
                "label":   "Nombre del animal",
                "type":    "text",
                "required": True,
                "placeholder": "Ej. Luna · Briciola · Pepe",
            },
            {
                "name":    "pet_species",
                "label":   "Especie y raza",
                "type":    "text",
                "required": True,
                "placeholder": "Ej. Gato · Conejo enano · Perro Border Collie",
            },
            {
                "name":    "pet_age",
                "label":   "Edad del animal",
                "type":    "text",
                "required": True,
                "placeholder": "Ej. 8 años · 6 meses",
            },
            {
                "name":    "visit_reason",
                "label":   "Motivo de la consulta",
                "type":    "textarea",
                "required": True,
                "placeholder":
                    "Ej. Revisión preventiva anual · control "
                    "postoperatorio · dudas sobre la alimentación. "
                    "Para urgencias llame al número de "
                    "disponibilidad.",
            },
        ],
        "submit_label": "Enviar la solicitud",
        "consent":
            "Acepto el tratamiento de los datos personales y "
            "sanitarios de mi animal conforme al RGPD. La historia "
            "clínica será compartida entre los tres veterinarios "
            "asociados del estudio.",
        "footnote":
            "Para urgencias clínicas fuera del horario de "
            "apertura (cojera repentina, vómitos recurrentes, "
            "postración, traumatismo), llame al número de "
            "disponibilidad 24/7: +39 333 410 7726. Para pacientes "
            "aún no registrados en historia derivamos al Ospedale "
            "Veterinario de Legnaro o a la Clinica San Marco de "
            "Veggiano.",
    },
}
