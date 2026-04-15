"""Phase 2g3.7 · Session 53 · Lex — Spanish native-voice tree. Bar / cabinet / despacho / مكتب voice."""
from __future__ import annotations

from typing import Any


LEX_CONTENT_ES: dict[str, Any] = {
    "pages": [
        {"slug": "home",      "label": "Despacho",           "kind": "home"},
        {"slug": "studio",    "label": "El Despacho",        "kind": "about"},
        {"slug": "pratiche",  "label": "Áreas de práctica",  "kind": "services"},
        {"slug": "avvocati",  "label": "Nuestros Abogados",  "kind": "team"},
        {"slug": "notabili",  "label": "Asuntos relevantes", "kind": "blog_list"},
        {"slug": "contatti",  "label": "Contacto",           "kind": "contact"},
    ],

    # ─── SITE — chrome rendered by _base.html ─────────────────────
    "site": {
        "logo_initial":  "LF",
        "logo_word":     "Studio Legale Ferri",
        "tag":           "Colegio de Abogados de Roma · desde 1962",
        "phone":         "+39 06 4567 2300",
        "email":         "studio@studioferri.legal",
        "address":       "Via Piemonte 39 · 00187 Roma",
        "hours_compact": "Lunes – Viernes · 09:00 – 19:00",
        "hours_footer_rows": [
            "Sábado · solo con cita previa",
            "Domingo · cerrado",
        ],
        "license":       "Insc. Colegio de Abogados de Roma A18449 · N.I.F. 03124770581",
        "nav_cta":       "Solicitar consulta",
        "footer_intro":
            "Studio Legale Ferri — sesenta y dos años de "
            "ejercicio, dos sedes (Roma y Milán), catorce "
            "abogados colegiados. Competencia, reserva, "
            "resultados.",
        "foot_studio":  "El Despacho",
        "foot_pages":   "Páginas",
        "foot_contact": "Contacto",
        "foot_offices": "Sedes",
        "offices_footer_rows": [
            "Roma · via Piemonte 39",
            "Milán · corso Venezia 11",
        ],

        # Cross-page meta labels (lifted from skin so each locale picks
        # up the right translation). Used by blog_list/blog_detail and
        # by services / team chrome strips.
        "case_practice_label":  "Área",
        "case_year_label":      "Año",
        "case_outcome_label":   "Resultado",
        "case_lead_label":      "Socio responsable",
    },

    # ════════════════════════════════════════════════════════════
    # HOME (studio)
    # ════════════════════════════════════════════════════════════
    "home": {
        "eyebrow":    "Studio Legale Ferri · Roma · Milán · desde 1962",
        "headline":   "Competencia, <em>reserva</em>, resultados.",
        "intro":
            "Asesoramos a empresas, familias y profesionales con "
            "un enfoque riguroso, personalizado y discreto. "
            "Sesenta y dos años de ejercicio, dos sedes, catorce "
            "abogados colegiados. Cada encargo se sigue "
            "personalmente por un socio del despacho, desde la "
            "apertura del expediente hasta la firmeza de la "
            "resolución.",
        "primary_cta":   "Solicitar consulta confidencial",
        "primary_href":  "contatti",
        "secondary_cta": "Áreas de práctica",
        "secondary_href":"pratiche",

        # Hero — split-ledger-monogram silhouette
        # LEFT: gold vertical rule + eyebrow + serif drama headline + credit cells
        # RIGHT: monogram crest + meta_strip institutional rows
        "hero_credit_left":  ("Dirección",       "Prof. Abogado A. Ferri"),
        "hero_credit_right": ("Colegios",        "Roma · Milán"),
        "hero_meta_strip": [
            ("Sede principal",     "Roma · via Piemonte"),
            ("Socios fundadores",  "1962 · familia Ferri"),
            ("Abogados colegiados","14 · Colegio de Roma"),
        ],

        # Practice-area ledger — 4 numbered rows on home, full 12 on /pratiche
        "practice_label":   "Áreas de práctica",
        "practice_heading": "Doce disciplinas, una única <em>firma</em>.",
        "practice_intro":
            "Las áreas de práctica del despacho abarcan el "
            "derecho civil, mercantil, penal empresarial y "
            "administrativo. Cada encargo se coordina por un "
            "socio senior y nunca se delega íntegramente en "
            "colaboradores junior.",
        "practice": [
            ("01", "Derecho societario",
             "M&A, gobierno corporativo, contratación mercantil "
             "y operaciones de reestructuración. Ampliaciones "
             "de capital conforme al art. 2343 del Código "
             "Civil italiano con pericial jurada, fusiones "
             "transfronterizas, reestructuraciones de grupo, "
             "pactos parasociales."),
            ("02", "Derecho de familia y sucesiones",
             "Separaciones de mutuo acuerdo y contenciosas, "
             "divorcios, régimen de custodia, sucesiones "
             "internacionales, trusts familiares, donaciones "
             "y pactos sucesorios conforme al art. 768-bis del "
             "Código Civil italiano."),
            ("03", "Derecho laboral",
             "Litigio individual y colectivo, negociación "
             "colectiva de segundo nivel, seguridad laboral "
             "conforme al Decreto Legislativo 81/2008, "
             "despidos procedentes y objetivos, transacciones "
             "en sede sindical."),
            ("04", "Derecho penal empresarial",
             "Delitos societarios conforme a los arts. 2621-"
             "2641 del Código Civil italiano, responsabilidad "
             "administrativa de las personas jurídicas conforme "
             "al Decreto Legislativo 231/2001, delitos de "
             "cuello blanco, delitos fiscales conforme al "
             "Decreto Legislativo 74/2000, modelos de "
             "prevención y órganos de vigilancia."),
        ],

        # Stats band on dark ink — counter animation (D-081 binding)
        "stats_label":   "Sesenta y dos años de ejercicio",
        "stats_heading": "El despacho en cifras",
        "stats": [
            ("62",     "años de actividad"),
            ("14",     "abogados colegiados"),
            ("2.400+", "asuntos defendidos"),
            ("96%",    "resultados favorables"),
        ],

        # Partners portrait preview — 3 senior partners on home, 14 on /avvocati
        "partners_label":   "Dirección",
        "partners_heading": "Tres socios, una única dirección",
        "partners_intro":
            "Los socios del despacho firman personalmente "
            "cada acto. Ningún encargo se acepta sin previa "
            "verificación de conflictos de interés y sin "
            "atribución formal a un socio responsable.",
        "partners": [
            {
                "name":  "Avv. Prof. Alberto Ferri",
                "role":  "Socio director · Derecho societario",
                "foro":  "Colegio de Abogados de Roma desde 1986 · Letrado ante el Tribunal Supremo desde 1999",
                "bio":
                    "Hijo del fundador, dirige el despacho desde "
                    "2004. Profesor asociado de derecho mercantil "
                    "en LUISS Guido Carli. Autor de la obra "
                    "\"L'aumento di capitale nelle società quotate\" "
                    "(Giuffrè, 2018).",
            },
            {
                "name":  "Avv. Maria Grazia Conti",
                "role":  "Socia senior · Derecho de familia",
                "foro":  "Colegio de Abogados de Roma desde 1991 · Letrada ante el Tribunal Supremo desde 2003",
                "bio":
                    "Especialista en sucesiones internacionales "
                    "y pactos sucesorios. Colaboradora de la "
                    "revista \"Famiglia e Diritto\" desde 2007. "
                    "Mediadora familiar inscrita en el Registro "
                    "de Mediadores del Tribunal de Roma.",
            },
            {
                "name":  "Avv. Lorenzo Marchetti",
                "role":  "Socio · Derecho penal empresarial",
                "foro":  "Colegio de Abogados de Roma desde 1995 · Letrado ante el Tribunal Supremo desde 2007",
                "bio":
                    "Anteriormente fiscal de la Fiscalía de "
                    "Milán (1998-2003), hoy especializado en "
                    "materia del Decreto 231 y delitos "
                    "fiscales. Miembro del órgano de vigilancia "
                    "de tres grupos industriales cotizados en "
                    "Euronext Milán.",
            },
        ],

        # Publications ribbon — riviste + opere monografiche
        "publications_label": "Publicaciones y citas",
        "publications": [
            "FORO ITALIANO",
            "DIRITTO E GIUSTIZIA",
            "IL SOLE 24 ORE · LEGALE",
            "GUIDA AL DIRITTO",
            "CASSAZIONE PENALE",
            "RIVISTA DELLE SOCIETÀ",
        ],

        # Final CTA band — private-consultation ghost serif
        "cta_label":     "Consulta preliminar confidencial",
        "cta_heading":   "Una conversación preliminar con un socio.",
        "cta_intro":
            "El primer contacto se produce directamente con un "
            "socio del despacho. Se discute el alcance del "
            "encargo, el posible conflicto de interés y el "
            "arancel indicativo — antes de cualquier encargo "
            "formal y bajo estricta reserva profesional.",
        "cta_primary":      "Solicitar consulta",
        "cta_primary_href": "contatti",
        "cta_secondary":    "Conozca el despacho",
        "cta_secondary_href":"studio",
    },

    # ════════════════════════════════════════════════════════════
    # STUDIO (about) — storia, fondatori, metodo, valori, sedi
    # ════════════════════════════════════════════════════════════
    "studio": {
        "eyebrow":  "El Despacho · 1962 — 2026",
        "headline": "Sesenta y dos años de ejercicio, <em>dos generaciones</em> de la familia Ferri.",
        "intro":
            "Studio Legale Ferri nace en Roma en 1962 por "
            "iniciativa del Abogado Giuseppe Ferri, entonces "
            "magistrado dimisionario de treinta y dos años, con "
            "tres expedientes de derecho societario y un único "
            "pasante. Sesenta y dos años después, somos catorce "
            "abogados colegiados, dos sedes, un único órgano de "
            "gobierno — junto con la independencia del capital "
            "de terceros que el fundador estableció como primera "
            "regla de los estatutos.",

        # History timeline — sei date che hanno definito lo studio
        "history_label":   "Historia del despacho",
        "history_heading": "Seis fechas, sesenta y dos años",
        "history_intro":
            "Seis hitos que marcan la trayectoria del despacho — "
            "desde la fundación de 1962 al relevo generacional "
            "de 2004, hasta la apertura de la sede de Milán en "
            "2019. Detrás de cada una de estas fechas hay una "
            "decisión estructural de independencia, de práctica "
            "o de geografía que aún hoy orienta los encargos.",
        "history": [
            ("1962", "Fundación",
             "El Abogado Giuseppe Ferri, dimisionario de la "
             "magistratura, abre el despacho en via Piemonte "
             "39 con tres expedientes de derecho societario "
             "y un único pasante."),
            ("1978", "Inscripción como letrado ante el Tribunal Supremo",
             "Tras dieciséis años de actuación ante los "
             "tribunales de instancia, el fundador es inscrito "
             "en el Turno especial de Letrados del Tribunal "
             "Supremo — el despacho civil puede actuar ante "
             "la Corte Suprema italiana directamente, sin "
             "procurador local."),
            ("1989", "Práctica penal empresarial",
             "El despacho constituye un departamento autónomo "
             "de derecho penal empresarial, anticipándose una "
             "década al Decreto Legislativo 231/2001. Los "
             "primeros modelos de prevención se redactan para "
             "dos grupos industriales del sector "
             "metalomecánico."),
            ("2004", "Relevo generacional",
             "El Prof. Abogado Alberto Ferri asume la dirección "
             "del despacho. El fundador mantiene la condición "
             "de Senior of Counsel hasta 2014. Los estatutos "
             "se actualizan para regular la incorporación de "
             "nuevos socios por cooptación, nunca por "
             "adquisición."),
            ("2014", "Práctica de sucesiones internacionales",
             "Con la entrada en vigor del Reglamento UE "
             "650/2012 en materia de sucesiones "
             "transfronterizas, el despacho constituye una "
             "práctica específica. Los primeros encargos "
             "afectan a familias empresariales italianas con "
             "patrimonios en Suiza y Luxemburgo."),
            ("2019", "Apertura de la sede de Milán",
             "Para acompañar los encargos de derecho "
             "societario y M&A del Norte, el despacho abre "
             "su segunda sede en corso Venezia 11. Tres "
             "socios y dos colaboradores permanentes. Las "
             "dos sedes mantienen un único órgano de gobierno "
             "y ninguna lista de conflictos autónoma."),
        ],

        # Method — quattro principi non negoziabili
        "values_label":   "Método",
        "values_heading": "Cuatro principios <em>innegociables</em>",
        "values_intro":
            "Son las cuatro reglas que distinguen un encargo "
            "Studio Ferri de una actuación legal estándar. "
            "Figuran en la hoja de encargo, no en material de "
            "marketing.",
        "values": [
            ("01", "Confidencialidad absoluta",
             "El secreto profesional conforme al art. 622 "
             "del Código Penal italiano se aplica en su "
             "acepción más amplia: las identidades de los "
             "clientes nunca se divulgan, ni siquiera en "
             "forma anonimizada, sin consentimiento escrito "
             "expreso. El despacho no publica historiales "
             "nominativos ni cita a clientes en material "
             "promocional."),
            ("02", "Un socio por cada encargo",
             "Cada expediente se sigue personalmente por un "
             "socio de la asociación profesional, desde la "
             "apertura hasta la firmeza. El socio firma los "
             "actos sustanciales y participa en las vistas "
             "de fondo. Ningún encargo se delega íntegramente "
             "en colaboradores junior, jamás."),
            ("03", "Verificación rigurosa de conflictos",
             "Antes de la aceptación de cualquier nuevo "
             "encargo, el Compliance Officer interno verifica "
             "la ausencia de conflictos de interés respecto "
             "de la cartera activa de clientes y los encargos "
             "cerrados en los últimos cinco años. En caso de "
             "duda, el encargo se rechaza preventivamente."),
            ("04", "Aranceles transparentes",
             "Los honorarios profesionales se acuerdan por "
             "escrito en la hoja de encargo conforme a los "
             "parámetros del DM 55/2014. Los honorarios de "
             "éxito se admiten solo dentro de los límites "
             "del Código Deontológico Forense. Sin "
             "retrocesiones, sin acuerdos verbales con "
             "contrapartes."),
        ],

        # Coordinates strip — le due sedi
        "coordinates_label": "Nuestras sedes",
        "coordinates": [
            ("Roma",     "Via Piemonte 39 · 00187 · Barrio del Quirinale"),
            ("Milán",    "Corso Venezia 11 · 20121 · Barrio de Porta Venezia"),
        ],

        # Page-level CTA
        "cta_heading":  "Una evaluación preliminar confidencial.",
        "cta_intro":
            "La primera entrevista se mantiene directamente "
            "con un socio del despacho. Se discute el alcance "
            "del encargo, el posible conflicto de interés y "
            "el arancel indicativo, bajo estricta reserva.",
        "cta_primary":      "Solicitar consulta",
        "cta_primary_href": "contatti",
    },

    # ════════════════════════════════════════════════════════════
    # PRATICHE (services) — 12 aree di pratica
    # ════════════════════════════════════════════════════════════
    "pratiche": {
        "eyebrow":  "Áreas de práctica · 2026",
        "headline": "Doce disciplinas, una única <em>firma</em>.",
        "intro":
            "Las doce áreas de práctica del despacho. Cada "
            "cliente accede a un equipo multidisciplinar — no "
            "se factura por separado por cada práctica; el "
            "encargo cubre la combinación de competencias "
            "necesarias para resolver el asunto planteado.",

        # Card meta labels (lifted from skin for locale support)
        "svc_lead_label":     "Socio responsable",
        "svc_jurisdiction_label": "Colegio de referencia",

        # 12 services in airy ledger
        "services": [
            {
                "num":     "01",
                "title":   "Derecho societario",
                "blurb":
                    "Constitución de sociedades, gobierno "
                    "corporativo, pactos parasociales, "
                    "operaciones de reestructuración. "
                    "Ampliaciones de capital conforme al art. "
                    "2343 del Código Civil italiano con "
                    "pericial jurada, fusiones transfronterizas "
                    "conforme al Decreto Legislativo 108/2008, "
                    "transformaciones heterogéneas, escisiones "
                    "proporcionales y no proporcionales.",
                "scope": [
                    "Constitución y estatutos sociales",
                    "Ampliaciones de capital y pericial art. 2343",
                    "Pactos parasociales y gobierno corporativo",
                    "Fusiones, escisiones, transformaciones",
                ],
                "lead":   "Avv. Prof. Alberto Ferri",
                "jurisdiction": "Colegios de Roma · Milán · Bruselas",
            },
            {
                "num":     "02",
                "title":   "M&A y operaciones de reestructuración",
                "blurb":
                    "Due diligence, redacción de SPA y pactos "
                    "parasociales, negociación, integración "
                    "post-adquisición. Actuamos en el lado "
                    "vendedor o en el lado comprador, nunca "
                    "en ambos en el mismo expediente. Tipología: "
                    "carve-out, joint ventures, salidas de "
                    "capital privado, MBO familiares.",
                "scope": [
                    "Due diligence legal vendor-side",
                    "Due diligence comprador y SPA",
                    "Pactos parasociales y earn-out",
                    "Integración post-fusión 100 días",
                ],
                "lead":   "Avv. Prof. Alberto Ferri",
                "jurisdiction": "Colegios de Roma · Milán",
            },
            {
                "num":     "03",
                "title":   "Derecho de familia",
                "blurb":
                    "Separaciones de mutuo acuerdo y "
                    "contenciosas, divorcios, régimen de "
                    "custodia de menores, modificaciones de "
                    "las condiciones de separación y divorcio. "
                    "Mediación familiar en fase "
                    "pre-contenciosa conforme al art. 5 del "
                    "Decreto Legislativo 28/2010.",
                "scope": [
                    "Separaciones de mutuo acuerdo y contenciosas",
                    "Divorcios contenciosos y consensuados",
                    "Custodia y pensión de alimentos de menores",
                    "Mediación familiar",
                ],
                "lead":   "Avv. Maria Grazia Conti",
                "jurisdiction": "Colegios de Roma · Milán",
            },
            {
                "num":     "04",
                "title":   "Sucesiones y patrimonios",
                "blurb":
                    "Sucesiones nacionales e internacionales "
                    "conforme al Reg. UE 650/2012, redacción "
                    "de testamentos públicos y ológrafos, "
                    "particiones hereditarias, donaciones y "
                    "pactos sucesorios conforme al art. "
                    "768-bis del Código Civil italiano. "
                    "Trusts familiares regidos por el Convenio "
                    "de La Haya.",
                "scope": [
                    "Planificación sucesoria internacional",
                    "Testamentos y pactos sucesorios",
                    "Particiones hereditarias y arbitrajes",
                    "Trusts y fundaciones familiares",
                ],
                "lead":   "Avv. Maria Grazia Conti",
                "jurisdiction": "Colegios de Roma · Milán · Lugano",
            },
            {
                "num":     "05",
                "title":   "Derecho laboral",
                "blurb":
                    "Litigio individual y colectivo, "
                    "negociación colectiva de segundo nivel, "
                    "seguridad laboral conforme al Decreto "
                    "Legislativo 81/2008, despidos conforme "
                    "al art. 18 del Estatuto de los "
                    "Trabajadores y al Jobs Act, transacciones "
                    "en sede sindical conforme al art. 411 "
                    "del Código Procesal Civil italiano.",
                "scope": [
                    "Litigio laboral individual y colectivo",
                    "Despidos procedentes y por causas objetivas",
                    "Negociación colectiva de segundo nivel",
                    "Seguridad laboral y Decreto 81/2008",
                ],
                "lead":   "Avv. Federica Ronchi",
                "jurisdiction": "Colegios de Roma · Milán",
            },
            {
                "num":     "06",
                "title":   "Derecho penal empresarial",
                "blurb":
                    "Delitos societarios conforme a los arts. "
                    "2621-2641 del Código Civil italiano, "
                    "responsabilidad administrativa de las "
                    "personas jurídicas conforme al Decreto "
                    "Legislativo 231/2001, delitos de cuello "
                    "blanco, delitos fiscales conforme al "
                    "Decreto Legislativo 74/2000. Defensa de "
                    "administradores, auditores legales y "
                    "miembros de órganos de vigilancia.",
                "scope": [
                    "Defensa en procedimientos Decreto 231",
                    "Delitos societarios y fiscales",
                    "Modelos de prevención y órganos de vigilancia",
                    "Investigaciones internas y canal de denuncias",
                ],
                "lead":   "Avv. Lorenzo Marchetti",
                "jurisdiction": "Colegios de Roma · Milán · Tribunal Supremo",
            },
            {
                "num":     "07",
                "title":   "Contratación mercantil",
                "blurb":
                    "Redacción y negociación de contratos "
                    "mercantiles italianos e internacionales "
                    "— distribución, agencia, franquicia, "
                    "joint ventures, licencias. Convención "
                    "de Viena de 1980 sobre compraventa "
                    "internacional de mercaderías.",
                "scope": [
                    "Distribución y agencia mercantil",
                    "Franquicia y joint ventures",
                    "Licencias PI y know-how",
                    "Contratos internacionales (CISG)",
                ],
                "lead":   "Avv. Stefano Bellini",
                "jurisdiction": "Colegios de Roma · Milán · Bruselas",
            },
            {
                "num":     "08",
                "title":   "Derecho bancario y financiero",
                "blurb":
                    "Operaciones de financiación, garantías "
                    "reales y personales, litigio bancario, "
                    "anatocismo, usura, renegociaciones, "
                    "derivados. Supervisión del Banco de "
                    "Italia, normativa CRR/CRD IV, MAR y "
                    "abuso de mercado.",
                "scope": [
                    "Financiación corporativa y LBO",
                    "Litigio bancario y usura",
                    "Instrumentos derivados (IRS, FX)",
                    "Supervisión Banco de Italia · MAR",
                ],
                "lead":   "Avv. Caterina Albini",
                "jurisdiction": "Colegios de Roma · Milán",
            },
            {
                "num":     "09",
                "title":   "Derecho administrativo",
                "blurb":
                    "Litigio ante los TAR y el Consejo de "
                    "Estado italiano, contratación pública "
                    "conforme al Decreto Legislativo 36/2023, "
                    "concesiones, autorizaciones urbanísticas, "
                    "derecho de acceso a documentos conforme "
                    "a la ley 241/1990, recursos "
                    "extraordinarios al Jefe del Estado.",
                "scope": [
                    "Contratación pública y concesiones",
                    "Autorizaciones urbanísticas y VIA",
                    "Derecho de acceso y transparencia",
                    "Recursos TAR y Consejo de Estado",
                ],
                "lead":   "Avv. Giulio Mancini",
                "jurisdiction": "Colegio de Roma · TAR Lazio",
            },
            {
                "num":     "10",
                "title":   "Inmobiliario",
                "blurb":
                    "Adquisiciones y transmisiones de carteras "
                    "inmobiliarias, operaciones de desarrollo, "
                    "fondos inmobiliarios, arrendamientos "
                    "comerciales, litigio de propiedad "
                    "horizontal. Comprobaciones urbanísticas "
                    "y catastrales, escrituras notariales "
                    "coordinadas con notario de confianza.",
                "scope": [
                    "Adquisiciones y transmisiones inmobiliarias",
                    "Desarrollo y fondos inmobiliarios",
                    "Arrendamientos comerciales (Ley 392/78)",
                    "Litigio de propiedad horizontal",
                ],
                "lead":   "Avv. Stefano Bellini",
                "jurisdiction": "Colegios de Roma · Milán",
            },
            {
                "num":     "11",
                "title":   "Protección de datos personales",
                "blurb":
                    "Cumplimiento del Reglamento UE 679/2016 "
                    "(RGPD), cartografía de datos, EIPD, "
                    "nombramiento de DPD, registro de "
                    "actividades de tratamiento, gestión de "
                    "brechas de seguridad, litigio ante la "
                    "Autoridad Garante italiana. AI Act y "
                    "elaboración de perfiles algorítmicos.",
                "scope": [
                    "Cumplimiento RGPD y EIPD",
                    "Nombramiento DPD y registro de tratamientos",
                    "Brechas de seguridad y notificación a la Autoridad",
                    "AI Act y elaboración de perfiles algorítmicos",
                ],
                "lead":   "Avv. Caterina Albini",
                "jurisdiction": "Colegios de Roma · Milán",
            },
            {
                "num":     "12",
                "title":   "Arbitraje y ADR",
                "blurb":
                    "Arbitraje ad hoc e institucional (CCI, "
                    "CAM, ICC, LCIA), mediación civil y "
                    "mercantil conforme al Decreto Legislativo "
                    "28/2010, negociación asistida conforme al "
                    "Decreto-ley 132/2014, pericial contractual.",
                "scope": [
                    "Arbitraje CCI / CAM / ICC / LCIA",
                    "Mediación civil y mercantil",
                    "Negociación asistida",
                    "Pericial contractual y arbitraje",
                ],
                "lead":   "Avv. Prof. Alberto Ferri",
                "jurisdiction": "Colegios de Roma · Milán · Cámara Arbitral",
            },
        ],

        # Process strip — come si svolge un mandato
        "process_label":   "Iter del encargo",
        "process_heading": "Cuatro fases, una única secuencia",
        "process": [
            ("01", "Entrevista preliminar confidencial",
             "Primer encuentro con un socio del despacho. Se "
             "discute el alcance, el posible conflicto de "
             "interés y el arancel indicativo. Sin propuesta "
             "escrita en esta fase, solo evaluación de "
             "viabilidad."),
            ("02", "Hoja de encargo",
             "En un plazo de cinco días, hoja de encargo "
             "escrita con alcance detallado, entregables, "
             "calendario y arancel profesional conforme al "
             "DM 55/2014. El encargo se formaliza únicamente "
             "con la firma de ambas partes."),
            ("03", "Ejecución y defensa",
             "El socio responsable firma personalmente los "
             "actos sustanciales y participa en las vistas "
             "de fondo. El cliente recibe informes escritos "
             "periódicos sobre el estado del expediente, "
             "nunca por vía telemática sin cifrar."),
            ("04", "Cierre y archivo",
             "Al alcanzarse la firmeza o al cierre del "
             "encargo, carta de cierre confidencial con "
             "síntesis del resultado y dictamen final. "
             "Archivo cifrado durante diez años conforme al "
             "Código Deontológico Forense."),
        ],

        # Final CTA
        "cta_heading":  "¿Qué área se ajusta a su caso?",
        "cta_intro":
            "Si el alcance aún no está claro, envíe una "
            "breve descripción del problema a la secretaría "
            "del despacho. Le orientaremos al socio competente "
            "en un plazo de cuarenta y ocho horas, aun cuando "
            "el encargo no encaje finalmente entre los "
            "aceptables.",
        "cta_primary":      "Escríbanos",
        "cta_primary_href": "contatti",
    },

    # ════════════════════════════════════════════════════════════
    # AVVOCATI (team) — 14 avvocati abilitati
    # ════════════════════════════════════════════════════════════
    "avvocati": {
        "eyebrow":  "Nuestros Abogados · 14 colegiados",
        "headline": "Catorce abogados, <em>una sola</em> dirección.",
        "intro":
            "El despacho está integrado por catorce abogados "
            "colegiados en los Colegios de Roma y Milán — "
            "seis socios de la asociación profesional y ocho "
            "abogados asociados. La selección se realiza por "
            "cooptación, no por adquisición: cada incorporación "
            "requiere la unanimidad de los socios.",

        # Card meta labels
        "lawyer_foro_label":  "Colegio",
        "lawyer_year_label":  "Colegiación",
        "lawyer_specialization_label": "Especialización",

        # 14 avvocati — 6 soci + 8 associati
        "lawyers": [
            {
                "name":  "Avv. Prof. Alberto Ferri",
                "role":  "Socio director",
                "specialization": "Derecho societario · M&A · Arbitraje",
                "foro":  "Colegio de Abogados de Roma",
                "year":  "Colegiado desde 1986 · Letrado ante el Tribunal Supremo desde 1999",
                "bio":
                    "Hijo del fundador, dirige el despacho "
                    "desde 2004. Profesor asociado de derecho "
                    "mercantil en LUISS Guido Carli. Autor de "
                    "la obra \"L'aumento di capitale nelle "
                    "società quotate\" (Giuffrè, 2018) y de "
                    "numerosos artículos en la \"Rivista "
                    "delle Società\".",
            },
            {
                "name":  "Avv. Maria Grazia Conti",
                "role":  "Socia senior",
                "specialization": "Derecho de familia · Sucesiones",
                "foro":  "Colegio de Abogados de Roma",
                "year":  "Colegiada desde 1991 · Letrada ante el Tribunal Supremo desde 2003",
                "bio":
                    "Especialista en sucesiones "
                    "internacionales y pactos sucesorios. "
                    "Colaboradora de la revista \"Famiglia "
                    "e Diritto\" desde 2007. Mediadora "
                    "familiar inscrita en el Registro de "
                    "Mediadores del Tribunal de Roma.",
            },
            {
                "name":  "Avv. Lorenzo Marchetti",
                "role":  "Socio",
                "specialization": "Penal empresarial · Decreto 231",
                "foro":  "Colegio de Abogados de Roma · Tribunal Supremo",
                "year":  "Colegiado desde 1995 · Letrado ante el Tribunal Supremo desde 2007",
                "bio":
                    "Anteriormente fiscal de la Fiscalía de "
                    "la República de Milán (1998-2003). "
                    "Miembro del órgano de vigilancia de tres "
                    "grupos industriales cotizados en Euronext "
                    "Milán. Docente en la Escuela de "
                    "Especialización para las Profesiones "
                    "Jurídicas.",
            },
            {
                "name":  "Avv. Federica Ronchi",
                "role":  "Socia",
                "specialization": "Derecho laboral · Seguridad",
                "foro":  "Colegios de Roma · Milán",
                "year":  "Colegiada desde 1999",
                "bio":
                    "Especialista en despidos colectivos y "
                    "negociación colectiva de segundo nivel. "
                    "Asesora de tres grandes empresas del "
                    "sector industrial en la negociación "
                    "sindical. Miembro del Comité de Igualdad "
                    "de Oportunidades del Colegio de Abogados "
                    "de Roma.",
            },
            {
                "name":  "Avv. Stefano Bellini",
                "role":  "Socio",
                "specialization": "Contratación mercantil · Inmobiliario",
                "foro":  "Colegios de Roma · Bruselas",
                "year":  "Colegiado desde 2001",
                "bio":
                    "Experto en contratación mercantil "
                    "internacional y operaciones "
                    "inmobiliarias complejas. Colegiado en "
                    "el Colegio de Bruselas para asuntos de "
                    "derecho comunitario. LL.M. en "
                    "International Business Law por "
                    "Université Libre de Bruxelles.",
            },
            {
                "name":  "Avv. Caterina Albini",
                "role":  "Socia",
                "specialization": "Bancario · RGPD y datos",
                "foro":  "Colegio de Abogados de Milán",
                "year":  "Colegiada desde 2003",
                "bio":
                    "Coordina el departamento bancario de la "
                    "sede de Milán. Especialista en derivados "
                    "e instrumentos financieros complejos. "
                    "DPD certificada conforme al esquema UNI "
                    "11697:2017. Autora de \"GDPR e "
                    "responsabilità del titolare\" (Wolters "
                    "Kluwer, 2021).",
            },
            {
                "name":  "Avv. Giulio Mancini",
                "role":  "Of counsel",
                "specialization": "Derecho administrativo · Contratación pública",
                "foro":  "Colegio de Abogados de Roma · TAR Lazio",
                "year":  "Colegiado desde 1998",
                "bio":
                    "Anteriormente magistrado del TAR del "
                    "Lazio (2002-2014), hoy abogado en parte "
                    "en los contenciosos ante los TAR y el "
                    "Consejo de Estado italiano. Especialista "
                    "en contratación pública y concesiones "
                    "de servicios. Miembro del Consejo "
                    "Directivo de AIDA.",
            },
            {
                "name":  "Avv. Beatrice Lazzaro",
                "role":  "Abogada asociada",
                "specialization": "Penal empresarial · Investigaciones internas",
                "foro":  "Colegio de Abogados de Roma",
                "year":  "Colegiada desde 2008",
                "bio":
                    "Colaboradora del departamento de derecho "
                    "penal empresarial desde 2010. "
                    "Especializada en investigaciones internas "
                    "empresariales y canal de denuncias "
                    "conforme al Decreto Legislativo 24/2023. "
                    "Docente del Máster en Compliance 231 de "
                    "la Universidad LUMSA.",
            },
            {
                "name":  "Avv. Marco Vergani",
                "role":  "Abogado asociado",
                "specialization": "M&A · Derecho societario",
                "foro":  "Colegio de Abogados de Milán",
                "year":  "Colegiado desde 2011",
                "bio":
                    "Coordinador de la sede de Milán para las "
                    "operaciones de M&A mid-market. "
                    "Experiencia previa en un destacado "
                    "despacho internacional. Especialista en "
                    "operaciones cross-border Italia-DACH, "
                    "en particular con contrapartes alemanas "
                    "y suizas.",
            },
            {
                "name":  "Avv. Sara Donati",
                "role":  "Abogada asociada",
                "specialization": "Derecho de familia · Menores",
                "foro":  "Colegio de Abogados de Roma",
                "year":  "Colegiada desde 2013",
                "bio":
                    "Especializada en los procedimientos "
                    "relativos a la custodia de menores y en "
                    "los procedimientos ante el Tribunal de "
                    "Menores. Defensora judicial del menor "
                    "en procedimientos de adopción. Máster "
                    "en Derecho de Familia por la Universidad "
                    "de Roma Tre.",
            },
            {
                "name":  "Avv. Tommaso Ricci",
                "role":  "Abogado asociado",
                "specialization": "Laboral · Litigio colectivo",
                "foro":  "Colegio de Abogados de Milán",
                "year":  "Colegiado desde 2014",
                "bio":
                    "Sede de Milán. Especializado en litigio "
                    "colectivo laboral y procedimientos "
                    "conforme a la ley 223/1991 (despidos "
                    "colectivos). Experiencia previa en la "
                    "dirección legal de un grupo industrial "
                    "cotizado del sector manufacturero.",
            },
            {
                "name":  "Avv. Elisa Falcone",
                "role":  "Abogada asociada",
                "specialization": "Bancario · Litigio de usura",
                "foro":  "Colegio de Abogados de Milán",
                "year":  "Colegiada desde 2015",
                "bio":
                    "Especializada en litigio bancario y en "
                    "las acciones de declaración de "
                    "anatocismo y usura. Coordina la sección "
                    "bancaria de la sede de Milán. Máster "
                    "en Derecho Bancario por la Universidad "
                    "Bocconi.",
            },
            {
                "name":  "Avv. Riccardo Zambelli",
                "role":  "Abogado asociado",
                "specialization": "Administrativo · Urbanismo",
                "foro":  "Colegio de Abogados de Roma · TAR Lazio",
                "year":  "Colegiado desde 2016",
                "bio":
                    "Colabora en la práctica administrativa "
                    "con foco en el urbanismo, la evaluación "
                    "de impacto ambiental (VIA) y las "
                    "autorizaciones paisajísticas. "
                    "Experiencia previa en el departamento "
                    "legal de un gran operador de "
                    "infraestructuras.",
            },
            {
                "name":  "Avv. Chiara Tomei",
                "role":  "Abogada asociada",
                "specialization": "Datos personales · AI Act · Tech",
                "foro":  "Colegio de Abogados de Milán",
                "year":  "Colegiada desde 2019",
                "bio":
                    "Especializada en protección de datos "
                    "personales, con foco en los temas "
                    "emergentes de inteligencia artificial "
                    "generativa y cumplimiento del AI Act "
                    "(Reg. UE 2024/1689). Máster en Derecho "
                    "de las Nuevas Tecnologías por la "
                    "Universidad de Pavía.",
            },
        ],
    },

    # ════════════════════════════════════════════════════════════
    # NOTABILI (blog_list) — cause notabili e pubblicazioni
    # ════════════════════════════════════════════════════════════
    "notabili": {
        "eyebrow":  "Asuntos relevantes y publicaciones · 2018 — 2026",
        "headline": "Seis encargos seleccionados, <em>en pleno respeto</em> del secreto profesional.",
        "intro":
            "Una selección de asuntos relevantes y "
            "publicaciones recientes. Por reserva profesional "
            "y en cumplimiento del art. 622 del Código Penal "
            "italiano, las identidades de los clientes nunca "
            "se indican: los asuntos se identifican por sector "
            "industrial y por alcance técnico, las "
            "publicaciones por revista y materia tratada.",

        # Lead post + list — 6 posts referenced below
        "lead_image": "https://images.pexels.com/photos/5668858/pexels-photo-5668858.jpeg?auto=compress&cs=tinysrgb&w=1200&h=800&fit=crop",
    },

    # Posts powering blog_detail. URL: /notabili/<slug>/
    "posts": [
        {
            "slug":     "aumento-capitale-quotata-2343cc",
            "kicker":   "Derecho societario",
            "title":    "Ampliación de capital conforme al art. 2343 del Código Civil italiano de sociedad cotizada · pericial jurada · 2024",
            "date":     "Marzo 2024",
            "read_min": "8",
            "author":   "Avv. Prof. Alberto Ferri",
            "lede":
                "Por encargo de un grupo industrial cotizado "
                "del sector energético, el despacho asistió al "
                "consejo de administración en la deliberación "
                "y ejecución de una ampliación de capital en "
                "especie por 145 millones de euros, con "
                "aportación de una filial extranjera valorada "
                "mediante pericial jurada conforme al art. "
                "2343 del Código Civil italiano.",
            "body": [
                ("p",
                 "El encargo abarcó toda la fase deliberativa, "
                 "desde la redacción del informe explicativo "
                 "del consejo de administración conforme al "
                 "art. 2441 del Código Civil italiano hasta "
                 "la designación por el Tribunal de Roma del "
                 "experto encargado de la pericial jurada de "
                 "valoración de la filial aportada."),
                ("h2", "El marco normativo"),
                ("p",
                 "La operación se desarrolló en pleno respeto "
                 "del art. 2343 del Código Civil italiano "
                 "(pericial jurada) y del art. 2441 del "
                 "Código Civil italiano (derecho de "
                 "suscripción preferente), con exclusión del "
                 "derecho de suscripción preferente en favor "
                 "de un inversor institucional identificado "
                 "por el consejo. El procedimiento exigió "
                 "informe específico del órgano de auditores "
                 "conforme al art. 2441 apartado 6 del "
                 "Código Civil italiano."),
                ("h2", "El papel del despacho"),
                ("p",
                 "El despacho coordinó las relaciones con la "
                 "Consob para el depósito del folleto de la "
                 "oferta, con el Tribunal de Roma para la "
                 "designación del perito, con el notario "
                 "para el acta de la junta general "
                 "extraordinaria y con el auditor de cuentas "
                 "para las comprobaciones sucesivas conforme "
                 "al art. 2343-bis del Código Civil italiano."),
                ("blockquote",
                 "El respeto del procedimiento del art. 2343 "
                 "del Código Civil italiano es condición de "
                 "validez de la ampliación de capital. "
                 "Cualquier simplificación operativa que "
                 "pretenda comprimir los plazos legales "
                 "expone la operación al riesgo de nulidad."),
            ],
        },
        {
            "slug":     "modello-231-gruppo-utility",
            "kicker":   "Penal empresarial",
            "title":    "Modelo de prevención conforme al Decreto Legislativo 231/2001 para grupo utility cotizado",
            "date":     "Noviembre 2024",
            "read_min": "11",
            "author":   "Avv. Lorenzo Marchetti",
            "lede":
                "El despacho redactó el modelo de prevención "
                "conforme al Decreto Legislativo 231/2001 "
                "para un grupo utility cotizado tras la "
                "renovación de su órgano de vigilancia. El "
                "encargo incluyó el mapeo de riesgos "
                "delictivos, el diseño de los protocolos "
                "operativos y la formación interna a sesenta "
                "y dos directivos.",
            "body": [
                ("p",
                 "El encargo tuvo una duración de nueve meses "
                 "y se desarrolló en tres flujos paralelos: "
                 "mapeo de riesgos delictivos presuntos, "
                 "rediseño de los protocolos operativos, "
                 "formación obligatoria al personal expuesto."),
                ("h2", "Mapeo de riesgos delictivos"),
                ("p",
                 "Se mapearon los veintidós delitos presuntos "
                 "relevantes para el sector utility, con "
                 "especial atención a los delitos ambientales "
                 "conforme al art. 25-undecies del Decreto "
                 "Legislativo 231/2001 y a los delitos contra "
                 "la administración pública conforme al art. "
                 "25 del Decreto Legislativo 231/2001. El "
                 "mapeo requirió entrevistas con cuarenta "
                 "process owners."),
                ("h2", "Diseño de los protocolos"),
                ("p",
                 "Los protocolos operativos se rediseñaron "
                 "conforme al principio de separación de "
                 "funciones y trazabilidad documental. Se "
                 "prestó especial atención a los procesos de "
                 "aprovisionamiento, a las licitaciones "
                 "públicas y a la gestión de las relaciones "
                 "con la administración pública."),
            ],
        },
        {
            "slug":     "successione-internazionale-reg-650",
            "kicker":   "Sucesiones internacionales",
            "title":    "Sucesión internacional conforme al Reg. UE 650/2012 · familia empresarial Italia-Suiza",
            "date":     "Septiembre 2024",
            "read_min": "9",
            "author":   "Avv. Maria Grazia Conti",
            "lede":
                "Para una familia empresarial del Noreste "
                "italiano con patrimonios en Italia, Suiza y "
                "Luxemburgo, el despacho coordinó la apertura "
                "de la sucesión del causante — domiciliado en "
                "Lugano desde hacía más de veinte años — "
                "conforme al Reglamento UE 650/2012.",
            "body": [
                ("p",
                 "La sucesión planteó cuestiones complejas de "
                 "derecho internacional privado, en "
                 "particular sobre la professio iuris "
                 "conforme al art. 22 del Reg. 650/2012 a "
                 "favor de la ley italiana, ejercida por el "
                 "causante mediante testamento ológrafo "
                 "redactado en Lugano en 2018."),
                ("h2", "Coordinación multi-jurisdiccional"),
                ("p",
                 "El despacho coordinó las relaciones con el "
                 "notario italiano para la aceptación de la "
                 "herencia, con la fiduciaria suiza para la "
                 "partición de las cuentas bancarias y con "
                 "el Colegio de Luxemburgo para la "
                 "liquidación de una holding luxemburguesa."),
                ("h2", "Resultado"),
                ("p",
                 "Todo el procedimiento se cerró en catorce "
                 "meses, con acuerdo divisorio ratificado "
                 "ante el notario de Roma. Sin contencioso "
                 "judicial, impuesto de sucesiones liquidado "
                 "según tabla."),
            ],
        },
        {
            "slug":     "ferri-aumento-capitale-giuffre-2018",
            "kicker":   "Publicación monográfica",
            "title":    "\"L'aumento di capitale nelle società quotate\" · Giuffrè · 2018",
            "date":     "2018",
            "read_min": "5",
            "author":   "Avv. Prof. Alberto Ferri",
            "lede":
                "La monografía, editada por Giuffrè Francis "
                "Lefebvre en 2018, recoge la experiencia "
                "profesional del autor en materia de "
                "ampliaciones de capital de sociedades "
                "cotizadas en los mercados regulados "
                "italianos. La obra se adopta hoy en tres "
                "universidades italianas como texto de "
                "referencia del curso de derecho mercantil.",
            "body": [
                ("p",
                 "La obra se articula en doce capítulos que "
                 "recorren las distintas tipologías de "
                 "ampliación de capital: en efectivo, en "
                 "especie, liberadas, reservadas, con "
                 "exclusión del derecho de suscripción "
                 "preferente."),
                ("h2", "Estructura de la obra"),
                ("p",
                 "Los cuatro primeros capítulos abordan la "
                 "regulación general conforme a los arts. "
                 "2438-2444 del Código Civil italiano. Los "
                 "capítulos centrales profundizan en los "
                 "supuestos especiales — ampliaciones "
                 "delegadas al consejo de administración, "
                 "ampliaciones escindibles e inescindibles, "
                 "ampliaciones con warrants. Los tres últimos "
                 "capítulos se dedican a las particularidades "
                 "de las sociedades cotizadas."),
            ],
        },
        {
            "slug":     "licenziamento-collettivo-l-223-91",
            "kicker":   "Derecho laboral",
            "title":    "Procedimiento de despido colectivo conforme a la Ley 223/1991 · grupo manufacturero",
            "date":     "Mayo 2024",
            "read_min": "7",
            "author":   "Avv. Federica Ronchi",
            "lede":
                "El despacho asistió a un grupo "
                "manufacturero del sector metalomecánico en "
                "el procedimiento de despido colectivo "
                "conforme a la Ley 223/1991, concluido con "
                "acuerdo sindical y recolocación del 78% "
                "del personal excedente.",
            "body": [
                ("p",
                 "El procedimiento afectó a ciento cuarenta "
                 "puestos de trabajo y se desarrolló en dos "
                 "fases — examen conjunto a nivel empresarial "
                 "conforme al art. 4 de la Ley 223/1991 y "
                 "examen sucesivo a nivel ministerial ante "
                 "el Ministerio de Trabajo."),
                ("h2", "El acuerdo sindical"),
                ("p",
                 "El acuerdo, suscrito con todas las "
                 "organizaciones sindicales representativas, "
                 "previó la activación de un fondo bilateral "
                 "de recualificación, el incentivo a la "
                 "salida para los trabajadores de mayor edad "
                 "y un plan de recolocación interna para el "
                 "personal restante."),
                ("h2", "Resultado cuantitativo"),
                ("p",
                 "Sobre los ciento cuarenta empleados "
                 "afectados, veintiocho se adhirieron al "
                 "incentivo a la salida, ochenta y tres "
                 "fueron recolocados en otras líneas "
                 "productivas, veintinueve fueron apoyados "
                 "por el fondo bilateral de outplacement."),
            ],
        },
        {
            "slug":     "carve-out-dach-mid-cap-2023",
            "kicker":   "M&A cross-border",
            "title":    "Carve-out y cesión de división industrial a operador alemán · 2023",
            "date":     "Diciembre 2023",
            "read_min": "10",
            "author":   "Avv. Marco Vergani",
            "lede":
                "El despacho actuó sell-side en una "
                "operación de carve-out y cesión de una "
                "división industrial (112 millones de euros "
                "de ingresos anuales) a un operador "
                "estratégico alemán, cerrada en el cuarto "
                "trimestre de 2023 tras veintidós semanas "
                "de negociación.",
            "body": [
                ("p",
                 "El encargo abarcó toda la operación de "
                 "carve-out — desde la preparación del "
                 "teaser hasta la negociación del share "
                 "purchase agreement, hasta las seis "
                 "primeras semanas de integración "
                 "post-fusión."),
                ("h2", "Las fases"),
                ("ol", [
                    "Preparación del teaser e information memorandum",
                    "Vendor due diligence (legal, fiscal, laboral)",
                    "Subasta privada sobre cuatro adquirentes potenciales",
                    "Negociación SPA y pacto parasocial",
                    "Closing e integración post-fusión 100 días",
                ]),
                ("h2", "El resultado"),
                ("p",
                 "Cesión cerrada al múltiplo EBITDA de "
                 "mercado (8,4x), con cláusula de earn-out "
                 "sobre dos ejercicios. El 100% de los "
                 "contratos con los tres principales "
                 "clientes DACH se renovaron en los seis "
                 "meses siguientes al closing."),
            ],
        },
    ],

    # ════════════════════════════════════════════════════════════
    # CONTATTI (contact) — 2 sedi, form riservato
    # ════════════════════════════════════════════════════════════
    "contatti": {
        "eyebrow":  "Consulta preliminar confidencial",
        "headline": "Una conversación preliminar con un <em>socio del despacho</em>.",
        "intro":
            "El primer contacto se produce directamente con "
            "un socio de la asociación profesional. Se discute "
            "el alcance del encargo, el posible conflicto de "
            "interés y el arancel indicativo — bajo el "
            "vínculo del secreto profesional conforme al art. "
            "622 del Código Penal italiano, antes de cualquier "
            "encargo formal.",

        # Form fields
        "form_label":   "Formulario confidencial",
        "form_heading": "Cumplimente el formulario confidencial",
        "form_intro":
            "Recibirá acuse de recibo en un plazo de cuarenta "
            "y ocho horas hábiles, firmado por el socio "
            "responsable del área solicitada. La información "
            "se trata conforme al Reglamento UE 679/2016 y "
            "se custodia en archivo cifrado de acceso "
            "restringido a los socios del despacho.",
        "form_fields": [
            {"name": "name", "label": "Nombre", "type": "text", "required": True,
             "placeholder": "Ej. Alessandro",
             "helper": "Solo el nombre de pila, gracias."},
            {"name": "surname", "label": "Apellido", "type": "text", "required": True,
             "placeholder": "Ej. Costa",
             "helper": "Tal como figura en su documento de identidad."},
            {"name": "email", "label": "Dirección de email", "type": "email", "required": True,
             "placeholder": "alessandro.costa@ejemplo.es",
             "helper": "Para la correspondencia preliminar. No utilizaremos la dirección para otros fines."},
            {"name": "phone", "label": "Teléfono", "type": "tel", "required": True,
             "placeholder": "+34 ...",
             "helper": "Línea directa del contacto, no centralita."},
            {"name": "capacity", "label": "En calidad de", "type": "select", "required": True,
             "options": [
                 "Particular",
                 "Empresario o socio de sociedad",
                 "Administrador o auditor de sociedad",
                 "Dirección legal de grupo industrial",
                 "Profesional (asesor fiscal, notario, etc.)",
             ],
             "helper": "Para orientar la entrevista preliminar."},
            {"name": "practice", "label": "Área de práctica", "type": "select", "required": True,
             "options": [
                 "A determinar en entrevista",
                 "Derecho societario",
                 "M&A y operaciones de reestructuración",
                 "Derecho de familia",
                 "Sucesiones y patrimonios",
                 "Derecho laboral",
                 "Derecho penal empresarial",
                 "Contratación mercantil",
                 "Derecho bancario y financiero",
                 "Derecho administrativo",
                 "Inmobiliario",
                 "Protección de datos personales",
                 "Arbitraje y ADR",
             ],
             "helper": "Seleccione \"A determinar\" si el alcance abarca varias áreas."},
            {"name": "urgency", "label": "Urgencia", "type": "select", "required": True,
             "options": [
                 "Dentro de la semana en curso",
                 "En un mes",
                 "En tres meses",
                 "Exploratorio, sin urgencia",
             ],
             "helper": "Ayuda a planificar al socio competente."},
            {"name": "perimeter", "label": "Breve descripción del problema",
             "type": "textarea", "required": True, "full_width": True,
             "placeholder":
                 "Máximo 800 caracteres. Los nombres de "
                 "contrapartes, filiales o terceros solo se "
                 "divulgan tras firma de NDA recíproco, nunca "
                 "en este formulario.",
             "helper":
                 "Suficiente para realizar la verificación "
                 "preliminar de conflictos y encauzar el "
                 "expediente al socio competente. Los detalles "
                 "sensibles se discuten en entrevista."},
        ],

        "form_sections": [
            {"num": "01", "title": "Contacto",
             "meta": "La persona que firmará la eventual hoja de encargo.",
             "fields": ["name", "surname", "email", "phone"]},
            {"num": "02", "title": "Condición",
             "meta": "Para la verificación preliminar de conflictos.",
             "fields": ["capacity"]},
            {"num": "03", "title": "Objeto de la consulta",
             "meta":
                 "Ningún nombre de contraparte aquí — el "
                 "alcance técnico se discute en entrevista "
                 "tras NDA recíproco.",
             "fields": ["practice", "urgency", "perimeter"]},
            {"num": "04", "title": "Adjuntos (facultativos)",
             "meta":
                 "Documentos preliminares, organigramas o NDA "
                 "estándar pueden acelerar la entrevista.",
             "fields": ["__upload__"]},
        ],

        "upload_field": {
            "name":     "documenti_preliminari",
            "label":    "Documentos preliminares",
            "helper":
                "Documentos preliminares, organigrama "
                "societario o NDA estándar. PDF / DOCX · 15 "
                "MB máximo en total. Archivo cifrado de "
                "acceso restringido a los socios del "
                "despacho.",
            "accept":   ".pdf,.docx",
            "multiple": True,
            "primary":  "Arrastre los documentos aquí o",
            "link":     "seleccione desde su carpeta",
            "meta":     "PDF / DOCX · 15 MB máx · archivo cifrado",
        },

        "form_submit_label": "Enviar solicitud confidencial",
        "form_submit_note":
            "Acuse de recibo firmado por un socio en un "
            "plazo de cuarenta y ocho horas hábiles. Sin BDR, "
            "sin automatización, sin comunicación comercial.",
        "form_consent":
            "Consiento el tratamiento de los datos personales "
            "conforme al Reglamento UE 679/2016 y declaro "
            "haber sido informado de que los datos se "
            "custodian en archivo cifrado de acceso "
            "restringido a los socios del Studio Legale "
            "Ferri. Los datos no se comunican a terceros sin "
            "consentimiento escrito expreso.",

        # Office meta-row labels (lifted from skin for i18n)
        "office_address_label": "Dirección",
        "office_area_label":    "Barrio",
        "office_phone_label":   "Teléfono",
        "office_email_label":   "Email",
        "office_hours_label":   "Horario",

        # Sidebar — sedi + canali diretti
        "offices_label":   "Nuestras sedes",
        "offices": [
            {
                "city":    "Roma",
                "tag":     "Sede principal",
                "address": "Via Piemonte 39 · 00187",
                "area":    "Quirinale · cerca de Piazza Barberini",
                "phone":   "+39 06 4567 2300",
                "email":   "roma@studioferri.legal",
                "hours":   "Lun – Vie · 09:00 – 19:00",
            },
            {
                "city":    "Milán",
                "tag":     "Sede de Milán",
                "address": "Corso Venezia 11 · 20121",
                "area":    "Porta Venezia · cerca de los Giardini Pubblici",
                "phone":   "+39 02 7634 5500",
                "email":   "milano@studioferri.legal",
                "hours":   "Lun – Vie · 09:00 – 19:00",
            },
        ],

        "channels_label": "Canales directos",
        "channels": [
            ("Secretaría del despacho",
             "+39 06 4567 2300",
             "Lun – Vie · 09:00 – 19:00"),
            ("Email institucional",
             "studio@studioferri.legal",
             "Respuesta en 48 horas hábiles"),
            ("PEC certificada",
             "studio.ferri@cert.ordineavvocatiroma.it",
             "Para actos y notificaciones"),
        ],

        "footnote":
            "El Studio Legale Ferri no emite opiniones "
            "preliminares por email sin una primera "
            "entrevista con un socio. La información "
            "administrativa (parámetros arancelarios "
            "indicativos, modalidades de facturación, "
            "criterios de aceptación del encargo) se expone "
            "en el curso de la entrevista preliminar "
            "confidencial, nunca por escrito en fase "
            "preliminar.",
    },
}


# ─────────────────────────────────────────────────────────────────
# D-047 — chrome-authoring contract.
# Every visible string in the lawyer/classic-gold skin templates
# must come from THIS file (or from chrome.* / dna.content.*).
# Zero literal "Ferri", "1962", "Roma", "Via Piemonte", partner
# names, headline text, or other brand-specific strings in the
# .html files. When a new label is needed in the skin, add it here
# first (preferably under `site` if shared across pages, or under
# the page block if scoped) and read it via `{{ page_data.* }}` /
# `{{ site.* }}`.
# ─────────────────────────────────────────────────────────────────
