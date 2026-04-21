"""Fiscus — Despacho de asesoría fiscal — Spanish (peninsular) content tree.

Wave 2 Pilot #1 — Phase X.4 (Session 80, 2026-04-20). ES locale mirrors the
shape of ``FISCUS_CONTENT_IT`` verbatim and ships the peninsular Spanish
institutional register (Cinco Días / Expansión / El Confidencial), usted form
in the first-line CTA and nosotros/ustedes when the firm addresses the client.

Italian normative references (ODCEC, art. 2477 c.c., D.Lgs. 39/2010, art. 177
TUIR, CTP/CTR, Quadro RW, Partita IVA, etc.) are preserved verbatim with
parenthetical clarification in Spanish where appropriate. Proper names
(Ruffini, Balestrieri, Conti, Lomazzi, Prevedini, Kouadio), albo numbers,
years and Euro figures stay intact. Euro format follows peninsular
convention: the symbol « € » appears AFTER the value, comma decimal, period
thousands (e.g. « 180 M € », « 12,4 M € », « 187.000 € »).
"""
from __future__ import annotations

from typing import Any


FISCUS_CONTENT_ES: dict[str, Any] = {
    "pages": [
        {"slug": "home",          "label": "Despacho",             "kind": "home"},
        {"slug": "lo-studio",     "label": "El despacho",          "kind": "about"},
        {"slug": "competenze",    "label": "Áreas de competencia", "kind": "services"},
        {"slug": "casi-seguiti",  "label": "Casos seguidos",       "kind": "case_study_list"},
        {"slug": "contatti",      "label": "Contacto",             "kind": "contact"},
    ],

    # Site-wide chrome — used by _base.html nav + footer
    "site": {
        "logo_initial": "F",
        "logo_word":    "Fiscus",
        "tag":          "Despacho de asesoría fiscal · Milán · colegiados ODCEC desde 2003",
        "phone":        "+39 02 4951 3388",
        "email":        "segreteria@fiscusstudio.it",
        "address":      "Via Melzo 14 · 20129 Milán",
        "hours_compact": "Lun. – Vie. · 9:00 – 18:30 · con cita previa",
        "hours_footer_rows": [
            "Sábado · con cita previa en proximidad de los vencimientos",
            "Domingo · cerrado",
        ],
        "license":      "Colegiados ODCEC Milán · Sección A · desde 2003",
        "footer_intro":
            "Despacho de asesoría fiscal independiente para números de IVA "
            "(Partita IVA), pymes y familias empresariales. Declaración de la "
            "renta, cuentas anuales, contencioso tributario y planificación "
            "fiscal plurianual. Sede en Milán, relación de asesoramiento "
            "recurrente — no servicios puntuales.",
        "foot_studio":   "El despacho",
        "foot_pages":    "Secciones",
        "foot_contact":  "Contacto",
        "foot_offices":  "Sede",
        "offices_footer_rows": [
            "Milán · Porta Venezia",
        ],
        # Case study cross-page meta labels
        "case_practice_label":     "Área",
        "case_year_label":         "Año",
        "case_duration_label":     "Duración",
        "case_lead_label":         "Responsable",
        "case_lead_partner_label": "Responsable",
        "case_team_label":         "Equipo y plazos",
        "case_timeline_label":     "Calendario",
    },

    # ─── HOME ───────────────────────────────────────────────────
    "home": {
        "eyebrow":     "Despacho de asesoría fiscal · Milán · colegiados ODCEC desde 2003",
        "headline":    "El cumplimiento <em>correcto</em>, no la ocurrencia.",
        "intro":
            "Despacho de asesoría fiscal para números de IVA, pymes y "
            "familias empresariales. Declaración de la renta, cuentas "
            "anuales, contencioso tributario y planificación fiscal "
            "plurianual — sin promesas de ahorro, con el calendario de "
            "vencimientos en la mano.",
        "primary_cta":   "Primera cita",
        "primary_href":  "contatti",
        "secondary_cta": "Descargar la guía de vencimientos",
        "secondary_href":"lo-studio",

        # Right-hand hero photo + credit overlay (fiscal-desk direction)
        "hero_image":              "https://images.pexels.com/photos/8927688/pexels-photo-8927688.jpeg?auto=compress&cs=tinysrgb&w=1600",
        "hero_image_credit_left":  ("Dirección",       "Dott. A. Ruffini"),
        "hero_image_credit_right": ("Año de fundación", "2003"),
        "hero_meta_strip": [
            ("Sede",              "Milán · Porta Venezia"),
            ("Colegio ODCEC",     "4 colegiados · desde 2003"),
            ("Clientes activos",  "260 números de IVA"),
        ],

        # Advisory pillars — three practice areas on home
        "pillars_label":   "Áreas de competencia",
        "pillars_heading": "Tres prácticas, una única firma",
        "pillars_intro":
            "Un único equipo multidisciplinar acompaña a cada cliente. El "
            "asesor fiscal colegiado no es un coste que minimizar: es un "
            "garante que elegir.",
        "pillars": [
            ("01", "Declaración y cuentas anuales",
             "Declaración de la renta, Anexo RW para rentas en el extranjero, "
             "certificación única, cuentas anuales — audit-ready, con "
             "calendario de revisiones acordado en enero y firma dentro de "
             "los plazos de la Agencia Tributaria italiana."),
            ("02", "Contencioso tributario",
             "Asistencia en inspecciones fiscales, regularización voluntaria "
             "(ravvedimento operoso), recurso ante el Tribunal económico-"
             "administrativo provincial y regional (Commissione Tributaria). "
             "Nunca promesas de resultado, siempre una estimación preliminar "
             "de probabilidades — por escrito, en papel de carta, antes del "
             "otorgamiento del poder."),
            ("03", "Planificación patrimonial y sucesión generacional",
             "Planificación fiscal plurianual, sociedad holding familiar, "
             "sucesión y donación — para patrimonios privados medio-altos "
             "y familias empresariales que preparan el relevo generacional "
             "en un horizonte de 5-10 años."),
        ],

        # KPI strip — document the studio's continuity track record
        "kpi_heading": "Veintidós años de práctica continuada",
        "kpi_strip": [
            ("22",       "años desde la fundación"),
            ("260",      "números de IVA en cartera"),
            ("180 M €",  "facturación agregada de los clientes"),
            ("0",        "sanciones imprevistas en 2025"),
        ],

        # Sectors ribbon — the client base
        "sectors_label": "Sectores de los clientes",
        "sectors": [
            "Autónomos y profesionales independientes",
            "Pymes manufactureras",
            "Despachos profesionales",
            "Patrimonios privados",
            "Inmobiliario",
        ],

        # Trust band — anonymized client categories (commercialisti don't
        # disclose client logos per secreto profesional)
        "trust_label":   "Confían en Fiscus para su fiscalidad",
        "trust_logos":   [
            "AUTÓNOMOS Y PROFESIONALES",
            "DESPACHOS DE CONSULTORÍA",
            "PYMES MANUFACTURERAS",
            "FAMILIAS EMPRESARIALES",
            "INMOBILIARIAS PRIVADAS",
            "PROFESIONALES COLEGIADOS",
        ],

        # Leadership preview — 3 partners on home
        "leadership_label":   "Dirección",
        "leadership_heading": "Los asesores fiscales que se sentarán a su mesa",
        "leadership_intro":
            "Cada cliente es seguido personalmente por al menos un socio "
            "colegiado ODCEC. Ningún júnior con delegación, ninguna rotación "
            "silenciosa — el responsable con el que se reúne en la primera "
            "cita firma las declaraciones y responde de los trámites.",
        "leadership": [
            {
                "name":  "Dott. Andrea Ruffini",
                "role":  "Socio fundador · Declaración y cuentas anuales",
                "bio":
                    "Asesor fiscal colegiado ODCEC Milán desde 1999, Sección A. "
                    "Inscrito en el Registro de Auditores Legales italiano desde "
                    "2004. Economista titulado con especialización en fiscalidad "
                    "empresarial y cuentas anuales. Fundador del despacho en "
                    "2003 junto con la Dott.ssa Balestrieri.",
                "credentials": [
                    "ODCEC Milán n.º 4488/A (desde 1999)",
                    "Auditor Legal n.º 137952 (desde 2004)",
                    "Università Bocconi — CLEA ’96",
                ],
            },
            {
                "name":  "Dott.ssa Ilaria Balestrieri",
                "role":  "Socia · Contencioso tributario",
                "bio":
                    "Asesora fiscal colegiada ODCEC Milán desde 2001, Sección A. "
                    "Abogada habilitada ante el Tribunal Supremo italiano desde "
                    "2010, inscrita en el Colegio de Abogados de Milán y "
                    "especializada en contencioso tributario. Litiga ante los "
                    "Tribunales económico-administrativos (Commissioni Tributarie) "
                    "provinciales y regionales de Lombardía y Piamonte.",
                "credentials": [
                    "ODCEC Milán n.º 5611/A (desde 2001)",
                    "Colegio de Abogados de Milán (desde 2010)",
                    "Habilitación ante el Tribunal Supremo desde 2018",
                ],
            },
            {
                "name":  "Dott. Stefano Conti",
                "role":  "Socio · Planificación patrimonial y sucesión generacional",
                "bio":
                    "Asesor fiscal colegiado ODCEC Milán desde 2008, Sección A. "
                    "Especialista en planificación patrimonial para familias "
                    "empresariales — holding, trust, sucesión. Se incorpora al "
                    "despacho en 2014, socio desde 2019. Profesor contratado de "
                    "fiscalidad internacional en la LIUC de Castellanza.",
                "credentials": [
                    "ODCEC Milán n.º 7912/A (desde 2008)",
                    "LL.M. Derecho Tributario Bocconi",
                    "TEP · Society of Trust and Estate Practitioners",
                ],
            },
        ],

        # Case studies preview — three recent mandates on home
        "cases_label":   "Casos seguidos",
        "cases_heading": "Tres casos, tres áreas de competencia",
        "cases_intro":
            "Una selección reciente de clientes acompañados en los últimos "
            "tres años. Por secreto profesional, los nombres se sustituyen "
            "por el código de sector, pero las cifras son verificables en "
            "fase de reference call.",

        # Final CTA band before footer — appointment-focused
        "cta_label":     "Primera cita",
        "cta_heading":   "Cuarenta y cinco minutos, agenda abierta, sin compromiso",
        "cta_intro":
            "La primera visita se celebra con un socio colegiado ODCEC. "
            "Discutimos el área de competencia, el horizonte temporal de la "
            "relación y la minuta de honorarios orientativa — antes de "
            "cualquier otorgamiento firmado. Los clientes existentes "
            "reservan en el espacio reservado.",
        "cta_primary":   "Solicitar cita",
        "cta_primary_href": "contatti",
        "cta_secondary": "Descargar la guía de vencimientos",
        "cta_secondary_href": "lo-studio",
    },

    # ─── LO STUDIO (about + values + team + history) ────────────
    "lo-studio": {
        "eyebrow":   "El despacho · 2003 — 2026",
        "headline":  "Un despacho de asesoría fiscal <em>independiente</em>, veintidós años de práctica continuada.",
        "intro":
            "Fiscus nace en Milán en 2003 del encuentro entre Andrea Ruffini "
            "e Ilaria Balestrieri — dos asesores fiscales colegiados ODCEC "
            "con formación en fiscalidad empresarial y contencioso "
            "tributario. Hemos crecido por cooptación, nunca por adquisición, "
            "y hemos mantenido la independencia del capital ajeno.",

        # Studio history — 5-step timeline
        "history_label":   "Historia del despacho",
        "history_heading": "Cinco hitos, veintidós años",
        "history_intro":
            "Cinco fechas que han definido Fiscus. Cada una refleja una "
            "decisión estructural — de independencia, de especialización, "
            "de perímetro — que todavía hoy orienta la forma en que "
            "aceptamos a los nuevos clientes.",
        "history": [
            ("2003", "Fundación",
             "Andrea Ruffini e Ilaria Balestrieri abren Fiscus en Via Melzo, "
             "con doce clientes ya en cartera — todos heredados del despacho "
             "anterior con el consentimiento expreso de los propios clientes."),
            ("2008", "Práctica de contencioso tributario",
             "La habilitación de Ilaria Balestrieri como abogada abre la "
             "práctica de contencioso: recursos ante los Tribunales económico-"
             "administrativos (CTP/CTR), inspecciones fiscales y "
             "regularización voluntaria. Primera vista ante la CTP de Milán "
             "en marzo de 2009."),
            ("2014", "Incorporación del Dott. Conti",
             "Stefano Conti se incorpora como asociado para constituir la "
             "práctica de planificación patrimonial — sociedad holding "
             "familiar, trust, sucesión generacional. Socio desde 2019 tras "
             "cinco años de acompañamiento."),
            ("2020", "Digitalización de la declaración",
             "Integración completa con la Agencia Tributaria italiana vía "
             "Entratel y facturación electrónica. Archivo documental "
             "cifrado con retención decenal y acceso del cliente a través "
             "del área reservada."),
            ("2024", "Práctica de auditoría de cuentas",
             "Andrea Ruffini formaliza la práctica de auditoría de cuentas "
             "para pymes con obligación de órgano de control (collegio "
             "sindacale). Tres mandatos de auditoría activos antes de "
             "diciembre de 2024."),
        ],

        # Method / values — 4 principi
        "values_label":   "Método",
        "values_heading": "Cuatro principios <em>no negociables</em>",
        "values_intro":
            "Las cuatro reglas que separan a un cliente Fiscus de una relación "
            "de asesoramiento ordinaria. Están escritas en papel de carta "
            "sobre el mandato de otorgamiento — no solo en esta página.",
        "values": [
            ("01", "Independencia del capital",
             "El capital del despacho está íntegramente en manos de los socios "
             "activos. Ninguna aportación de grupos, ningún fondo en minoría, "
             "ningún accionista externo. La selección de clientes nunca está "
             "influida por agendas ajenas — y los clientes históricos saben "
             "que la relación no cambia de color porque haya cambiado un socio."),
            ("02", "Un socio por cada cliente",
             "Cada cliente tiene un socio de referencia colegiado ODCEC que "
             "acompaña personalmente la práctica desde la apertura del "
             "expediente hasta la firma de las declaraciones. El socio con el "
             "que se reúne en la primera cita responde de los trámites — sin "
             "delegaciones silenciosas, sin rotaciones a fin de año."),
            ("03", "Ninguna promesa de ahorro",
             "No firmamos propuestas con promesas de reducción fiscal en "
             "porcentaje: es contrario al código deontológico ODCEC y es el "
             "síntoma de relaciones oportunistas. Nuestro oficio consiste en "
             "aplicar correctamente la normativa y señalar los instrumentos "
             "de fomento fiscal cuando existan."),
            ("04", "Honorarios a tanto alzado transparentes",
             "Tarifa anual acordada en diciembre para el ejercicio siguiente, "
             "revisada únicamente en caso de variación objetiva del perímetro "
             "(nueva sede, nuevo número de IVA, nueva rama de actividad). "
             "Ninguna facturación por consumo oculta, ninguna retrocesión "
             "de comisiones."),
        ],

        # Full team — 3 soci + 4 collaboratori iscritti albo o praticanti
        "team_label":   "Equipo",
        "team_heading": "Tres socios, cuatro colaboradores, un único gobierno",
        "team_intro":
            "Las personas que acompañarán su mandato. Cada declaración la "
            "firma un socio — los colaboradores asisten en la recogida de "
            "datos, la verificación preliminar y la gestión documental.",
        "team": [
            {"name": "Dott. Andrea Ruffini",
             "role": "Socio fundador · Declaración y cuentas anuales · Auditor legal",
             "office": "Milán",
             "bio": "Asesor fiscal colegiado ODCEC desde 1999 y auditor legal "
                    "desde 2004. Bocconi CLEA ’96. Fundador del despacho."},
            {"name": "Dott.ssa Ilaria Balestrieri",
             "role": "Socia · Contencioso tributario · Habilitada ante el Tribunal Supremo italiano",
             "office": "Milán",
             "bio": "Asesora fiscal colegiada ODCEC desde 2001 y abogada "
                    "habilitada ante el Tribunal Supremo italiano desde 2018. "
                    "Litiga en Lombardía y Piamonte."},
            {"name": "Dott. Stefano Conti",
             "role": "Socio · Planificación patrimonial y sucesión generacional · Profesor LIUC",
             "office": "Milán",
             "bio": "Asesor fiscal colegiado ODCEC desde 2008. LL.M. Derecho "
                    "Tributario Bocconi. TEP desde 2021."},
            {"name": "Dott.ssa Serena Lomazzi",
             "role": "Colaboradora · Declaración de personas físicas",
             "office": "Milán",
             "bio": "Asesora fiscal colegiada ODCEC desde 2017. Coordina la "
                    "recogida de datos y la cumplimentación de las "
                    "declaraciones 730 y RPF italianas."},
            {"name": "Dott. Giacomo Prevedini",
             "role": "Colaborador · Cuentas anuales de pymes · Auditor en prácticas",
             "office": "Milán",
             "bio": "Asesor fiscal colegiado ODCEC desde 2021. Lleva la "
                    "contabilidad ordinaria y el cierre de cuentas anuales "
                    "de las pymes manufactureras de la cartera."},
            {"name": "Rag. Nadia Kouadio",
             "role": "Responsable de contabilidad · Nóminas y cotizaciones",
             "office": "Milán",
             "bio": "Contable colegiada en el Colegio de Graduados Sociales "
                    "italiano desde 2012. Gestiona las nóminas en "
                    "colaboración con un graduado social externo y la "
                    "contabilidad ordinaria."},
        ],

        # Coordinates strip
        "coordinates_label": "Sede",
        "coordinates": [
            ("Milán", "Via Melzo 14 · 20129 · Porta Venezia — a 200 metros de la estación MM Porta Venezia"),
        ],

        # Page-level CTA
        "cta_heading": "Una primera reunión exploratoria",
        "cta_intro":
            "Los primeros cuarenta y cinco minutos con un socio son una "
            "conversación exploratoria, no una propuesta comercial. Se "
            "discute el área de competencia, el horizonte temporal y la "
            "minuta de honorarios orientativa. Al término, usted es libre "
            "de elegir otro despacho — y de llevarse consigo toda la "
            "documentación preliminar.",
        "cta_primary":  "Solicitar cita",
        "cta_primary_href": "contatti",
    },

    # ─── COMPETENZE (services) ──────────────────────────────────
    "competenze": {
        "eyebrow":  "Áreas de competencia · 2026",
        "headline": "Seis áreas de competencia, <em>una única firma</em>.",
        "intro":
            "Las seis áreas de práctica de Fiscus. Cada cliente accede al "
            "equipo multidisciplinar — no se paga por cada área por separado, "
            "la minuta anual cubre la combinación de competencias necesarias "
            "para el mandato.",

        # Card meta labels
        "svc_duration_label": "Duración típica",
        "svc_leader_label":   "Socio responsable",

        # 6 areas in airy cards
        "services": [
            {
                "num":   "01",
                "title": "Declaración de la renta y fiscalidad ordinaria",
                "blurb":
                    "Declaración de la renta italiana (Modello Redditi PF · SP · SC · "
                    "ENC), modelo 730, Anexo RW para rentas en el extranjero, "
                    "certificación única. Trabajamos sobre un calendario acordado en "
                    "enero, con plazos internos 30 días antes de los de la Agencia "
                    "Tributaria italiana — porque una declaración firmada el 30 de "
                    "septiembre es mejor que la del 30 de noviembre.",
                "scope": [
                    "Modello Redditi PF / SP / SC / ENC",
                    "Modelo 730 para asalariados y pensionistas",
                    "Anexo RW — monitoreo fiscal de rentas en el extranjero",
                    "Certificación Única para retenedores fiscales",
                    "Regularización voluntaria (ravvedimento operoso) para declaraciones complementarias",
                ],
                "duration": "Relación anual recurrente",
                "leader":   "Dott. Andrea Ruffini",
            },
            {
                "num":   "02",
                "title": "Cuentas anuales y contabilidad ordinaria",
                "blurb":
                    "Contabilidad ordinaria, cuentas anuales según el formato CEE "
                    "italiano, memoria, informe de gestión, acta de junta. Para las "
                    "pymes con órgano de control interno nos ocupamos también de la "
                    "preparación de la documentación para el auditor legal — "
                    "audit-ready antes de marzo, depósito en el Registro Mercantil "
                    "(Camera di Commercio) antes de mayo.",
                "scope": [
                    "Contabilidad ordinaria y simplificada",
                    "Cuentas anuales formato CEE italiano + memoria",
                    "Depósito de cuentas en el Registro Mercantil (Camera di Commercio)",
                    "Informe de gestión para sociedades de capital",
                    "Asistencia al órgano de control interno y al auditor externo",
                ],
                "duration": "Relación anual recurrente",
                "leader":   "Dott. Andrea Ruffini",
            },
            {
                "num":   "03",
                "title": "Contencioso tributario",
                "blurb":
                    "Asistencia en fase de inspección fiscal con adhesión, "
                    "regularización voluntaria (ravvedimento operoso), recurso ante "
                    "el Tribunal económico-administrativo provincial y regional "
                    "(Commissione Tributaria) y conciliación judicial. Litigamos en "
                    "Lombardía y Piamonte. Para cada expediente facilitamos una "
                    "estimación preliminar de probabilidades por escrito, antes del "
                    "otorgamiento del poder.",
                "scope": [
                    "Inspección fiscal con adhesión (accertamento con adesione)",
                    "Regularización voluntaria y aplazamientos",
                    "Recurso CTP · CTR · Tribunal Supremo italiano (con abogado)",
                    "Conciliación judicial",
                    "Solicitudes de revisión ante la Agencia Tributaria italiana",
                ],
                "duration": "De 3 a 24 meses según la instancia",
                "leader":   "Dott.ssa Ilaria Balestrieri",
            },
            {
                "num":   "04",
                "title": "Planificación fiscal y patrimonial",
                "blurb":
                    "Planificación fiscal plurianual para patrimonios privados "
                    "medio-altos y familias empresariales. Sociedad holding familiar, "
                    "trust, fundaciones, pólizas de seguros fiscalmente eficientes, "
                    "planificación sucesoria. Siempre con horizonte de 5-10 años — "
                    "no con promesas fiscales anuales.",
                "scope": [
                    "Sociedad holding familiar y pactos parasociales",
                    "Trust y fundaciones familiares",
                    "Planificación sucesoria y donación",
                    "Estructuración de pólizas de seguros del Ramo IV",
                    "Evaluación de instrumentos de fomento fiscal (PIR, ELTIF)",
                ],
                "duration": "12 – 36 meses para reestructuración patrimonial",
                "leader":   "Dott. Stefano Conti",
            },
            {
                "num":   "05",
                "title": "Nóminas y asesoría laboral · retenedor fiscal",
                "blurb":
                    "Gestión de nóminas, cotizaciones, retenedor fiscal para pymes y "
                    "despachos profesionales — en colaboración con un graduado social "
                    "externo colegiado. Nos ocupamos de la parte fiscal y contable; "
                    "el graduado social se ocupa de la parte jurídico-laboral y de "
                    "la previsión social.",
                "scope": [
                    "Elaboración de nóminas y modelos F24 mensuales",
                    "Certificación Única del retenedor fiscal",
                    "Modelo 770 italiano",
                    "Asistencia en inspecciones INPS / INAIL / Inspección de Trabajo italianas",
                    "Coordinación con graduado social externo (Rag. Kouadio)",
                ],
                "duration": "Relación mensual recurrente",
                "leader":   "Rag. Nadia Kouadio · Dott. A. Ruffini",
            },
            {
                "num":   "06",
                "title": "Auditoría de cuentas y órgano de control",
                "blurb":
                    "Auditoría legal de cuentas para pymes con obligación de órgano "
                    "de control (collegio sindacale) — sociedades anónimas no "
                    "cotizadas, sociedades de responsabilidad limitada (S.r.l.) que "
                    "superan los umbrales del art. 2477 c.c. Actualmente tres "
                    "mandatos activos. Siempre nos presentamos como auditor externo, "
                    "nunca como miembro interno del órgano de control del mismo grupo.",
                "scope": [
                    "Informe de auditoría legal ex D.Lgs. 39/2010",
                    "Verificación periódica trimestral de las cuentas",
                    "Planificación ISA Italia de la auditoría",
                    "Comunicación con el órgano de control interno",
                    "Informe ante la junta de socios",
                ],
                "duration": "Mandato trienal o novenal",
                "leader":   "Dott. Andrea Ruffini",
            },
        ],

        # Process — how a new client onboarding is run
        "process_label":   "Cómo trabajamos",
        "process_heading": "Cuatro pasos, una única secuencia",
        "process": [
            ("01", "Primera cita",
             "Cuarenta y cinco minutos reservados con un socio colegiado "
             "ODCEC. Se discute el área de competencia, el horizonte temporal "
             "y la minuta de honorarios orientativa. Ningún otorgamiento "
             "firmado, ningún coste."),
            ("02", "Propuesta por escrito",
             "En un plazo de siete días laborables, una propuesta de tres "
             "páginas con el perímetro del mandato, la lista de trámites, el "
             "calendario de plazos internos y la minuta anual acordada."),
            ("03", "Apertura del expediente",
             "Otorgamiento ante la Agencia Tributaria italiana vía Entratel, "
             "traspaso de la documentación desde el asesor fiscal anterior "
             "(si existe) y apertura del área de cliente reservada en el "
             "archivo cifrado."),
            ("04", "Relación continuada",
             "Un socio de referencia durante toda la relación. Vencimientos "
             "atendidos 30 días antes de las fechas de la Agencia Tributaria "
             "italiana. Revisión anual en diciembre para el ejercicio "
             "siguiente."),
        ],

        # Final CTA
        "cta_heading":   "¿Qué área de competencia es la adecuada para usted?",
        "cta_intro":
            "Si el perímetro no está claro, envíenos una breve descripción "
            "de la situación (tipo de empresa, año de apertura, trámites "
            "eventualmente vencidos). Respondemos en un plazo de 48 horas "
            "laborables — incluso si la respuesta es «no somos el despacho "
            "adecuado».",
        "cta_primary":   "Escríbanos",
        "cta_primary_href": "contatti",
    },

    # ─── CASI SEGUITI (case-studies list) ───────────────────────
    "casi-seguiti": {
        "eyebrow":  "Casos seguidos · 2022 — 2026",
        "headline": "Tres casos, <em>tres áreas de competencia</em>.",
        "intro":
            "Una selección de casos seguidos en los últimos cuatro años. "
            "Los clientes se identifican mediante un código de sector en "
            "cumplimiento del secreto profesional (art. 199 c.p.p. italiano "
            "y Código Deontológico ODCEC), pero las cifras son reales y "
            "verificables mediante reference call con el interlocutor "
            "interno del cliente.",

        "cases_label": "Casos",
        "cases_intro":
            "Selección equilibrada sobre las tres áreas principales — "
            "declaración y cuentas anuales, contencioso, planificación "
            "patrimonial. La lista completa de casos disponibles como "
            "referencia se facilita en formato PDF a través de la página "
            "de contacto.",

        "cta_heading":   "¿Un caso parecido al suyo?",
        "cta_intro":
            "Los dossieres completos (perímetro, cifras agregadas, posible "
            "reference call con el interlocutor interno del cliente) son "
            "accesibles previa firma de compromiso de confidencialidad "
            "recíproca. La firma se produce durante la primera cita, antes "
            "de cualquier compromiso sobre la minuta de honorarios.",
        "cta_primary":   "Solicitar los dossieres íntegros",
        "cta_primary_href": "contatti",
    },

    # Posts powering case_study_detail. URL: /casi-seguiti/<slug>/
    "posts": [
        {
            "slug":     "pmi-manifattura-bilancio-revisione",
            "title":    "Pyme manufacturera lombarda · implantación de la auditoría legal",
            "category": "Declaración y cuentas anuales",
            "year":     "2025",
            "duration": "10 semanas + mandato trienal",
            "client_code":
                "Industria manufacturera · Brescia · 42 empleados · "
                "12,4 M € de ingresos · S.r.l. con órgano de control interno ex art. 2477",
            "lead":
                "Primer ejercicio con obligación de auditoría legal tras la "
                "superación de los umbrales del art. 2477 c.c. italiano. El "
                "cliente encargó a Fiscus como auditor externo en continuidad "
                "con la relación tributaria ordinaria de larga duración.",
            "sections": [
                {
                    "label": "El problema",
                    "heading": "Paso al órgano de control interno en mitad del ejercicio",
                    "body":
                        "La sociedad superó durante el segundo año consecutivo "
                        "los umbrales dimensionales previstos en el art. 2477 "
                        "c.c. italiano (ingresos > 8,8 M €, activo > 4,4 M €, "
                        "empleados > 50). El órgano de control interno "
                        "(collegio sindacale) fue nombrado en junta en marzo "
                        "de 2025 y era necesario encargar a un auditor legal "
                        "externo ex D.Lgs. 39/2010 en un plazo de tres meses. "
                        "La sociedad tenía preferencia por la continuidad con "
                        "el despacho tributario histórico — siempre que no "
                        "hubiera conflictos de interés en materia de "
                        "independencia.",
                },
                {
                    "label": "El enfoque",
                    "heading": "Segregación de prácticas y planificación ISA",
                    "body":
                        "Fiscus aceptó el mandato de auditoría bajo la "
                        "condición de segregación operativa: un socio "
                        "distinto acompaña la práctica tributaria (Dott. A. "
                        "Ruffini) y la práctica de auditoría (Dott.ssa I. "
                        "Balestrieri, inscrita en el Registro de Auditores "
                        "italiano desde 2011). Planificación de la auditoría "
                        "según ISA Italia 315 — evaluación del sistema de "
                        "control interno, identificación de los riesgos "
                        "significativos, determinación de la materialidad. "
                        "El plan de auditoría fue compartido con el órgano "
                        "de control interno antes de la ejecución.",
                },
                {
                    "label": "El resultado",
                    "heading": "Informe de auditoría sin salvedades",
                    "body":
                        "Informe de auditoría ex art. 14 D.Lgs. 39/2010 "
                        "publicado en mayo de 2025 sin salvedades, sin "
                        "párrafos de énfasis y sin incertidumbres "
                        "significativas. La auditoría evidenció dos "
                        "recomendaciones de refuerzo del sistema de control "
                        "interno (segregation of duties en el ciclo de "
                        "compras, procedimiento de cierre mensual del "
                        "inventario) que la sociedad implementó antes de "
                        "septiembre. Mandato de auditoría trienal "
                        "confirmado para los ejercicios 2025-2027.",
                },
            ],
            "kpi": [
                ("0",        "salvedades en el informe de auditoría"),
                ("2",        "recomendaciones implementadas por el cliente"),
                ("3 años",   "duración del mandato de auditoría"),
                ("10 sem.",  "desde el encargo a la firma del informe"),
            ],
            "lead_partner": "Dott.ssa Ilaria Balestrieri (auditoría) · Dott. Andrea Ruffini (tributario)",
            "team":         "2 socios · 1 sénior · 1 auditor en prácticas · 10 semanas",
            "next_label":   "Caso siguiente",
        },
        {
            "slug":     "contenzioso-tributario-accertamento-iva",
            "title":    "Contencioso · liquidación de IVA sobre operaciones intracomunitarias",
            "category": "Contencioso tributario",
            "year":     "2024",
            "duration": "14 meses desde la inspección hasta la sentencia CTR",
            "client_code":
                "Comercio mayorista · Como · 18 empleados · "
                "6,2 M € de ingresos · liquidación de la Agencia Tributaria italiana por 187.000 € de IVA",
            "lead":
                "Liquidación de la Agencia Tributaria italiana por "
                "operaciones intracomunitarias recalificadas como entregas "
                "internas ordinarias (presunción de destino nacional). El "
                "cliente encargó a Fiscus en fase de contradictorio "
                "preliminar, a pocos días del plazo para la adhesión.",
            "sections": [
                {
                    "label": "El problema",
                    "heading": "Presunción de factura nacional sobre operaciones UE",
                    "body":
                        "La Agencia Tributaria italiana notificó un acta de "
                        "liquidación correspondiente al ejercicio 2021 con "
                        "una recuperación de IVA de 187.000 €, sanciones del "
                        "90% e intereses. La oficina recalificaba una serie "
                        "de operaciones dirigidas a un cliente eslovaco como "
                        "entregas internas ordinarias, sobre la base de que "
                        "la documentación de transporte no probaba de forma "
                        "suficiente la salida efectiva de la mercancía del "
                        "territorio italiano. El plazo para la adhesión "
                        "vencía en 28 días.",
                },
                {
                    "label": "El enfoque",
                    "heading": "Contradictorio con documentación CMR complementaria",
                    "body":
                        "Fiscus instruyó un contradictorio preliminar en "
                        "tres semanas. Se recabó: 64 cartas de porte CMR "
                        "originales selladas por el destinatario UE, "
                        "extractos bancarios de los pagos del cliente "
                        "eslovaco desde su banco eslovaco, verificaciones "
                        "VIES históricas del cliente UE, una peritación "
                        "jurada del responsable logístico del cliente. La "
                        "documentación se presentó en contradictorio y, en "
                        "paralelo, en fase de recurso ante el Tribunal "
                        "económico-administrativo provincial (Commissione "
                        "Tributaria Provinciale) de Como, para anticipar "
                        "la hipótesis de denegación administrativa.",
                },
                {
                    "label": "El resultado",
                    "heading": "Recurso estimado en CTP y confirmado en CTR",
                    "body":
                        "La CTP de Como estimó íntegramente el recurso en "
                        "junio de 2024, anulando el acta de liquidación "
                        "mediante sentencia n.º 412/2024. La Agencia "
                        "Tributaria italiana presentó recurso de apelación "
                        "ante la CTR de Lombardía, que en diciembre de 2024 "
                        "confirmó la sentencia de primera instancia "
                        "desestimando el recurso de la oficina. Sentencia "
                        "firme en enero de 2025. El cliente recuperó las "
                        "costas procesales ex art. 15 D.Lgs. 546/1992 por "
                        "14.200 €.",
                },
            ],
            "kpi": [
                ("187.000 €", "IVA liquidada — totalmente anulada"),
                ("100%",      "costas procesales recuperadas ex art. 15"),
                ("2/2",       "instancias falladas a favor"),
                ("14 meses",  "desde la inspección hasta la firmeza"),
            ],
            "lead_partner": "Dott.ssa Ilaria Balestrieri",
            "team":         "1 socia habilitada ante el Tribunal Supremo italiano · 1 sénior · 14 meses",
            "next_label":   "Caso siguiente",
        },
        {
            "slug":     "wealth-passaggio-generazionale-holding",
            "title":    "Planificación patrimonial · sociedad holding familiar para la sucesión generacional",
            "category": "Planificación patrimonial y sucesión generacional",
            "year":     "2025",
            "duration": "20 meses desde el mandato hasta la finalización",
            "client_code":
                "Familia empresarial · Varese · patrimonio agregado "
                "38 M € (participación en pyme manufacturera + inmuebles + liquidez) · "
                "dos hijos, ambos implicados en la empresa",
            "lead":
                "Familia empresarial con participación de control en una "
                "pyme manufacturera de segundo nivel, tres inmuebles "
                "instrumentales, dos inmuebles de lujo y liquidez "
                "significativa. Fundador de 68 años, dos hijos operativos "
                "en la empresa, esposa no implicada en la gestión. "
                "Objetivo: preparar el relevo generacional en un horizonte "
                "de 7-10 años.",
            "sections": [
                {
                    "label": "El problema",
                    "heading": "Patrimonio heterogéneo, dos hijos con roles distintos",
                    "body":
                        "El fundador tenía tres preocupaciones concretas. "
                        "Primera: preservar la unidad del control "
                        "societario también tras la sucesión — ambos hijos "
                        "trabajaban en la empresa, pero con roles y "
                        "perspectivas distintos. Segunda: permitir una "
                        "liquidez de «retirada» a la esposa y a la rama "
                        "familiar no operativa sin obligar a vender "
                        "participaciones. Tercera: minimizar el impacto "
                        "fiscal de la sucesión (impuesto sobre sucesiones "
                        "italiano por encima del umbral de 1 M € por "
                        "pariente en línea recta) siempre en el respeto "
                        "absoluto de la normativa vigente — ninguna "
                        "estructura offshore, ningún trust agresivo.",
                },
                {
                    "label": "El enfoque",
                    "heading": "Holding familiar + pacto parasocial + PIR",
                    "body":
                        "Fiscus coordinó un recorrido de 20 meses en cuatro "
                        "fases. Fase 1 (meses 1-4): constitución de una "
                        "sociedad holding familiar S.r.l. (sociedad de "
                        "responsabilidad limitada italiana) con aportación "
                        "de las participaciones operativas en neutralidad "
                        "fiscal ex art. 177 TUIR. Fase 2 (meses 5-8): "
                        "redacción del pacto parasocial entre las dos ramas "
                        "familiares con mecanismo de tag-along/drag-along "
                        "para prevenir fracturas futuras. Fase 3 (meses "
                        "9-14): donación gradual de las participaciones de "
                        "la holding a los hijos, con usufructo vitalicio a "
                        "favor del fundador y de la esposa — se beneficia "
                        "de la bonificación del art. 3, apartado 4-ter, "
                        "D.Lgs. 346/1990 italiano (exención del impuesto "
                        "sobre sucesiones para participaciones de control). "
                        "Fase 4 (meses 15-20): suscripción de instrumentos "
                        "PIR compatibles para la rama no operativa de la "
                        "familia, sobre los flujos de dividendos.",
                },
                {
                    "label": "El resultado",
                    "heading": "Sucesión fiscalmente optimizada + gobierno familiar",
                    "body":
                        "La estructura se completó en septiembre de 2025. "
                        "Impuesto sobre sucesiones reducido a cero sobre "
                        "las participaciones operativas gracias a la "
                        "bonificación del art. 3, apartado 4-ter (pacto "
                        "de familia + holding de control). Pacto parasocial "
                        "suscrito por los dos hermanos y los padres, con "
                        "cláusulas de buy-out al valor de tasación "
                        "independiente actualizada anualmente. La rama no "
                        "operativa (esposa y eventuales nietos) percibe "
                        "dividendos regulares de la holding y ha suscrito "
                        "PIR individuales por 180.000 € cada uno en el "
                        "horizonte 2025-2030. El fundador ha mantenido los "
                        "derechos de voto en usufructo hasta los 75 años "
                        "más 5 de opción adicional.",
                },
            ],
            "kpi": [
                ("0 €",      "impuesto sobre sucesiones sobre las participaciones operativas"),
                ("100%",     "unidad del control preservada"),
                ("20 meses", "desde el mandato hasta la finalización"),
                ("4/4",      "fases completadas en los plazos acordados"),
            ],
            "lead_partner": "Dott. Stefano Conti",
            "team":         "1 socio · 1 sénior · notario externo · 20 meses",
            "next_label":   "Caso siguiente",
        },
    ],

    # ─── CONTATTI ───────────────────────────────────────────────
    "contatti": {
        "eyebrow":  "Primera cita",
        "headline": "Cuarenta y cinco minutos, agenda <em>abierta</em>, sin compromiso.",
        "intro":
            "El primer contacto se mantiene con un socio colegiado ODCEC. "
            "Discutimos el área de competencia, el horizonte temporal de la "
            "relación y la minuta de honorarios orientativa — antes de "
            "cualquier otorgamiento firmado. Los clientes existentes "
            "reservan en el espacio reservado del área de cliente.",

        # Form fields — commercialista onboarding shape
        "form_label":   "Solicitar cita",
        "form_heading": "Cumplimente la ficha exploratoria",
        "form_intro":
            "Recibirá confirmación en un plazo de 48 horas laborables desde "
            "el envío. Los datos se tratan conforme al Reglamento UE "
            "2016/679 (RGPD) y se custodian en el archivo cifrado del "
            "despacho con retención decenal.",
        "form_fields": [
            {"name": "name",      "label": "Nombre",          "type": "text",     "required": True,  "placeholder": "Ej. Andrea",
             "helper": "Solo el nombre de pila."},
            {"name": "surname",   "label": "Apellidos",       "type": "text",     "required": True,  "placeholder": "Ej. Ruffini",
             "helper": "Tal como figura en los documentos de identidad."},
            {"name": "company",   "label": "Razón social o actividad como autónomo", "type": "text", "required": False,
             "placeholder": "Ej. Officine Meccaniche Bresciane S.r.l.",
             "helper": "Opcional — cumplimentar si el contacto se realiza en nombre de una empresa."},
            {"name": "vat",       "label": "Número de IVA (Partita IVA)",    "type": "text",     "required": False, "placeholder": "IT 12345678901",
             "helper": "Opcional — útil si la relación se refiere a la fiscalidad empresarial."},
            {"name": "fiscal_code","label": "Código Fiscal italiano","type": "text",     "required": True,  "placeholder": "RFFNDR72M15F205Z",
             "helper": "Obligatorio — necesario para habilitar el otorgamiento Entratel en caso de continuar."},
            {"name": "email",     "label": "Correo electrónico",          "type": "email",    "required": True,  "placeholder": "andrea.ruffini@ejemplo.es",
             "helper": "A esta dirección enviamos la confirmación de la cita."},
            {"name": "phone",     "label": "Teléfono",        "type": "tel",      "required": True,  "placeholder": "+39 ...",
             "helper": "Para eventuales aclaraciones previas a la cita."},
            {"name": "area",      "label": "Área de competencia de interés", "type": "select", "required": True,
             "options": [
                 "Por definir en la cita",
                 "Declaración de la renta y fiscalidad ordinaria",
                 "Cuentas anuales y contabilidad ordinaria",
                 "Contencioso tributario",
                 "Planificación fiscal y patrimonial",
                 "Nóminas y asesoría laboral",
                 "Auditoría de cuentas",
             ],
             "helper": "Seleccione «Por definir» si la situación es compleja."},
            {"name": "time_slot", "label": "Franja horaria preferida", "type": "select", "required": True,
             "options": [
                 "Mañana 9:00 – 12:00",
                 "Primera tarde 14:00 – 16:30",
                 "Segunda tarde 16:30 – 18:30",
                 "Indiferente",
             ],
             "helper": "En proximidad de los vencimientos damos prioridad a las franjas de mañana."},
            {"name": "situation", "label": "Breve descripción de la situación", "type": "textarea",
             "required": True, "full_width": True,
             "placeholder": "Máximo 600 caracteres. Ejemplo: «Número de IVA en régimen de tanto alzado italiano (regime forfettario) desde 2021, primer año de salida del régimen, necesito entender cómo proceder con la contabilidad ordinaria».",
             "helper": "Lo justo para valorar si la situación entra dentro de nuestras áreas de competencia y preparar la primera conversación."},
        ],

        "form_sections": [
            {"num": "01", "title": "Contacto",
             "meta": "La persona con la que nos reuniremos en la primera cita.",
             "fields": ["name", "surname", "email", "phone"]},
            {"num": "02", "title": "Identificadores fiscales",
             "meta": "Obligatorio el Código Fiscal italiano; Número de IVA (Partita IVA) y razón social únicamente si la relación se refiere a una actividad empresarial.",
             "fields": ["fiscal_code", "vat", "company"]},
            {"num": "03", "title": "Perímetro de la reunión",
             "meta": "Para agendar al socio de referencia en la franja solicitada. Ningún detalle sensible aquí — los documentos se traen a la cita.",
             "fields": ["area", "time_slot", "situation"]},
            {"num": "04", "title": "Documentación (opcional)",
             "meta": "Última declaración de la renta, últimas cuentas anuales, eventuales comunicaciones de la Agencia Tributaria italiana: pueden adelantar la cita.",
             "fields": ["__upload__"]},
        ],

        "upload_field": {
            "name":     "allegati_preliminari",
            "label":    "Documentos preliminares",
            "helper":   "Última declaración de la renta italiana (Modello Redditi o 730), últimas cuentas anuales depositadas, comunicaciones recibidas de la Agencia Tributaria italiana. "
                        "PDF · máx. 10 MB en total. Archivo cifrado con acceso limitado a los socios.",
            "accept":   ".pdf",
            "multiple": True,
            "primary":  "Arrastre aquí los documentos o",
            "link":     "busque en el archivo",
            "meta":     "PDF · máx. 10 MB · archivo cifrado AES-256",
        },

        "form_submit_label": "Solicitar cita",
        "form_submit_note":
            "Confirmación por parte de un socio colegiado ODCEC en un plazo "
            "de 48 horas laborables. Ninguna secretaría externa, ninguna "
            "automatización — leemos personalmente cada solicitud.",
        "form_consent":
            "Consiento el tratamiento de los datos personales conforme al "
            "Reglamento UE 2016/679 (RGPD). Los datos se custodian en el "
            "archivo cifrado del despacho con retención decenal, acceso "
            "limitado a los socios y a los colaboradores colegiados. Ningún "
            "dato se comunica a terceros sin autorización expresa por escrito.",

        # Office meta-row labels (lifted from skin for i18n)
        "office_address_label": "Dirección",
        "office_area_label":    "Zona",
        "office_phone_label":   "Teléfono",
        "office_email_label":   "Correo",

        # Sidebar — sede + canales directos
        "offices_label":   "Sede",
        "offices": [
            {
                "city":    "Milán",
                "tag":     "Sede única",
                "address": "Via Melzo 14 · 20129",
                "area":    "Porta Venezia · a 200 metros de la estación MM Porta Venezia",
                "phone":   "+39 02 4951 3388",
                "email":   "segreteria@fiscusstudio.it",
            },
        ],

        "channels_label": "Canales directos",
        "channels": [
            ("Secretaría del despacho", "+39 02 4951 3388",           "Lun. – Vie. · 9:00 – 18:30"),
            ("Correo institucional",    "segreteria@fiscusstudio.it", "Respuesta en un plazo de 48 horas laborables"),
            ("Área de cliente reservada","area.fiscusstudio.it",       "Para clientes existentes — vencimientos y documentos"),
        ],

        "footnote":
            "Fiscus no responde a solicitudes anónimas y no emite opiniones "
            "fiscales preliminares por correo electrónico. La información "
            "administrativa (minuta de honorarios orientativa, modalidad de "
            "facturación, calendario de vencimientos del perímetro propuesto) "
            "se detalla en la primera cita — a título gratuito y sin "
            "compromiso de otorgamiento.",
    },
}
