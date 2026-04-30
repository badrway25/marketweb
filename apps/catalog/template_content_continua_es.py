"""Continua — Family-office stewardship (corporate-suite archetype) ·
Spanish locale content tree.

Phase X.4b Continua Pass B · 2026-04-30 · Multilingual rollout pass on
top of the approved LF-5 Italian layout. Mirrors the shape of
``CONTINUA_CONTENT_IT`` exactly — same keys, same nesting, same list
shapes. Only values are translated and adapted.

Voice register: institucional, custodial, longitudinal,
multi-generacional. Native Spanish equivalent of the IT register —
el español de los family offices ibéricos (Banque Pictet & Cie España,
Caser Family Office, Mirabaud España). Adulto a adulto, declarativo,
nunca SaaS-marketing. Reference voices: Funds People Wealth, Cinco
Días Patrimonio, El Confidencial Wealth.

Voice anchor (CS-EXEC-01 / CS-BLOCK-11 · preserved verbatim-in-translation
across all 5 locales · the load-bearing italic moves with the equivalent
TEMPORAL noun):
    "La continuidad de una familia se mide en <em>generaciones</em>."

Italian normative references and proper nouns are preserved (D.lgs.
24/2023 whistleblowing, Codice della Crisi, OAM mediazione creditizia,
Albo dei Trustees, STEP, ANC audit, Codice Deontologico, Reg. UE
679/2016, Consiglio di Famiglia / Consejo de Familia). Italian
addresses, phone formats, Euro figures and years are kept as-is.
Anti-pattern guardrails carry across: ningún «Libera tu potencial
patrimonial», ningún «Asegura tu legado familiar», ningún «La mejor
versión de tu family office», ninguna cita Botín / Carlos Slim /
Amancio Ortega, ningún cliché boardroom de banca privada.
"""
from __future__ import annotations

from typing import Any


from apps.catalog.template_content_continua import (  # noqa: E402
    _HERO_IMAGE,
    _PILLAR_ICON_01,
    _PILLAR_ICON_02,
    _PILLAR_ICON_03,
    _PILLAR_ICON_04,
    _PORTRAIT_ELEONORA,
    _PORTRAIT_TOMAS,
    _PORTRAIT_GINEVRA,
)


CONTINUA_CONTENT_ES: dict[str, Any] = {
    "pages": [
        {"slug": "home",       "label": "El despacho",      "kind": "home"},
        {"slug": "chi-siamo",  "label": "Sobre nosotros",   "kind": "about"},
        {"slug": "custodia",   "label": "Custodia",         "kind": "services"},
        {"slug": "mandati",    "label": "Mandatos",         "kind": "case_study_list"},
        {"slug": "contatti",   "label": "Contacto",         "kind": "contact"},
    ],

    "site": {
        "logo_initial": "C",
        "logo_word":    "Continua",
        "tag":          "Family office multi-generacional · Milán",
        "phone":        "+39 02 7600 4188",
        "email":        "mandato@continua.it",
        "address":      "Via San Marco 22 · 20121 Milán",
        "hours_compact":"Lun – Vie · 9:30 – 18:30 · con cita previa",
        "hours_footer_rows": [
            "Sábado · solo Consejos de Familia programados",
            "Domingo · cerrado",
        ],
        "license":      "Inscrito Albo dei Trustees · STEP Affiliate · auditoría de continuidad ANC",
        "footer_intro":
            "Custodios del patrimonio familiar a través de las "
            "generaciones. Una boutique de stewardship independiente, "
            "mandatos de custodia en horizonte multi-generacional, "
            "gobierno familiar presidido por el Consejo de Familia. "
            "Sede principal en Milán, asociaciones fiduciarias en "
            "Lugano y Luxemburgo.",
        "foot_studio":   "El despacho",
        "foot_pages":    "Secciones",
        "foot_contact":  "Contacto",
        "foot_offices":  "Sedes",
        "offices_footer_rows": [
            "Milán · Brera (sede principal)",
            "Lugano · Riva Caccia (corresponsal fiduciario)",
            "Luxemburgo · Boulevard Royal (corresponsal trustee)",
        ],
        "whistleblowing_footer": {
            "heading":      "Denuncias",
            "eyebrow":      "Canal interno · D.lgs. 24/2023",
            "note":
                "Canal cifrado gestionado por el Compliance Officer. "
                "Reservado a miembros de la familia bajo mandato y a "
                "stewards Continua. Levantamiento de actas fiduciario.",
            "email":        "whistleblowing@continua.it",
            "policy_label": "Protección del denunciante",
            "policy_href":  "contatti",
        },
        "case_practice_label":     "Perfil",
        "case_year_label":         "Mandato abierto en",
        "case_duration_label":     "Años en continuidad",
        "case_lead_label":         "Steward referente",
        "case_lead_partner_label": "Senior Steward",
        "case_team_label":         "Equipo y cadencia",
        "case_timeline_label":     "Hitos de continuidad",
    },

    # ─── HOME ───────────────────────────────────────────────────
    "home": {
        "eyebrow":     "Family office · Milán · stewardship multi-generacional",
        "headline":
            "La continuidad de una familia se mide en <em>generaciones</em>.",
        "intro":
            "Custodios del patrimonio familiar a través de las "
            "generaciones. Una boutique de stewardship independiente — "
            "un Consejo de Familia, un mandato que no se mide en "
            "trimestres, una vigilancia fiduciaria que atraviesa el "
            "paso entre padres, hijos y nietos.",
        "primary_cta":   "Inicie un diálogo de mandato",
        "primary_href":  "contatti",
        "secondary_cta": "El despacho de custodia",
        "secondary_href":"chi-siamo",

        "hero_image":              _HERO_IMAGE,
        "hero_image_credit_left":  ("Stewards del mandato", "Inscrito Albo dei Trustees"),
        "hero_image_credit_right": ("Sede principal",        "Milán · Brera"),
        "hero_meta_strip": [
            ("Horizonte mandato",         "18 años de media"),
            ("Generaciones bajo custodia","3"),
            ("Consejos de Familia",       "4 / año"),
        ],

        "pillars_label":   "Custodia",
        "pillars_heading": "Cuatro pilares, <em>un solo</em> mandato",
        "pillars_intro":
            "Cuatro prácticas que trabajan en continuidad sobre el "
            "mismo patrimonio. No se factura cada pilar por separado — "
            "el mandato cubre la combinación de custodia, gobierno, "
            "sucesión y cumplimiento para el horizonte acordado con la familia.",
        "pillars": [
            ("01", "Custodia patrimonial",
             "Custodiamos el patrimonio familiar en sus cuatro estratos "
             "— activos financieros líquidos, participaciones "
             "industriales, inmuebles operativos y de familia — a "
             "través del ciclo de las generaciones, en coherencia con "
             "el pacto familiar en vigor y los mandatos fiduciarios subyacentes."),
            ("02", "Gobierno familiar",
             "Facilitamos el Consejo de Familia con cadencia "
             "trimestral, redactamos y revisamos el pacto familiar, "
             "diseñamos las voting structures de las ramas y los "
             "códigos de conducta compartidos entre generaciones en "
             "ejercicio y generaciones entrantes."),
            ("03", "Sucesión estructurada",
             "Planificamos el paso multi-generacional — donaciones "
             "moduladas, holdings de familia, trusts dedicados, "
             "formación técnica y de gobierno para la generación "
             "entrante antes de la transferencia efectiva de la "
             "responsabilidad decisoria."),
            ("04", "Cumplimiento fiduciario",
             "Vigilancia fiduciaria continuada, auditoría de "
             "continuidad anual independiente, presidio normativo en "
             "evolución (D.lgs. 24/2023 whistleblowing, Codice della "
             "Crisi, OAM mediación crediticia) y custodia documental "
             "con acceso controlado sobre los registros de familia."),
        ],

        "pillars_matrix": [
            {
                "num":   "01",
                "title": "Custodia patrimonial",
                "body":
                    "Cuatro estratos custodiados simultáneamente — "
                    "financiero líquido, participaciones industriales, "
                    "inmuebles operativos y de familia — coherentes "
                    "con el pacto familiar en vigor.",
                "icon_image": _PILLAR_ICON_01,
            },
            {
                "num":   "02",
                "title": "Gobierno familiar",
                "body":
                    "Consejo de Familia trimestral. Levantamiento de "
                    "actas fiduciario. Pacto familiar con revisión "
                    "trienal. Voting structures dedicadas por rama.",
                "icon_image": _PILLAR_ICON_02,
            },
            {
                "num":   "03",
                "title": "Sucesión estructurada",
                "body":
                    "Holding de familia, trusts dedicados, donaciones "
                    "moduladas. Programa bienal de formación técnica "
                    "de la generación entrante.",
                "icon_image": _PILLAR_ICON_03,
            },
            {
                "num":   "04",
                "title": "Cumplimiento fiduciario",
                "body":
                    "Auditoría de continuidad ANC anual. Presidio "
                    "AML, Codice della Crisi, D.lgs. 24/2023. "
                    "Custodia documental con acceso controlado.",
                "icon_image": _PILLAR_ICON_04,
            },
        ],

        "kpi_heading": "Dieciocho años de mandatos en continuidad",
        "kpi_strip": [
            ("18",      "años · horizonte medio del mandato"),
            ("3",       "generaciones · familias bajo custodia"),
            ("€ 1.800 M","patrimonio bajo custodia"),
            ("4",       "Consejos de Familia · por año"),
        ],

        "cycle_label":   "Ciclo de gobierno",
        "cycle_heading": "La continuidad tiene una <em>cadencia</em>, no un plazo.",
        "cycle_intro":
            "Tres ritmos que rigen el mandato — no KPI, no plazos "
            "fiscales, no sesiones de coaching. Son los compases "
            "regulares de un Consejo de Familia, repetidos a lo largo "
            "de los años y atravesados por las generaciones.",
        "cycle_strip": [
            ("Cadencia Consejo de Familia", "4 reuniones / año",
             "Calendario de gobierno compartido con la familia · "
             "levantamiento de actas fiduciario · orden del día abierto "
             "a ambas generaciones en ejercicio."),
            ("Auditoría de continuidad", "anual",
             "Verificación independiente sobre la coherencia "
             "plurianual del mandato (ANC) · revisión de la custodia "
             "documental · resultado comunicado en el Consejo de "
             "Familia de diciembre."),
            ("Pacto familiar", "revisión trienal",
             "Actualización de las reglas internas, con o sin la "
             "generación entrante en la mesa · cláusulas de voto y de "
             "protección de las ramas redebatidas cada tres años."),
        ],

        "sectors_label": "Perfiles familiares",
        "sectors": [
            "Familias empresariales",
            "Holdings de participaciones",
            "Fundaciones de familia",
            "Grupos multi-activo",
            "Segundas generaciones en transferencia",
            "Trustees independientes",
            "Oficinas de representación",
            "Single family offices extranjeros",
        ],

        "trust_label":   "Reconocimientos institucionales",
        "trust_logos":   [
            "ALBO DEI TRUSTEES",
            "STEP AFFILIATE",
            "AUDITORÍA DE CONTINUIDAD ANC",
            "OAM MEDIADORES CREDITICIOS",
            "ASSOCIAZIONE BANCHE FIDUCIARIE",
            "FAMILY OFFICE NETWORK ITALIA",
        ],

        "whistleblowing": {
            "eyebrow":      "Protección del denunciante",
            "channel_name": "Canal interno · D.lgs. 24/2023",
        },

        "leadership_label":   "Stewards del mandato",
        "leadership_heading": "Tres stewards que se sentarán en su Consejo de Familia.",
        "leadership_intro":
            "Cada mandato lo sigue personalmente al menos un Senior "
            "Steward, que se sienta en el Consejo de Familia desde la "
            "apertura del expediente hasta la transición entre "
            "generaciones. Ningún steward de recambio, ninguna "
            "intervención externa no acordada.",
        "leadership": [
            {
                "name":  "Eleonora Marchesi",
                "role":  "Senior Steward",
                "station": "Sala del archivo · Brera",
                "bio":
                    "Treinta y cinco años de práctica fiduciaria entre "
                    "Milán y Lugano. Inscrita en el Albo dei Trustees "
                    "desde 2007, ha presidido siete mandatos de "
                    "continuidad sobre tres generaciones completas y "
                    "once pasos intergeneracionales documentados.",
                "credentials": [
                    "Albo dei Trustees · inscripción 2007",
                ],
                "portrait": _PORTRAIT_ELEONORA,
            },
            {
                "name":  "Tomas Okafor",
                "role":  "Family Officer",
                "station": "Mesa del Consejo · sede principal",
                "bio":
                    "Catorce años de práctica entre family offices "
                    "anglosajones y advisory continental. STEP "
                    "Affiliate desde 2014, coordina la facilitación "
                    "del Consejo de Familia y la formación técnica de "
                    "la generación entrante antes de la transferencia "
                    "de responsabilidad.",
                "credentials": [
                    "STEP Affiliate · 2014",
                ],
                "portrait": _PORTRAIT_TOMAS,
            },
            {
                "name":  "Ginevra Conti",
                "role":  "Compliance Officer",
                "station": "Despacho de cumplimiento · custodia documental",
                "bio":
                    "Veintidós años en la vigilancia fiduciaria de "
                    "patrimonios privados. Inscrita en OAM como "
                    "mediadora crediticia desde 2011, preside el "
                    "respeto del D.lgs. 24/2023 (whistleblowing) y la "
                    "auditoría de continuidad anual de cada mandato bajo custodia.",
                "credentials": [
                    "OAM · inscripción mediadores crediticios",
                ],
                "portrait": _PORTRAIT_GINEVRA,
            },
        ],

        "cases_label":   "Mandatos en continuidad",
        "cases_heading": "Cuatro mandatos, cuatro generaciones, <em>una sola cadencia</em>.",
        "cases_intro":
            "Una selección de mandatos en continuidad — no cerrados, "
            "todavía bajo custodia. Los nombres de las familias se "
            "divulgan únicamente bajo pacto de confidencialidad fiduciaria.",

        "cases_timeline": [
            {
                "slug":          "famiglia-b-fondazione-di-famiglia",
                "year":          "2011",
                "eyebrow":       "Fundación de familia",
                "title":         "Familia B · 3ª generación · rama filantrópica + industrial",
                "horizon_label": "Horizonte",
                "horizon":       "15 años en continuidad · auditoría conjunta",
            },
            {
                "slug":          "famiglia-a-quarta-generazione-holding-industriale",
                "year":          "2014",
                "eyebrow":       "Holding industrial",
                "title":         "Familia A · 4ª generación · seis ramas familiares",
                "horizon_label": "Horizonte",
                "horizon":       "12 años · renovación del mandato 2034",
            },
            {
                "slug":          "famiglia-d-single-family-office-estero",
                "year":          "2017",
                "eyebrow":       "Single family office",
                "title":         "Familia D · custodia transfronteriza IT · CH · LU",
                "horizon_label": "Horizonte",
                "horizon":       "9 años · extensión AML 2030",
            },
            {
                "slug":          "famiglia-c-trasferimento-intergenerazionale",
                "year":          "2019",
                "eyebrow":       "Transferencia intergeneracional",
                "title":         "Familia C · 2ª → 3ª generación · trusts dedicados",
                "horizon_label": "Horizonte",
                "horizon":       "Paso decenal · 2026 — 2029",
            },
        ],

        "cta_label":     "Un primer diálogo confidencial",
        "cta_heading":   "La continuidad de una familia se mide en <em>generaciones</em>.",
        "cta_intro":
            "El primer diálogo se desarrolla con un Senior Steward. "
            "Discutimos el perímetro del mandato, el horizonte "
            "temporal y un eventual conflicto fiduciario — antes de "
            "cualquier propuesta de Consejo de Familia. No vendemos la "
            "primera reunión: la regalamos, una sola vez, por familia.",
        "cta_primary":   "Inicie un diálogo de mandato",
        "cta_primary_href": "contatti",
        "cta_secondary": "Descargue el dossier institucional",
        "cta_secondary_href": "chi-siamo",
    },

    # ─── CHI SIAMO (about + values) ─────────────────────────────
    "chi-siamo": {
        "eyebrow":   "El despacho · 2007 — 2026",
        "headline":  "Una boutique de custodia, <em>diecinueve</em> años de mandatos en continuidad.",
        "intro":
            "Continua nace en Milán en 2007 como oficina de custodia "
            "para dos familias empresariales lombardas. Desde "
            "entonces hemos presidido el paso entre padres e hijos en "
            "siete mandatos en total, nunca por adquisición, nunca "
            "con capital de terceros.",

        "history_label":   "Hitos de continuidad",
        "history_heading": "Cinco fechas, diecinueve años de stewardship.",
        "history_intro":
            "Cinco decisiones estructurales detrás de las cuales se "
            "lee el carácter del despacho — la independencia del "
            "capital de terceros, la cadencia trimestral del Consejo "
            "de Familia, la auditoría de continuidad anual, el pacto "
            "familiar trienal, el paso intergeneracional como método "
            "antes que como producto.",
        "history": [
            ("2007", "Fundación",
             "Eleonora Marchesi y dos co-stewards abren el despacho "
             "en via San Marco en Milán, por mandato de dos familias "
             "empresariales lombardas, para la custodia patrimonial "
             "en horizonte vicenal."),
            ("2011", "Inscripción OAM mediadores crediticios",
             "Ginevra Conti se incorpora como Compliance Officer y "
             "activa la vigilancia fiduciaria continuada sobre los "
             "mandatos bajo custodia, según el principio de "
             "separación entre custodia y advisory."),
            ("2014", "STEP Affiliate · Family Officer",
             "Tomas Okafor se incorpora como Family Officer e "
             "introduce la facilitación del Consejo de Familia — "
             "cuatro reuniones al año, orden del día compartido, "
             "levantamiento de actas fiduciario."),
            ("2019", "Auditoría de continuidad (ANC)",
             "El despacho adopta el protocolo ANC para la auditoría "
             "de continuidad anual — verificación independiente de la "
             "coherencia plurianual de cada mandato, resultado "
             "siempre comunicado en el Consejo de Familia de diciembre."),
            ("2024", "Corresponsales fiduciarios Lugano + Luxemburgo",
             "Para acompañar los mandatos de transferencia "
             "intergeneracional de las familias italianas, activamos "
             "asociaciones fiduciarias en Riva Caccia y Boulevard "
             "Royal — nunca sedes propias, siempre corresponsales acreditados."),
        ],

        "values_label":   "Principios de custodia",
        "values_heading": "Cuatro principios <em>no negociables</em>",
        "values_intro":
            "Cuatro principios que distinguen un mandato Continua de "
            "un encargo advisory estándar. Están escritos en el pacto "
            "de mandato firmado en Consejo de Familia, no en la web.",
        "values": [
            ("01", "Independencia del capital de terceros",
             "El capital del despacho está enteramente en manos de "
             "los stewards activos. Ningún fondo, ningún grupo "
             "bancario, ningún accionista externo. La elección de los "
             "mandatos nunca está influida por agendas de terceros "
             "que puedan condicionar la custodia."),
            ("02", "Un Senior Steward por mandato",
             "Un Senior Steward se sienta en el Consejo de Familia "
             "desde la apertura del expediente hasta el paso de la "
             "responsabilidad. Sin steward-of-record que desaparece "
             "tras el primer diálogo: el custodio encontrado en la "
             "primera reunión es el mismo que firmará el paso "
             "intergeneracional."),
            ("03", "Auditoría de continuidad independiente",
             "Cada mandato es objeto, una vez al año, de una "
             "auditoría de continuidad (ANC) llevada a cabo por un "
             "revisor externo al despacho. El resultado se comunica "
             "en el Consejo de Familia de diciembre sin filtro: la "
             "familia conoce siempre el estado de custodia de su patrimonio."),
            ("04", "Confidencialidad fiduciaria",
             "Ningún caso de estudio público, ninguna newsletter "
             "sobre la marcha de los mandatos, ninguna referencia "
             "cruzada entre familias. Las anonimizaciones mostradas "
             "en las páginas públicas se acuerdan caso por caso y se "
             "firman en Consejo de Familia."),
        ],

        "team_label":   "Stewards & officers",
        "team_heading": "Seis custodios, tres sedes, una sola cadencia.",
        "team_intro":
            "Las personas que se sentarán en su Consejo de Familia. "
            "Stewards, no consultores, y no le confiamos a un "
            "departamento — el custodio encontrado en la primera "
            "reunión es el mismo que presidirá el paso entre las generaciones.",
        "team": [
            {"name": "Eleonora Marchesi",
             "role": "Senior Steward · Custodia",
             "office": "Milán",
             "bio": "Treinta y cinco años de práctica fiduciaria. "
                    "Inscrita en el Albo dei Trustees desde 2007 · "
                    "siete mandatos de continuidad sobre tres "
                    "generaciones completas."},
            {"name": "Tomas Okafor",
             "role": "Family Officer · Gobierno",
             "office": "Milán",
             "bio": "STEP Affiliate desde 2014. Facilitación del "
                    "Consejo de Familia y formación de la generación "
                    "entrante antes de la transferencia de responsabilidad."},
            {"name": "Ginevra Conti",
             "role": "Compliance Officer · Vigilancia fiduciaria",
             "office": "Milán",
             "bio": "OAM mediadores crediticios desde 2011. Presidio "
                    "del D.lgs. 24/2023 (whistleblowing) y de la "
                    "auditoría de continuidad anual de cada mandato bajo custodia."},
            {"name": "Lorenzo Pellegrini",
             "role": "Steward · Sucesión estructurada",
             "office": "Milán",
             "bio": "Dieciocho años en el paso generacional de los "
                    "patrimonios industriales lombardos. Coordina "
                    "holdings de familia, trusts dedicados y "
                    "formación técnica de la generación entrante."},
            {"name": "Camille Béranger",
             "role": "Corresponsal fiduciaria",
             "office": "Luxemburgo",
             "bio": "Veinte años de práctica en derecho del trust "
                    "luxemburgués. Custodia las estructuras "
                    "transfronterizas para las familias italianas con "
                    "residencias fiscales secundarias."},
            {"name": "Sofia Pessina",
             "role": "Junior Steward · Pactos de familia",
             "office": "Milán",
             "bio": "Seis años de práctica en redacción y revisión "
                    "de pactos de familia. Asiste a los Senior "
                    "Stewards en las reuniones de Consejo de Familia "
                    "y en los ciclos de revisión trienal."},
        ],

        "coordinates_label": "Sedes",
        "coordinates": [
            ("Milán",      "Via San Marco 22 · 20121 · Brera"),
            ("Lugano",     "Riva Caccia 1 · 6900 · corresponsal fiduciario"),
            ("Luxemburgo", "Boulevard Royal 28 · L-2449 · corresponsal trustee"),
        ],

        "cta_heading": "Un primer diálogo confidencial.",
        "cta_intro":
            "Los primeros cuarenta y cinco minutos con un Senior "
            "Steward son un diálogo exploratorio, no una propuesta "
            "comercial. Se discute el perímetro del mandato, el "
            "horizonte temporal y un eventual conflicto fiduciario — "
            "antes de cualquier convocatoria de Consejo.",
        "cta_primary":  "Inicie un diálogo de mandato",
        "cta_primary_href": "contatti",
    },

    # ─── CUSTODIA (services · 4 pilares) ────────────────────────
    "custodia": {
        "eyebrow":  "Custodia · gobierno · sucesión · cumplimiento · 2026",
        "headline": "Cuatro prácticas, <em>una sola firma fiduciaria</em>.",
        "intro":
            "Las cuatro prácticas de Continua. Cada familia accede a "
            "un equipo de stewardship que las preside todas "
            "simultáneamente — no se factura cada pilar por separado, "
            "el mandato cubre la combinación de custodia, gobierno, "
            "sucesión y cumplimiento requerida por el horizonte "
            "acordado en Consejo de Familia.",

        "svc_duration_label": "Cadencia",
        "svc_leader_label":   "Steward referente",

        "services": [
            {
                "num":   "01",
                "title": "Custodia patrimonial",
                "blurb":
                    "Custodiamos el patrimonio en sus cuatro estratos "
                    "— financiero líquido, participaciones "
                    "industriales, inmuebles operativos, inmuebles de "
                    "familia. La custodia no es gestión de cartera: "
                    "es la asunción, año tras año, de la coherencia "
                    "entre el patrimonio y el pacto familiar en vigor.",
                "scope": [
                    "Reporting trimestral firmado conjuntamente",
                    "Registro de custodia digital con acceso controlado",
                    "Auditoría de continuidad ANC anual independiente",
                    "Coordinación de los corresponsales fiduciarios extranjeros",
                ],
                "duration": "Trimestral · auditoría anual",
                "leader":   "Eleonora Marchesi",
            },
            {
                "num":   "02",
                "title": "Gobierno familiar",
                "blurb":
                    "Facilitamos el Consejo de Familia con cadencia "
                    "trimestral, levantamiento de actas fiduciario "
                    "depositado en el despacho, redacción y revisión "
                    "trienal del pacto familiar. El gobierno no es "
                    "una reunión: es la repetición regular de un "
                    "compás de custodia atravesado por las generaciones.",
                "scope": [
                    "Cuatro Consejos de Familia al año",
                    "Levantamiento de actas fiduciario depositado",
                    "Voting structures dedicadas por rama familiar",
                    "Código de conducta intergeneracional",
                ],
                "duration": "4 Consejos / año · revisión trienal del pacto",
                "leader":   "Tomas Okafor",
            },
            {
                "num":   "03",
                "title": "Sucesión estructurada",
                "blurb":
                    "Planificamos el paso intergeneracional en "
                    "horizonte decenal — donaciones moduladas, "
                    "holdings de familia, trusts dedicados para ramas "
                    "menores o no operativas. La sucesión no se "
                    "improvisa el día de la firma del notario: se "
                    "prepara con un programa bienal de formación técnica.",
                "scope": [
                    "Holdings de familia y pactos parasociales",
                    "Trusts dedicados para ramas menores",
                    "Donaciones moduladas en horizonte decenal",
                    "Formación bienal de la generación entrante",
                ],
                "duration": "Horizonte decenal · formación bienal",
                "leader":   "Lorenzo Pellegrini",
            },
            {
                "num":   "04",
                "title": "Cumplimiento fiduciario",
                "blurb":
                    "Vigilancia fiduciaria continuada sobre el "
                    "respeto del D.lgs. 24/2023 (whistleblowing), del "
                    "Codice della Crisi, de la normativa OAM "
                    "mediación crediticia y de las directivas AML "
                    "aplicables. El cumplimiento no es un obstáculo "
                    "administrativo: es la garantía de continuidad "
                    "del mandato entre las generaciones.",
                "scope": [
                    "Canal whistleblowing interno cifrado",
                    "Vigilancia AML reforzada sobre movimientos transfronterizos",
                    "Auditoría de continuidad ANC anual independiente",
                    "Custodia documental con acceso controlado",
                ],
                "duration": "Continuado · auditoría ANC anual",
                "leader":   "Ginevra Conti",
            },
        ],

        "process_label":   "Cómo custodiamos",
        "process_heading": "Cuatro fases, una sola secuencia.",
        "process": [
            ("01", "Primer diálogo confidencial",
             "Cuarenta y cinco minutos con un Senior Steward. Se "
             "discute el perímetro del mandato y el horizonte "
             "temporal, nunca una propuesta económica."),
            ("02", "Pacto de mandato",
             "En diez días, un pacto de mandato fiduciario de cuatro "
             "páginas con perímetro, horizonte, cadencia de los "
             "Consejos y tarifario fiduciario transparente."),
            ("03", "Apertura del expediente",
             "Inauguración del primer Consejo de Familia. El Senior "
             "Steward se sienta en el Consejo desde la apertura del "
             "expediente hasta el paso de la responsabilidad."),
            ("04", "Continuidad + auditoría anual",
             "Cuatro Consejos al año, auditoría de continuidad ANC "
             "independiente cada diciembre, revisión trienal del "
             "pacto familiar. El mandato no se cierra: se renueva en "
             "continuidad."),
        ],

        "cta_heading":   "¿Qué pilar conviene a su familia?",
        "cta_intro":
            "Si el perímetro no está claro, escríbanos una breve "
            "descripción del núcleo familiar y del horizonte temporal "
            "acordado. Le indicaremos el Steward apropiado en 72 "
            "horas — incluso si no abrimos mandato.",
        "cta_primary":   "Inicie un diálogo de mandato",
        "cta_primary_href": "contatti",
    },

    # ─── MANDATI (case_study_list) ─────────────────────────────
    "mandati": {
        "eyebrow":  "Mandatos en continuidad · 2007 — 2026",
        "headline": "Cuatro mandatos, cuatro generaciones, una sola <em>cadencia fiduciaria</em>.",
        "intro":
            "Una selección de los mandatos bajo custodia — no "
            "cerrados, todavía en continuidad. Los nombres de las "
            "familias se divulgan únicamente bajo pacto de "
            "confidencialidad fiduciaria. Los hitos mostrados se "
            "acuerdan caso por caso y se firman en Consejo de Familia.",

        "cases_label": "Mandatos bajo custodia",
        "cases_intro":
            "Por cada mandato mostramos perfil familiar, generaciones "
            "bajo custodia, años de continuidad, perímetro acordado y "
            "cadencia de auditoría. Las familias están codificadas "
            "por rama (A · B · C · D) según el orden cronológico de "
            "entrada en mandato.",

        "cta_heading":   "¿Un mandato similar al suyo?",
        "cta_intro":
            "Los dossieres completos (perímetro fiduciario, horizonte, "
            "cadencia del Consejo, auditoría ANC más reciente) son "
            "accesibles bajo pacto de confidencialidad fiduciaria "
            "recíproco. La firma se realiza en el primer diálogo, "
            "antes de cualquier propuesta de mandato.",
        "cta_primary":   "Solicite los dossieres íntegros",
        "cta_primary_href": "contatti",
    },

    "posts": [
        {
            "slug":     "famiglia-a-quarta-generazione-holding-industriale",
            "title":    "Familia A · 4ª generación · holding industrial lombardo",
            "category": "Familia empresarial",
            "year":     "2014",
            "duration": "12 años · en continuidad",
            "client_code":
                "Holding industrial · 4ª generación · 6 ramas "
                "familiares · patrimonio industrial lombardo · "
                "perímetro: continuidad + gobierno + auditoría trienal.",
            "lead":
                "Un holding industrial lombardo en su cuarta "
                "generación de custodia, seis ramas familiares, dos "
                "generaciones simultáneamente bajo custodia. Continua "
                "preside el paso entre tercera y cuarta generación desde 2014.",
            "sections": [
                {
                    "label": "El contexto",
                    "heading": "Seis ramas, dos generaciones, un patrimonio compartido",
                    "body":
                        "En 2014 el holding entraba en la fase de "
                        "paso entre la tercera generación (cuatro "
                        "hermanos fundadores) y la cuarta (doce "
                        "primos, seis ramas familiares). El pacto "
                        "familiar en vigor — redactado en 1989 — no "
                        "preveía voting structures para la cuarta "
                        "generación y la tercera no había acordado "
                        "todavía un calendario de transferencia. "
                        "Continua fue llamada a presidir la cadencia "
                        "del Consejo de Familia y a establecer el paso.",
                },
                {
                    "label": "La custodia",
                    "heading": "Cadencia trimestral + revisión trienal del pacto",
                    "body":
                        "Continua estableció el Consejo de Familia "
                        "con cadencia trimestral desde 2014, con "
                        "actas fiduciarias depositadas tras cada "
                        "reunión. En 2017 se completó la primera "
                        "revisión trienal del pacto familiar, con "
                        "voting structures dedicadas a las seis ramas "
                        "de la cuarta generación y cláusula de "
                        "protección para las ramas no operativas. "
                        "Auditoría de continuidad ANC cada diciembre.",
                },
                {
                    "label": "El paso",
                    "heading": "Pacto familiar 2023 · transferencia progresiva",
                    "body":
                        "La revisión trienal 2023 del pacto familiar "
                        "ha formalizado el calendario de transferencia "
                        "progresiva de la responsabilidad decisoria "
                        "de la tercera a la cuarta generación en "
                        "horizonte septenal (2024-2031). El programa "
                        "bienal de formación técnica de la cuarta "
                        "generación se inició en 2024. La continuidad "
                        "del mandato Continua ha sido renovada hasta 2034.",
                },
            ],
            "kpi": [
                ("12 años", "en continuidad · desde 2014"),
                ("4ª",      "generación bajo custodia"),
                ("6",       "ramas familiares · voting structures dedicadas"),
                ("2034",    "renovación del mandato"),
            ],
            "lead_partner": "Eleonora Marchesi · Senior Steward",
            "team":         "Senior Steward + Family Officer + Compliance Officer · Consejo trimestral · auditoría ANC anual",
            "next_label":   "Mandato siguiente",
        },
        {
            "slug":     "famiglia-b-fondazione-di-famiglia",
            "title":    "Familia B · fundación de familia · 3ª generación",
            "category": "Fundación de familia",
            "year":     "2011",
            "duration": "15 años · en continuidad",
            "client_code":
                "Fundación de familia · 3ª generación · 4 ramas · "
                "patrimonio filantrópico + participaciones "
                "industriales · perímetro: gobierno + cumplimiento + "
                "auditoría trienal.",
            "lead":
                "Una fundación de familia lombarda en la tercera "
                "generación, patrimonio filantrópico junto a "
                "participaciones industriales operativas. Continua "
                "preside el gobierno fundativo y el cumplimiento "
                "fiduciario desde 2011.",
            "sections": [
                {
                    "label": "El contexto",
                    "heading": "Una fundación, dos naturalezas de patrimonio",
                    "body":
                        "La fundación, constituida en 1986, custodia "
                        "un patrimonio filantrópico de € 240 M y "
                        "participaciones de control en tres realidades "
                        "industriales lombardas. La tercera "
                        "generación, en custodia desde 2009, solicitó "
                        "a Continua en 2011 presidir el gobierno "
                        "fundativo y el cumplimiento separado entre "
                        "la rama filantrópica y la rama industrial.",
                },
                {
                    "label": "La custodia",
                    "heading": "Separación de las dos naturalezas · auditoría conjunta",
                    "body":
                        "Continua estableció dos Consejos de Familia "
                        "distintos — uno fundativo y uno industrial — "
                        "con reuniones trimestrales concatenadas y "
                        "orden del día coordinado por el Family "
                        "Officer. La auditoría de continuidad ANC es "
                        "conjunta sobre las dos ramas una vez al año, "
                        "con resultado comunicado a la familia en el "
                        "Consejo de diciembre.",
                },
                {
                    "label": "El presidio",
                    "heading": "Cumplimiento D.lgs. 24/2023 + AML reforzada",
                    "body":
                        "Desde 2023 Continua ha extendido el "
                        "presidio fiduciario a la nueva normativa "
                        "whistleblowing (D.lgs. 24/2023) para la "
                        "fundación, con canal de denuncia interno "
                        "dedicado y levantamiento de actas ante el "
                        "Compliance Officer. AML reforzada sobre los "
                        "movimientos de la rama industrial en "
                        "coherencia con las directivas 2024.",
                },
            ],
            "kpi": [
                ("15 años",  "en continuidad · desde 2011"),
                ("3ª",       "generación bajo custodia"),
                ("€ 240 M",  "patrimonio filantrópico bajo custodia"),
                ("2",        "Consejos de Familia · cadencia trimestral"),
            ],
            "lead_partner": "Ginevra Conti · Compliance Officer",
            "team":         "Senior Steward + Family Officer + Compliance Officer · 2 Consejos trimestrales · auditoría ANC anual conjunta",
            "next_label":   "Mandato siguiente",
        },
        {
            "slug":     "famiglia-c-trasferimento-intergenerazionale",
            "title":    "Familia C · transferencia intergeneracional · 2ª → 3ª generación",
            "category": "Familia en transferencia",
            "year":     "2019",
            "duration": "7 años · en transferencia",
            "client_code":
                "Familia empresarial · 2ª → 3ª generación · 3 ramas · "
                "trusts dedicados + holding de familia · perímetro: "
                "sucesión estructurada + formación de la generación "
                "entrante.",
            "lead":
                "Un patrimonio industrial familiar en transferencia "
                "de la segunda a la tercera generación, tres ramas "
                "familiares, horizonte de paso decenal. Continua "
                "coordina la sucesión estructurada y la formación "
                "técnica de los sucesores desde 2019.",
            "sections": [
                {
                    "label": "El contexto",
                    "heading": "Una transición en horizonte decenal",
                    "body":
                        "En 2019 la segunda generación (tres "
                        "hermanos, fundadores de la empresa en 1978) "
                        "solicitó a Continua establecer el paso "
                        "decenal hacia la tercera generación (siete "
                        "sucesores biológicos, de los cuales cinco "
                        "activos en el negocio). El primer paso fue "
                        "la separación entre holding operativa y "
                        "holding de familia, con trusts dedicados "
                        "para las dos ramas menores.",
                },
                {
                    "label": "La estructura",
                    "heading": "Holding de familia + trusts dedicados",
                    "body":
                        "Continua presidió la constitución del "
                        "holding de familia en 2020 y de los dos "
                        "trusts dedicados en 2021. El programa bienal "
                        "de formación técnica de los cinco sucesores "
                        "activos comenzó en 2022, con sesiones "
                        "mensuales facilitadas por el Family Officer "
                        "y un día anual de simulación de Consejo de Familia.",
                },
                {
                    "label": "La renovación",
                    "heading": "Pacto familiar 2025 · revisión trienal",
                    "body":
                        "La revisión trienal del pacto familiar 2025 "
                        "ha formalizado la voting structure "
                        "post-transferencia, el calendario de paso de "
                        "la responsabilidad decisoria (2026-2029) y "
                        "las cláusulas de protección de las dos ramas "
                        "menores. La continuidad del mandato Continua "
                        "ha sido renovada hasta 2032 con presidio "
                        "sobre la conclusión del paso.",
                },
            ],
            "kpi": [
                ("7 años", "en transferencia · desde 2019"),
                ("2 → 3",  "generación en paso"),
                ("2",      "trusts dedicados · ramas menores"),
                ("2032",   "renovación del mandato"),
            ],
            "lead_partner": "Lorenzo Pellegrini · Steward Sucesión",
            "team":         "Senior Steward + Family Officer + Steward Sucesión · Consejo trimestral · formación mensual + anual",
            "next_label":   "Mandato siguiente",
        },
        {
            "slug":     "famiglia-d-single-family-office-estero",
            "title":    "Familia D · single family office extranjero · custodia transfronteriza",
            "category": "Single family office extranjero",
            "year":     "2017",
            "duration": "9 años · en continuidad",
            "client_code":
                "Single family office · 2ª generación · 1 rama "
                "principal · patrimonio transfronterizo IT/CH/LU · "
                "perímetro: custodia + cumplimiento + corresponsales "
                "fiduciarios Lugano + Luxemburgo.",
            "lead":
                "Un single family office italiano con patrimonio "
                "transfronterizo (Italia, Suiza, Luxemburgo). "
                "Continua preside la custodia patrimonial y el "
                "cumplimiento fiduciario coordinando los "
                "corresponsales de Lugano y Boulevard Royal desde 2017.",
            "sections": [
                {
                    "label": "El contexto",
                    "heading": "Un patrimonio en tres jurisdicciones",
                    "body":
                        "En 2017 la familia solicitaba la "
                        "coordinación fiduciaria de un patrimonio "
                        "distribuido en tres jurisdicciones — Italia "
                        "(inmuebles operativos y de familia), Suiza "
                        "(activos financieros líquidos), Luxemburgo "
                        "(trusts dedicados para las ramas no "
                        "operativas). Continua activó los dos "
                        "corresponsales fiduciarios acreditados en "
                        "Lugano (Riva Caccia) y Boulevard Royal."},
                {
                    "label": "La custodia",
                    "heading": "Reporting unificado + auditoría conjunta",
                    "body":
                        "Continua produce un reporting trimestral "
                        "unificado sobre las tres ramas "
                        "jurisdiccionales, firmado por el Senior "
                        "Steward + Compliance Officer + corresponsales "
                        "acreditados. La auditoría de continuidad "
                        "ANC es conjunta sobre las tres ramas una vez "
                        "al año, con resultado comunicado en el "
                        "Consejo de enero (desfasada respecto al "
                        "ciclo italiano por alineación fiscal "
                        "transfronteriza).",
                },
                {
                    "label": "La evolución",
                    "heading": "Directivas AML 2024 · presidio reforzado",
                    "body":
                        "Desde 2024 Continua coordina el presidio "
                        "AML reforzado según las directivas europeas "
                        "2024, con verificación trimestral de los "
                        "movimientos transfronterizos y doble firma "
                        "fiduciaria para las operaciones > € 500 K. "
                        "El mandato ha sido extendido hasta 2030 con "
                        "perímetro coordinado sobre los tres corresponsales.",
                },
            ],
            "kpi": [
                ("9 años",     "en continuidad · desde 2017"),
                ("3",          "jurisdicciones · IT · CH · LU"),
                ("trimestral", "reporting unificado"),
                ("2030",       "renovación del mandato"),
            ],
            "lead_partner": "Eleonora Marchesi · Senior Steward",
            "team":         "Senior Steward + Compliance Officer + 2 corresponsales acreditados · auditoría ANC anual conjunta",
            "next_label":   "Mandato siguiente",
        },
    ],

    # ─── CONTATTI ───────────────────────────────────────────────
    "contatti": {
        "eyebrow":  "Primer diálogo confidencial",
        "headline": "Cuarenta y cinco minutos, agenda <em>familiar</em>, sin compromiso.",
        "intro":
            "El primer diálogo se desarrolla con un Senior Steward. "
            "Discutimos el perímetro del mandato, el horizonte "
            "temporal y un eventual conflicto fiduciario — antes de "
            "cualquier convocatoria de Consejo. Las informaciones "
            "sensibles se custodian en archivo cifrado con acceso "
            "limitado a los stewards.",

        "form_label":   "Inicie un diálogo de mandato",
        "form_heading": "Cumplimente el formulario confidencial",
        "form_intro":
            "Recibirá confirmación de un Senior Steward en 72 horas "
            "laborables desde el envío. Los datos se tratan al amparo "
            "del Reg. UE 679/2016 y se custodian en archivo cifrado "
            "en el despacho de via San Marco. Sin BDR externo, sin "
            "automatización de secuencia — el diálogo se abre con un "
            "steward, siempre.",

        "form_fields": [
            {"name": "name",      "label": "Nombre",          "type": "text", "required": True,
             "placeholder": "Ej. Eleonora",
             "helper": "Solo el nombre de pila, gracias."},
            {"name": "surname",   "label": "Apellido",        "type": "text", "required": True,
             "placeholder": "Ej. Marchesi",
             "helper": "Tal como aparece en el pacto familiar en vigor (si existe)."},
            {"name": "family",    "label": "Núcleo familiar", "type": "text", "required": True,
             "placeholder": "Ej. Familia Marchesi · rama lombarda",
             "helper": "El nombre con el que se presenta en Consejo de Familia."},
            {"name": "role",      "label": "Rol en la familia", "type": "text", "required": True,
             "placeholder": "Ej. Cabeza de familia · Sucesor designado · Miembro del Consejo",
             "helper": "La posición en el paso entre generaciones bajo custodia."},
            {"name": "email",     "label": "Email confidencial", "type": "email", "required": True,
             "placeholder": "eleonora@famigliamarchesi.it",
             "helper": "Una bandeja que recibe únicamente comunicaciones fiduciarias. No utilizaremos dominios consumer para el primer contacto."},
            {"name": "phone",     "label": "Teléfono directo", "type": "tel", "required": True,
             "placeholder": "+39 ...",
             "helper": "Línea directa del referente, no centralita de empresa."},
            {"name": "horizon",   "label": "Horizonte temporal", "type": "select", "required": True,
             "options": [
                 "5 años",
                 "10 años",
                 "25 años",
                 "Multi-generacional (horizonte más allá de 25 años)",
             ],
             "helper": "El horizonte acordado en familia para el mandato de custodia. Ayuda a programar al Senior Steward apropiado."},
            {"name": "structure", "label": "Estructura actual", "type": "select", "required": True,
             "options": [
                 "Holding de familia",
                 "Fundación de familia",
                 "Trust dedicado (italiano o extranjero)",
                 "Pacto de familia en vigor",
                 "Ninguna formalización",
             ],
             "helper": "La estructura jurídica existente (incluso si aún no está formalizada)."},
            {"name": "scope",     "label": "Perímetro familiar", "type": "textarea",
             "required": True, "full_width": True,
             "placeholder": "Máximo 800 caracteres. Díganos brevemente la estructura actual y su preocupación de continuidad — quedará custodiada en archivo cifrado desde este formulario.",
             "helper": "Lo justo para evaluar si el mandato es de nuestra competencia. Los nombres de las otras ramas y las cifras se comparten solo tras pacto de confidencialidad fiduciaria recíproco."},
        ],

        "form_sections": [
            {"num": "01", "title": "Referente",
             "meta": "La persona que firmará el eventual pacto de confidencialidad fiduciaria recíproco antes del primer Consejo.",
             "fields": ["name", "surname", "email", "phone"]},
            {"num": "02", "title": "Familia",
             "meta": "Para el conflict-check fiduciario preliminar.",
             "fields": ["family", "role"]},
            {"num": "03", "title": "Mandato de custodia",
             "meta": "El horizonte y la estructura — el detalle del patrimonio se discute solo en diálogo, nunca por escrito en fase de primer contacto.",
             "fields": ["horizon", "structure", "scope"]},
            {"num": "04", "title": "Adjuntos (opcionales)",
             "meta": "Pacto familiar en vigor, estatuto de la fundación, escritura de constitución del trust o dossier sucesorio: anticipan la primera reunión y abrevian el diálogo.",
             "fields": ["__upload__"]},
        ],

        "upload_field": {
            "name":     "dossier_familiare",
            "label":    "Documentos preliminares",
            "helper":   "Pacto familiar en vigor, estatuto de la "
                        "fundación, escritura de constitución del "
                        "trust o dossier sucesorio. PDF / DOCX · max "
                        "20 MB en total. Archivo cifrado con acceso "
                        "limitado a los stewards Continua.",
            "accept":   ".pdf,.docx",
            "multiple": True,
            "primary":  "Arrastre los documentos aquí o",
            "link":     "examine desde su archivo",
            "meta":     "PDF / DOCX · max 20 MB · archivo cifrado fiduciario",
        },

        "form_submit_label": "Inicie un diálogo de mandato",
        "form_submit_note":
            "Confirmación de un Senior Steward en 72 horas "
            "laborables. Sin BDR externo, sin automatización de "
            "secuencia — el diálogo se abre con un steward, siempre.",
        "form_consent":
            "Consiento el tratamiento de los datos personales al "
            "amparo del Reg. UE 679/2016 y del D.lgs. 196/2003 "
            "modificado. Los datos se custodian en archivo cifrado "
            "en el despacho de via San Marco con acceso limitado a "
            "los stewards Continua. Ningún dato se comunica a "
            "terceros sin autorización fiduciaria explícita. Estoy "
            "informado del canal whistleblowing (D.lgs. 24/2023) "
            "activo en el despacho.",

        "office_address_label": "Dirección",
        "office_area_label":    "Zona",
        "office_phone_label":   "Teléfono",
        "office_email_label":   "Email",

        "offices_label":   "Sedes",
        "offices": [
            {
                "city":    "Milán",
                "tag":     "Sede principal",
                "address": "Via San Marco 22 · 20121",
                "area":    "Brera · cerca de Piazza San Marco",
                "phone":   "+39 02 7600 4188",
                "email":   "milano@continua.it",
            },
            {
                "city":    "Lugano",
                "tag":     "Corresponsal fiduciario",
                "address": "Riva Caccia 1 · 6900",
                "area":    "Centro · cerca de Piazza della Riforma",
                "phone":   "+41 91 922 7700",
                "email":   "lugano@continua.it",
            },
            {
                "city":    "Luxemburgo",
                "tag":     "Corresponsal trustee",
                "address": "Boulevard Royal 28 · L-2449",
                "area":    "Ville Haute · cerca de Place d'Armes",
                "phone":   "+352 24 87 5500",
                "email":   "luxembourg@continua.it",
            },
        ],

        "channels_label": "Canales directos",
        "channels": [
            ("Secretaría de custodia",          "+39 02 7600 4188",            "Lun – Vie · 9:30 – 18:30"),
            ("Email fiduciario",                "mandato@continua.it",         "Respuesta en 72 horas"),
            ("Whistleblowing (D.lgs. 24/2023)", "whistleblowing@continua.it",  "Canal interno cifrado · acta levantada por el Compliance Officer"),
        ],

        "footnote":
            "Continua no responde a solicitudes anónimas y no emite "
            "pareceres preliminares por escrito sin un primer diálogo "
            "con un Senior Steward. Las informaciones administrativas "
            "(honorarios indicativos, modalidades de facturación, "
            "criterios de aceptación del mandato) se exponen en el "
            "primer diálogo, nunca por escrito. El canal "
            "whistleblowing es gestionado por el Compliance Officer "
            "al amparo del D.lgs. 24/2023 y es accesible también "
            "exclusivamente a los miembros de la familia bajo mandato.",
    },
}
