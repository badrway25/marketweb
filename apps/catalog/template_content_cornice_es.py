"""Cornice — Estudio de arquitectura (corporate-suite archetype) ·
locale español.

Phase X.5 Cornice · workflow C · despliegue multilingüe sobre el
borrador italiano LF-2 bloqueado (A.6 review-lock). Refleja
exactamente la forma de ``CORNICE_CONTENT_IT`` — mismas claves, mismo
anidamiento, mismas formas de listas. Sólo se traducen y adaptan los
valores.

Registro editorial-curatorial · disciplina arquitectónica. Voz
española nativa equivalente a la del IT — la prensa de arquitectura
española e iberoamericana (Arquitectura Viva, El Croquis, AV
Proyectos, A+T, Domus en español, ArchDaily ediciones críticas).
Adulto-a-adulto, declarativo, nunca SaaS-marketing. Tratamiento
formal por defecto.

Voice anchor (CS-EXEC-01 / CS-BLOCK-11 · preservado verbatim-en-
traducción a través de las 5 locales · la cursiva porta el sustantivo
CURATORIAL equivalente — `argumento` es el cognado español directo de
`argomento` y porta el mismo sentido discursivo-tesis):
    "Cada proyecto es un <em>argumento</em> construido, no un servicio prestado."

Las referencias normativas italianas y los nombres propios se
preservan (D.lgs. 24/2023, Codice dei Beni Culturali D.lgs. 42/2004,
D.M. 154/2017 cualificación MIBAC, OAPPC Milano, CNAPPC,
Soprintendenza Belle Arti, PRG, DAStU Politecnico di Milano, Reg. UE
679/2016 / RGPD). Direcciones, teléfonos, importes en euros y años
se conservan tal cual. Salvaguardas anti-patrón: sin «libera el
potencial», sin «el mejor estudio de Milán», sin citas de Calatrava
/ RCR / Moneo / Le Corbusier, sin moodboard de Pinterest.
"""
from __future__ import annotations

from typing import Any


from apps.catalog.template_content_cornice import (  # noqa: E402
    _HERO_BOLOGNA_PORTICO,
    _PORTRAIT_FOUNDER,
    _CASE_CONCORSO,
    _CASE_RESIDENZIALE,
    _CASE_RESTAURO,
    _CASE_CORNICE_DETAIL,
)


CORNICE_CONTENT_ES: dict[str, Any] = {
    "pages": [
        {"slug": "home",      "label": "El estudio", "kind": "home"},
        {"slug": "studio",    "label": "Archivo",    "kind": "about"},
        {"slug": "servizi",   "label": "Práctica",   "kind": "services"},
        {"slug": "progetti",  "label": "Proyectos",  "kind": "case_study_list"},
        {"slug": "contatti",  "label": "Contacto",   "kind": "contact"},
    ],

    "site": {
        "logo_initial": "C",
        "logo_word":     "CORNICE",
        "logo_subtitle": "estudio de arquitectura",
        "tag":           "Arquitectura editorial · Milán · desde 2008",
        "phone":         "+39 02 6610 4708",
        "email":         "fascicolo@cornice-architettura.it",
        "address":       "Via Pasquale Paoli 9 · 20143 Milán",
        "hours_compact": "Mar – Vie · 10:00 – 18:00 · con cita previa",
        "hours_footer_rows": [
            "Sábado · sólo con cita previa para visita de obra",
            "Domingo · cerrado",
        ],
        "license": "Colegio OAPPC Milán N.º 12.847 · CNAPPC · cualificación MIBAC restauración",
        "footer_intro":
            "Arquitectura editorial · encargos públicos y "
            "privados · Milán desde 2008. Cuarenta y siete obras "
            "construidas, veintitrés concursos entregados, "
            "noventa fascículos abiertos en colección monográfica.",
        "foot_studio":   "Estudio",
        "foot_pages":    "Páginas",
        "foot_contact":  "Contacto",
        "foot_offices":  "Sede",
        "offices_footer_rows": [
            "Milán · Via Paoli 9 (sede única)",
            "Estudio abierto con cita previa · martes-viernes",
            "Obras activas · Bolonia · Pietrasanta · Roma",
        ],
        "whistleblowing_footer": {
            "heading":      "Denuncias",
            "eyebrow":      "Canal interno · D.lgs. 24/2023",
            "note":
                "El estudio ha activado un canal de denuncia "
                "interno conforme al D.lgs. 24/2023 (directiva "
                "UE 2019/1937). Tutela del anonimato y "
                "confidencialidad de los datos. El canal está "
                "abierto a clientes públicos, proveedores de "
                "obra y colaboradores externos.",
            "email":        "whistleblowing@cornice-architettura.it",
            "policy_label": "Política de gestión de denuncias",
            "policy_href":  "contatti",
        },
        "case_practice_label":     "Programa",
        "case_year_label":         "Año del fascículo",
        "case_duration_label":     "Estado de obra",
        "case_lead_label":         "Arquitecta responsable",
        "case_lead_partner_label": "Arquitecta responsable",
        "case_team_label":         "Equipo de obra",
        "case_timeline_label":     "Cronología de obra",
    },

    "home": {
        "eyebrow":     "ESTUDIO DE ARQUITECTURA · MILÁN · DESDE 2008",
        "headline":
            "Cada proyecto es un <em>argumento</em> construido, no un servicio prestado.",
        "intro":
            "Estudio de arquitectura editorial · encargos "
            "públicos y privados · noventa fascículos abiertos "
            "desde 2008.",
        "primary_cta":   "Abrir un fascículo de proyecto",
        "primary_href":  "contatti",
        "secondary_cta": "El estudio · publicaciones",
        "secondary_href":"studio",

        "hero_image":              _HERO_BOLOGNA_PORTICO,
        "hero_image_alt":          "Pórtico restaurado en Bolonia · 2023",
        "hero_image_credit_left":  ("Bolonia · pórtico restaurado · 2023", "fascículo n.º 31"),
        "hero_image_credit_right": ("Sede del estudio", "Milán · Via Paoli 9"),
        "hero_meta_strip": [
            ("Obras construidas",  "47"),
            ("Años de práctica",   "18"),
            ("Ciudades italianas", "6"),
        ],
        "hero_side_quote":
            "La buena arquitectura se <em>argumenta</em> — no se "
            "demuestra, no se vende, no se decora.",

        "narrative_label":   "EL ESTUDIO · MANIFIESTO EDITORIAL",
        "narrative_drop":    "L",
        "narrative_blocks": [
            ("drop",
             "a buena arquitectura se argumenta. Cornice es un "
             "estudio de arquitectura editorial: cada proyecto "
             "publicado es un argumento construido sobre el sitio, "
             "sobre el encargo, sobre la restricción. No firmamos "
             "imágenes seductoras — publicamos obras, cada una con "
             "su historia de obra y su documentación propia. El "
             "estudio existe para medir el contexto antes de "
             "dibujarlo, para escribir el programa antes de "
             "habitarlo, para reconocer lo que ya está antes de "
             "añadir lo que falta. Es un oficio lento, que produce "
             "pocas páginas al año, pero las produce enteras."),

            ("quote",
             "El levantamiento es la <em>primera</em> forma de "
             "respeto. Lo que se argumenta sobre un sitio ya leído "
             "será siempre más sólido que lo que se decora sobre "
             "un sitio mudo."),

            ("para",
             "Cada encargo atraviesa cuatro estaciones. El "
             "levantamiento, ante todo: la obra existente se lee "
             "como un texto, con sus acentos, sus párrafos, sus "
             "cesuras. El contexto, después: el encargo, el uso, "
             "las restricciones del PRG y de la Soprintendenza, "
             "los hábitos del paisaje. El argumento, finalmente: "
             "el proyecto se escribe como una tesis — qué problema "
             "resuelve, qué herencia respeta, qué figura propone. "
             "Sólo entonces abrimos la obra, y la seguimos semana "
             "a semana, lugar a lugar, hasta la recepción. Las "
             "decisiones de proyecto quedan escritas: publicamos "
             "cada obra en nuestra colección monográfica, porque "
             "una arquitectura sin memoria no deja regla."),

            ("quote",
             "Un <em>autor</em> no es quien firma más proyectos, "
             "sino quien sabe decir qué proyecto no ha firmado — "
             "y por qué."),

            ("para",
             "Trabajamos para clientes públicos y privados que "
             "buscan un autor — no un ejecutor, no un paquete "
             "llave en mano. Ayuntamientos que restauran un patio "
             "histórico, entes culturales que reprograman un "
             "edificio en desuso, familias que reescriben una casa "
             "de campo, promotores privados con sensibilidad "
             "editorial, oficinas técnicas municipales que "
             "convocan un concurso. Nuestra firma es la de una "
             "sola arquitecta, no la de una marca a varias manos: "
             "la responsabilidad autoral queda concentrada, "
             "porque un argumento debe tener una voz para ser "
             "reconocible. Las colaboraciones con calculistas, "
             "paisajistas, restauradores y técnicos de obra pasan "
             "por el estudio, no lo sustituyen."),

            ("quote",
             "Publicar un proyecto no es promocionarlo. Es dejar "
             "una <em>regla</em> — para que quien venga después "
             "pueda contestarla, modificarla o reconocerla."),

            ("para",
             "Las obras publicadas aquí no son un portfolio "
             "comercial. Son argumentos construidos, agrupados por "
             "programa y por año, con la documentación de obra "
             "que los acompaña. Cada ficha nombra el sitio, el "
             "encargo, el programa, la cronología, la "
             "restricción, y el argumento del proyecto en cinco "
             "líneas — porque una obra que no se deja contar en "
             "cinco líneas, probablemente todavía no se ha "
             "aclarado."),
        ],
        "narrative_side_rail": [
            ("El estudio", "studio"),
            ("Práctica · encargos", "servizi"),
            ("Proyectos · fascículos", "progetti"),
            ("Contacto · sede", "contatti"),
        ],

        "sectors_label": "TIPOLOGÍAS DE INTERVENCIÓN",
        "sectors_lead":
            "El estudio interviene en doce tipologías "
            "principales, agrupadas por escala de la obra, "
            "programa del encargo y relación con la restricción "
            "paisajística o patrimonial. No trabajamos con un "
            "menú de servicios: cada entrada nombra un argumento "
            "ya construido, ya publicado en fascículo "
            "monográfico.",
        "sectors": [
            "residencial", "público", "interior", "paisaje",
            "restauración", "concurso", "cultural", "oficinas",
            "industrial", "sanitario", "escolar", "uso mixto",
        ],
        "sectors_trailing":
            "Las obras de restauración y concurso pasan por la "
            "cualificación MIBAC y por los procedimientos de la "
            "Soprintendenza; los encargos públicos entran por "
            "licitación o por concurso por invitación.",
        "sectors_counter":
            "Numeración de las intervenciones publicadas en la "
            "colección: desde 2008, <em>noventa</em> fascículos "
            "abiertos — cuarenta y siete obras construidas y "
            "recibidas, veintitrés concursos entregados, diez "
            "publicaciones de relieve.",

        "leadership_label":   "FUNDADORA DEL ESTUDIO · ARQUITECTA",
        "leadership_heading": "Marta <em>Roveri</em>",
        "leadership_role":    "fundadora · responsable editorial de los fascículos",
        "leadership_caption": "El estudio · interior · 2024",
        "leadership_portrait": _PORTRAIT_FOUNDER,
        "leadership_bio_paragraphs": [
            "Marta Roveri abrió Cornice en 2008, tras diez años "
            "de práctica entre Milán y Bolonia en dos estudios "
            "de restauración pública. Se formó en el Politecnico "
            "di Milano bajo la cátedra de restauración "
            "arquitectónica, con un periodo de investigación en "
            "la École Polytechnique de Lausanne sobre los "
            "caracteres estereotómicos de las bóvedas de piedra. "
            "Trabaja a tiempo completo en los proyectos del "
            "estudio: dirige el levantamiento, escribe el "
            "argumento del fascículo, sigue la obra hasta la "
            "recepción y cuida la colección monográfica que "
            "publica las obras realizadas.",

            "Entre las obras realizadas destaca la restauración "
            "del patio de Palazzo Lignari en Bolonia (2019, "
            "cualificación MIBAC), el concurso ganado para la "
            "nueva biblioteca cívica de Pietrasanta (2021, en "
            "obra) y el edificio residencial de Via Volpe en "
            "Roma (2023, seis viviendas en lote estrecho). Sus "
            "notas críticas — sobre la relación entre cornisa y "
            "fachada secundaria, sobre la regla del módulo en "
            "los concursos públicos — se recogen en dos "
            "monografías publicadas por la colección del estudio "
            "(2018, 2024) y en ensayos aparecidos en Casabella, "
            "Domus y Il Giornale dell'Architettura.",
        ],
        "leadership_credentials": [
            "Colegio OAPPC · Colegio de Arquitectos de Milán N.º 12.847",
            "CNAPPC · Consejo Nacional de Arquitectos P.P.C.",
            "MIBAC · Cualificación para la restauración arquitectónica (D.M. 154/2017)",
            "Politecnico di Milano · Profesora asociada · Cátedra de Restauración",
        ],
        "leadership_secondary_cta_label": "El estudio · biografía completa",
        "leadership_secondary_cta_href":  "studio",

        "cases_label":   "PROYECTOS — ARGUMENTOS CONSTRUIDOS",
        "cases_intro":
            "Cuatro fascículos abiertos, en orden de "
            "publicación. Sitio, encargo, programa, año, "
            "restricción, y el argumento de la obra.",
        "cases_magazine": [
            {
                "rank":     "hero",
                "num":      "01",
                "eyebrow":  "01 · CONCURSO GANADO · 2021 · PIETRASANTA (LU)",
                "title":    "Biblioteca cívica · el argumento es la <em>geometría</em> del módulo",
                "body":
                    "Concurso por invitación para la nueva "
                    "biblioteca cívica de Pietrasanta. Lote al "
                    "borde del centro histórico, a sesenta metros "
                    "de la muralla, con restricción paisajística "
                    "y doble fachada (calle urbana al este, "
                    "parque público al oeste). El argumento del "
                    "proyecto es un módulo de seis por nueve "
                    "metros, repetido ocho veces, que organiza "
                    "tres salas de lectura, un depósito a doble "
                    "altura y un pórtico continuo hacia el "
                    "parque. La piel en hormigón visto narra la "
                    "regla, los huecos leen la luz, la cornisa "
                    "del frente sostiene el peso cívico del "
                    "edificio.",
                "pill":     "Programa · concurso / cultural  ·  1.450 m²  ·  5,2 M €",
                "photo":    _CASE_CONCORSO,
                "photo_alt":"Arquitectura minimalista en hormigón · concurso Pietrasanta",
                "slug":     "biblioteca-pietrasanta-concorso",
            },
            {
                "rank":     "small",
                "num":      "02",
                "eyebrow":  "02 · OBRA REALIZADA · 2023 · ROMA (TIBURTINO)",
                "title":    "Via Volpe — seis viviendas en <em>parcela</em> estrecha",
                "body":
                    "Edificio residencial de seis viviendas en "
                    "parcela urbana de nueve metros de frente y "
                    "veintiocho de fondo. El argumento es la "
                    "profundidad: la fachada se cierra, el "
                    "interior se abre a un patio ciego llevado a "
                    "cubierta. Cinco plantas más bajocubierta, "
                    "estructura de hormigón armado y "
                    "cerramiento de fábrica de ladrillo visto. "
                    "Publicado en el fascículo n.º 38 de la "
                    "colección.",
                "pill":     "Programa · residencial  ·  720 m²  ·  privado",
                "photo":    _CASE_RESIDENZIALE,
                "photo_alt":"Edificios residenciales contemporáneos en Roma · Via Volpe",
                "slug":     "via-volpe-roma-residenziale",
            },
            {
                "rank":     "small",
                "num":      "03",
                "eyebrow":  "03 · RESTAURACIÓN PÚBLICA · 2019 · BOLONIA (CENTRO)",
                "title":    "Palazzo Lignari — el patio como <em>argumento</em> cívico",
                "body":
                    "Restauración del patio interior y de la "
                    "planta noble de Palazzo Lignari, sede de "
                    "una institución cultural municipal. El "
                    "argumento es el patio como espacio cívico: "
                    "el pórtico restaurado vuelve a ser un "
                    "pasaje público, los pavimentos de barro "
                    "cocido leen las tres intervenciones "
                    "históricas estratificadas. Cualificación "
                    "MIBAC; Soprintendenza Belle Arti de "
                    "Bolonia.",
                "pill":     "Programa · restauración / pública  ·  980 m²  ·  MIBAC",
                "photo":    _CASE_RESTAURO,
                "photo_alt":"Patio histórico boloñés restaurado · Palazzo Lignari",
                "slug":     "palazzo-lignari-bologna-restauro",
            },
            {
                "rank":     "small",
                "num":      "04",
                "eyebrow":  "04 · PUBLICACIÓN · 2024 · ENSAYO EN COLECCIÓN",
                "title":    "La cornisa de la fachada <em>menor</em> — una nota crítica",
                "body":
                    "Ensayo ilustrado sobre la regla de la "
                    "cornisa en las fachadas menores de la "
                    "edificación ochocentista milanesa. Ciento "
                    "veinticuatro fachadas levantadas, "
                    "veintidós cornisas tipológicas, ocho "
                    "reglas de proporción documentadas. La "
                    "publicación argumenta el valor de la "
                    "cornisa como dispositivo cívico, no "
                    "decorativo. Coedición con el Politecnico "
                    "di Milano · DAStU.",
                "pill":     "Programa · publicación  ·  124 fachadas  ·  DAStU",
                "photo":    _CASE_CORNICE_DETAIL,
                "photo_alt":"Detalle de cornisa y capitel · ensayo en colección 2024",
                "slug":     "cornice-fronte-minore-saggio",
            },
        ],
        "cases_trailing_label": "Todos los fascículos abiertos · cronología 2008–2024",
        "cases_trailing_href":  "progetti",

        "cta_label":     "FASCÍCULO DE PROYECTO",
        "cta_intro":
            "Los encargos comienzan por una sola página: el fascículo de proyecto.",
        "cta_heading":
            "Cada proyecto es un <em>argumento</em> construido, no un servicio prestado.",
        "cta_form_hint":
            "Brief en español o italiano · sitio · programa · "
            "calendario · documentos ya disponibles. Respuesta "
            "en cinco días laborables.",
        "cta_primary":   "Abrir un fascículo de proyecto",
        "cta_primary_href": "contatti",
        "cta_closing_line":
            "Sin llamada de descubrimiento. Sin presupuesto por "
            "consumo. Sólo el argumento del proyecto, y su regla.",
        "cta_sub_line":
            "Cornice · estudio de arquitectura · Milán · desde 2008",
    },

    "studio": {
        "eyebrow":   "EL ESTUDIO · ARCHIVO · CV",
        "headline":  "Cornice · estudio de arquitectura editorial desde <em>2008</em>.",
        "intro":
            "Milán. Una arquitecta fundadora, dos colaboradores, "
            "noventa fascículos abiertos. Trabajamos poco, y por "
            "entero.",

        "history_label":   "HITOS DEL ESTUDIO",
        "history_heading": "Cinco fechas, dieciséis años de práctica editorial.",
        "history_intro":
            "Cinco decisiones estructurales detrás de las cuales "
            "se lee el carácter del estudio — la autoría de una "
            "sola arquitecta, la colección monográfica como "
            "método, el levantamiento como primer gesto de "
            "respeto, la cornisa como dispositivo cívico, la "
            "restauración cualificada como práctica de lectura.",
        "history": [
            ("2008", "Fundación",
             "Marta Roveri abre Cornice en Via Paoli en Milán, "
             "tras diez años de colaboración en dos estudios de "
             "restauración pública entre Milán y Bolonia. La "
             "sede se elige por una sola razón: dos locales en "
             "patio interior, uno para el levantamiento, uno "
             "para la escritura."),
            ("2014", "Cualificación MIBAC restauración",
             "Marta Roveri obtiene la cualificación para la "
             "restauración arquitectónica (D.M. 154/2017). Desde "
             "ese año el estudio acepta encargos de restauración "
             "sobre edificios protegidos según el Código de los "
             "Bienes Culturales y tramita los expedientes con "
             "la Soprintendenza Belle Arti."),
            ("2017", "Cátedra en el Politecnico di Milano",
             "Marta Roveri es nombrada Profesora asociada en la "
             "Cátedra de Restauración del Politecnico di "
             "Milano. La práctica docente entra en el método del "
             "estudio: el levantamiento, el contexto y el "
             "argumento se escriben como una tesis."),
            ("2019", "Palazzo Lignari · primera restauración pública",
             "El estudio entrega la restauración del patio y de "
             "la planta noble de Palazzo Lignari en Bolonia "
             "(sede cultural municipal · Soprintendenza Belle "
             "Arti). Publicada en el fascículo n.º 31 de la "
             "colección monográfica."),
            ("2024", "Ensayo sobre la cornisa de la fachada menor",
             "Coedición con el Politecnico di Milano · DAStU · "
             "ensayo ilustrado sobre la regla de la cornisa en "
             "las fachadas menores de la edificación "
             "ochocentista milanesa. Publicado en el fascículo "
             "n.º 47. La colección monográfica alcanza noventa "
             "fascículos abiertos."),
        ],

        "values_label":   "PRINCIPIOS EDITORIALES",
        "values_heading": "Cuatro principios <em>no negociables</em>",
        "values_intro":
            "Son los cuatro principios que separan un fascículo "
            "Cornice de un encargo estandarizado. Están escritos "
            "en el mandato firmado en la primera reunión, no en "
            "el sitio web.",
        "values": [
            ("01", "Una arquitecta autora",
             "La firma del proyecto es la de una sola "
             "arquitecta, no la de una marca a varias manos. La "
             "responsabilidad autoral queda concentrada, porque "
             "un argumento debe tener una voz para ser "
             "reconocible. Las colaboraciones externas pasan por "
             "el estudio, no lo sustituyen."),
            ("02", "El levantamiento como primer gesto",
             "Cada encargo se abre con un levantamiento serio. "
             "La obra existente se lee como un texto, con sus "
             "acentos, sus párrafos, sus cesuras. Ningún "
             "proyecto antes de que el sitio haya sido leído "
             "íntegramente."),
            ("03", "La colección monográfica como método",
             "Todas las obras realizadas se publican en la "
             "colección monográfica en los doce meses "
             "posteriores a la recepción, con la documentación "
             "de obra completa. La colección no es marketing: "
             "es la regla que dejamos a quien venga después."),
            ("04", "Sin presupuestos por consumo",
             "Los honorarios del estudio se calculan sobre las "
             "tarifas mínimas CNAPPC por clase y categoría, sin "
             "descuentos porcentuales. La primera valoración de "
             "un encargo es gratuita; los estudios "
             "preliminares rechazados no se facturan."),
        ],

        "team_label":   "ESTUDIO Y COLABORADORES",
        "team_heading": "Tres arquitectos, una sola sede.",
        "team_intro":
            "El estudio está formado por una arquitecta "
            "fundadora y dos colaboradores. Trabajamos a tiempo "
            "completo en tres o cuatro encargos en paralelo, "
            "nunca más. Los expedientes con la Soprintendenza, "
            "las oficinas municipales y los entes contratantes "
            "se tramitan en estudio, nunca se delegan.",
        "team": [
            {"name": "Marta Roveri",
             "role": "Fundadora · Arquitecta",
             "office": "Milán",
             "bio": "Fundadora. Politecnico di Milano · cátedra "
                    "de restauración arquitectónica · "
                    "investigación en la EPFL Lausanne sobre los "
                    "caracteres estereotómicos de las bóvedas "
                    "de piedra. Colegio OAPPC Milán N.º 12.847 "
                    "· CNAPPC · cualificación MIBAC "
                    "restauración. Profesora asociada en el "
                    "Politecnico di Milano desde 2017."},
            {"name": "Arquitecto asociado",
             "role": "Arquitecto asociado · Obra",
             "office": "Milán",
             "bio": "Arquitecto asociado desde 2018. "
                    "Politecnico di Torino · máster en "
                    "proyectación del paisaje. Colegio OAPPC "
                    "Milán. Se ocupa de la obra y de la "
                    "coordinación de los encargos públicos, en "
                    "particular de los expedientes con la "
                    "Soprintendenza y con las oficinas "
                    "municipales."},
            {"name": "Arquitecta junior",
             "role": "Arquitecta junior · Levantamiento",
             "office": "Milán",
             "bio": "Arquitecta junior desde 2022. Politecnico "
                    "di Milano · tesis sobre la cornisa como "
                    "dispositivo cívico (directora: Roveri). "
                    "Colegio OAPPC Milán. Se ocupa del "
                    "levantamiento digital, del modelo y de la "
                    "redacción gráfica de los fascículos. "
                    "Coautora del ensayo sobre la cornisa "
                    "(colección, 2024)."},
        ],

        "coordinates_label": "LA SEDE",
        "coordinates": [
            ("Milán", "Via Pasquale Paoli 9 · 20143 · dos locales en patio interior"),
            ("Estudio", "abierto con cita previa · martes-viernes · 10:00-18:00"),
            ("Obras activas", "Bolonia · Pietrasanta · Roma · en curso 2024-2026"),
        ],

        "cta_heading": "Un encargo comienza por una sola página.",
        "cta_intro":
            "La primera página de cada encargo es el fascículo "
            "de proyecto: una ficha de síntesis que el estudio "
            "lee íntegramente, y a la que responde en cinco días "
            "laborables con una nota crítica.",
        "cta_primary":   "Abrir un fascículo de proyecto",
        "cta_primary_href": "contatti",
    },

    "servizi": {
        "eyebrow":  "PRÁCTICA · ENCARGOS · CUALIFICACIONES",
        "headline": "Cuatro modalidades de <em>encargo</em>.",
        "intro":
            "El estudio acepta encargos directos, concursos "
            "públicos, restauraciones cualificadas MIBAC y "
            "publicaciones en colección. Sin paquetes llave en "
            "mano.",

        "svc_duration_label": "Cadencia",
        "svc_leader_label":   "Arquitecta responsable",

        "services": [
            {
                "num":   "01",
                "title": "Encargo directo",
                "blurb":
                    "Familias que reescriben una casa de campo, "
                    "promotores privados con sensibilidad "
                    "editorial, comunidades religiosas que "
                    "reprograman un edificio en desuso, "
                    "pequeñas empresas que construyen una sede. "
                    "El encargo directo es la modalidad más "
                    "antigua del estudio: el cliente trae un "
                    "sitio y un programa, el estudio escribe el "
                    "argumento y acompaña el proyecto hasta la "
                    "recepción.",
                "scope": [
                    "Levantamiento inicial incluido · cinco días en obra",
                    "Fascículo monográfico incluido · publicado en la recepción",
                    "Tramitaciones urbanísticas y dirección de obra incluidas",
                    "Tarifas mínimas CNAPPC · sin descuentos porcentuales",
                ],
                "duration": "Del levantamiento a la recepción · 18-30 meses",
                "leader":   "Marta Roveri",
            },
            {
                "num":   "02",
                "title": "Concurso público",
                "blurb":
                    "El estudio participa en concursos públicos "
                    "(licitación abierta, procedimiento "
                    "restringido, diálogo competitivo) y en "
                    "concursos por invitación convocados por "
                    "ayuntamientos, entes culturales, "
                    "fundaciones y regiones. Nuestra firma es "
                    "la de una sola arquitecta — no la de un "
                    "consorcio multidisciplinar — por lo que "
                    "aceptamos concursos sólo cuando el "
                    "argumento del proyecto puede sostener "
                    "nuestra voz.",
                "scope": [
                    "Veintitrés concursos entregados desde 2008",
                    "Seis ganados · cuatro en lista corta · trece publicados",
                    "Paneles archivados y disponibles para el cliente",
                    "Inscripción CNAPPC verificable",
                ],
                "duration": "Según las bases · 2-9 meses",
                "leader":   "Marta Roveri",
            },
            {
                "num":   "03",
                "title": "Restauración cualificada MIBAC",
                "blurb":
                    "Marta Roveri está habilitada para la "
                    "restauración arquitectónica según el D.M. "
                    "154/2017. El estudio acepta encargos de "
                    "restauración sobre edificios protegidos "
                    "según el Código de los Bienes Culturales "
                    "(D.lgs. 42/2004) y sobre patios, pórticos, "
                    "fachadas menores, edificios del XIX y del "
                    "XX. Las estratigrafías se leen como textos.",
                "scope": [
                    "Cualificación MIBAC verificable (D.M. 154/2017)",
                    "Expedientes con la Soprintendenza tramitados internamente",
                    "Tres obras de restauración pública realizadas",
                    "Publicación íntegra en colección monográfica",
                ],
                "duration": "24-48 meses · restricciones incluidas",
                "leader":   "Marta Roveri",
            },
            {
                "num":   "04",
                "title": "Publicación editorial",
                "blurb":
                    "El estudio publica sus propios proyectos en "
                    "colección monográfica, pero también acepta "
                    "encargos externos de publicación: "
                    "monografías sobre fachadas menores, ensayos "
                    "tipológicos, fichas críticas para "
                    "catálogos de exposición, voces para "
                    "repertorios arquitectónicos. Un argumento "
                    "de proyecto publicado sin haberse "
                    "construido es un argumento que la "
                    "disciplina puede recoger.",
                "scope": [
                    "Ensayo ilustrado · 80-200 páginas",
                    "Coedición con instituciones académicas",
                    "Tirada limitada · 200 ejemplares numerados",
                    "Distribución museos + librerías especializadas",
                ],
                "duration": "Del encargo a la imprenta · 12-18 meses",
                "leader":   "Marta Roveri",
            },
        ],

        "process_label":   "MÉTODO · CUATRO ESTACIONES",
        "process_heading": "Cuatro fases, una sola secuencia editorial.",
        "process": [
            ("01", "Levantamiento",
             "La obra existente se lee como un texto. Medidas, "
             "materiales, cesuras, acentos. El levantamiento es "
             "la primera forma de respeto y dura típicamente "
             "cinco días en obra."),
            ("02", "Contexto",
             "Cliente, restricciones del PRG, restricciones "
             "paisajísticas y de la Soprintendenza, ordenanza "
             "de edificación, hábitos del sitio. El contexto es "
             "la cornisa del proyecto."),
            ("03", "Argumento",
             "El proyecto se escribe como una tesis — qué "
             "problema resuelve, qué herencia respeta, qué "
             "figura propone. Cinco líneas en las que la obra "
             "debe poder contarse."),
            ("04", "Obra",
             "Semana a semana, lugar a lugar, hasta la "
             "recepción. Todo queda escrito en el fascículo "
             "monográfico — publicado en los doce meses "
             "posteriores a la recepción."),
        ],

        "cta_heading":   "¿Qué modalidad encaja con su proyecto?",
        "cta_intro":
            "Si la modalidad no está clara, escríbanos una "
            "breve descripción del sitio y de la intervención "
            "imaginada. Indicaremos la modalidad correcta en "
            "cinco días laborables — incluso si no abrimos "
            "fascículo.",
        "cta_primary":   "Abrir un fascículo de proyecto",
        "cta_primary_href": "contatti",
    },

    "progetti": {
        "eyebrow":  "PROYECTOS · FASCÍCULOS ABIERTOS · 2008-2024",
        "headline": "Cuarenta argumentos <em>construidos</em>.",
        "intro":
            "Cuarenta y siete obras realizadas, veintitrés "
            "concursos entregados, diez publicaciones de "
            "relieve. Todos los fascículos están en colección "
            "monográfica.",

        "cases_label": "Cuatro fascículos representativos · en detalle",
        "cases_intro":
            "Para cada fascículo abierto publicamos aquí la "
            "página de argumento — sitio, encargo, programa, "
            "cronología, restricción, y el argumento del "
            "proyecto en cinco líneas.",

        "cta_heading":   "¿Un argumento parecido al suyo?",
        "cta_intro":
            "Los fascículos completos (levantamiento, planos "
            "técnicos, documentación de obra, nota crítica de "
            "cierre) están disponibles en el estudio bajo "
            "petición motivada. La consulta es gratuita; el "
            "fascículo impreso se entrega a cobertura de los "
            "gastos de impresión.",
        "cta_primary":   "Solicitar un fascículo en estudio",
        "cta_primary_href": "contatti",
    },

    "posts": [
        {
            "slug":     "biblioteca-pietrasanta-concorso",
            "title":    "Biblioteca cívica · el argumento es la geometría del módulo",
            "category": "Concurso · cultural",
            "year":     "2021",
            "duration": "Obra abierta · recepción prevista 2026",
            "client_code":
                "Concurso por invitación ganado · Ayuntamiento "
                "de Pietrasanta (Dirección de Cultura) · 1.450 "
                "m² · 5,2 M € · restricción paisajística · "
                "doble fachada (urbana + parque).",
            "lead":
                "Concurso por invitación para la nueva "
                "biblioteca cívica de Pietrasanta. El argumento "
                "del proyecto es un módulo de seis por nueve "
                "metros, repetido ocho veces, que organiza "
                "tres salas de lectura, un depósito a doble "
                "altura y un pórtico continuo hacia el parque "
                "público.",
            "sections": [
                {
                    "label": "El sitio",
                    "heading": "Una doble fachada y una restricción paisajística",
                    "body":
                        "Lote al borde del centro histórico de "
                        "Pietrasanta, a sesenta metros de la "
                        "muralla, con restricción paisajística "
                        "según el Código de los Bienes "
                        "Culturales (D.lgs. 42/2004) y doble "
                        "fachada: calle urbana al este, parque "
                        "público al oeste. El levantamiento se "
                        "cerró con doce semanas de campaña en "
                        "2020, dos estratigrafías sobre los "
                        "muros perimetrales y una campaña "
                        "fotográfica sobre los contextos "
                        "adyacentes.",
                },
                {
                    "label": "El argumento",
                    "heading": "Un módulo que se argumenta, no se ve",
                    "body":
                        "El módulo de seis por nueve metros se "
                        "repite ocho veces según una matriz "
                        "ortogonal. La piel en hormigón visto "
                        "narra la regla, los huecos leen la luz "
                        "solar a lo largo del arco del día, la "
                        "cornisa del frente sostiene el peso "
                        "cívico del edificio hacia la calle y "
                        "la apertura al parque hacia el oeste. "
                        "El módulo no se ve: se argumenta.",
                },
                {
                    "label": "La obra",
                    "heading": "Obra abierta noviembre 2023",
                    "body":
                        "Obra abierta en noviembre de 2023 tras "
                        "la entrega del proyecto de ejecución "
                        "en mayo de 2023. Dirección de obra del "
                        "estudio. Recepción prevista para junio "
                        "de 2026, con apertura al público en "
                        "septiembre de 2026 con motivo de la "
                        "inauguración de la temporada cultural "
                        "municipal. El fascículo monográfico se "
                        "publicará en la recepción (n.º 44 de "
                        "la colección).",
                },
            ],
            "kpi": [
                ("1.450 m²", "superficie neta"),
                ("8",        "módulos repetidos"),
                ("5,2 M €",  "valor de obra"),
                ("2026",     "recepción prevista"),
            ],
            "lead_partner": "Marta Roveri · Fundadora",
            "team":         "Arquitecta + 2 colaboradores · calculista externo · DO interna",
            "next_label":   "Siguiente fascículo",
        },
        {
            "slug":     "via-volpe-roma-residenziale",
            "title":    "Via Volpe — seis viviendas en parcela estrecha",
            "category": "Residencial · privado",
            "year":     "2023",
            "duration": "Realizado · recepción junio 2023",
            "client_code":
                "Edificio residencial · seis viviendas · "
                "cliente privado · parcela urbana 9×28 m · 720 "
                "m² superficie · cinco plantas + bajocubierta · "
                "publicado en el fascículo n.º 38.",
            "lead":
                "Edificio residencial de seis viviendas en "
                "parcela urbana de nueve metros de frente y "
                "veintiocho de fondo. El argumento es la "
                "profundidad: la fachada se cierra, el interior "
                "se abre a un patio ciego llevado a cubierta.",
            "sections": [
                {
                    "label": "El sitio",
                    "heading": "Nueve metros de frente, veintiocho de fondo",
                    "body":
                        "Parcela residencial en Tiburtino, "
                        "Roma, en una calle de edificación "
                        "mixta de los años Cincuenta. "
                        "Restricciones del PRG municipal "
                        "bastante permisivas en altura, pero "
                        "estrictas en la profundidad de "
                        "fachada. El cliente pedía seis "
                        "viviendas vendibles, garaje en "
                        "sótano, zona verde compartida.",
                },
                {
                    "label": "El argumento",
                    "heading": "La profundidad llevada a cubierta",
                    "body":
                        "El argumento del proyecto resuelve la "
                        "restricción de profundidad llevando "
                        "el patio ciego desde la planta sótano "
                        "a la planta de cubierta — un patio "
                        "común en altura, cinco metros por "
                        "ocho, iluminado por lucernario. La "
                        "fachada a la calle se cierra en "
                        "fábrica de ladrillo visto; las "
                        "viviendas reciben luz por los dos "
                        "lados cortos y por el patio en "
                        "cubierta.",
                },
                {
                    "label": "La obra",
                    "heading": "Diecinueve meses · obra cerrada 2023",
                    "body":
                        "Obra abierta en octubre de 2021, "
                        "recibida en junio de 2023. Estructura "
                        "de hormigón armado, cerramiento de "
                        "fábrica de ladrillo visto, carpintería "
                        "de aluminio anodizado bronce. "
                        "Dirección de obra del estudio. El "
                        "fascículo n.º 38 se publicó en la "
                        "colección en junio de 2024.",
                },
            ],
            "kpi": [
                ("720 m²",   "superficie total"),
                ("6",        "viviendas · 70-130 m²"),
                ("19 meses", "duración de obra"),
                ("n.º 38",   "fascículo en colección"),
            ],
            "lead_partner": "Marta Roveri · Fundadora",
            "team":         "Arquitecta + 2 colaboradores · calculista + DO interna",
            "next_label":   "Siguiente fascículo",
        },
        {
            "slug":     "palazzo-lignari-bologna-restauro",
            "title":    "Palazzo Lignari — el patio como argumento cívico",
            "category": "Restauración · pública",
            "year":     "2019",
            "duration": "Realizado · recepción junio 2019",
            "client_code":
                "Restauración patio interior + planta noble · "
                "Ayuntamiento de Bolonia (Sector Cultura) · "
                "cualificación MIBAC · Soprintendenza Belle "
                "Arti Bolonia · 980 m² · publicado en el "
                "fascículo n.º 31 de la colección (2020).",
            "lead":
                "Restauración del patio interior y de la "
                "planta noble de Palazzo Lignari, sede de una "
                "institución cultural municipal dedicada a la "
                "didáctica del patrimonio. El argumento es el "
                "patio como espacio cívico.",
            "sections": [
                {
                    "label": "El sitio",
                    "heading": "Un patio porticado de origen quattrocento",
                    "body":
                        "Bolonia, centro histórico, zona A1. "
                        "Restricción según el Código de los "
                        "Bienes Culturales (D.lgs. 42/2004) y "
                        "restricción de la Soprintendenza "
                        "Belle Arti para la ciudad "
                        "metropolitana. Palazzo Lignari es de "
                        "origen quattrocento, retomado en el "
                        "Seiscientos, en el Ochocientos y en "
                        "la posguerra. El patio interior "
                        "porticado conserva dos fachadas "
                        "renacentistas y tres estratificaciones "
                        "históricas distintas.",
                },
                {
                    "label": "El argumento",
                    "heading": "La restauración no añade figura, hace legible la estratigrafía",
                    "body":
                        "Hemos escrito dos gestos: el primero, "
                        "el pavimento de barro cocido a listón "
                        "puesto en obra según tres "
                        "orientaciones ligeramente distintas, "
                        "una para cada estratificación "
                        "histórica leída en el levantamiento; "
                        "el segundo, la iluminación integrada "
                        "en el listón, que enciende las "
                        "cesuras tras el ocaso y dibuja el "
                        "patio como texto legible también de "
                        "noche. La regla: la restauración hace "
                        "legible la estratigrafía que ya está "
                        "ahí.",
                },
                {
                    "label": "La obra",
                    "heading": "Treinta y un meses · campaña estratigráfica independiente",
                    "body":
                        "Obra abierta en noviembre de 2016, "
                        "recibida en junio de 2019. Las 31 "
                        "semanas de campaña estratigráfica "
                        "sobre los pavimentos exigieron la "
                        "colaboración de un restaurador "
                        "cualificado y de un equipo de "
                        "asentadores especializados. Los "
                        "expedientes con la Soprintendenza "
                        "exigieron once visitas técnicas y "
                        "tres revisiones del proyecto de "
                        "ejecución. Recepción sin "
                        "prescripciones.",
                },
            ],
            "kpi": [
                ("980 m²",   "patio + planta noble"),
                ("31 meses", "duración de obra"),
                ("n.º 31",   "fascículo en colección 2020"),
                ("MIBAC",    "cualificación restauración"),
            ],
            "lead_partner": "Marta Roveri · Fundadora",
            "team":         "Arquitecta + 2 colaboradores · restaurador externo · DO interna",
            "next_label":   "Siguiente fascículo",
        },
        {
            "slug":     "cornice-fronte-minore-saggio",
            "title":    "La cornisa de la fachada menor — una nota crítica",
            "category": "Publicación · ensayo",
            "year":     "2024",
            "duration": "Publicado · en librería",
            "client_code":
                "Ensayo ilustrado · coedición Politecnico di "
                "Milano (DAStU) · 124 fachadas levantadas · "
                "22 cornisas tipológicas · 8 reglas de "
                "proporción · publicado en el fascículo n.º "
                "47 de la colección (2024) · tirada 200 "
                "ejemplares.",
            "lead":
                "Ensayo ilustrado sobre la regla de la cornisa "
                "en las fachadas menores de la edificación "
                "ochocentista milanesa. La publicación "
                "argumenta el valor de la cornisa como "
                "dispositivo cívico, no decorativo.",
            "sections": [
                {
                    "label": "El levantamiento",
                    "heading": "Ciento veinticuatro fachadas menores en Milán",
                    "body":
                        "El levantamiento se cerró entre 2021 "
                        "y 2023 sobre ciento veinticuatro "
                        "fachadas menores ochocentistas en los "
                        "barrios de Brera, Magenta, Porta "
                        "Nuova y Porta Romana. Para cada "
                        "fachada: levantamiento gráfico a "
                        "1:50, campaña fotográfica con luz "
                        "diurna y rasante, ficha tipológica de "
                        "la cornisa y de sus relaciones con la "
                        "fachada.",
                },
                {
                    "label": "El argumento",
                    "heading": "La cornisa como dispositivo cívico",
                    "body":
                        "La cornisa de la fachada menor no es "
                        "un ornamento: es el dispositivo "
                        "cívico que sostiene la fachada del "
                        "edificio junto con la cortina de la "
                        "calle. Es la regla que permite a "
                        "fachadas distintas mantenerse en "
                        "conversación. El ensayo argumenta "
                        "ocho reglas de proporción "
                        "documentables y veinte tipologías "
                        "recurrentes, y propone una directriz "
                        "operativa para la restauración "
                        "contemporánea.",
                },
                {
                    "label": "La publicación",
                    "heading": "Coedición Politecnico DAStU · 200 ejemplares",
                    "body":
                        "Publicación en coedición con el "
                        "Politecnico di Milano · DAStU. "
                        "Formato 24×33 cm, 192 páginas, "
                        "cubierta en papel uso mano, "
                        "impresión offset a cuatro colores, "
                        "tirada limitada a 200 ejemplares "
                        "numerados. Distribución: librerías "
                        "especializadas · bibliotecas del "
                        "Politecnico · Triennale di Milano · "
                        "MAXXI Architettura.",
                },
            ],
            "kpi": [
                ("124", "fachadas levantadas"),
                ("22",  "cornisas tipológicas"),
                ("192", "páginas ilustradas"),
                ("200", "ejemplares numerados"),
            ],
            "lead_partner": "Marta Roveri · Fundadora",
            "team":         "Arquitecta + 2 colaboradores · coedición DAStU",
            "next_label":   "Siguiente fascículo",
        },
    ],

    "contatti": {
        "eyebrow":  "ABRIR UN FASCÍCULO DE PROYECTO",
        "headline": "El encargo comienza por una <em>página</em>.",
        "intro":
            "Brief en español o italiano. Sitio · programa · "
            "calendario · documentos ya disponibles. Respuesta "
            "en cinco días laborables.",

        "form_label":   "FASCÍCULO DE PROYECTO",
        "form_heading": "Cumplimente el fascículo de apertura",
        "form_intro":
            "El estudio acepta tres o cuatro nuevos encargos al "
            "año. La primera página de cada encargo es el "
            "fascículo de proyecto: el estudio lo lee "
            "íntegramente y responde en cinco días laborables "
            "con una nota crítica. La nota crítica es gratuita "
            "y es la forma con la que declaramos si el encargo "
            "está en línea con la colección.",

        "form_fields": [
            {"name": "name",      "label": "Nombre",   "type": "text", "required": True,
             "placeholder": "Ej. Ana",
             "helper": "Sólo el nombre de pila, gracias."},
            {"name": "surname",   "label": "Apellido", "type": "text", "required": True,
             "placeholder": "Ej. García",
             "helper": "Tal como aparece en los documentos del cliente."},
            {"name": "email",     "label": "Correo",   "type": "email", "required": True,
             "placeholder": "ana@dominio.es",
             "helper": "Un buzón que reciba la nota crítica fiduciaria."},
            {"name": "phone",     "label": "Teléfono", "type": "tel", "required": False,
             "placeholder": "+34 ...",
             "helper": "Línea directa para el primer contacto. Opcional."},
            {"name": "tipologia", "label": "Tipología de intervención", "type": "select", "required": True,
             "options": [
                 "residencial",
                 "público",
                 "interior",
                 "paisaje",
                 "restauración",
                 "concurso",
                 "cultural",
                 "oficinas",
                 "industrial",
                 "sanitario",
                 "escolar",
                 "uso mixto",
             ],
             "helper": "La tipología de la intervención imaginada."},
            {"name": "cronoprogramma", "label": "Calendario deseado", "type": "select", "required": True,
             "options": [
                 "Menos de 12 meses",
                 "Entre 12 y 24 meses",
                 "Entre 24 y 36 meses",
                 "Más de 36 meses",
             ],
             "helper": "El horizonte temporal acordado con el cliente."},
            {"name": "documenti", "label": "Documentos ya disponibles", "type": "select", "required": False,
             "options": [
                 "Levantamiento · planos",
                 "Restricciones · PRG · Soprintendenza",
                 "Ordenanza de edificación · pliegos",
                 "Concepto inicial",
                 "Otro",
                 "Ninguno (empezamos por el levantamiento)",
             ],
             "helper": "Documentos ya disponibles para el cliente. Opcional."},
            {"name": "sito", "label": "El sitio · la intervención · el cliente",
             "type": "textarea", "required": True, "full_width": True,
             "placeholder":
                 "Máximo 800 caracteres. Indíquenos brevemente "
                 "la localización (Municipio · provincia), la "
                 "tipología de la intervención y de qué cliente "
                 "procede la solicitud. Una sola voz — no es "
                 "necesario ser exhaustivo.",
             "helper":
                 "Lo suficiente para entender si el sitio "
                 "merece un levantamiento. Las cifras y los "
                 "demás datos se discuten en la primera "
                 "reunión, nunca por escrito en fase de "
                 "primer contacto."},
        ],

        "form_sections": [
            {"num": "01", "title": "Contacto",
             "meta": "La persona que firmará el encargo en la primera reunión.",
             "fields": ["name", "surname", "email", "phone"]},
            {"num": "02", "title": "Argumento de proyecto",
             "meta": "Tipología · calendario · documentos ya disponibles.",
             "fields": ["tipologia", "cronoprogramma", "documenti"]},
            {"num": "03", "title": "El sitio",
             "meta": "El sitio es el primer texto del proyecto. Cuatrocientas palabras bastan.",
             "fields": ["sito"]},
        ],

        "form_submit_label": "Abrir el fascículo",
        "form_submit_note":
            "El estudio leerá el fascículo en cinco días "
            "laborables y responderá con una nota crítica a la "
            "dirección indicada. Sin BDR externo, sin "
            "automatización de secuencia — el primer contacto "
            "es con la arquitecta.",
        "form_consent":
            "Consiento el tratamiento de los datos personales "
            "según el Reg. UE 679/2016 y el D.lgs. 196/2003. "
            "Los datos se custodian en el estudio de Via Paoli "
            "con acceso limitado a los tres arquitectos. Estoy "
            "informado(a) del canal whistleblowing (D.lgs. "
            "24/2023) activo en el estudio.",

        "office_address_label": "Dirección",
        "office_area_label":    "Zona",
        "office_phone_label":   "Teléfono",
        "office_email_label":   "Correo",

        "offices_label":   "LA SEDE",
        "offices": [
            {
                "city":    "Milán",
                "tag":     "Sede única",
                "address": "Via Pasquale Paoli 9 · 20143",
                "area":    "Sant'Agostino · cerca de Bocconi",
                "phone":   "+39 02 6610 4708",
                "email":   "fascicolo@cornice-architettura.it",
            },
        ],

        "channels_label": "CANALES DIRECTOS",
        "channels": [
            ("Secretaría del estudio",            "+39 02 6610 4708",                       "Mar – Vie · 10:00 – 18:00"),
            ("Correo fiduciario",                 "fascicolo@cornice-architettura.it",      "Respuesta en 5 días laborables"),
            ("Whistleblowing (D.lgs. 24/2023)",   "whistleblowing@cornice-architettura.it", "Canal interno · cifrado"),
        ],

        "footnote":
            "Cornice no responde a solicitudes anónimas y no "
            "emite dictámenes preliminares por escrito sin un "
            "primer diálogo. La información sobre los "
            "honorarios se ilustra en la primera reunión, "
            "según las tarifas mínimas CNAPPC. El canal "
            "whistleblowing se gestiona según el D.lgs. "
            "24/2023 y está abierto a clientes públicos, "
            "proveedores de obra y colaboradores externos.",
    },
}
