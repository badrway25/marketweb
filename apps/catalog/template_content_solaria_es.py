"""Solaria — Business Coaching · Spanish (peninsular) locale content tree.

Phase X.4 Pass B · 2026-04-26 · Multilingual completion pass.

Mirrors the shape of `SOLARIA_CONTENT_IT` exactly. Voice register:
warm-professional, usted/ustedes throughout (peninsular Spanish),
ICF-aligned. Reference voices: Harvard Business Review en español,
Cinco Días sección Directivos, Capital Humano. Adulto que habla a
adulto. Sin jerga de desarrollo personal, sin promesas de
transformación.

Voice anchor (CS-EXEC-01 · preserved verbatim-in-translation):
    «El coaching no es terapia y no es consultoría. No le decimos
     qué hacer y no analizamos el pasado para comprenderlo.
     Trabajamos sobre las decisiones que está a punto de tomar, con
     un método y una cadencia. Un recorrido tiene un comienzo
     declarado y un final declarado. Al final, si ha funcionado, es
     más autónomo en sus decisiones — no más dependiente de un coach.»

Italian normative references and proper nouns preserved (ICF,
EMCC, ODCEC, GROW, Co-Active, Immunity to Change, Codice
Deontologico ICF §2.4, Reg. UE 679/2016 ≈ RGPD europeo).
Direcciones italianas, números de colegiado, formato telefónico
italiano, importes en euros y años se mantienen sin cambios.
Antipatrones prohibidos (briefing §13): «Desbloquea tu
potencial», «Transforma tu vida en N días», «Versión mejor de ti
mismo», «Mentalidad ganadora», citas Einstein/Jung/Gandhi/Steve
Jobs, metáforas de cima de montaña.
"""
from __future__ import annotations

from typing import Any


from apps.catalog.template_content_solaria import (  # noqa: E402
    _POOL_HERO,
    _POOL_FEATURE,
    _POOL_PORTRAIT_A,
    _POOL_PORTRAIT_B,
    _POOL_DETAIL,
    _POOL_AMBIENT,
)


SOLARIA_CONTENT_ES: dict[str, Any] = {
    "pages": [
        {"slug": "home",       "label": "Despacho",   "kind": "home"},
        {"slug": "il-coach",   "label": "La coach",   "kind": "about"},
        {"slug": "percorsi",   "label": "Recorridos", "kind": "services"},
        {"slug": "casi",       "label": "Casos",      "kind": "case_study_list"},
        {"slug": "contatti",   "label": "Contacto",   "kind": "contact"},
    ],

    "site": {
        "logo_initial": "S",
        "logo_word":    "Solaria",
        "tag":          "Business coaching · Milán Isola · ICF-PCC desde 2017",
        "phone":        "+39 02 3663 4712",
        "email":        "discovery@solariacoaching.it",
        "address":      "Via Thaon di Revel 21 · 20159 Milán",
        "hours_compact": "Lun – Vie · 9:00 – 19:00 · con cita previa",
        "hours_footer_rows": [
            "Sesiones vespertinas para coachees internacionales (UTC+5 / UTC-5)",
            "Sábado y domingo · cerrado",
        ],
        "license":      "Professional Certified Coach (PCC) · International Coaching Federation (ICF)",
        "footer_intro":
            "Despacho de coaching profesional para empresarios, "
            "directivos en transición y equipos de mando intermedio. "
            "Método declarado, cadencia acordada, comienzo y final del "
            "recorrido escritos en el contrato — ninguna transformación "
            "prometida, ninguna dependencia buscada. Sede en Milán, "
            "sesiones presenciales y en línea.",
        "foot_studio":   "El despacho",
        "foot_pages":    "Secciones",
        "foot_contact":  "Contacto",
        "foot_offices":  "Sede",
        "offices_footer_rows": [
            "Milán · Isola",
        ],
        "case_practice_label":     "Área",
        "case_year_label":         "Año",
        "case_duration_label":     "Duración",
        "case_lead_label":         "Coach",
        "case_lead_partner_label": "Coach",
        "case_team_label":         "Recorrido y patrocinador",
        "case_timeline_label":     "Cronograma",
    },

    # ─── HOME ───────────────────────────────────────────────────
    "home": {
        "eyebrow":     "Business coaching · Milán Isola · ICF-PCC desde 2017",
        "headline":    "El coaching no es <em>terapia</em>, ni es <em>consultoría</em>.",
        "intro":
            "Recorridos de coaching para empresarios, directivos en "
            "transición y mandos intermedios. Método declarado, "
            "cadencia acordada, comienzo y final escritos en el "
            "contrato — ninguna transformación en treinta días.",
        "primary_cta":   "Reservar una discovery call",
        "primary_href":  "contatti",
        "secondary_cta": "El método",
        "secondary_href":"il-coach",

        "hero_image":              _POOL_HERO,
        "hero_image_credit_left":  ("Reportaje",   "Sesión executive 1:1"),
        "hero_image_credit_right": ("Despacho",    "Solaria · Milán Isola"),
        "hero_meta_strip": [
            ("Sesión",           "60 minutos · cadencia quincenal"),
            ("Discovery call",   "20 – 30 minutos · gratuita"),
            ("Supervisión",      "ICF-MCC continua desde 2019"),
        ],

        "pillars_label":   "Recorridos",
        "pillars_heading": "Tres formatos, un recorrido escrito",
        "pillars_intro":
            "El mismo método para cada formato: contrato inicial con "
            "objetivo medible, sesiones a cadencia acordada, "
            "re-contracting a mitad del recorrido, cierre con "
            "verificación, follow-up a tres meses incluido en los "
            "honorarios.",
        "pillars": [
            ("01", "Executive 1:1",
             "Ocho sesiones de sesenta minutos a cadencia quincenal "
             "para directivos en transición de función, recién "
             "promovidos, o en preparación de un cambio de perímetro. "
             "Marcos de referencia: Co-Active + Immunity to Change."),
            ("02", "Team coaching",
             "Seis sesiones con el equipo (cinco a diez personas) más "
             "re-contracting con el patrocinador corporativo a mitad "
             "de recorrido. Para mando intermedio en crecimiento o "
             "tras reorganización. Marco de referencia: GROW grupal."),
            ("03", "Grupo corporativo",
             "Masterclass de un día + ocho sesiones individuales para "
             "tres a ocho personas del mismo cliente corporativo. "
             "Objetivos individuales ligados a objetivos de sistema, "
             "follow-up trimestral con el patrocinador."),
        ],

        "kpi_heading": "Doce años de práctica certificada",
        "kpi_strip": [
            ("12",        "años de práctica ICF"),
            ("2.400+",    "horas de coaching impartidas"),
            ("160+",      "coachees acompañados desde 2014"),
            ("100 %",     "recorridos con follow-up a tres meses"),
        ],

        "sectors_label": "Perfiles de los coachees",
        "sectors": [
            "CEO recién promovidos",
            "Directores de función en transición",
            "Mandos intermedios en crecimiento",
            "Equipos de liderazgo tras reorganización",
            "Socios de despachos profesionales",
        ],

        "trust_label":   "Empresas patrocinadoras 2023 — 2025 · nombres anonimizados según Código ICF §2.4",
        "trust_logos":   [
            "SCALE-UP FINTECH · SERIE B",
            "GRUPO INDUSTRIAL COTIZADO",
            "DESPACHO DE ABOGADOS ASOCIADO",
            "FABRICANTE DE DISPOSITIVOS MÉDICOS",
            "FUNDACIÓN EDUCATIVA",
            "BOUTIQUE DE SERVICIOS PROFESIONALES",
        ],

        "leadership_label":   "La coach",
        "leadership_heading": "Quién se sienta al otro lado de la mesa",
        "leadership_intro":
            "Una coach fundadora y una coach asociada. Cada recorrido "
            "lo conduce personalmente la misma coach desde el inicio "
            "hasta el cierre — ningún relevo júnior-sénior, ninguna "
            "rotación silenciosa.",
        "leadership": [
            {
                "name":  "Dra. Giulia Loreti",
                "role":  "Coach fundadora · ICF-PCC · EMCC Senior Practitioner",
                "portrait": _POOL_PORTRAIT_A,
                "bio":
                    "Quince años en RR. HH. corporativo como "
                    "responsable del desarrollo directivo en un grupo "
                    "industrial cotizado, antes de dedicarse "
                    "íntegramente al coaching en 2014. Professional "
                    "Certified Coach (PCC) acreditada por la "
                    "International Coaching Federation desde 2017. "
                    "Supervisión continua con una sénior ICF-MCC desde 2019.",
                "credentials": [
                    "ICF-PCC n.º 011749 (desde 2017 · renovada 2023)",
                    "EMCC Senior Practitioner (desde 2020)",
                    "Coach Training Institute · cursus Co-Active (2014)",
                    "Università Bocconi — Psicología del Trabajo '02",
                ],
            },
            {
                "name":  "Dra. Martina Erriquez",
                "role":  "Coach asociada · ICF-ACC · en recorrido PCC",
                "portrait": _POOL_PORTRAIT_B,
                "bio":
                    "Ocho años como consultora de desarrollo "
                    "organizativo antes de iniciar el recorrido "
                    "coaching en 2020. Associate Certified Coach "
                    "(ACC) acreditada desde 2022, actualmente en "
                    "recorrido de certificación PCC (finalización "
                    "prevista en 2027). Supervisada mensualmente "
                    "por Giulia Loreti y por una supervisora EMCC externa.",
                "credentials": [
                    "ICF-ACC n.º 028914 (desde 2022)",
                    "Co-Active Training Institute · Fundamentals + Intermediate (2020-2022)",
                    "Università Cattolica — Psicología del Trabajo '12",
                    "Supervisión mensual ICF + EMCC",
                ],
            },
        ],

        "cases_label":   "Casos",
        "cases_heading": "Tres recorridos, tres objetivos medidos",
        "cases_intro":
            "Casos concluidos en los últimos tres años — coachees "
            "anonimizados según el Código ICF §2.4, objetivos y "
            "resultados reales. Reference call con el patrocinador "
            "corporativo disponible bajo NDA recíproco para los "
            "recorridos corporativos.",

        "cta_label":     "¿Es el momento adecuado?",
        "cta_heading":   "Veinte minutos para comprobar si Solaria es para usted",
        "cta_intro":
            "Ninguna sesión de coaching gratuita, ningún diagnóstico, "
            "ningún presupuesto en frío. Una conversación honesta "
            "sobre su objetivo y la adecuación del coaching a su "
            "necesidad. Si no es coaching, se lo decimos — e "
            "indicamos al profesional adecuado.",
        "cta_primary":   "Reservar una discovery call",
        "cta_primary_href": "contatti",
        "cta_secondary": "El método en cinco pasos",
        "cta_secondary_href": "il-coach",
    },

    # ─── IL COACH ───────────────────────────────────────────────
    "il-coach": {
        "eyebrow":   "La coach · 2014 — 2026",
        "headline":  "Un método <em>declarado</em>, doce años de práctica certificada.",
        "intro":
            "Solaria nace en 2014, cuando Giulia Loreti deja un puesto "
            "de responsable de RR. HH. corporativo para dedicarse "
            "íntegramente al coaching. El primer recorrido Solaria — "
            "un team coaching para una scale-up fintech milanesa "
            "recién constituida — arranca en noviembre del mismo año. "
            "En 2020 se incorpora Martina Erriquez como coach asociada.",

        "history_label":   "El método · recorrido tipo en cinco pasos",
        "history_heading": "Cinco pasos, una cadencia acordada",
        "history_intro":
            "El recorrido Solaria sigue la misma estructura "
            "independientemente del formato (1:1 executive, equipo, "
            "grupo corporativo). Estos cinco pasos están escritos en "
            "el contrato de coaching que el coachee firma al inicio "
            "del recorrido.",
        "history": [
            ("01", "Discovery call",
             "Veinte a treinta minutos gratuitos, sin compromiso. "
             "Verificamos si el objetivo entra en el ámbito del "
             "coaching, si Solaria es el despacho adecuado, "
             "comentamos un presupuesto orientativo. Sin obligación al final."),
            ("02", "Contrato inicial",
             "Primera reunión de noventa minutos remunerada. "
             "Definición del objetivo medible (marco SMART), "
             "elección del marco de conducción (GROW · Co-Active · "
             "Immunity to Change), firma del contrato de coaching "
             "que precisa número de sesiones, cadencia, "
             "confidencialidad y referencia al Código Deontológico ICF."),
            ("03", "Sesiones regulares",
             "Sesiones de 60 minutos a la cadencia acordada "
             "(habitualmente quincenal para executive 1:1, mensual "
             "para equipos, trimestral para follow-up). Cada sesión "
             "se cierra con un commitment escrito que el coachee "
             "verifica de forma autónoma antes de la siguiente."),
            ("04", "Re-contracting a mitad del recorrido",
             "A mitad del recorrido, sesión de re-contracting con "
             "el coachee (y con el patrocinador corporativo si el "
             "coaching está patrocinado por la empresa). Se revisa "
             "el objetivo inicial, se deciden ajustes eventuales, "
             "se decide continuar o cerrar antes. Sin obligación de continuar."),
            ("05", "Cierre y follow-up",
             "Sesión final de consolidación con verificación "
             "explícita del resultado frente al objetivo inicial. "
             "Follow-up programado a tres meses del cierre — una "
             "sesión de sesenta minutos para verificar la "
             "durabilidad del cambio. El follow-up está incluido "
             "en los honorarios del recorrido, nunca se factura aparte."),
        ],

        "values_label":   "Principios",
        "values_heading": "Cuatro principios <em>no negociables</em>",
        "values_intro":
            "Cuatro reglas que distinguen un recorrido Solaria de un "
            "coaching genérico. Están escritas en el contrato firmado "
            "al inicio del recorrido, y el coachee puede invocar su "
            "aplicación en cualquier momento.",
        "values": [
            ("01", "El coaching no es terapia y no es consultoría",
             "No diagnosticamos trastornos psicológicos (no somos "
             "psicoterapeutas). No proponemos soluciones empresariales "
             "(no somos consultoras estratégicas). Si en la discovery "
             "call o durante el recorrido se constata que la "
             "necesidad encaja en una de las otras dos disciplinas, "
             "lo declaramos explícitamente y derivamos a un "
             "profesional de la disciplina adecuada — aunque suponga "
             "cerrar la relación con Solaria."),
            ("02", "Confidencialidad sin excepciones",
             "Todo lo que ocurre en sesión queda en sesión. Los "
             "patrocinadores corporativos reciben únicamente "
             "informes agregados acordados en el contrato inicial — "
             "nunca contenidos específicos. Sin excepciones salvo "
             "obligación legal, que se explica al coachee antes de "
             "cualquier comunicación a terceros."),
            ("03", "Recorrido acotado, autonomía como objetivo",
             "Cada recorrido tiene un número de sesiones declarado "
             "en el contrato inicial. No ofrecemos suscripciones "
             "ilimitadas ni coaching perpetuo. Al final del "
             "recorrido, si ha funcionado, el coachee es más "
             "autónomo en sus decisiones — no más dependiente de un coach."),
            ("04", "Supervisión continua obligatoria",
             "Las dos coaches Solaria están en supervisión continua: "
             "Giulia con una sénior ICF-MCC desde 2019, Martina con "
             "Giulia mensualmente más una supervisora EMCC externa. "
             "La supervisión es el equivalente del control de "
             "calidad en una práctica profesional seria — y su "
             "coste lo asume el despacho, no el coachee."),
        ],

        "team_label":   "Despacho",
        "team_heading": "Dos coaches, una supervisora externa, una sola gobernanza",
        "team_intro":
            "Las personas que siguen el trabajo de Solaria. Las "
            "sesiones de coaching las imparten únicamente Giulia o "
            "Martina; la supervisora externa nunca interactúa con "
            "los coachees, pero verifica la calidad de la práctica "
            "de la coach asociada.",
        "team": [
            {"name": "Dra. Giulia Loreti",
             "role": "Coach fundadora · ICF-PCC · EMCC Senior Practitioner",
             "office": "Milán",
             "bio": "Coaching 1:1 executive y team coaching. "
                    "2.400+ horas impartidas desde 2014. Supervisión con ICF-MCC desde 2019."},
            {"name": "Dra. Martina Erriquez",
             "role": "Coach asociada · ICF-ACC · en recorrido PCC",
             "office": "Milán",
             "bio": "Coaching 1:1 para neo-managers y recorridos de grupo corporativo. "
                    "Supervisión mensual con Giulia + EMCC externa."},
            {"name": "Dra. Elena Mannucci",
             "role": "Supervisora externa · ICF-MCC",
             "office": "Trento · consultora",
             "bio": "Supervisa la práctica de Giulia desde 2019 y la de Martina desde 2022. "
                    "Nunca interactúa con los coachees — verifica la calidad de la práctica."},
            {"name": "Sra. Donatella Rinaldi",
             "role": "Asistente del despacho · back-office",
             "office": "Milán",
             "bio": "Gestión de agendas, facturación, contratación. "
                    "Nunca accede a los contenidos de las sesiones de coaching."},
        ],

        "coordinates_label": "Sede",
        "coordinates": [
            ("Milán",  "Via Thaon di Revel 21 · 20159 · Isola — a 300 metros de la estación MM Garibaldi FS"),
        ],

        "cta_heading": "Discovery call o consulta por correo",
        "cta_intro":
            "La discovery call de veinte a treinta minutos es la vía "
            "canónica para evaluar si un recorrido Solaria es para "
            "usted. Si prefiere plantear una consulta escrita antes "
            "de reservar la llamada, el correo de la secretaría lo "
            "lee Donatella cada mañana y una de nosotras le responde "
            "dentro de la jornada.",
        "cta_primary":  "Reservar una discovery call",
        "cta_primary_href": "contatti",
    },

    # ─── PERCORSI ───────────────────────────────────────────────
    "percorsi": {
        "eyebrow":  "Recorridos de coaching · 2026",
        "headline": "Cuatro recorridos, <em>un solo método</em>.",
        "intro":
            "Cuatro formatos de recorrido, cada uno con su número "
            "de sesiones declarado, su cadencia acordada, su "
            "formato (presencial · en línea · híbrido) y su precio "
            "orientativo. Cada recorrido sigue el mismo método — "
            "contrato inicial, sesiones regulares, re-contracting "
            "a mitad, cierre con verificación, follow-up a tres meses.",

        "svc_duration_label": "Duración típica",
        "svc_leader_label":   "Coach referente",

        "services": [
            {
                "num":   "01",
                "title": "Executive 1:1",
                "blurb":
                    "El formato más solicitado. Ocho sesiones de "
                    "sesenta minutos a cadencia quincenal, objetivo "
                    "medible definido en la primera reunión y "
                    "escrito en el contrato. Para directivos en "
                    "transición de función, recién promovidos, o en "
                    "preparación de un cambio de perímetro. Marcos "
                    "de referencia: Co-Active + Immunity to Change.",
                "scope": [
                    "Contrato inicial con objetivo SMART medible",
                    "Ocho sesiones 60 min · cadencia quincenal",
                    "Re-contracting a mitad (cuarta sesión)",
                    "Cierre con verificación del resultado",
                    "Follow-up 60 min a tres meses incluido",
                ],
                "duration": "16 semanas · 8 sesiones + follow-up",
                "leader":   "Dra. Giulia Loreti",
            },
            {
                "num":   "02",
                "title": "Team coaching",
                "blurb":
                    "Trabajo con equipos de mando intermedio (cinco "
                    "a diez personas). Seis sesiones con el equipo "
                    "más una sesión de re-contracting con el "
                    "patrocinador corporativo a mitad del recorrido. "
                    "Para equipos en crecimiento, integración "
                    "post-reorganización, o preparación de un reto "
                    "específico. Marco de referencia: GROW aplicado al grupo.",
                "scope": [
                    "Contrato inicial tripartito (equipo · patrocinador · coach)",
                    "Seis sesiones 120 min · cadencia mensual",
                    "Re-contracting con patrocinador a mitad del recorrido",
                    "Informe agregado al patrocinador (nunca contenidos específicos)",
                    "Follow-up 90 min a tres meses incluido",
                ],
                "duration": "6 meses · 6 sesiones + re-contracting + follow-up",
                "leader":   "Dra. Giulia Loreti",
            },
            {
                "num":   "03",
                "title": "Grupo corporativo",
                "blurb":
                    "Programa de RR. HH. estructurado para tres a "
                    "ocho personas del mismo cliente corporativo. "
                    "Masterclass de un día al inicio + ocho sesiones "
                    "individuales para cada participante. "
                    "Patrocinador corporativo definido, objetivos "
                    "individuales ligados a objetivos de sistema, "
                    "follow-up trimestral con el patrocinador.",
                "scope": [
                    "Masterclass diaria de apertura (marco + código deontológico)",
                    "Ocho sesiones 1:1 para cada participante",
                    "Cuadro de mando agregado para el patrocinador (KPI acordados)",
                    "Follow-up trimestral con el patrocinador durante los primeros 12 meses",
                    "Presupuesto personalizado según número de participantes",
                ],
                "duration": "6-9 meses · masterclass + 8 sesiones/persona",
                "leader":   "Dra. Giulia Loreti · Dra. Martina Erriquez",
            },
            {
                "num":   "04",
                "title": "Sesión única exploratoria",
                "blurb":
                    "Una sola sesión de noventa minutos, sin "
                    "contrato de recorrido. Para quien quiere "
                    "evaluar el enfoque de coaching sobre un tema "
                    "específico antes de comprometerse en un "
                    "recorrido. Al final, el coachee decide si "
                    "abrir un recorrido executive 1:1 o cerrar la "
                    "relación — sin obligación de continuar.",
                "scope": [
                    "Sesión 90 min con GROW aplicado al tema",
                    "Entregable escrito remitido en 48 horas",
                    "Evaluación honesta: coaching · terapia · consultoría",
                    "Si coaching: presupuesto orientativo para un recorrido",
                    "Si no coaching: derivación al profesional adecuado",
                ],
                "duration": "1 sesión · 90 minutos",
                "leader":   "Dra. Martina Erriquez",
            },
        ],

        "process_label":   "Cómo se abre un recorrido",
        "process_heading": "Cuatro pasos, una sola secuencia",
        "process": [
            ("01", "Discovery call",
             "Veinte a treinta minutos gratuitos por "
             "videoconferencia. Verificamos si el objetivo entra "
             "en el ámbito del coaching o es terapia/consultoría, "
             "si Solaria es el despacho adecuado, comentamos "
             "presupuesto orientativo."),
            ("02", "Contrato inicial",
             "Primera reunión de noventa minutos remunerada, "
             "dentro de los siete días laborables siguientes a la "
             "discovery call. Definición del objetivo SMART, "
             "elección del marco, firma del contrato de coaching escrito."),
            ("03", "Recorrido regular",
             "Sesiones a la cadencia acordada en el contrato. "
             "Cada sesión se cierra con un commitment escrito que "
             "el coachee verifica de forma autónoma. "
             "Re-contracting a mitad del recorrido con el coachee "
             "(y el patrocinador para el ámbito corporativo)."),
            ("04", "Cierre y follow-up",
             "Sesión final con verificación explícita del "
             "resultado frente al objetivo inicial. Follow-up 60 "
             "min a tres meses del cierre — incluido en los "
             "honorarios del recorrido, nunca facturado aparte."),
        ],

        "cta_heading":   "¿Qué formato es para usted?",
        "cta_intro":
            "Si no está seguro/a del recorrido a elegir, la "
            "discovery call es la vía canónica para valorarlo "
            "juntos. Le escuchamos e indicamos el formato más "
            "coherente — incluso si la respuesta es «otro "
            "profesional responde mejor a su necesidad».",
        "cta_primary":   "Reservar una discovery call",
        "cta_primary_href": "contatti",
    },

    # ─── CASI ───────────────────────────────────────────────────
    "casi": {
        "eyebrow":  "Casos seguidos · 2022 — 2026",
        "headline": "Tres recorridos, <em>tres objetivos medidos</em>.",
        "intro":
            "Una selección de casos concluidos en los últimos tres "
            "años. Los coachees se identifican por código de sector "
            "y función según el Código Deontológico ICF §2.4 "
            "(confidencialidad), pero los objetivos iniciales y los "
            "resultados medidos son reales. Reference call con el "
            "patrocinador corporativo disponible para los recorridos "
            "corporativos tras discovery call y NDA recíproco.",

        "cases_label": "Casos",
        "cases_intro":
            "Selección equilibrada sobre los tres formatos "
            "principales — executive 1:1, team coaching, grupo "
            "corporativo. No son testimonios mitológicos («mi vida "
            "ha cambiado»): son recorridos documentados con "
            "objetivo inicial declarado, recorrido realizado, "
            "resultado verificado.",

        "cta_heading":   "¿Un caso parecido al suyo?",
        "cta_intro":
            "Si un caso descrito aquí se parece a su situación, "
            "la discovery call es la vía canónica para "
            "explorarlo. Sin obligación de abrir recorrido tras "
            "la llamada — solo una valoración honesta de la "
            "adecuación del coaching a su necesidad específica.",
        "cta_primary":   "Reservar una discovery call",
        "cta_primary_href": "contatti",
    },

    "posts": [
        {
            "slug":     "executive-neo-ceo-tech-scaleup",
            "title":    "Executive 1:1 · CEO recién nombrado de una scale-up tech milanesa",
            "category": "Executive 1:1",
            "thumb":    _POOL_DETAIL,
            "year":     "2025",
            "duration": "8 sesiones · 16 semanas + follow-up",
            "client_code":
                "Tech & producto · Milán · scale-up fintech · Serie B · "
                "CEO 42 años · promovido internamente tras la salida del fundador",
            "lead":
                "El fundador salió tras una ronda Serie B y se "
                "promovió internamente al CTO como nuevo CEO. El "
                "neo-CEO tenía experiencia técnica y de producto pero "
                "ninguna experiencia de dirección general, y el "
                "consejo de administración exigía verificación de su "
                "posicionamiento en seis meses.",
            "sections": [
                {
                    "label": "El objetivo inicial",
                    "heading": "De CTO a dirección general en seis meses",
                    "body":
                        "El objetivo declarado en el contrato de "
                        "coaching consistía en trabajar la identidad "
                        "de función (de CTO a CEO), la delegación "
                        "operativa (el neo-CEO tendía a permanecer en "
                        "la técnica de producto) y la relación con "
                        "el consejo (tres miembros independientes más "
                        "dos de los fondos Serie B). Resultado "
                        "medible acordado: retorno del consejo al "
                        "término del semestre con valoración "
                        "«confirmado en el cargo» en lugar de «en observación».",
                },
                {
                    "label": "El recorrido",
                    "heading": "Co-Active + Immunity to Change",
                    "body":
                        "Ocho sesiones quincenales con marco "
                        "combinado. Las cuatro primeras sesiones "
                        "(Co-Active) trabajaron los valores que el "
                        "neo-CEO traía al cargo y su traducción en "
                        "comportamientos de liderazgo observables. "
                        "Las cuatro siguientes (Immunity to Change "
                        "de Kegan & Lahey) identificaron y "
                        "desactivaron las resistencias inconscientes "
                        "al cambio de identidad. Re-contracting a "
                        "mitad con confirmación del objetivo "
                        "originario y afinamiento de los indicadores "
                        "operativos. Supervisión ICF-MCC sobre el "
                        "caso antes de la sexta sesión.",
                },
                {
                    "label": "El resultado",
                    "heading": "Cargo confirmado con observaciones positivas",
                    "body":
                        "Al término del recorrido, el consejo "
                        "confirmó por unanimidad al CEO en el cargo "
                        "con un bonus de desempeño íntegro. El CEO "
                        "reestructuró su agenda reduciendo un 40 % "
                        "el tiempo en llamadas técnicas y "
                        "redistribuyendo ese tiempo a la relación "
                        "con el fondo lead investor y con los "
                        "miembros independientes del consejo. Dos "
                        "años después (follow-up a tres meses + "
                        "check-ins anuales espontáneos) sigue en el "
                        "cargo y la sociedad ha cerrado "
                        "positivamente la Serie C.",
                },
            ],
            "kpi": [
                ("8/8",        "sesiones del recorrido completadas"),
                ("100 %",      "objetivo inicial alcanzado"),
                ("-40 %",      "tiempo en llamadas técnicas operativas"),
                ("24 meses",   "permanencia en el cargo desde el cierre"),
            ],
            "lead_partner": "Dra. Giulia Loreti · ICF-PCC",
            "team":         "1 coach · 1 supervisora ICF-MCC · 16 semanas",
            "next_label":   "Caso siguiente",
        },
        {
            "slug":     "team-coaching-middle-management-manifattura",
            "title":    "Team coaching · mando intermedio de una manufactura en reestructuración",
            "category": "Team coaching",
            "thumb":    _POOL_AMBIENT,
            "year":     "2024",
            "duration": "6 sesiones · 6 meses + re-contracting + follow-up",
            "client_code":
                "Manufactura e industria · Brescia · 320 empleados · "
                "equipo de siete mandos intermedios tras reorganización · "
                "patrocinador: director de operaciones",
            "lead":
                "Un grupo industrial bresciano había reorganizado su "
                "estructura de producción consolidando tres centros "
                "en dos. Los siete mandos intermedios de las líneas "
                "de producción se encontraban coordinando equipos "
                "mixtos (personas de centros distintos con procesos "
                "distintos). El director de operaciones, como "
                "patrocinador corporativo, contrató a Solaria para "
                "un team coaching de seis meses.",
            "sections": [
                {
                    "label": "El objetivo inicial",
                    "heading": "Un equipo que habla, no siete referentes separados",
                    "body":
                        "Antes del encargo, los siete mandos "
                        "intermedios funcionaban como «siete "
                        "referentes separados del director de "
                        "operaciones», sin intercambio lateral de "
                        "información y sin escalado coherente de los "
                        "problemas. El objetivo declarado en el "
                        "contrato tripartito (equipo · patrocinador "
                        "· coach) era pasar a un modelo de equipo "
                        "coordinado con prácticas de intercambio "
                        "lateral medibles en seis meses. KPI "
                        "acordado con el patrocinador: frecuencia de "
                        "los intercambios laterales documentados + "
                        "disminución de los escalados «silenciosos» "
                        "al director.",
                },
                {
                    "label": "El recorrido",
                    "heading": "GROW aplicado al equipo + artefactos operativos",
                    "body":
                        "Seis sesiones de 120 minutos a cadencia "
                        "mensual, más un re-contracting de 90 "
                        "minutos con el patrocinador a mitad del "
                        "recorrido. Marco GROW aplicado a la "
                        "dinámica de grupo (Goal colectiva · "
                        "Reality colectiva · Options colectivas · "
                        "Will colectiva) para cada sesión. Se "
                        "introdujeron tres artefactos operativos "
                        "co-creados por el equipo: un stand-up "
                        "diario de diez minutos, una retrospectiva "
                        "semanal de treinta minutos, una matriz de "
                        "escalado acordada con el patrocinador. "
                        "Reporte agregado mensual al patrocinador "
                        "(nunca contenidos específicos, según "
                        "código deontológico ICF).",
                },
                {
                    "label": "El resultado",
                    "heading": "Equipo coordinado con artefactos operativos sostenidos",
                    "body":
                        "Al término del recorrido, el equipo "
                        "mantenía en autonomía los tres artefactos "
                        "operativos sin intervención de la coach. "
                        "Los escalados silenciosos al director "
                        "pasaron de una media de unos seis a la "
                        "semana a una media inferior a uno a la "
                        "semana. En el follow-up a tres meses, seis "
                        "de los siete mandos seguían en plantilla y "
                        "los artefactos operativos se habían "
                        "absorbido en la práctica habitual. El "
                        "patrocinador renovó el mandato para un "
                        "segundo equipo en la división de logística.",
                },
            ],
            "kpi": [
                ("6/6",        "sesiones del recorrido completadas"),
                ("-85 %",      "escalados silenciosos documentados"),
                ("3/3",        "artefactos operativos sostenidos en follow-up"),
                ("6/7",        "mandos aún en plantilla en follow-up"),
            ],
            "lead_partner": "Dra. Giulia Loreti · ICF-PCC",
            "team":         "1 coach · 1 supervisora ICF-MCC · 6 meses",
            "next_label":   "Caso siguiente",
        },
        {
            "slug":     "gruppo-aziendale-neo-manager-studio-legale",
            "title":    "Grupo corporativo · cinco nuevas asociadas de un despacho de abogados",
            "category": "Grupo corporativo",
            "thumb":    _POOL_FEATURE,
            "year":     "2023",
            "duration": "Masterclass + 8 sesiones/persona · 8 meses",
            "client_code":
                "Servicios profesionales · Milán · despacho de abogados asociado · "
                "cinco abogadas recién promovidas a asociadas el mismo año · "
                "patrocinador: managing partner de RR. HH.",
            "lead":
                "Un despacho de abogados milanés mediano-grande "
                "había promovido el mismo año a cinco abogadas al "
                "estatus de asociada (un esfuerzo deliberado por la "
                "pipeline femenina del partnership). El managing "
                "partner de RR. HH. contrató a Solaria para un "
                "recorrido de grupo corporativo de ocho meses: "
                "masterclass inicial común más ocho sesiones 1:1 "
                "para cada una de las cinco coachees, con follow-up "
                "trimestral al patrocinador.",
            "sections": [
                {
                    "label": "El objetivo inicial",
                    "heading": "De sénior a asociada, con visibilidad diferenciada",
                    "body":
                        "Las cinco coachees, pese al mismo "
                        "tránsito de rol, partían con necesidades "
                        "individuales distintas: algunas con retos "
                        "de delegación hacia las séniors que ellas "
                        "mismas habían sido el mes anterior, otras "
                        "con retos de visibilidad en los comités "
                        "de decisión del despacho, otras con "
                        "tensiones de identidad respecto a la "
                        "carrera partnership futura. Objetivo "
                        "acordado con el patrocinador: cada coachee "
                        "con un plan personal de desarrollo escrito "
                        "+ un set de prácticas observables "
                        "activadas en ocho meses. Cuadro de mando "
                        "agregado para el patrocinador (nunca "
                        "contenidos específicos de sesión).",
                },
                {
                    "label": "El recorrido",
                    "heading": "Masterclass común + ocho 1:1 personalizadas",
                    "body":
                        "Masterclass de un día abierta a las cinco "
                        "coachees en el despacho, con marco de "
                        "función + código deontológico ICF + "
                        "expectativas recíprocas coach-coachee. A "
                        "continuación, ocho sesiones 1:1 de "
                        "sesenta minutos para cada coachee a "
                        "cadencia acordada individualmente. "
                        "Distribución de carga: tres coachees "
                        "seguidas por Giulia (ICF-PCC) y dos por "
                        "Martina (ICF-ACC en recorrido PCC), con "
                        "supervisión mensual de la cohorte de "
                        "Martina. Cuadro de mando de progreso al "
                        "patrocinador con tres KPI agregados acordados.",
                },
                {
                    "label": "El resultado",
                    "heading": "Cinco planes individuales activos, tres promociones",
                    "body":
                        "Al término del recorrido, las cinco "
                        "coachees disponían de un plan de "
                        "desarrollo personal escrito y activo con "
                        "prácticas observables. Tres de las cinco "
                        "han sido promovidas a equity partner en "
                        "los tres años siguientes (follow-ups "
                        "espontáneos 2024 · 2025 · 2026), una "
                        "decidió dejar el despacho por una "
                        "dirección general en un equipo legal "
                        "interno, y una sigue siendo asociada "
                        "sénior con un mandato declarado de "
                        "desarrollo. El patrocinador renovó el "
                        "mandato en 2024 para una nueva cohorte de cuatro asociadas.",
                },
            ],
            "kpi": [
                ("40/40",      "sesiones del recorrido completadas (5 × 8)"),
                ("5/5",        "planes personales activos al cierre"),
                ("3/5",        "promovidas a equity partner en 3 años"),
                ("1/1",        "renovación de mandato del patrocinador al año siguiente"),
            ],
            "lead_partner": "Dra. Giulia Loreti · Dra. Martina Erriquez",
            "team":         "2 coaches · 1 supervisora ICF-MCC + 1 supervisora EMCC · 8 meses",
            "next_label":   "Caso siguiente",
        },
    ],

    # ─── CONTATTI ───────────────────────────────────────────────
    "contatti": {
        "eyebrow":  "Discovery call",
        "headline": "Veinte a treinta minutos, <em>sin compromiso</em>, sin coste.",
        "intro":
            "La discovery call es una conversación exploratoria — "
            "ni una sesión de coaching gratuita ni un diagnóstico. "
            "Verificamos juntos si su objetivo entra en el ámbito "
            "del coaching, si Solaria es el despacho adecuado para "
            "usted, y comentamos un presupuesto orientativo. Al "
            "final es libre de elegir otro coach, otra disciplina "
            "profesional, o de no abrir ningún recorrido — sin "
            "presión comercial.",

        "form_label":   "Reservar una discovery call",
        "form_heading": "Rellene la ficha de encuadre",
        "form_intro":
            "Recibirá confirmación de la secretaría del despacho "
            "en 24 horas laborables, con tres propuestas de huecos "
            "para la discovery call (videoconferencia de 20-30 "
            "minutos). Los datos se tratan al amparo del Regl. UE "
            "679/2016 (RGPD) y se conservan en archivo cifrado "
            "accesible solo a las coaches del despacho.",
        "form_fields": [
            {"name": "name",      "label": "Nombre",        "type": "text",  "required": True,  "placeholder": "P. ej. Giulia",
             "helper": "Solo el nombre de pila."},
            {"name": "surname",   "label": "Apellidos",     "type": "text",  "required": True,  "placeholder": "P. ej. Loreti",
             "helper": "Tal como aparecen en su firma profesional."},
            {"name": "company",   "label": "Empresa o contexto profesional", "type": "text", "required": False,
             "placeholder": "P. ej. Scale-up fintech milanesa",
             "helper": "Opcional — nos ayuda a preparar la discovery call."},
            {"name": "role",      "label": "Función actual", "type": "text", "required": True,  "placeholder": "P. ej. CEO recién promovido · Mando intermedio · Socio de despacho",
             "helper": "La función actual o aquella hacia la que evoluciona."},
            {"name": "email",     "label": "Correo electrónico", "type": "email", "required": True,  "placeholder": "giulia.loreti@ejemplo.es",
             "helper": "A esta dirección enviamos confirmación y tres propuestas de huecos."},
            {"name": "phone",     "label": "Teléfono",      "type": "tel",   "required": False, "placeholder": "+34 ...",
             "helper": "Opcional — solo si prefiere que la secretaría le devuelva la llamada."},
            {"name": "format",    "label": "Formato preferido", "type": "select", "required": True,
             "options": [
                 "Decidir en discovery call",
                 "Executive 1:1",
                 "Team coaching (soy patrocinador o RR. HH. de empresa)",
                 "Grupo corporativo (soy patrocinador o RR. HH. de empresa)",
                 "Sesión única exploratoria",
             ],
             "helper": "Elegir «Decidir» si no está seguro/a del formato adecuado."},
            {"name": "availability", "label": "Disponibilidad en los próximos 7 días", "type": "select", "required": True,
             "options": [
                 "Mañana 9:00 – 12:00",
                 "Primera tarde 14:00 – 16:00",
                 "Tarde-noche 16:30 – 19:00",
                 "Noche 19:30 – 21:00 (solo en línea)",
                 "Indistinto",
             ],
             "helper": "Ayuda a la secretaría a proponerle los tres huecos más cercanos a sus disponibilidades."},
            {"name": "objective", "label": "Objetivo en una-dos líneas", "type": "textarea",
             "required": True, "full_width": True,
             "placeholder": "P. ej. «Me promovieron a CEO en enero y debo trabajar la delegación operativa; el consejo me evalúa en julio.»",
             "helper": "Una-dos líneas bastan para evaluar si el objetivo entra en el ámbito del coaching. Sin detalles reservados aquí — eso se trata en discovery call bajo NDA."},
        ],

        "form_sections": [
            {"num": "01", "title": "Contacto",
             "meta": "La persona que encontraremos en la discovery call.",
             "fields": ["name", "surname", "email", "phone"]},
            {"num": "02", "title": "Contexto",
             "meta": "Opcional — nos ayuda a preparar la llamada. Sin detalles reservados aquí.",
             "fields": ["company", "role"]},
            {"num": "03", "title": "Perímetro de la llamada",
             "meta": "Para proponerle el hueco adecuado con la coach adecuada. Una-dos líneas bastan para el objetivo.",
             "fields": ["format", "availability", "objective"]},
            {"num": "04", "title": "Adjuntos (facultativos)",
             "meta": "Descripción de puesto actual, brief del patrocinador, otros materiales: pueden adelantar la discovery call.",
             "fields": ["__upload__"]},
        ],

        "upload_field": {
            "name":     "allegati_preliminari",
            "label":    "Documentos preliminares",
            "helper":   "Descripción de puesto, brief del "
                        "patrocinador, eventual evaluación 360°: "
                        "todo lo que adelante aquí hace la "
                        "discovery call más útil. "
                        "PDF · máx. 10 MB en total. Archivo "
                        "cifrado accesible solo a las coaches.",
            "accept":   ".pdf",
            "multiple": True,
            "primary":  "Arrastre aquí los documentos o",
            "link":     "examine su archivo",
            "meta":     "PDF · máx. 10 MB · archivo cifrado AES-256",
        },

        "form_submit_label": "Reservar una discovery call",
        "form_submit_note":
            "Confirmación de la secretaría del despacho en 24 "
            "horas laborables, con tres propuestas de huecos para "
            "la llamada. Sin automatización comercial, sin "
            "secuencias de correo — leemos personalmente cada solicitud.",
        "form_consent":
            "Doy mi consentimiento al tratamiento de mis datos "
            "personales al amparo del Regl. UE 679/2016 (RGPD). "
            "Los datos se conservan en el archivo cifrado del "
            "despacho y son accesibles solo a las coaches "
            "Solaria. Ningún dato se comunica a terceros sin "
            "autorización explícita.",

        "office_address_label": "Dirección",
        "office_area_label":    "Zona",
        "office_phone_label":   "Teléfono",
        "office_email_label":   "Correo",

        "offices_label":   "Sede",
        "offices": [
            {
                "city":    "Milán",
                "tag":     "Sede · también en línea",
                "address": "Via Thaon di Revel 21 · 20159",
                "area":    "Isola · a 300 metros de la estación MM Garibaldi FS",
                "phone":   "+39 02 3663 4712",
                "email":   "discovery@solariacoaching.it",
            },
        ],

        "channels_label": "Canales directos",
        "channels": [
            ("Secretaría del despacho", "+39 02 3663 4712",               "Lun – Vie · 9:00 – 19:00"),
            ("Correo discovery",        "discovery@solariacoaching.it",   "Respuesta en 24 horas laborables"),
            ("LinkedIn Giulia Loreti",  "in/giulialoreti-icf-pcc",        "Para consultas públicas no reservadas"),
        ],

        "footnote":
            "Solaria no responde a solicitudes anónimas y no "
            "ofrece «diagnóstico gratuito en diez preguntas» "
            "(diagnosticar es una actividad de consultoría, no de "
            "coaching). La información administrativa "
            "(presupuesto orientativo, modalidades de "
            "facturación, criterios de aceptación) se explica en "
            "la discovery call — gratuita, sin compromiso, con "
            "valoración honesta de la adecuación del coaching a "
            "su necesidad específica.",
    },
}
