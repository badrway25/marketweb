"""Causa — Studio legale (corporate-suite archetype) ·
Spanish locale content tree.

Phase X.6 Causa · workflow C · multilingual rollout on top of the
locked LF-2 Italian draft (A.6 review-lock + A.5b imagery re-curate +
slice-01 + slice-02 + motion_profile DNA pass 1). Mirrors the shape
of ``CAUSA_CONTENT_IT`` exactly — same keys, same nesting, same list
shapes. Only values are translated and adapted.

Voice register: forense-publicación · adosado a la prueba · registro
de Sala Civil del Tribunal Supremo. Equivalente nativo en español
del registro IT — la prensa jurídica del despacho contencioso
español: La Ley, Aranzadi, Diario La Ley, Revista de Derecho
Procesal, crónicas de la Sala Civil del TS. Trato de usted,
declarativo, nunca SaaS-marketing, nunca discurso comercial. Voces de
referencia: crónicas de Aranzadi · editoriales de La Ley ·
sentencias incardinadas en el repertorio de jurisprudencia.

Voice anchor (CS-EXEC-01 / CS-BLOCK-11 · preserved
verbatim-in-translation across all 5 locales · the load-bearing
italic moves with the equivalent PUBLIC-RECORD-EVIDENCE noun · per
factory/reports/copy/causa-legale/voice-anchor-lock.md §4.2 +
factory/reports/causa/causa-planner-brief.md §11):
    "Cada sentencia es una <em>evidencia</em> incardinada — no una opinión defendida."

The translator binding contract (voice-anchor-lock §6.5) explicitly
locks the ES rendering to `evidencia` (NOT `prueba` — Spanish forensic
press treats `prueba` as proof-of-fact and prefers `evidencia` for
evidence-on-the-record · NOT `argumento` — that is Cornice's cognate).

Italian normative references and Italian proper nouns are preserved
verbatim (D.lgs. 24/2023 whistleblowing · D.lgs. 196/2003 datos
personales · D.M. 55/2014 tarifas forenses · Codice Deontologico
Forense · art. 622 c.p. secreto profesional · D.lgs. 28/2010
mediación obligatoria · D.lgs. 74/2000 penal-tributario · D.lgs.
259/2003 telecom · ENCA · CTU forense · Tribunale di Milano ·
Cassazione · TAR Lombardia · Corte d'Appello di Milano · Foro di
Milano · Foro Italiano · Giurisprudenza Italiana · Albo Avvocati ·
Reg. UE 679/2016 / RGPD). Italian addresses, phone formats, Euro
figures and years are kept as-is. Italian sentence-identifiers carry
verbatim across all locales (Cass. SS.UU. n. 11237/2024 · Cass. civ.
sez. III n. 28914/2023 · TAR Lombardia sez. III n. 814/2022 · Corte
d'Appello Milano sez. trib. n. 3187/2021).
"""
from __future__ import annotations

from typing import Any


from apps.catalog.template_content_causa import (  # noqa: E402
    _HERO_COURTROOM_INTERIOR,
    _PORTRAIT_FOUNDER,
    _CASE_HIGHCOURT_EXTERIOR,
    _CASE_FASCICOLI_STACK,
    _CASE_BENCH_CHAIR,
    _CASE_CODEX_SPINE,
)


CAUSA_CONTENT_ES: dict[str, Any] = {
    "pages": [
        {"slug": "home",        "label": "El bufete",     "kind": "home"},
        {"slug": "materie",     "label": "Materias",      "kind": "services"},
        {"slug": "studio",      "label": "Publicaciones", "kind": "about"},
        {"slug": "contenzioso", "label": "Contencioso",   "kind": "case_study_list"},
        {"slug": "contatti",    "label": "Contacto",      "kind": "contact"},
    ],

    "site": {
        "logo_initial": "C",
        "logo_word":     "CAUSA",
        "logo_subtitle": "studio legale",
        "tag":           "Bufete · Milán · desde 1995",
        "phone":         "+39 02 7634 8210",
        "email":         "parere@causa.legal",
        "address":       "Via Borgonuovo 14 · 20121 Milán",
        "hours_compact": "Lun – Vie · 09:00 – 18:00 · con cita previa",
        "hours_footer_rows": [
            "Sábado · solo para términos en vencimiento",
            "Domingo · cerrado · respuesta como muy tarde el lunes",
        ],
        "license":
            "Albo Avvocati Milano · Cassazionista desde 2003 · "
            "ENCA mediadores · Albo CTU forense Tribunale di Milano",
        "footer_intro":
            "Bufete de defensa editorial. Letrado fundador "
            "Lorenzo Marchetti · inscrito en el Colegio de "
            "Abogados de Milán desde 1995. Sede única en Milán "
            "· Foro di Milano. Defensa en todos los grados de "
            "jurisdicción hasta la Casación · veintiocho "
            "sentencias citadas · catorce voces en el "
            "repertorio interno · treinta y un años de defensa "
            "editorial.",
        "foot_studio":   "Bufete",
        "foot_pages":    "Páginas",
        "foot_contact":  "Contacto",
        "foot_offices":  "Sede",
        "offices_footer_rows": [
            "Milán · Via Borgonuovo 14 · sede única",
            "Con cita previa · lunes-viernes",
            "Foro di Milano · trámites con la secretaría judicial internos",
        ],
        "whistleblowing_footer": {
            "heading":      "Denuncias",
            "eyebrow":      "Canal interno · D.lgs. 24/2023",
            "note":
                "El bufete ha establecido un canal interno de "
                "denuncias conforme al D.lgs. 24/2023 (Directiva "
                "UE 2019/1937). Responsable de prevención: "
                "letrado asociado senior, independiente del "
                "fundador. Confidencialidad garantizada "
                "conforme a la normativa vigente. Abierto a "
                "colaboradores, asociados y secretaría.",
            "email":        "whistleblowing@causa.legal",
            "policy_label": "Política de gestión de las denuncias",
            "policy_href":  "contatti",
        },
        "case_practice_label":     "Materia",
        "case_year_label":         "Año · depósito",
        "case_duration_label":     "Grado · resolución",
        "case_lead_label":         "Defensa",
        "case_lead_partner_label": "Defensa",
        "case_team_label":         "Redacción del bufete",
        "case_timeline_label":     "Cronología procesal",
    },

    "home": {
        "eyebrow":     "BUFETE · MILÁN · DESDE 1995",
        # Voice anchor verbatim · italic on `evidencia`, the Spanish
        # forensic-press cognate of `evidenza` (per voice-anchor-lock
        # §4.2 · §6 binding rule). Carries the public-record-evidence
        # sense ("evidencia en el expediente"), NOT the proof-of-fact
        # sense `prueba` (translator-binding contract §6.5 ban).
        "headline":
            "Cada sentencia es una <em>evidencia</em> incardinada — no una opinión defendida.",
        "intro":
            "Bufete de defensa editorial · letrado fundador "
            "Cassazionista · veintiocho sentencias citadas "
            "desde 1995.",
        "primary_cta":   "Someta un dictamen preliminar",
        "primary_href":  "contatti",
        "secondary_cta": "El bufete · sede única en Milán",
        "secondary_href":"studio",

        "hero_image":              _HERO_COURTROOM_INTERIOR,
        "hero_image_alt":
            "Sala de vistas vacía · luz fría · paredes de "
            "madera vertical y tonos hueso · interior "
            "arquitectónico",
        "hero_image_credit_left":  ("Sala de vistas · interior · 2024", "Foro di Milano"),
        "hero_image_credit_right": ("Sede del bufete", "Milán · Via Borgonuovo 14"),
        "hero_image_provenance":
            "Pexels · CC0 · St George's Hall, Liverpool · n.º 33939830",
        "hero_image_provenance_aria":
            "Procedencia de la fotografía · biblioteca Pexels · licencia CC0",
        "hero_meta_strip": [
            ("Sentencias citadas",         "28"),
            ("Voces en el repertorio",     "14"),
            ("Años de defensa",            "31"),
        ],
        # Side-quote em on the verb form `incardina` — Spanish
        # forensic press uses `incardinar` (third-person `incardina`)
        # as the canonical verb for placing matter on the procedural
        # record. Per voice-anchor-lock §6.4: the side-quote em moves
        # with the verb-form of the public-record-evidence anchor.
        "hero_side_quote":
            "Defensa ante el Tribunal de Casación y en todos "
            "los grados de fondo. El bufete sostiene solo lo "
            "que <em>incardina</em> en el expediente procesal: "
            "la prueba depositada, el fundamento citable, la "
            "materia del derecho.",

        "narrative_label":   "EL BUFETE · MÉTODO PROBATORIO",
        "narrative_drop":    "L",
        "narrative_chronotick": [
            ("1995", "Fundación · Milán"),
            ("2003", "Habilitación Cassazionista"),
            ("2008", "Primera voz en el repertorio interno"),
            ("2014", "Primera remisión SS.UU."),
            ("2018", "Inscripción Albo CTU forense"),
            ("2024", "Decimocuarta voz · SS.UU. responsabilidad profesional"),
        ],
        "narrative_blocks": [
            ("drop",
             "a buena jurisprudencia se incardina. Causa es "
             "un bufete de defensa editorial: cada causa "
             "llevada a vista es una evidencia incardinada en "
             "el objeto del contencioso, en el grado de "
             "jurisdicción, en la jurisdicción misma. No "
             "firmamos opiniones decorativas — depositamos "
             "memorias, cada una con su documentación y su "
             "voz citable. El bufete existe para medir el "
             "expediente antes de defenderlo, para escribir "
             "la voz antes de sostenerla, para reconocer lo "
             "que ya está decidido antes de proponer lo que "
             "todavía debe decidirse. Es un oficio lento, "
             "que abre pocas causas al año, pero las lleva "
             "hasta Casación."),

            ("quote",
             "La <em>jurisdicción</em> es la primera forma "
             "de respeto. Lo que se sostiene ante el foro "
             "competente será siempre más sólido que lo que "
             "se decanta en el grado equivocado."),

            ("para",
             "Cada causa atraviesa cuatro estaciones. La "
             "jurisdicción, en primer lugar: la materia que "
             "ya existe se lee como un expediente, con sus "
             "precedentes, sus grados, sus excepciones "
             "preliminares. El fondo, después: el objeto del "
             "contencioso, las partes en causa, la franja de "
             "valor, la urgencia procesal, la evidencia "
             "preliminar adjuntable. La voz, finalmente: el "
             "recurso se escribe como una tesis citable — "
             "qué principio invoca, qué orientación confirma, "
             "qué evidencia deposita. Solo entonces abrimos "
             "el procedimiento, y lo seguimos vista a vista, "
             "grado a grado, hasta el depósito de la "
             "decisión. Las memorias permanecen escritas: "
             "publicamos las sentencias obtenidas en el "
             "repertorio interno del bufete, porque una "
             "defensa sin memoria no deja regla."),

            ("quote",
             "Una <em>voz</em> no es quien gana más causas, "
             "sino quien sabe decir qué recurso no ha "
             "depositado — y por qué."),

            ("para",
             "Defendemos a empresas y particulares que "
             "buscan un letrado — no un ejecutor de "
             "estándares, no un asistente en paquete. "
             "Empresas con contencioso bancario complejo, "
             "profesionales con responsabilidad profesional "
             "controvertida, contribuyentes con liquidaciones "
             "agresivas, entidades privadas con contencioso "
             "administrativo regulatorio, partes civiles en "
             "procesos penales tributarios. Nuestra firma es "
             "la de un Cassazionista único, no de una marca "
             "de bufete a varias manos: la responsabilidad "
             "técnica permanece concentrada, porque una "
             "evidencia, para ser sostenida, debe tener una "
             "voz. Las colaboraciones con consultores "
             "técnicos, peritos contables, fiscalistas "
             "especializados y consejeros de parte pasan por "
             "el bufete — no lo sustituyen. Defendemos poco, "
             "y hasta el final."),

            ("quote",
             "Publicar una voz no significa publicitarla. "
             "Significa dejar evidencia <em>sostenida</em> — "
             "para que quien venga después pueda "
             "contestarla, distinguirla o reconocerla."),

            ("para",
             "Las sentencias publicadas aquí no son un "
             "currículum forense. Son evidencias "
             "incardinadas, recogidas por materia y por año, "
             "con la documentación del juicio que las "
             "acompaña. Cada ficha nombra la jurisdicción, "
             "el grado, la materia, el año, el objeto del "
             "contencioso, y la voz depositada en cinco "
             "líneas — porque una decisión que no se deja "
             "contar en cinco líneas, probablemente todavía "
             "no se ha clarificado. Las cuatro decisiones "
             "seleccionadas a continuación cubren cuatro "
             "años y cuatro materias diferentes: una "
             "orientación de las Sezioni Unite sobre "
             "responsabilidad profesional, una casación "
             "civil en contencioso bancario, una sentencia "
             "del TAR Lombardia en administrativo "
             "regulatorio, y una apelación tributaria en "
             "Milán."),
        ],
        "narrative_side_rail": [
            ("Bufete · el letrado fundador",                 "studio"),
            ("Materias · las doce materias",                  "materie"),
            ("Publicaciones · repertorio interno",            "studio"),
            ("Contacto · someta un dictamen preliminar",      "contatti"),
        ],

        "sectors_label":    "MATERIAS · EL CAMPO DEL CONTENCIOSO",
        "sectors_lead":
            "Doce materias del contencioso: todas tratadas en "
            "el bufete, nunca delegadas a corresponsales "
            "externos. El bufete no se declara generalista ni "
            "especialista — escoge sus causas por objeto, por "
            "grado de jurisdicción y por jurisdicción.",
        "sectors": [
            "penal-tributario", "civil contractual", "administrativo regulatorio",
            "contencioso bancario", "responsabilidad profesional", "recobro complejo",
            "derecho societario", "tributario", "ejecución",
            "laboral complejo", "perito judicial", "mediación ENCA",
        ],
        "sectors_trailing":
            "Una materia entra en el bufete cuando la "
            "evidencia es incardinable y la jurisprudencia es "
            "legible. Sale cuando el expediente no se deja "
            "escribir en cinco líneas.",
        "sectors_counter":
            "Veintiocho sentencias citadas · catorce voces "
            "publicadas por el Foro Italiano y la "
            "Giurisprudenza Italiana entre <em>2008</em> y "
            "2024 · treinta y un años de defensa en todos los "
            "grados hasta la Casación.",

        "leadership_label":   "FUNDADOR DEL BUFETE · CASSAZIONISTA",
        "leadership_heading": "Lorenzo <em>Marchetti</em>",
        "leadership_role":
            "fundador · responsable de las memorias y de los recursos en Casación",
        "leadership_caption": "El bufete · despacho de Via Borgonuovo · 2024",
        "leadership_portrait": _PORTRAIT_FOUNDER,
        "leadership_bio_paragraphs": [
            "Lorenzo Marchetti abrió Causa en Milán en 1995, "
            "tras ocho años de defensa en dos despachos "
            "milaneses especializados en contencioso civil "
            "comercial y en derecho bancario. Se licenció en "
            "Derecho en la Università degli Studi di Milano "
            "en 1987, con una tesis sobre el concurso aparente "
            "de normas en derecho tributario, y obtuvo la "
            "especialización en derecho privado en la misma "
            "universidad. Está inscrito en el Colegio de "
            "Abogados de Milán desde 1995 y habilitado para "
            "comparecer ante las Magistraturas Superiores "
            "(Cassazionista) desde 2003. Trabaja a tiempo "
            "completo en los contenciosos del bufete: dirige "
            "la redacción de las memorias, escribe los "
            "recursos en Casación, sigue el procedimiento "
            "hasta el depósito de la decisión, y cuida el "
            "repertorio interno que publica las sentencias "
            "obtenidas.",

            "Entre las sentencias citadas: la orientación de "
            "las Sezioni Unite de 2024 en materia de "
            "responsabilidad profesional del consultor "
            "fiscal, la casación civil sez. III de 2023 "
            "sobre el derecho del cliente bancario al "
            "reembolso de los intereses anatocistas, una "
            "sentencia del TAR Lombardia de 2022 sobre la "
            "legitimidad de una sanción AGCOM, y la casación "
            "tributaria de 2021 sobre la interpretación del "
            "art. 36-bis D.P.R. 600/1973. Sus voces se "
            "recogen en catorce entradas publicadas por el "
            "Foro Italiano y la Giurisprudenza Italiana "
            "entre 2008 y 2024.",
        ],
        "leadership_credentials": [
            "Albo Avvocati Milano · Inscrito Colegio de Abogados de Milán · desde 1995",
            "Cassazionista · habilitado ante las Magistraturas Superiores desde 2003",
            "ENCA · Ente Nacional Conciliación Abogados · sección mediadores",
            "Albo CTU forense · Tribunale di Milano · sección contencioso civil",
        ],
        "leadership_secondary_cta_label": "Bufete · biografía extendida, voces en el repertorio",
        "leadership_secondary_cta_href":  "studio",

        "cases_label":   "CONTENCIOSO — EVIDENCIAS INCARDINADAS",
        "cases_intro":
            "Cuatro evidencias depositadas, en orden "
            "cronológico inverso. Jurisdicción, grado, "
            "materia, año, objeto del contencioso y la voz.",
        "cases_magazine": [
            {
                "rank":     "hero",
                "num":      "01",
                "eyebrow":  "01 · CASS. SS.UU. · 2024 · RESPONSABILIDAD PROFESIONAL",
                "title":
                    "Sezioni Unite — la responsabilidad "
                    "profesional del consultor fiscal, releída "
                    "como obligación de resultado "
                    "<em>incardinada</em> en la evidencia "
                    "preliminar",
                "body":
                    "Causa fue letrado de la parte recurrente "
                    "en el recurso que las Sezioni Unite de la "
                    "Corte de Casación resolvieron en abril "
                    "de 2024, por remisión de la tercera "
                    "sección civil. La controversia oponía a "
                    "un contribuyente frente a su consultor "
                    "fiscal, en materia de responsabilidad "
                    "profesional por omisión de señalización "
                    "de un plazo de impugnación tributaria. "
                    "El bufete ha sostenido, y la Corte ha "
                    "acogido, la orientación según la cual la "
                    "responsabilidad del consultor fiscal se "
                    "incardina en la evidencia preliminar de "
                    "la que el profesional podía y debía "
                    "tener conocimiento al momento del "
                    "encargo — releyendo la prestación como "
                    "obligación de resultado circunscrito. "
                    "La voz ha sido publicada por el Foro "
                    "Italiano (entrada n.º 14 del repertorio "
                    "interno).",
                "pill":
                    "Cassazione SS.UU.  ·  grado de legitimidad  ·  2024  ·  recurrente",
                "photo":    _CASE_HIGHCOURT_EXTERIOR,
                "photo_alt":
                    "Detalle arquitectónico de alta corte "
                    "italiana · frontón clásico con "
                    "inscripción latina · luz fría overcast",
                "slug":     "cass-ssuu-responsabilita-consulente-fiscale-2024",
                "citation_label": "Ver la voz n.º 14",
                "citation":
                    "Cass. SS.UU. n. 11237/2024 — La "
                    "<em>responsabilidad</em> profesional "
                    "del consultor fiscal se incardina en la "
                    "evidencia preliminar de la que el "
                    "profesional podía y debía tener "
                    "conocimiento al momento del encargo, "
                    "releída la prestación como obligación "
                    "de resultado circunscrito al objeto "
                    "del mandato. Entrada n.º 14 del "
                    "repertorio interno · publicada Foro "
                    "Italiano 2024.",
            },
            {
                "rank":     "small",
                "num":      "02",
                "eyebrow":  "02 · CASS. CIV. SEZ. III · 2023 · CONTENCIOSO BANCARIO",
                "title":
                    "Casación civil sez. III — anatocismo "
                    "bancario y carga de la prueba en la "
                    "<em>jurisprudencia</em> de legitimidad",
                "body":
                    "Causa ha defendido al cliente bancario "
                    "en la casación civil sez. III de "
                    "octubre de 2023, en materia de reembolso "
                    "de los intereses anatocistas "
                    "satisfechos en una cuenta corriente "
                    "entre 2003 y 2014. El bufete ha "
                    "sostenido la atribución de la carga "
                    "probatoria del nexo causal a la "
                    "entidad bancaria, conforme a la "
                    "orientación de legitimidad consolidada "
                    "desde 2014. La sentencia ha casado con "
                    "remisión. Entrada n.º 11 del repertorio "
                    "interno.",
                "pill":
                    "Cass. civ. III  ·  grado de legitimidad  ·  2023  ·  recurrente",
                "photo":    _CASE_FASCICOLI_STACK,
                "photo_alt":
                    "Pila de expedientes legales con "
                    "etiquetas de registro · luz fría de "
                    "escritorio · macro · cero personas",
                "slug":     "cass-civ-iii-anatocismo-bancario-2023",
                "citation_label": "Ver la voz n.º 11",
                "citation":
                    "Cass. civ. sez. III n. 28914/2023 — En "
                    "materia de reembolso de los intereses "
                    "<em>anatocistas</em> satisfechos en "
                    "cuenta corriente bancaria, la carga "
                    "probatoria del nexo causal entre "
                    "capitalización trimestral y aumento "
                    "del saldo recae sobre la entidad "
                    "bancaria, conforme a la orientación "
                    "de legitimidad consolidada desde "
                    "2014. Casa con remisión. Entrada "
                    "n.º 11 del repertorio interno.",
            },
            {
                "rank":     "small",
                "num":      "03",
                "eyebrow":  "03 · TAR LOMBARDIA · 2022 · ADMINISTRATIVO REGULATORIO",
                "title":
                    "TAR Lombardia — anulación de una "
                    "sanción AGCOM y el <em>principio</em> "
                    "de proporcionalidad",
                "body":
                    "Causa fue letrado de la parte "
                    "recurrente en el procedimiento de primer "
                    "grado ante el TAR Lombardia, sez. III, "
                    "concluido en abril de 2022 con "
                    "anulación de la sanción AGCOM "
                    "impugnada por desviación de poder y "
                    "violación del principio de "
                    "proporcionalidad de la sanción "
                    "administrativa pecuniaria, a la luz de "
                    "la orientación del Consejo de Estado "
                    "de 2019. La sentencia no fue apelada "
                    "por AGCOM. Entrada n.º 9 del "
                    "repertorio interno.",
                "pill":
                    "TAR Lombardia  ·  primer grado  ·  2022  ·  recurrente",
                "photo":    _CASE_BENCH_CHAIR,
                "photo_alt":
                    "Silla de estrado vacía · alto respaldo "
                    "de roble · paneles verticales de madera "
                    "al fondo · luz fría · cero personas",
                "slug":     "tar-lombardia-agcom-proporzionalita-2022",
                "citation_label": "Ver la voz n.º 9",
                "citation":
                    "TAR Lombardia sez. III n. 814/2022 — "
                    "Anulación de la sanción AGCOM por "
                    "desviación de poder y violación del "
                    "<em>principio</em> de proporcionalidad "
                    "de la sanción administrativa "
                    "pecuniaria, a la luz de la "
                    "orientación del Consejo de Estado sec. "
                    "VI 4419/2019. Sentencia no apelada por "
                    "AGCOM. Entrada n.º 9 del repertorio "
                    "interno.",
            },
            {
                "rank":     "small",
                "num":      "04",
                "eyebrow":  "04 · CORTE DE APELACIÓN DE MILÁN · 2021 · TRIBUTARIO",
                "title":
                    "Apelación Milán — el art. 36-bis D.P.R. "
                    "600/1973 y el perímetro de la "
                    "<em>controversia</em> tributaria",
                "body":
                    "Causa ha sostenido, en grado de "
                    "apelación ante la Corte d'Appello di "
                    "Milano sez. tributaria, la "
                    "interpretación restrictiva del art. "
                    "36-bis D.P.R. 600/1973 en materia de "
                    "liquidación automatizada de las "
                    "declaraciones tributarias. La "
                    "sentencia, depositada en septiembre de "
                    "2021, ha reformado la decisión de "
                    "primer grado de la Comisión Tributaria, "
                    "anulando la providencia de pago. "
                    "Entrada n.º 7 del repertorio interno.",
                "pill":
                    "App. Milano trib.  ·  segundo grado  ·  2021  ·  apelante",
                "photo":    _CASE_CODEX_SPINE,
                "photo_alt":
                    "Macro del lomo de un códice "
                    "encuadernado · tipografía de oro sobre "
                    "cuero oscuro · numeración romana · luz "
                    "fría suave",
                "slug":     "appello-milano-art-36bis-dpr-600-1973-2021",
                "citation_label": "Ver la voz n.º 7",
                "citation":
                    "Corte d'Appello Milano sez. trib. n. "
                    "3187/2021 — Interpretación restrictiva "
                    "del art. 36-bis D.P.R. 29 de "
                    "septiembre de 1973 n. 600 en materia "
                    "de liquidación automatizada de las "
                    "declaraciones tributarias · el "
                    "perímetro de la <em>controversia</em> "
                    "tributaria se limita a los meros "
                    "errores materiales y de cálculo "
                    "detectables a partir de la "
                    "declaración, excluida toda valoración "
                    "de fondo. Sentencia reformada en "
                    "apelación. Entrada n.º 7 del "
                    "repertorio interno.",
            },
        ],
        "cases_trailing_label": "Todo el contencioso · cronología 1995–2024",
        "cases_trailing_href":  "contenzioso",

        "cta_label":     "DICTAMEN PRELIMINAR",
        "cta_intro":
            "Toda defensa comienza por una sola página: el dictamen preliminar.",
        "cta_heading":
            "Cada sentencia es una <em>evidencia</em> incardinada — no una opinión defendida.",
        "cta_form_hint":
            "Objeto del contencioso · grado de jurisdicción "
            "· contraparte · franja de valor · jurisdicción "
            "· evidencia preliminar adjuntable. Respuesta en "
            "cinco días hábiles.",
        "cta_primary":   "Someta un dictamen preliminar",
        "cta_primary_href": "contatti",
        "cta_closing_line":
            "Ninguna llamada de descubrimiento. Ningún "
            "mandato sin screening. Solo la evidencia, y su "
            "jurisdicción.",
        "cta_sub_line":
            "Causa · bufete · Milán · desde 1995",
    },

    "studio": {
        "eyebrow":   "EL BUFETE · QUIÉNES SOMOS · CV",
        "headline":
            "Causa · bufete de defensa editorial desde <em>1995</em>.",
        "intro":
            "Milán. Un letrado fundador, dos asociados, una "
            "secretaría. Defendemos poco, y hasta el final.",
        "primary_cta":  "Someta un dictamen preliminar",

        "history_label":   "HITOS DEL BUFETE",
        "history_heading": "Cinco fechas, treinta y un años de defensa editorial.",
        "history_intro":
            "Cinco elecciones estructurales detrás de las "
            "cuales se lee el carácter del bufete — la "
            "autoría de un Cassazionista único, el "
            "repertorio interno como método, la "
            "jurisdicción como primera forma de respeto, la "
            "materia como campo del contencioso, la "
            "defensa hasta el depósito de la decisión.",
        "history": [
            ("1995", "Fundación",
             "Lorenzo Marchetti abre Causa en Via Borgonuovo "
             "en Milán, tras ocho años de defensa en dos "
             "despachos milaneses especializados en "
             "contencioso civil comercial y en derecho "
             "bancario. La sede se elige por una sola razón: "
             "tres salas en un patio interior, una para la "
             "redacción de las memorias, una para el "
             "repertorio interno, una para la secretaría."),
            ("2003", "Habilitación Cassazionista",
             "Lorenzo Marchetti obtiene la habilitación "
             "para comparecer ante las Magistraturas "
             "Superiores (Cassazionista). Desde ese año el "
             "bufete acepta recursos de casación en materia "
             "civil, tributaria y administrativa, y atiende "
             "las memorias de parte recurrida en juicios "
             "de legitimidad."),
            ("2008", "Primera voz publicada en el repertorio",
             "La primera sentencia de legitimidad citando "
             "una orientación sostenida por el bufete es "
             "publicada por el Foro Italiano. Desde ese año "
             "el bufete registra cada sentencia obtenida — "
             "ganada o perdida — en el repertorio interno "
             "dentro de los sesenta días desde el depósito."),
            ("2018", "Inscripción Albo CTU forense",
             "El bufete se inscribe en el Albo CTU forense "
             "del Tribunale di Milano (sección contencioso "
             "civil). Desde ese año acepta consultorías "
             "técnicas de oficio sobre contencioso "
             "societario, valoraciones de empresa "
             "controvertidas y responsabilidad contable."),
            ("2024", "Decimocuarta voz en el repertorio interno",
             "La decimocuarta voz del bufete entra en el "
             "repertorio interno: la orientación de las "
             "Sezioni Unite en materia de responsabilidad "
             "profesional del consultor fiscal, con "
             "remisión de la tercera sección civil. "
             "Defensa del cliente recurrente, sentencia "
             "depositada en abril, voz publicada por el "
             "Foro Italiano."),
        ],

        "values_label":   "PRINCIPIOS EDITORIALES",
        "values_heading": "Cuatro principios <em>no negociables</em>",
        "values_intro":
            "Cuatro principios separan una defensa Causa de "
            "un mandato estandarizado. Están escritos en el "
            "pacto de mandato firmado en primera vista, no "
            "en el sitio.",
        "values": [
            ("01", "Un Cassazionista autorial",
             "La firma del recurso es la de un único "
             "letrado, no la de una marca de bufete a "
             "varias manos. La responsabilidad técnica "
             "permanece concentrada, porque una evidencia, "
             "para ser sostenida, debe tener una voz. Las "
             "colaboraciones externas pasan por el bufete "
             "— no lo sustituyen."),
            ("02", "La jurisdicción como primer gesto",
             "Cada causa se abre con un screening serio de "
             "la jurisdicción. La materia que ya existe se "
             "lee como un expediente, con sus precedentes, "
             "sus grados, sus excepciones preliminares. "
             "Ninguna defensa antes de que el foro, el "
             "grado y la jurisdicción hayan sido leídos "
             "íntegramente."),
            ("03", "El repertorio interno como método",
             "Todas las sentencias obtenidas — ganadas y "
             "perdidas — se inscriben en el repertorio "
             "interno dentro de los sesenta días desde el "
             "depósito, con la documentación del juicio "
             "completa. El repertorio no es marketing: es "
             "la regla que dejamos a quien venga después."),
            ("04", "Sin screenings rechazados de pago",
             "Los dictámenes preliminares que no superan la "
             "fase de screening se devuelven con una nota "
             "motivada, gratuitamente. No facturamos "
             "screenings rechazados. La valoración de la "
             "incardinabilidad de la evidencia es la "
             "puerta del bufete, no un servicio a "
             "consumo."),
        ],

        "team_label":   "BUFETE Y ASOCIADOS",
        "team_heading": "Tres letrados, una sola sede, una sola secretaría.",
        "team_intro":
            "El bufete está formado por un letrado fundador "
            "Cassazionista, dos asociados y una secretaría. "
            "Defendemos a tiempo completo entre doce y "
            "dieciocho causas en paralelo — nunca más de "
            "veinte. Los trámites con la secretaría "
            "judicial, las oficinas de la Fiscalía, la "
            "Avvocatura dello Stato y los entes "
            "reguladores se tratan en el bufete, nunca "
            "delegados a corresponsales externos.",
        "team": [
            {"name": "Lorenzo Marchetti",
             "role": "Studio Founder · Letrado Cassazionista",
             "office": "Milán",
             "bio":
                "Fundador. Università degli Studi di Milano "
                "· Derecho · especialización en derecho "
                "privado. Colegio de Abogados de Milán "
                "desde 1995 · Cassazionista desde 2003 · "
                "ENCA mediadores · Albo CTU forense "
                "Tribunale di Milano. Dirige la redacción "
                "de las memorias, escribe los recursos en "
                "Casación, cuida el repertorio interno."},
            {"name": "Avv. Chiara Bevilacqua",
             "role": "Letrada asociada · Societario + bancario",
             "office": "Milán",
             "bio":
                "Asociada desde 2017 · Colegio de Abogados "
                "de Milán desde 2014 · especialización en "
                "derecho societario y contencioso bancario "
                "· supervisa las memorias de parte "
                "recurrente en los contenciosos societarios "
                "y en las acciones de responsabilidad · "
                "referente del repertorio interno · "
                "inscrita sección mediadores ENCA desde "
                "2020."},
            {"name": "Avv. Tommaso De Luca",
             "role": "Letrado asociado · Administrativo + tributario",
             "office": "Milán",
             "bio":
                "Asociado desde 2021 · Colegio de Abogados "
                "de Milán desde 2018 · especialización en "
                "derecho administrativo y contencioso "
                "tributario · referente para los recursos "
                "ante el TAR Lombardia y las Comisiones "
                "Tributarias · Albo CTU forense Tribunale "
                "di Milano desde 2022 (sección "
                "contencioso civil)."},
        ],

        "coordinates_label": "LA SEDE",
        "coordinates": [
            ("Milán", "Via Borgonuovo 14 · 20121 · tres salas en patio interior"),
            ("Bufete", "con cita previa · lunes-viernes · 09:00-18:00"),
            ("Foro di Milano", "trámites con la secretaría judicial internos · cero corresponsales externos"),
        ],

        "cta_heading": "Una defensa comienza por una sola página.",
        "cta_intro":
            "La primera página de toda defensa es el "
            "dictamen preliminar: una ficha de síntesis que "
            "el bufete lee íntegramente, y a la que "
            "responde en cinco días hábiles con una nota "
            "motivada. Si el dictamen es negativo, la nota "
            "motivada se entrega igualmente gratis · sin "
            "facturación de screening · sin obligación de "
            "mandato.",
        "cta_primary":   "Someta un dictamen preliminar",
        "cta_primary_href": "contatti",
    },

    "materie": {
        "eyebrow":  "MATERIAS · LAS DOCE MATERIAS DEL CONTENCIOSO",
        "headline": "Las <em>materias</em> del contencioso — doce, todas tratadas en el bufete.",
        "intro":
            "El bufete no se declara generalista ni "
            "especialista. Las materias son el campo del "
            "contencioso: lo que determina la jurisdicción "
            "y el grado de jurisdicción. Una materia entra "
            "en el bufete cuando la evidencia es "
            "incardinable y la jurisprudencia es legible "
            "en cinco líneas.",
        "primary_cta":  "Someta un dictamen preliminar",

        "svc_duration_label": "Foro · grado",
        "svc_leader_label":   "Defensa",

        "services": [
            {
                "num":   "01",
                "title": "Penal-tributario",
                "blurb":
                    "Defensa en todos los grados del "
                    "proceso penal-tributario para "
                    "empresarios, administradores y "
                    "profesionales liberales. Defensa en "
                    "procesos por omisión de declaración, "
                    "omisión de pago, sustracción "
                    "fraudulenta al pago de impuestos al "
                    "amparo del D.lgs. 74/2000.",
                "scope": [
                    "Defensa de imputados y partes civiles",
                    "Procedimientos especiales y conformidad ex art. 444 c.p.p.",
                    "Recursos de casación penal (sez. III + sez. V)",
                    "Coordinación con consultores tributarios de parte",
                ],
                "duration": "Tribunal · Apel. · Casación",
                "leader":   "Lorenzo Marchetti",
            },
            {
                "num":   "02",
                "title": "Civil contractual",
                "blurb":
                    "Contencioso civil sobre contratos "
                    "comerciales, suministro, agencia, "
                    "distribución, prestación de servicios. "
                    "Acciones de incumplimiento, "
                    "resolución contractual, "
                    "responsabilidad por daños y acciones "
                    "de nulidad por vicio del "
                    "consentimiento.",
                "scope": [
                    "Causas de valor superior a € 50.000",
                    "Demandas y conclusiones autorizadas",
                    "Medidas cautelares ex art. 700 c.p.c.",
                    "Recursos de casación civil",
                ],
                "duration": "Tribunal · Apel. · Casación",
                "leader":   "Lorenzo Marchetti",
            },
            {
                "num":   "03",
                "title": "Administrativo regulatorio",
                "blurb":
                    "Recursos contra los actos de las "
                    "Autoridades independientes (AGCOM, "
                    "AGCM, Garante Privacy, ANAC). "
                    "Impugnación de actos sancionadores, "
                    "denegatorios, inhibitorios. Defensa "
                    "en primer grado TAR y en apelación "
                    "ante el Consejo de Estado.",
                "scope": [
                    "Recursos al TAR Lombardia · sez. III · regulatorias",
                    "Apelaciones al Consejo de Estado · sez. VI",
                    "Conclusiones de vista oral",
                    "Coordinación con consultores técnicos de parte",
                ],
                "duration": "TAR · Cons. Estado",
                "leader":   "Tommaso De Luca",
            },
            {
                "num":   "04",
                "title": "Contencioso bancario",
                "blurb":
                    "Causas contra entidades de crédito por "
                    "anatocismo bancario, usura, errónea "
                    "comunicación a la Central de Riesgos, "
                    "impugnación de contratos de "
                    "préstamo, leasing y derivados. "
                    "Defensa en todos los grados, hasta la "
                    "Casación civil.",
                "scope": [
                    "CTU contables y peritajes de parte",
                    "Acciones de restitución y de nulidad de cláusulas",
                    "Recursos de casación civil sez. I + III",
                    "Coordinación con peritos bancarios independientes",
                ],
                "duration": "Trib. · Apel. · Casación",
                "leader":   "Chiara Bevilacqua",
            },
            {
                "num":   "05",
                "title": "Responsabilidad profesional",
                "blurb":
                    "Acciones de responsabilidad contra "
                    "consultores fiscales, abogados, "
                    "médicos, profesionales técnicos. "
                    "Defensa tanto de la parte dañada como "
                    "del profesional demandado. Materia "
                    "en evolución jurisprudencial constante "
                    "(cf. Cass. SS.UU. 2024).",
                "scope": [
                    "Acciones resarcitorias contractuales y extracontractuales",
                    "Cuantificación del daño según legitimidad",
                    "Recursos de casación (incluidas SS.UU.)",
                    "Memorias técnicas y reconstrucción de la evidencia",
                ],
                "duration": "Trib. · Apel. · Casación · SS.UU.",
                "leader":   "Lorenzo Marchetti",
            },
            {
                "num":   "06",
                "title": "Recobro complejo",
                "blurb":
                    "Recobro de créditos comerciales "
                    "superiores a € 50.000 · "
                    "monitorios y oposiciones "
                    "correspondientes · ejecuciones "
                    "mobiliarias e inmobiliarias · "
                    "acciones revocatorias ordinarias y "
                    "concursales.",
                "scope": [
                    "Monitorios y oposiciones",
                    "Ejecuciones ante terceros y revocatorias",
                    "Embargos inmobiliarios y mobiliarios",
                    "Coordinación con peritos de tasación",
                ],
                "duration": "Trib. · Ejecuciones",
                "leader":   "Chiara Bevilacqua",
            },
            {
                "num":   "07",
                "title": "Derecho societario",
                "blurb":
                    "Acciones de responsabilidad contra "
                    "administradores, síndicos y "
                    "directores generales. Impugnación de "
                    "acuerdos de junta y consejo. Pactos "
                    "parasociales, covenant breach. "
                    "Contencioso entre socios en "
                    "sociedades de capital.",
                "scope": [
                    "Acciones ex artt. 2392-2395 c.c.",
                    "Impugnaciones de acuerdos ex art. 2377 c.c.",
                    "Causas ante el Tribunal de las Empresas",
                    "Recursos de casación civil sez. I",
                ],
                "duration": "Trib. impr. · Apel. · Casación",
                "leader":   "Chiara Bevilacqua",
            },
            {
                "num":   "08",
                "title": "Tributario",
                "blurb":
                    "Recursos contra actos de liquidación "
                    "de la Agencia Tributaria. Defensa "
                    "ante las Cortes de Justicia "
                    "Tributaria de primer y segundo grado. "
                    "Recursos de casación en materia "
                    "tributaria.",
                "scope": [
                    "Providencias de pago e inscripciones a recibo",
                    "Liquidaciones y rectificaciones",
                    "Conclusiones de contradictorio previo",
                    "Recursos ex art. 360 c.p.c. n. 3",
                ],
                "duration": "CGT 1° · CGT 2° · Casación",
                "leader":   "Tommaso De Luca",
            },
            {
                "num":   "09",
                "title": "Ejecución",
                "blurb":
                    "Procedimientos ejecutivos "
                    "mobiliarios, inmobiliarios, ante "
                    "terceros. Oposiciones a la ejecución "
                    "y a los actos ejecutivos. Defensa de "
                    "los acreedores ejecutantes y de los "
                    "deudores ejecutados.",
                "scope": [
                    "Embargos inmobiliarios y procedimientos de venta",
                    "Oposiciones ex artt. 615, 617, 619 c.p.c.",
                    "Distribución del producto",
                    "Coordinación con custodios judiciales",
                ],
                "duration": "Trib. ejecuciones",
                "leader":   "Chiara Bevilacqua",
            },
            {
                "num":   "10",
                "title": "Laboral complejo",
                "blurb":
                    "Contencioso laboral de alta "
                    "complejidad — despidos directivos, "
                    "acoso, descenso de categoría, "
                    "retribución variable controvertida. "
                    "Casos con implicaciones societarias o "
                    "regulatorias. NO contencioso "
                    "individual estándar.",
                "scope": [
                    "Despidos ex artt. 18 St. lav. + Jobs Act",
                    "Acciones resarcitorias por acoso y descenso de categoría",
                    "Pactos de no concurrencia y recursos cautelares",
                    "Recursos de casación civil sez. trabajo",
                ],
                "duration": "Trib. lab. · Apel. · Casación",
                "leader":   "Lorenzo Marchetti",
            },
            {
                "num":   "11",
                "title": "Perito judicial",
                "blurb":
                    "El bufete está inscrito en el Albo "
                    "CTU forense del Tribunale di Milano "
                    "(sección contencioso civil). "
                    "Consultorías técnicas sobre "
                    "contencioso societario, valoraciones "
                    "de empresa controvertidas y "
                    "responsabilidad contable.",
                "scope": [
                    "CTU sobre contencioso societario",
                    "Valoraciones de empresa controvertidas",
                    "Responsabilidad contable y financiera",
                    "Informes periciales por mandato del juez",
                ],
                "duration": "CTU · Trib. Milano",
                "leader":   "Tommaso De Luca",
            },
            {
                "num":   "12",
                "title": "Mediación ENCA",
                "blurb":
                    "El bufete está inscrito en la "
                    "sección mediadores ENCA (Ente "
                    "Nacional Conciliación Abogados). "
                    "Mediación civil obligatoria en las "
                    "materias de la ley, mediación "
                    "delegada, y procedimientos "
                    "arbitrales en convenio de arbitraje "
                    "ritual.",
                "scope": [
                    "Mediación civil obligatoria ex D.lgs. 28/2010",
                    "Mediaciones delegadas por el juez",
                    "Arbitrajes rituales ex artt. 806 ss. c.p.c.",
                    "Actas de acuerdo y de cierre motivado",
                ],
                "duration": "ENCA · arbitraje",
                "leader":   "Chiara Bevilacqua",
            },
        ],

        "process_label":   "MÉTODO · CUATRO ESTACIONES DE LA DEFENSA",
        "process_heading": "Cuatro fases, una sola secuencia forense.",
        "process": [
            ("01", "Jurisdicción",
             "La materia que ya existe se lee como un "
             "expediente. Foro, grado, excepciones "
             "preliminares. La jurisdicción es la primera "
             "forma de respeto y dura típicamente cinco "
             "días de screening."),
            ("02", "Fondo",
             "Objeto del contencioso, partes en causa, "
             "franja de valor, urgencia procesal, "
             "evidencia preliminar adjuntable. El fondo "
             "es el marco de la defensa: define qué "
             "recurso se escribe y cuál no."),
            ("03", "Voz",
             "El recurso se escribe como una tesis "
             "citable — qué principio invoca, qué "
             "orientación confirma, qué evidencia "
             "deposita. Cinco líneas en las que la "
             "decisión debe poder contarse."),
            ("04", "Depósito",
             "Vista a vista, grado a grado, hasta el "
             "depósito de la decisión. Todas las "
             "sentencias obtenidas permanecen escritas "
             "en el repertorio interno · publicadas "
             "dentro de los sesenta días desde el "
             "depósito."),
        ],

        "cta_heading":   "¿Qué materia conviene a su contencioso?",
        "cta_intro":
            "Si la materia no está clara, escríbanos una "
            "breve descripción del objeto del contencioso "
            "y del grado de jurisdicción actual. Le "
            "indicaremos la materia correcta en cinco "
            "días hábiles · en cuarenta y ocho horas si "
            "la urgencia es procesal (plazo en "
            "vencimiento · vista fijada).",
        "cta_primary":   "Someta un dictamen preliminar",
        "cta_primary_href": "contatti",
    },

    "contenzioso": {
        "eyebrow":  "CONTENCIOSO · CRONOLOGÍA 1995-2024",
        "headline":
            "Las sentencias citadas — la <em>cronología</em> de la defensa · 1995–2024.",
        "intro":
            "Catorce voces publicadas por el Foro Italiano "
            "y la Giurisprudenza Italiana, más los demás "
            "contenciosos seleccionados. Todas registradas "
            "en el repertorio interno dentro de los "
            "sesenta días desde el depósito.",
        "primary_cta":  "Someta un dictamen preliminar",

        "cases_label": "Cuatro decisiones representativas · en detalle",
        "cases_intro":
            "El bufete registra cada sentencia obtenida — "
            "ganada o perdida — en el repertorio interno "
            "dentro de los sesenta días desde el depósito. "
            "Las cuatro decisiones destacadas a "
            "continuación son las elegidas editorialmente "
            "para ilustrar el método del bufete: una para "
            "las Sezioni Unite de la Casación, una para "
            "la casación civil sección simple, una para el "
            "contencioso administrativo, y una para el "
            "contencioso tributario en apelación.",

        "cta_heading":   "¿Una causa similar a la suya?",
        "cta_intro":
            "Los expedientes completos (memorias, "
            "recursos, contrademandas, documentación del "
            "juicio, nota a sentencia) están disponibles "
            "en el bufete previa solicitud motivada. La "
            "consulta es gratuita conforme al Codice "
            "Deontologico Forense; la copia integral del "
            "repertorio interno se obtiene a cobertura de "
            "gastos de impresión.",
        "cta_primary":   "Someta un dictamen preliminar",
        "cta_primary_href": "contatti",
    },

    "posts": [
        {
            "slug":     "cass-ssuu-responsabilita-consulente-fiscale-2024",
            "title":
                "Sezioni Unite — la responsabilidad "
                "profesional del consultor fiscal, releída "
                "como obligación de resultado incardinada "
                "en la evidencia preliminar",
            "category": "Responsabilidad profesional",
            "year":     "2024 · depósito abril",
            "duration": "Cassazione SS.UU. · grado de legitimidad · casada sin remisión",
            "client_code":
                "Cassazione · Sezioni Unite civiles · "
                "remisión de la tercera sección civil · "
                "recurrente principal · contraparte: "
                "consultor fiscal demandado · materia: "
                "responsabilidad profesional · obligación "
                "de resultado circunscrito vs obligación "
                "de medios.",
            "lead":
                "La controversia ha sido remitida a la "
                "cognición de las Sezioni Unite de la "
                "Corte de Casación por la tercera sección "
                "civil, en razón del conflicto entre dos "
                "orientaciones de legitimidad sobre la "
                "calificación de la obligación del "
                "consultor fiscal respecto del "
                "señalamiento oportuno de un plazo de "
                "impugnación tributaria.",
            "sections": [
                {
                    "label": "La jurisdicción",
                    "heading": "Remisión de la tercera sección civil a las Sezioni Unite",
                    "body":
                        "El procedimiento ha sido remitido "
                        "a la cognición de las Sezioni Unite "
                        "de la Corte de Casación por la "
                        "tercera sección civil, mediante "
                        "ordenanza interlocutoria de "
                        "septiembre de 2023, en razón del "
                        "conflicto entre dos orientaciones "
                        "de legitimidad sobre la "
                        "calificación de la obligación del "
                        "consultor fiscal. La primera "
                        "orientación (dominante entre 2014 "
                        "y 2020) calificaba la obligación "
                        "como obligación de medios, con la "
                        "consecuente prueba del nexo "
                        "causal sobre el cliente; la "
                        "segunda (emergente desde 2021) "
                        "calificaba la obligación como "
                        "obligación de resultado "
                        "circunscrito.",
                },
                {
                    "label": "El argumento sostenido",
                    "heading": "Obligación de resultado incardinada en la evidencia preliminar",
                    "body":
                        "El bufete, en calidad de letrado "
                        "del cliente recurrente, ha "
                        "sostenido la orientación de la "
                        "obligación de resultado "
                        "circunscrito, invocando el "
                        "principio de previsibilidad de la "
                        "evidencia preliminar al momento "
                        "del encargo profesional. La "
                        "memoria de defensa ha invocado la "
                        "orientación de la casación civil "
                        "sec. III de 2022 sobre los "
                        "criterios de previsibilidad del "
                        "plazo de impugnación tributaria, "
                        "y ha propuesto la relectura de la "
                        "obligación como responsabilidad "
                        "incardinada sobre la diligencia "
                        "calificada exigida al consultor.",
                },
                {
                    "label": "El resultado",
                    "heading": "Casada sin remisión · entrada n.º 14",
                    "body":
                        "Las Sezioni Unite han acogido la "
                        "reconstrucción sostenida por el "
                        "bufete, confirmando la orientación "
                        "de la obligación de resultado "
                        "circunscrito e incardinándola en "
                        "el criterio de previsibilidad de "
                        "la evidencia preliminar. La "
                        "sentencia ha casado sin remisión "
                        "la sentencia de segundo grado de "
                        "la Corte de Apelación, declarando "
                        "la responsabilidad del consultor "
                        "fiscal demandado y cuantificando "
                        "el daño según la jurisprudencia "
                        "consolidada de legitimidad. La "
                        "voz ha sido publicada por el "
                        "Foro Italiano (entrada n.º 14 del "
                        "repertorio interno del bufete).",
                },
            ],
            "kpi": [
                ("SS.UU.",       "Sezioni Unite civiles"),
                ("abril 2024",   "depósito sentencia"),
                ("casada",       "sin remisión"),
                ("entrada 14",   "Foro Italiano"),
            ],
            "lead_partner": "Lorenzo Marchetti · Studio Founder",
            "team":
                "Letrado fundador + 1 asociada · redacción "
                "del recurso, contrademanda y memoria de "
                "defensa con vistas a la audiencia ante las "
                "Sezioni Unite",
            "next_label":   "Cronología siguiente",
        },
        {
            "slug":     "cass-civ-iii-anatocismo-bancario-2023",
            "title":
                "Casación civil sez. III — anatocismo "
                "bancario y carga de la prueba en la "
                "jurisprudencia de legitimidad",
            "category": "Contencioso bancario",
            "year":     "2023 · depósito octubre",
            "duration": "Cass. civ. III · grado de legitimidad · casada con remisión",
            "client_code":
                "Cassazione · sección III civil · "
                "recurrente · contraparte: entidad "
                "bancaria recurrida · materia: anatocismo "
                "bancario · carga de la prueba del nexo "
                "causal en cabeza de la entidad.",
            "lead":
                "El procedimiento de primer y segundo "
                "grado había rechazado la demanda del "
                "cliente bancario de reembolso de los "
                "intereses anatocistas. El bufete ha "
                "interpuesto recurso de casación, "
                "sosteniendo la atribución de la carga "
                "probatoria a la entidad de crédito.",
            "sections": [
                {
                    "label": "Los grados anteriores",
                    "heading": "Tribunal de Milán sec. empresas y Corte de Apelación de Milán",
                    "body":
                        "El procedimiento de primer grado "
                        "ante el Tribunal de Milán sec. "
                        "empresas y el de segundo grado "
                        "ante la Corte de Apelación de "
                        "Milán habían rechazado la "
                        "demanda del cliente bancario de "
                        "reembolso de los intereses "
                        "anatocistas satisfechos en una "
                        "cuenta corriente entre 2003 y "
                        "2014, con la motivación de que el "
                        "cliente no había aportado prueba "
                        "específica de la capitalización "
                        "ilegítima.",
                },
                {
                    "label": "El argumento sostenido",
                    "heading": "Carga probatoria incardinada sobre la entidad bancaria",
                    "body":
                        "El bufete ha interpuesto recurso "
                        "de casación, sosteniendo la "
                        "atribución de la carga probatoria "
                        "del nexo causal a la entidad "
                        "bancaria, en conformidad con la "
                        "orientación de legitimidad "
                        "consolidada por la casación "
                        "civil sec. I de 2014 y por las "
                        "Sezioni Unite de 2018. El recurso "
                        "ha articulado la relectura de la "
                        "disciplina del anatocismo "
                        "bancario en el marco de la "
                        "asimetría informativa entre "
                        "entidad de crédito y cliente "
                        "titular de cuenta.",
                },
                {
                    "label": "El resultado",
                    "heading": "Casada con remisión · entrada n.º 11",
                    "body":
                        "La casación civil sec. III ha "
                        "casado la sentencia de apelación "
                        "con remisión a la Corte de "
                        "Apelación de Milán en distinta "
                        "composición, acogiendo la "
                        "orientación sostenida por el "
                        "bufete. El procedimiento de "
                        "remisión ha sido ordenado bajo el "
                        "principio de legitimidad "
                        "conforme. La voz ha sido "
                        "registrada en el repertorio "
                        "interno (n.º 11) y está "
                        "pendiente de publicación externa.",
                },
            ],
            "kpi": [
                ("Cass. III",      "sección simple"),
                ("octubre 2023",   "depósito sentencia"),
                ("casada",         "con remisión"),
                ("entrada 11",     "repertorio interno"),
            ],
            "lead_partner": "Lorenzo Marchetti · Studio Founder",
            "team":
                "Letrado fundador + 1 asociada · recurso "
                "de casación, contrademanda y memoria "
                "depositada con vistas a la audiencia · "
                "apoyo perito bancario independiente",
            "next_label":   "Cronología siguiente",
        },
        {
            "slug":     "tar-lombardia-agcom-proporzionalita-2022",
            "title":
                "TAR Lombardia — anulación de una "
                "sanción AGCOM y el principio de "
                "proporcionalidad",
            "category": "Administrativo regulatorio",
            "year":     "2022 · depósito abril",
            "duration": "TAR Lombardia · primer grado · anulación íntegra",
            "client_code":
                "TAR Lombardia · sección III · "
                "recurrente · contraparte: AGCOM · "
                "materia: administrativo regulatorio · "
                "sanción pecuniaria · principio de "
                "proporcionalidad ex Cons. Estado sec. "
                "VI 2019.",
            "lead":
                "El bufete ha interpuesto recurso ante "
                "el TAR Lombardia para la anulación de "
                "una sanción AGCOM impuesta a un "
                "operador de comunicaciones electrónicas "
                "por presunta vulneración de las normas "
                "sobre transparencia de las ofertas "
                "comerciales.",
            "sections": [
                {
                    "label": "El acto impugnado",
                    "heading": "Sanción AGCOM ex art. 98 D.lgs. 259/2003",
                    "body":
                        "El bufete ha interpuesto recurso "
                        "ante el TAR Lombardia para la "
                        "anulación de una sanción AGCOM "
                        "impuesta a un operador de "
                        "comunicaciones electrónicas por "
                        "presunta vulneración de las "
                        "normas sobre transparencia de "
                        "las ofertas comerciales. La "
                        "sanción había sido impuesta al "
                        "término de una fase instructora "
                        "con contradictorio procedimental "
                        "de seis meses.",
                },
                {
                    "label": "Los motivos del recurso",
                    "heading": "Desviación de poder y violación del principio de proporcionalidad",
                    "body":
                        "El recurso se basó en dos "
                        "motivos principales. El primero, "
                        "por desviación de poder bajo el "
                        "perfil del defecto de "
                        "instrucción: la Autoridad no "
                        "había adquirido algunos "
                        "elementos probatorios "
                        "producidos por el operador en "
                        "sede de contradictorio "
                        "procedimental. El segundo, por "
                        "violación del principio de "
                        "proporcionalidad de la sanción "
                        "administrativa pecuniaria, a la "
                        "luz de la orientación del "
                        "Consejo de Estado sec. VI de "
                        "2019 sobre los criterios de "
                        "determinación de la sanción "
                        "atendiendo a la gravedad de la "
                        "conducta, al comportamiento "
                        "del agente y a su capacidad "
                        "contributiva.",
                },
                {
                    "label": "El resultado",
                    "heading": "Anulación íntegra · entrada n.º 9",
                    "body":
                        "El TAR Lombardia ha acogido el "
                        "recurso, anulando íntegramente "
                        "la sanción por violación del "
                        "principio de proporcionalidad. "
                        "La sentencia no fue apelada por "
                        "AGCOM. La voz ha sido registrada "
                        "en el repertorio interno (n.º 9) "
                        "y ha contribuido a la "
                        "consolidación de la orientación "
                        "sobre la proporcionalidad de las "
                        "sanciones regulatorias.",
                },
            ],
            "kpi": [
                ("TAR Lomb.",      "sección III"),
                ("abril 2022",     "depósito sentencia"),
                ("anulada",        "íntegramente"),
                ("entrada 9",      "repertorio interno"),
            ],
            "lead_partner": "Tommaso De Luca · Letrado asociado",
            "team":
                "Letrado asociado + letrado fundador · "
                "recurso introductorio, memoria de "
                "réplica a las contradeducciones AGCOM y "
                "conclusiones de vista oral",
            "next_label":   "Cronología siguiente",
        },
        {
            "slug":     "appello-milano-art-36bis-dpr-600-1973-2021",
            "title":
                "Corte de Apelación de Milán sec. "
                "tributaria — el art. 36-bis D.P.R. "
                "600/1973 y el perímetro de la "
                "controversia tributaria",
            "category": "Tributario",
            "year":     "2021 · depósito septiembre",
            "duration": "App. Milano trib. · segundo grado · reformada en apelación",
            "client_code":
                "Corte d'Appello Milano · sección "
                "tributaria · apelante · contraparte: "
                "Agenzia delle Entrate · materia: "
                "tributario · liquidación automatizada "
                "ex art. 36-bis D.P.R. 600/1973 · "
                "perímetro contributivo restrictivo.",
            "lead":
                "El procedimiento de primer grado ante "
                "la Comisión Tributaria Provincial de "
                "Milán había concluido con el rechazo "
                "del recurso del contribuyente contra "
                "una providencia de pago emitida a "
                "raíz de un control automatizado ex "
                "art. 36-bis D.P.R. 600/1973.",
            "sections": [
                {
                    "label": "El primer grado",
                    "heading": "Comisión Tributaria Provincial de Milán · rechazo del recurso",
                    "body":
                        "El procedimiento de primer "
                        "grado ante la Comisión "
                        "Tributaria Provincial de Milán "
                        "había concluido con el rechazo "
                        "del recurso del contribuyente "
                        "contra una providencia de pago "
                        "emitida a raíz de un control "
                        "automatizado ex art. 36-bis "
                        "D.P.R. 600/1973. La Comisión "
                        "había considerado suficiente el "
                        "control meramente formal para "
                        "fundamentar la pretensión "
                        "tributaria.",
                },
                {
                    "label": "El argumento sostenido",
                    "heading": "Interpretación restrictiva del art. 36-bis D.P.R. 600/1973",
                    "body":
                        "El bufete ha interpuesto "
                        "apelación, sosteniendo la "
                        "interpretación restrictiva del "
                        "art. 36-bis que limita el "
                        "control automatizado a una "
                        "liquidación meramente "
                        "aritmética de los impuestos "
                        "declarados, sin posibilidad de "
                        "rectificación del contenido "
                        "sustancial de la declaración "
                        "(orientación de la casación "
                        "tributaria de 2017 y de 2019). "
                        "La memoria de defensa ha "
                        "articulado la relectura del "
                        "perímetro de la controversia "
                        "tributaria en el marco del "
                        "reparto entre control "
                        "automatizado y rectificación "
                        "sustancial.",
                },
                {
                    "label": "El resultado",
                    "heading": "Reformada en apelación · entrada n.º 7",
                    "body":
                        "La Corte de Apelación ha "
                        "acogido íntegramente la "
                        "apelación, anulando la "
                        "providencia de pago y "
                        "condenando a la Agenzia delle "
                        "Entrate a las costas. La "
                        "sentencia no fue impugnada en "
                        "Casación y ha contribuido a la "
                        "consolidación de la "
                        "orientación restrictiva. "
                        "Entrada n.º 7 del repertorio "
                        "interno.",
                },
            ],
            "kpi": [
                ("App. Milán",       "sección tributaria"),
                ("septiembre 2021",  "depósito sentencia"),
                ("reformada",        "en apelación"),
                ("entrada 7",        "repertorio interno"),
            ],
            "lead_partner": "Tommaso De Luca · Letrado asociado",
            "team":
                "Letrado asociado + letrado fundador · "
                "escrito de apelación, memoria de "
                "réplica a la Agenzia delle Entrate y "
                "conclusiones de vista oral",
            "next_label":   "Cronología siguiente",
        },
    ],

    "contatti": {
        "eyebrow":  "SOMETA UN DICTAMEN PRELIMINAR",
        "headline": "Someta un <em>dictamen</em> preliminar — la primera página de la defensa.",
        "intro":
            "El bufete responde en cinco días hábiles · "
            "en cuarenta y ocho horas si la urgencia es "
            "procesal (plazo en vencimiento · vista "
            "fijada).",
        "primary_cta":  "Someta un dictamen preliminar",

        "form_label":   "DICTAMEN PRELIMINAR",
        "form_heading": "Rellene la ficha de screening",
        "form_intro":
            "El dictamen preliminar es la primera página "
            "de la defensa: el bufete lee el objeto del "
            "contencioso, el grado de jurisdicción "
            "actual, la jurisdicción, la franja de "
            "valor y la urgencia, y devuelve una "
            "valoración de la incardinabilidad de la "
            "evidencia y de la legibilidad de la "
            "jurisprudencia en cinco líneas. El "
            "dictamen NO es un mandato defensivo · NO "
            "es un presupuesto a consumo · NO es una "
            "llamada de descubrimiento. Es un "
            "screening técnico, motivado por escrito, "
            "a partir del cual decidir conjuntamente "
            "si abrir el expediente. Si el dictamen "
            "es negativo, la nota motivada se entrega "
            "igualmente gratis.",

        "form_fields": [
            {"name": "name",      "label": "Nombre",   "type": "text", "required": True,
             "placeholder": "Ej. Marcos",
             "helper": "Solo el nombre de pila, gracias."},
            {"name": "surname",   "label": "Apellidos","type": "text", "required": True,
             "placeholder": "Ej. Bianchi",
             "helper": "Tal como figura en los documentos del comitente."},
            {"name": "email",     "label": "Email",    "type": "email", "required": True,
             "placeholder": "marcos@dominio.es",
             "helper": "Un buzón que recibirá la nota motivada fiduciaria."},
            {"name": "phone",     "label": "Teléfono", "type": "tel", "required": False,
             "placeholder": "+39 ...",
             "helper": "Línea directa para el primer contacto. Opcional."},
            {"name": "oggetto", "label": "Objeto del contencioso",
             "type": "textarea", "required": True, "full_width": True,
             "placeholder":
                 "Describa en 5-10 líneas el objeto del "
                 "contencioso, las partes, el punto en "
                 "discusión. No es necesario ser "
                 "completo · una descripción sintética "
                 "es suficiente.",
             "helper":
                 "Lo suficiente para entender si la "
                 "materia es incardinable. No adjunte "
                 "todavía el expediente completo · las "
                 "cifras y los demás datos se discuten "
                 "en primera vista."},
            {"name": "grado", "label": "Grado de jurisdicción actual", "type": "select", "required": True,
             "options": [
                 "primer grado (Tribunal · CGT · TAR)",
                 "apelación (Corte de Apelación · CGT 2° · Cons. Estado)",
                 "Casación (en curso o por proponer)",
                 "procedimiento administrativo no iniciado",
                 "procedimiento no iniciado (dictamen previo)",
             ],
             "helper": "El grado en el que se encuentra actualmente la causa."},
            {"name": "controparte", "label": "Tipología de contraparte", "type": "text", "required": True,
             "placeholder":
                 "Ej. entidad bancaria · entidad "
                 "pública · contraparte comercial · "
                 "Administración pública · privado",
             "helper":
                 "No es necesario nombrar a la "
                 "contraparte específica en esta fase "
                 "· solo la tipología."},
            {"name": "valore", "label": "Franja de valor", "type": "select", "required": True,
             "options": [
                 "hasta € 50.000",
                 "€ 50.000 — € 250.000",
                 "€ 250.000 — € 1 M",
                 "€ 1 M — € 5 M",
                 "más de € 5 M",
             ],
             "helper": "El valor estimado de la controversia."},
            {"name": "urgenza", "label": "Urgencia procesal", "type": "select", "required": True,
             "options": [
                 "ordinaria (sin plazo en vencimiento)",
                 "cualificada (plazo en 30 días)",
                 "procesal (plazo en 7 días)",
             ],
             "helper":
                 "La urgencia determina la cadencia de "
                 "respuesta del bufete · 5 días "
                 "hábiles · 48 horas si procesal."},
            {"name": "giurisdizione", "label": "Jurisdicción", "type": "select", "required": True,
             "options": [
                 "Italia (foro italiano)",
                 "Unión Europea (TJUE · TUE)",
                 "extra-UE (con elementos de derecho internacional privado)",
             ],
             "helper": "La jurisdicción es la primera forma de respeto."},
        ],

        "form_sections": [
            {"num": "01", "title": "Referente",
             "meta": "La persona que firmará el poder, una vez iniciado el mandato.",
             "fields": ["name", "surname", "email", "phone"]},
            {"num": "02", "title": "Objeto del contencioso",
             "meta": "El objeto es el primer texto del expediente. Cinco a diez líneas bastan.",
             "fields": ["oggetto"]},
            {"num": "03", "title": "Encuadre procesal",
             "meta": "Grado · contraparte · valor · urgencia · jurisdicción.",
             "fields": ["grado", "controparte", "valore", "urgenza", "giurisdizione"]},
        ],

        "form_submit_label": "Someta el dictamen preliminar",
        "form_submit_note":
            "El bufete leerá la ficha en cinco días "
            "hábiles · en cuarenta y ocho horas si la "
            "urgencia es procesal · y responderá con "
            "una nota motivada a la dirección "
            "indicada. Sin BDR externo, sin "
            "automatización de secuencia — el primer "
            "contacto es con el letrado.",
        "form_consent":
            "Consiento al tratamiento de los datos "
            "personales conforme al Reg. UE 679/2016 "
            "y al D.lgs. 196/2003. Los datos se "
            "tratan con el fin exclusivo de la "
            "valoración del dictamen · custodiados en "
            "el bufete de Via Borgonuovo con acceso "
            "limitado a los tres letrados. Estoy "
            "informado del canal whistleblowing "
            "(D.lgs. 24/2023) activo en el bufete. "
            "El bufete respeta el secreto profesional "
            "conforme al art. 622 c.p. y al Codice "
            "Deontologico Forense.",

        "office_address_label": "Dirección",
        "office_area_label":    "Zona",
        "office_phone_label":   "Teléfono",
        "office_email_label":   "Email",

        "offices_label":   "LA SEDE",
        "offices": [
            {
                "city":    "Milán",
                "tag":     "Sede única · Foro di Milano",
                "address": "Via Borgonuovo 14 · 20121",
                "area":    "Brera · cerca del Tribunale di Milano",
                "phone":   "+39 02 7634 8210",
                "email":   "parere@causa.legal",
            },
        ],

        "channels_label": "CANALES DIRECTOS",
        "channels": [
            ("Secretaría del bufete",                      "+39 02 7634 8210",                "Lun – Vie · 09:00 – 18:00"),
            ("Email para dictámenes preliminares",         "parere@causa.legal",              "Respuesta en 5 días"),
            ("PEC para actos ya en plazo",                 "causa.legale@pec.causa.legal",    "Actos urgentes · en 24 horas"),
            ("Whistleblowing (D.lgs. 24/2023)",            "whistleblowing@causa.legal",      "Canal interno · cifrado"),
        ],

        "footnote":
            "Causa respeta el secreto profesional "
            "conforme al art. 622 c.p. y al Codice "
            "Deontologico Forense. La consulta del "
            "sitio no constituye otorgamiento de "
            "mandato. El bufete no responde a "
            "solicitudes anónimas y no emite "
            "dictámenes preliminares por escrito sin "
            "una ficha de screening cumplimentada. La "
            "información sobre honorarios se ilustra "
            "en primera vista, según las tarifas "
            "forenses mínimas y los parámetros D.M. "
            "55/2014. El canal whistleblowing se "
            "gestiona conforme al D.lgs. 24/2023 y es "
            "accesible a colaboradores, asociados y "
            "secretaría.",
    },
}
