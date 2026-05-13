"""Atto · Studio Notarile Conti–Sironi–Verri · Spanish (ES) content tree.

Wave 1 Pass-4 (T48 · 2026-05-12). Workflow C multilingual handshake:
four parallel sub-agent translators producing the IT mirror into ES,
FR, EN and AR locales for the same `classic-gold` notarial archetype.

This module ships the Spanish (peninsular) sibling of `ATTO_CONTENT_IT`
defined in `template_content_atto.py`. Shape-parity is a hard contract:
identical top-level keys (`pages`, `site`, `home`, `studio`, `pratiche`,
`avvocati`, `pubblicazioni`, `posts`, `contatti`), identical nested
structures and identical tuple arities. The skin templates under
`templates/live_templates/lawyer/classic-gold/` are reused verbatim —
the distinctness lives in the content tree, not in the HTML.

Voice anchor:
    `atto pubblico` → `escritura pública` (verbatim-in-translation)

`<em>escritura pública</em>` appears in the same surface locations the
IT tree uses `<em>atto pubblico</em>` for. Where IT shortens to a bare
`<em>atto</em>`, ES shortens to `<em>escritura</em>`. The wider load-
bearing notarial concept (`pubblica fede`) maps to `fe pública` — the
exact Spanish equivalent under the Latin notariat tradition.

Register: peninsular Spanish · usted formal throughout · BOE / El País
Sociedad institutional gravity with warmth. Doctor titles dropped per
Spanish convention; the honorific `Notario` / `Notaria` (capital N)
carries the public-officer weight. Italian legal citations and press
outlets are preserved verbatim, as are phone, email, prices and photo
URLs — only the address city translates: `Milano` → `Milán`.
"""
from __future__ import annotations

from typing import Any


# ─── Imagery — verified Pexels URLs from notary-commercialista X.3 pack ────
_NOTARY_HERO = "https://images.pexels.com/photos/6077091/pexels-photo-6077091.jpeg?auto=compress&cs=tinysrgb&w=1600&h=900&fit=crop"
_NOTARY_SIGNING = "https://images.pexels.com/photos/5235410/pexels-photo-5235410.jpeg?auto=compress&cs=tinysrgb&w=1200&h=800&fit=crop"
_NOTARY_PORTRAIT_F1 = "https://images.pexels.com/photos/6077124/pexels-photo-6077124.jpeg?auto=compress&cs=tinysrgb&w=800&h=1200&fit=crop"
_NOTARY_PORTRAIT_M = "https://images.pexels.com/photos/7841445/pexels-photo-7841445.jpeg?auto=compress&cs=tinysrgb&w=800&h=1200&fit=crop"
_NOTARY_DETAIL = "https://images.pexels.com/photos/5669602/pexels-photo-5669602.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&fit=crop"
_NOTARY_AMBIENT = "https://images.pexels.com/photos/1842502/pexels-photo-1842502.jpeg?auto=compress&cs=tinysrgb&w=800&h=600&fit=crop"


ATTO_CONTENT_ES: dict[str, Any] = {
    "pages": [
        {"slug": "home",          "label": "Notaría",              "kind": "home"},
        {"slug": "studio",        "label": "La Notaría",           "kind": "about"},
        {"slug": "pratiche",      "label": "Tipos de escrituras",  "kind": "services"},
        {"slug": "avvocati",      "label": "Los Notarios",         "kind": "team"},
        {"slug": "pubblicazioni", "label": "Publicaciones",        "kind": "blog_list"},
        {"slug": "contatti",      "label": "Contacto",             "kind": "contact"},
    ],

    # ─── SITE — chrome rendered by _base.html ──────────────────────────
    "site": {
        "logo_initial":  "CSV",
        "logo_word":     "Studio Notarile Conti–Sironi–Verri",
        "tag":           "Distrito Notarial de Milán · desde 2007",
        "phone":         "+39 02 7641 1898",
        "email":         "studio@notaiconti-sironi-verri.it",
        "address":       "Via Manzoni 18 · 20121 Milán",
        "hours_compact": "Lunes a viernes · 09:00 – 18:30",
        "hours_footer_rows": [
            "Sábado · con cita previa para escrituras urgentes",
            "Domingo · cerrado",
        ],
        "license":
            "Notarios inscritos en el Distrito Notarial de Milán · "
            "Colegio Notarial de los Distritos Reunidos de Milán, "
            "Busto Arsizio, Lodi, Monza y Varese · L. 89/1913",
        "nav_cta":       "Solicite una primera reunión",
        "footer_intro":
            "Studio Notarile Conti–Sironi–Verri — diecisiete años de "
            "escritura pública al servicio de familias, empresas y "
            "operadores del Distrito Notarial de Milán. Tres notarios "
            "asociados, una sola firma con fe pública.",
        "foot_studio":  "La notaría",
        "foot_pages":   "Páginas",
        "foot_contact": "Contacto",
        "foot_offices": "Sede",
        "offices_footer_rows": [
            "Milán · Via Manzoni 18",
            "Distrito Notarial de Milán",
        ],

        # Cross-page meta labels (lifted from skin for locale support).
        "case_practice_label":  "Tipo de escritura",
        "case_year_label":      "Año",
        "case_outcome_label":   "Resultado",
        "case_lead_label":      "Notario autorizante",
    },

    # ════════════════════════════════════════════════════════════════════
    # HOME (notaría)
    # ════════════════════════════════════════════════════════════════════
    "home": {
        "eyebrow":  "Studio Notarile Conti–Sironi–Verri · Milán · desde 2007",
        "headline": "Diecisiete años de <em>escritura pública</em>, una firma con valor legal.",
        "intro":
            "La notaría asiste a particulares, familias y empresas "
            "en la redacción de la escritura notarial — escrituras de "
            "compraventa, sucesiones hereditarias, actos societarios, "
            "donaciones, préstamos hipotecarios, poderes notariales y "
            "testamentos. Cada escritura es redactada personalmente "
            "por uno de los tres notarios asociados, inscritos en el "
            "escalafón del Distrito Notarial de Milán, en el pleno "
            "ejercicio de su función de funcionario público y de la "
            "fe pública que la ley les reconoce.",
        "primary_cta":    "Solicite una primera reunión",
        "primary_href":   "contatti",
        "secondary_cta":  "Tipos de escrituras",
        "secondary_href": "pratiche",

        # Hero — split-ledger-monogram silhouette
        "hero_credit_left":  ("Notaria fundadora",  "M. B. Conti"),
        "hero_credit_right": ("Distrito",           "Milán · inscripción en el escalafón"),
        "hero_meta_strip": [
            ("Sede de la notaría",   "Milán · Via Manzoni 18"),
            ("Notarios asociados",   "Tres · inscritos desde 2007/2014/2021"),
            ("Escrituras autorizadas", "4.200+ · ES · IT · EN · FR"),
        ],

        # Practice-area ledger — 4 rows on home, full 7 on /pratiche
        "practice_label":   "Tipos de escrituras",
        "practice_heading": "Siete tipos de <em>escritura</em>, una sola fe pública.",
        "practice_intro":
            "La notaría se ocupa de los principales tipos de escritura "
            "notarial previstos por el ordenamiento. Cada escritura "
            "pública es redactada personalmente por un notario del "
            "despacho, leída al compareciente en la lengua elegida "
            "(italiano, inglés, francés o español) e inscrita en el "
            "repertorio conforme a la Ley Notarial italiana "
            "(L. 89/1913).",
        "practice": [
            ("01", "Escrituras de compraventa inmobiliaria",
             "Redacción de la escritura notarial para la compraventa "
             "de inmuebles residenciales, comerciales y productivos. "
             "Las comprobaciones registrales, las certificaciones "
             "hipotecarias y el control de la regularidad urbanística "
             "preceden al otorgamiento. La escritura se autoriza en "
             "forma pública con la fe pública reconocida por el "
             "art. 2700 c.c. italiano."),
            ("02", "Sucesiones hereditarias y declaraciones",
             "Apertura de la sucesión, redacción de la declaración de "
             "sucesión, aceptación de herencia a beneficio de "
             "inventario, protocolización del testamento ológrafo, "
             "renuncias y particiones hereditarias. Para las "
             "sucesiones transfronterizas resulta aplicable el "
             "Reg. UE 650/2012."),
            ("03", "Actos societarios y operaciones extraordinarias",
             "Constitución de sociedades mediante escritura pública "
             "conforme a los arts. 2328 y 2463 c.c., modificaciones "
             "estatutarias, actas de junta extraordinaria, fusiones, "
             "escisiones y transformaciones. La notaría sigue el "
             "íter completo, desde el acuerdo hasta la inscripción "
             "en el Registro Mercantil."),
            ("04", "Préstamos hipotecarios y garantías reales",
             "Escrituras de préstamo con garantía hipotecaria, "
             "constitución de hipoteca voluntaria, subrogaciones "
             "ex L. 40/2007, escrituras de reconocimiento y "
             "cancelaciones. Coordinación operativa con la entidad "
             "financiera para la firma simultánea a la escritura "
             "de compraventa."),
        ],

        # Stats band — counter animation (notarial-institutional facts)
        "stats_label":   "Diecisiete años de fe pública",
        "stats_heading": "Las cifras de la notaría",
        "stats": [
            ("3",      "notarios inscritos en el escalafón"),
            ("17",     "años desde la fundación"),
            ("4.200+", "escrituras autorizadas"),
            ("4",      "lenguas de otorgamiento (ES/IT/EN/FR)"),
        ],

        # Partners portrait preview — 3 notarios asociados
        "partners_label":   "Los tres notarios",
        "partners_heading": "Tres notarios, una sola notaría",
        "partners_intro":
            "La notaría está regida por tres notarios asociados, cada "
            "uno inscrito en el escalafón del Distrito Notarial de "
            "Milán y responsable de sus propios tipos de escritura. "
            "La firma es personal: el notario que recibe al "
            "compareciente es el mismo que redacta, lee y autoriza la "
            "escritura pública en forma de repertorio.",
        "partners": [
            {
                "name":  "Notaria María Beatriz Conti",
                "role":  "Notaria titular · Actos societarios · M&A internacional",
                "foro":  "Distrito Notarial de Milán · inscrita en el escalafón desde 2007",
                "bio":
                    "Fundadora de la notaría, autoriza las escrituras "
                    "de constitución de sociedades, operaciones "
                    "extraordinarias y escrituras públicas en lengua "
                    "inglesa. Pasantía previa en notaría internacional "
                    "de Milán (2004-2006), se ocupa en particular de "
                    "operaciones de M&A transfronterizas y de grupos "
                    "multinacionales con filial italiana.",
            },
            {
                "name":  "Notario Andrés Sironi",
                "role":  "Notario asociado · Derecho de sociedades · Perito judicial Tribunal de Milán",
                "foro":  "Distrito Notarial de Milán · inscrito en el escalafón desde 2014",
                "bio":
                    "Se ocupa de actos societarios ordinarios y "
                    "extraordinarios, pactos parasociales, "
                    "financiación de socios y operaciones de capital. "
                    "Perito judicial ante el Tribunal de Milán para "
                    "peritajes ex art. 2343 c.c. Miembro de la "
                    "Comisión de Estudios del Colegio Notarial de los "
                    "Distritos Reunidos de Milán.",
            },
            {
                "name":  "Notario Esteban Verri",
                "role":  "Notario asociado · Inmobiliario · Sucesiones",
                "foro":  "Distrito Notarial de Milán · inscrito en el escalafón desde 2021",
                "bio":
                    "Autoriza las escrituras de compraventa "
                    "inmobiliaria, préstamo hipotecario, donación y "
                    "sucesión hereditaria. Auditor legal inscrito en "
                    "el registro mantenido por el MEF, coordina las "
                    "comprobaciones urbanísticas y registrales "
                    "previas al otorgamiento de la escritura. "
                    "Pasante notarial previo en Milán y Brescia "
                    "(2017-2020).",
            },
        ],

        # Publications ribbon — riviste notarili (preserved IT verbatim)
        "publications_label": "Publicaciones y citas",
        "publications": [
            "NOTARIATO",
            "RIVISTA DEL NOTARIATO",
            "GUIDA AL DIRITTO",
            "CNN NOTIZIE",
            "RIVISTA TRIMESTRALE DI DIRITTO E PROCEDURA",
            "FEDERNOTAI",
        ],

        # Final CTA band — first-meeting (orientación) ghost serif
        "cta_label":      "Primera reunión de orientación",
        "cta_heading":    "Treinta minutos para encuadrar la escritura.",
        "cta_intro":
            "La primera reunión con uno de los notarios de la notaría "
            "dura unos treinta minutos, es gratuita y no vinculante. "
            "Se examina el tipo de escritura, el listado de documentos "
            "preliminares que conviene reunir y el cuadro de aranceles "
            "notariales aplicables. No se solicita ninguna decisión "
            "operativa en esta fase.",
        "cta_primary":       "Solicite una primera reunión",
        "cta_primary_href":  "contatti",
        "cta_secondary":     "Conozca la notaría",
        "cta_secondary_href":"studio",
    },

    # ════════════════════════════════════════════════════════════════════
    # STUDIO (about) — historia, notarios asociados, valores, sede
    # ════════════════════════════════════════════════════════════════════
    "studio": {
        "eyebrow":  "La notaría · 2007 — 2026",
        "headline": "Diecisiete años de <em>escritura pública</em>, tres notarios asociados.",
        "intro":
            "El Studio Notarile Conti–Sironi–Verri nace en Milán en "
            "2007 con la inscripción en el escalafón de la Notaria "
            "María Beatriz Conti, primera notaria del distrito en "
            "autorizar escrituras públicas en lengua inglesa. La "
            "notaría ha crecido por cooptación de colegas y hoy "
            "cuenta con tres notarios asociados y seis colaboradores "
            "a tiempo completo, todos operativos en la sede única de "
            "Via Manzoni 18.",

        # History timeline — seis fechas que han definido la notaría
        "history_label":   "Historia de la notaría",
        "history_heading": "Seis fechas, diecisiete años",
        "history_intro":
            "Seis hitos que marcan la trayectoria de la notaría — "
            "desde la primera inscripción en el escalafón de 2007 "
            "hasta el ingreso del tercer notario en 2021. Cada "
            "etapa ha definido la composición colegiada de la "
            "asociación y la ampliación de los tipos de escritura "
            "atendidos.",
        "history": [
            ("2007", "Inscripción en el escalafón del notario fundador",
             "La Notaria María Beatriz Conti queda inscrita en el "
             "escalafón del Distrito Notarial de Milán y abre la "
             "notaría en Via Manzoni 18. Las primeras escrituras "
             "se refieren a constituciones de sociedades de capital "
             "para empresarios del norte de Italia."),
            ("2011", "Escrituras públicas trilingües",
             "La notaría comienza a autorizar escrituras públicas "
             "redactadas en italiano, inglés y francés conforme al "
             "art. 54 de la Ley Notarial. La sección internacional "
             "atiende sobre todo a grupos multinacionales con filial "
             "italiana y a familias residentes en el extranjero."),
            ("2014", "Ingreso del Notario Andrés Sironi",
             "El Notario Andrés Sironi, ya pasante de larga "
             "trayectoria en el distrito, es cooptado como segundo "
             "notario de la asociación. Se especializa en actos "
             "societarios, operaciones extraordinarias y peritajes "
             "de valoración ex art. 2343 c.c."),
            ("2018", "Sección de sucesiones e inmobiliario",
             "La notaría estructura una sección dedicada a las "
             "sucesiones hereditarias y al inmobiliario. Se "
             "codifican los procedimientos internos de "
             "certificación hipotecaria y consulta registral "
             "previos a la escritura de compraventa."),
            ("2021", "Ingreso del Notario Esteban Verri",
             "El Notario Esteban Verri completa la composición "
             "colegiada de la asociación. Auditor legal inscrito "
             "en el registro mantenido por el MEF, asume la "
             "responsabilidad operativa de la sección inmobiliaria "
             "y de sucesiones."),
            ("2025", "Diecisiete años de fe pública",
             "La notaría supera las cuatro mil doscientas escrituras "
             "autorizadas. Los tres notarios asociados están activos "
             "en la formación profesional: la Notaria Conti como "
             "miembro de la Comisión de Estudios del Colegio "
             "Notarial, el Notario Sironi como perito judicial ante "
             "el Tribunal de Milán y el Notario Verri como docente "
             "de práctica notarial."),
        ],

        # Method — cuatro principios no negociables
        "values_label":   "Método notarial",
        "values_heading": "Cuatro principios <em>no negociables</em>",
        "values_intro":
            "Son las cuatro reglas operativas que orientan el "
            "trabajo de la notaría. No describen un estilo comercial "
            "sino una práctica profesional fiel a la Ley Notarial "
            "(L. 89/1913) y al Código Deontológico del Consiglio "
            "Nazionale del Notariato.",
        "values": [
            ("01", "Imparcialidad del funcionario público",
             "El notario es funcionario público y actúa en defensa "
             "de todas las partes de la escritura, nunca de una "
             "sola. La notaría no acepta encargos de parte: ninguna "
             "escritura se redacta en beneficio de una u otra parte "
             "contratante. Las indicaciones operativas son iguales "
             "para vendedor y comprador, donante y donatario, "
             "aportante y receptora."),
            ("02", "Comprobación documental previa",
             "Antes de autorizar la escritura, la notaría comprueba "
             "los documentos urbanísticos, registrales e hipotecarios "
             "relativos al inmueble o a la sociedad objeto del "
             "negocio. La consulta registral, la certificación "
             "hipotecaria y el certificado de eficiencia energética "
             "se recaban directamente, nunca se delegan en las "
             "partes, y se acompañan a la escritura conforme a la "
             "práctica habitual."),
            ("03", "Lectura íntegra al compareciente",
             "La escritura pública se lee íntegramente a los "
             "comparecientes conforme al art. 51 de la Ley Notarial, "
             "en italiano o en la lengua elegida entre aquellas en "
             "las que el notario está habilitado (ES/IT/EN/FR). "
             "Solo tras la lectura y la aprobación explícita se "
             "estampa la firma y el número de repertorio."),
            ("04", "Cuadro de aranceles notariales transparente",
             "Los honorarios se determinan conforme al cuadro "
             "vigente aprobado por el Consiglio Nazionale del "
             "Notariato. La notaría comunica por escrito el "
             "presupuesto orientativo antes de cada escritura, "
             "comprensivo de impuestos y tasas de registro. No se "
             "añade ninguna partida en el momento del otorgamiento."),
        ],

        # Coordinates strip — sede única milanesa
        "coordinates_label": "La sede",
        "coordinates": [
            ("Milán · sede",         "Via Manzoni 18 · 20121 · Porta Nuova"),
            ("Distrito Notarial",    "Milán · Colegio Notarial de los Distritos Reunidos"),
        ],

        # Page-level CTA
        "cta_heading":  "Una primera reunión para encuadrar la escritura.",
        "cta_intro":
            "La primera reunión con uno de los notarios de la "
            "notaría es gratuita, dura unos treinta minutos y no "
            "obliga a ningún trámite posterior. Se examina el tipo "
            "de escritura, los documentos preliminares y el cuadro "
            "de aranceles notariales aplicables.",
        "cta_primary":       "Solicite una primera reunión",
        "cta_primary_href":  "contatti",
    },

    # ════════════════════════════════════════════════════════════════════
    # PRATICHE (services) — 7 tipos de escrituras notariales
    # ════════════════════════════════════════════════════════════════════
    "pratiche": {
        "eyebrow":  "Tipos de escrituras · 2026",
        "headline": "Siete tipos de <em>escritura notarial</em>, una sola firma.",
        "intro":
            "Los siete tipos de escritura atendidos por la notaría. "
            "Cada escritura pública es redactada personalmente por "
            "un notario de la asociación, inscrito en el escalafón "
            "del Distrito Notarial de Milán, e inscrita en el "
            "repertorio conforme a la Ley Notarial (L. 89/1913). "
            "Las partidas del cuadro de aranceles notariales se "
            "comunican por escrito antes del otorgamiento.",

        # Card meta labels (lifted from skin for locale support)
        "svc_lead_label":          "Notario responsable",
        "svc_jurisdiction_label":  "Distrito",

        # 7 tipos de escrituras notariales
        "services": [
            {
                "num":   "01",
                "title": "Escrituras de compraventa inmobiliaria",
                "blurb":
                    "Redacción de la escritura notarial para la "
                    "compraventa de inmuebles residenciales, "
                    "comerciales y productivos. La notaría se ocupa "
                    "también del contrato preliminar de compraventa "
                    "(compromiso) y de las escrituras de permuta. "
                    "La fe pública de la escritura está reconocida "
                    "por el art. 2700 c.c.",
                "scope": [
                    "Consulta registral y certificación hipotecaria",
                    "Comprobación de la regularidad urbanística y certificado energético",
                    "Contrato preliminar de compraventa registrado",
                    "Escritura pública leída al compareciente",
                ],
                "lead":          "Notario Esteban Verri",
                "jurisdiction":  "Milán · Distrito Notarial",
            },
            {
                "num":   "02",
                "title": "Sucesiones hereditarias y declaraciones",
                "blurb":
                    "Apertura de la sucesión, redacción de la "
                    "declaración de sucesión ante la Agencia "
                    "Tributaria italiana, aceptación de herencia "
                    "a beneficio de inventario, protocolización "
                    "del testamento ológrafo, particiones "
                    "hereditarias. Para las sucesiones "
                    "internacionales resulta aplicable el "
                    "Reg. UE 650/2012.",
                "scope": [
                    "Declaración de sucesión",
                    "Aceptación a beneficio de inventario y con reserva",
                    "Protocolización del testamento ológrafo",
                    "Particiones hereditarias y renuncias",
                ],
                "lead":          "Notario Esteban Verri",
                "jurisdiction":  "Milán · UE 650/2012",
            },
            {
                "num":   "03",
                "title": "Actos societarios · constituciones · operaciones extraordinarias",
                "blurb":
                    "Constitución de sociedad mediante escritura "
                    "pública conforme a los arts. 2328 y 2463 c.c., "
                    "modificaciones estatutarias, actas de junta "
                    "extraordinaria, fusiones ex arts. 2501 ss. c.c., "
                    "escisiones proporcionales y no proporcionales, "
                    "transformaciones heterogéneas. Inscripción en "
                    "el Registro Mercantil a cargo de la notaría.",
                "scope": [
                    "Constitución de s.p.a. y s.r.l.",
                    "Modificaciones estatutarias y pactos parasociales",
                    "Fusiones, escisiones, transformaciones",
                    "Inscripción en el Registro Mercantil",
                ],
                "lead":          "Notario Andrés Sironi",
                "jurisdiction":  "Milán · CCIAA Milano Monza Brianza Lodi",
            },
            {
                "num":   "04",
                "title": "Préstamos hipotecarios y garantías reales",
                "blurb":
                    "Escrituras de préstamo hipotecario y préstamo "
                    "con garantía fundiaria, constitución de "
                    "hipoteca voluntaria, subrogaciones "
                    "ex L. 40/2007 (portabilidad del préstamo), "
                    "escrituras de reconocimiento del crédito y "
                    "cancelaciones de hipoteca. El otorgamiento "
                    "se realiza por regla general de forma "
                    "simultánea a la escritura de compraventa.",
                "scope": [
                    "Préstamo fundiario simultáneo a la escritura",
                    "Constitución de hipoteca voluntaria",
                    "Subrogación ex L. 40/2007 (portabilidad)",
                    "Cancelación y reducción de hipoteca",
                ],
                "lead":          "Notario Esteban Verri",
                "jurisdiction":  "Milán · Agencia Tributaria",
            },
            {
                "num":   "05",
                "title": "Donaciones · actos entre vivos",
                "blurb":
                    "Escritura pública de donación de inmuebles, "
                    "dinero o participaciones sociales conforme a "
                    "los arts. 769 y ss. c.c. La notaría se ocupa "
                    "también de las donaciones indirectas, de los "
                    "pactos de familia ex art. 768-bis c.c. y de "
                    "las donaciones con reserva de usufructo.",
                "scope": [
                    "Donación inmobiliaria con/sin reserva de usufructo",
                    "Donación de participaciones sociales",
                    "Pactos de familia (art. 768-bis c.c.)",
                    "Planificación fiscal e impuesto sobre donaciones",
                ],
                "lead":          "Notaria María Beatriz Conti",
                "jurisdiction":  "Milán · Agencia Tributaria",
            },
            {
                "num":   "06",
                "title": "Poderes notariales · legitimaciones de firma",
                "blurb":
                    "Poder especial y poder general conforme al "
                    "art. 1387 c.c., legitimación de firma sobre "
                    "documento privado, autenticación de copia. "
                    "La notaría otorga poderes trilingües "
                    "(IT/EN/FR) para actos a otorgar en el "
                    "extranjero, con apostilla conforme al "
                    "Convenio de La Haya de 1961.",
                "scope": [
                    "Poder especial y poder general",
                    "Legitimación de firma sobre documento privado",
                    "Autenticación de copia",
                    "Apostilla y legalización internacional",
                ],
                "lead":          "Notaria María Beatriz Conti",
                "jurisdiction":  "Milán · Convenio de La Haya 1961",
            },
            {
                "num":   "07",
                "title": "Testamentos · planificación sucesoria",
                "blurb":
                    "Testamento abierto conforme al art. 603 c.c., "
                    "recepción del testamento ológrafo, testamento "
                    "internacional según Convenio de Washington de "
                    "1973. La notaría asiste a los comparecientes "
                    "en el inventario del patrimonio, en la "
                    "cuantificación de la cuota disponible y en la "
                    "legítima.",
                "scope": [
                    "Testamento abierto en forma de repertorio",
                    "Recepción de testamento ológrafo",
                    "Testamento internacional (Washington 1973)",
                    "Planificación de legítima y cuota disponible",
                ],
                "lead":          "Notario Esteban Verri",
                "jurisdiction":  "Milán · Archivo Notarial",
            },
        ],

        # Process strip — cómo se desarrolla la tramitación de la escritura
        "process_label":   "Tramitación de la escritura",
        "process_heading": "Cuatro fases, una sola secuencia",
        "process": [
            ("01", "Primera reunión de orientación",
             "Treinta minutos gratuitos con uno de los notarios de "
             "la asociación. Se encuadra el tipo de escritura, se "
             "aclara el listado de documentos preliminares y se "
             "comunica el cuadro de aranceles notariales aplicable. "
             "No se solicita ninguna decisión operativa en esta fase."),
            ("02", "Acopio documental y comprobaciones",
             "La notaría recaba y comprueba directamente los "
             "documentos necesarios: consulta registral, "
             "certificación hipotecaria, regularidad urbanística, "
             "certificado de eficiencia energética, certificados "
             "del registro civil. El compareciente recibe el "
             "listado escrito de lo que queda a su cargo."),
            ("03", "Preparación y borrador de la escritura",
             "El notario responsable prepara el borrador de la "
             "escritura y lo remite al compareciente al menos "
             "cinco días laborables antes del otorgamiento, para "
             "permitir una lectura reposada. Las posibles "
             "aclaraciones se examinan en una segunda reunión "
             "técnica."),
            ("04", "Otorgamiento, lectura e inscripción en repertorio",
             "El notario lee la escritura al compareciente conforme "
             "al art. 51 de la Ley Notarial, en italiano o en la "
             "lengua elegida. Tras la firma, la escritura se "
             "inscribe en el repertorio, se registra ante la "
             "Agencia Tributaria y se conserva en original en la "
             "notaría."),
        ],

        # Final CTA
        "cta_heading":  "¿No tiene claro qué escritura necesita?",
        "cta_intro":
            "Si el tipo de escritura aún no está definido, puede "
            "solicitar una primera reunión de orientación. En los "
            "treinta minutos gratuitos, uno de los notarios de la "
            "notaría le orienta hacia el trámite correcto y le "
            "comunica el listado de documentos preliminares que "
            "deberá reunir.",
        "cta_primary":       "Solicite una primera reunión",
        "cta_primary_href":  "contatti",
    },

    # ════════════════════════════════════════════════════════════════════
    # AVVOCATI (team) — los tres notarios asociados
    # ════════════════════════════════════════════════════════════════════
    "avvocati": {
        "eyebrow":  "Los notarios · tres inscritos en el escalafón",
        "headline": "Tres notarios asociados, <em>una sola</em> firma de fe pública.",
        "intro":
            "La notaría está compuesta por tres notarios asociados, "
            "todos inscritos en el escalafón del Distrito Notarial "
            "de Milán. El ingreso en la asociación se produce por "
            "cooptación unánime entre los notarios ya asociados, "
            "nunca por adquisición de despacho: cada nuevo notario "
            "aporta su propia inscripción y sus propias "
            "especializaciones. Seis colaboradores a tiempo "
            "completo completan la plantilla.",

        # Card meta labels
        "lawyer_foro_label":           "Distrito",
        "lawyer_year_label":           "Inscripción en el escalafón",
        "lawyer_specialization_label": "Tipos de escritura",

        # 3 notarios asociados
        "lawyers": [
            {
                "name":           "Notaria María Beatriz Conti",
                "role":           "Notaria titular fundadora",
                "specialization": "Actos societarios · M&A · donaciones · poderes trilingües",
                "foro":           "Distrito Notarial de Milán",
                "year":           "Inscrita en el escalafón desde 2007",
                "bio":
                    "Fundadora del Studio Notarile Conti–Sironi–Verri, "
                    "abrió la sede de Via Manzoni 18 en marzo de 2007 "
                    "inmediatamente después de su inscripción en el "
                    "escalafón del Distrito Notarial de Milán. "
                    "Autoriza escrituras públicas en italiano, "
                    "inglés y francés conforme al art. 54 de la Ley "
                    "Notarial, con especialización particular en "
                    "constituciones de sociedades para grupos "
                    "multinacionales con filial italiana, fusiones "
                    "transfronterizas y poderes internacionales con "
                    "apostilla conforme al Convenio de La Haya. "
                    "Miembro de la Comisión de Estudios del Colegio "
                    "Notarial de los Distritos Reunidos de Milán, "
                    "Busto Arsizio, Lodi, Monza y Varese.",
            },
            {
                "name":           "Notario Andrés Sironi",
                "role":           "Notario asociado · derecho de sociedades",
                "specialization": "Actos societarios · operaciones extraordinarias · peritajes ex art. 2343 c.c.",
                "foro":           "Distrito Notarial de Milán",
                "year":           "Inscrito en el escalafón desde 2014",
                "bio":
                    "Cooptado en la asociación en 2015 tras ocho "
                    "años de práctica notarial en un destacado "
                    "despacho milanés, se ocupa de actos societarios "
                    "ordinarios y extraordinarios, pactos "
                    "parasociales, financiación de socios y aumentos "
                    "de capital ex arts. 2441 y 2443 c.c. Perito "
                    "judicial ante el Tribunal de Milán para "
                    "peritajes de valoración ex art. 2343 c.c. y "
                    "para la valoración de liquidación ex art. "
                    "2437-ter c.c. Docente de práctica notarial en "
                    "la Scuola di Notariato della Lombardia.",
            },
            {
                "name":           "Notario Esteban Verri",
                "role":           "Notario asociado · inmobiliario y sucesiones",
                "specialization": "Escrituras de compraventa · préstamos hipotecarios · sucesiones · testamentos",
                "foro":           "Distrito Notarial de Milán",
                "year":           "Inscrito en el escalafón desde 2021",
                "bio":
                    "Último incorporado a la asociación, completa "
                    "la composición colegiada de los tres notarios. "
                    "Se ocupa de las escrituras de compraventa "
                    "inmobiliaria, préstamos hipotecarios, "
                    "subrogaciones ex L. 40/2007 y de toda la "
                    "cadena sucesoria — apertura de la sucesión, "
                    "declaración de sucesión, protocolización del "
                    "testamento ológrafo, aceptación a beneficio "
                    "de inventario. Auditor legal inscrito en el "
                    "registro mantenido por el MEF desde 2018, "
                    "coordina las comprobaciones urbanísticas, "
                    "registrales e hipotecarias previas a las "
                    "escrituras de la notaría.",
            },
        ],
    },

    # ════════════════════════════════════════════════════════════════════
    # PUBBLICAZIONI (blog_list) — publicaciones y análisis notariales
    # ════════════════════════════════════════════════════════════════════
    "pubblicazioni": {
        "eyebrow":  "Publicaciones y análisis · 2023 — 2026",
        "headline": "Cinco análisis sobre la <em>escritura notarial</em> contemporánea.",
        "intro":
            "Una selección de análisis y publicaciones redactados "
            "por los notarios de la notaría o citados en revistas "
            "del sector. Los artículos orientan a comparecientes, "
            "empresarios y profesionales en los principales tipos "
            "de escritura — compraventa, sucesión hereditaria, "
            "constitución de sociedad, donación y poder notarial — "
            "sin pretensión de exhaustividad ni valor de "
            "asesoramiento en el caso concreto.",

        # Lead post image
        "lead_image": _NOTARY_HERO,

        # Footer strap and fallbacks
        "footer_strap":
            "Las publicaciones de la notaría tienen finalidad "
            "divulgativa. Para el caso concreto resulta necesaria "
            "una primera reunión con uno de los notarios de la "
            "asociación.",
        "empty_body_fallback_paragraphs": [
            "El artículo está en curso de redacción. La notaría "
            "publica sus análisis tras una lectura colegiada de "
            "los tres notarios asociados, a fin de evitar "
            "imprecisiones o valoraciones superadas por "
            "modificaciones normativas.",
            "Para el caso concreto puede solicitar una primera "
            "reunión de orientación (treinta minutos gratuitos) "
            "con uno de los notarios de la notaría.",
        ],
    },

    # Posts powering blog_detail. URL: /pubblicazioni/<slug>/
    "posts": [
        {
            "slug":     "atto-pubblico-mercato-immobiliare-2026",
            "kicker":   "Escrituras inmobiliarias",
            "title":    "La escritura pública en el mercado inmobiliario 2026 · prácticas notariales y comprobaciones previas",
            "date":     "Abril de 2026",
            "read_min": "9",
            "author":   "Notario Esteban Verri",
            "lede":
                "Un recorrido por las comprobaciones urbanísticas, "
                "registrales e hipotecarias que la notaría realiza "
                "antes de autorizar una escritura de compraventa "
                "inmobiliaria, a la luz de las modificaciones "
                "introducidas por el D.Lgs. 23/2023 en materia de "
                "transparencia energética y de la jurisprudencia "
                "más reciente de la Corte de Casación sobre la "
                "disconformidad urbanística.",
            "body": [
                ("p",
                 "La escritura notarial de compraventa inmobiliaria "
                 "es escritura pública conforme al art. 2699 c.c. y "
                 "produce la fe pública reconocida por el "
                 "art. 2700 c.c. El notario autorizante, en su "
                 "condición de funcionario público, está obligado "
                 "a comprobar previamente la regularidad "
                 "urbanística, registral e hipotecaria del inmueble."),
                ("h2", "Las tres comprobaciones previas"),
                ("p",
                 "La notaría recaba tres conjuntos de documentos "
                 "antes del otorgamiento: la consulta registral "
                 "actualizada, la certificación hipotecaria de "
                 "veinte años y el certificado de eficiencia "
                 "energética en vigor. La comprobación de la "
                 "regularidad urbanística se basa además en el "
                 "examen de los títulos habilitantes depositados "
                 "en el Ayuntamiento."),
                ("h2", "El papel del notario"),
                ("p",
                 "El notario no es asesor de parte: asiste a ambos "
                 "comparecientes en el encuadre de la escritura y "
                 "en la lectura de las cláusulas. Las eventuales "
                 "incidencias urbanísticas detectadas en la "
                 "comprobación se comunican por escrito a vendedor "
                 "y comprador, de modo que la decisión de otorgar "
                 "o aplazar sea informada."),
                ("blockquote",
                 "La fe pública de la escritura pública solo está "
                 "tutelada si las comprobaciones previas se han "
                 "realizado con la diligencia propia del "
                 "funcionario público. Cualquier omisión documental "
                 "expone a las partes a riesgos de nulidad o "
                 "anulabilidad posteriores al otorgamiento."),
            ],
        },
        {
            "slug":     "successioni-famiglia-orientamento",
            "kicker":   "Sucesiones",
            "title":    "Sucesiones en familia · orientarse sin confusión entre declaración, aceptación y partición",
            "date":     "Febrero de 2026",
            "read_min": "8",
            "author":   "Notario Esteban Verri",
            "lede":
                "Los pasos reales de la sucesión mortis causa en "
                "el derecho italiano. Desde la apertura de la "
                "sucesión hasta la declaración ante la Agencia "
                "Tributaria, pasando por la protocolización del "
                "testamento ológrafo, la aceptación a beneficio "
                "de inventario y la partición hereditaria. Cuándo "
                "se necesita la escritura notarial, cuándo basta "
                "el documento privado.",
            "body": [
                ("p",
                 "La sucesión se abre en el momento de la muerte "
                 "del causante en el lugar de su último domicilio "
                 "conforme al art. 456 c.c. Desde ese instante "
                 "corren los plazos para la declaración de "
                 "sucesión (doce meses) y para las posibles "
                 "renuncias o aceptaciones a beneficio de "
                 "inventario."),
                ("h2", "Declaración de sucesión"),
                ("p",
                 "La notaría prepara la declaración de sucesión "
                 "que debe presentarse ante la Agencia Tributaria "
                 "en los doce meses siguientes a la apertura de "
                 "la sucesión. La declaración contiene el "
                 "listado de los bienes del causante, de los "
                 "llamados a la herencia y de las eventuales "
                 "pasividades deducibles."),
                ("h2", "Cuándo se necesita la escritura notarial"),
                ("p",
                 "La escritura notarial es necesaria para la "
                 "protocolización del testamento ológrafo "
                 "conforme al art. 620 c.c., para la aceptación "
                 "de herencia a beneficio de inventario ex "
                 "art. 484 c.c., para la partición hereditaria "
                 "de bienes inmuebles y para las renuncias a la "
                 "herencia que comprendan bienes inmuebles."),
            ],
        },
        {
            "slug":     "costituzione-srl-semplificata-passaggi-reali",
            "kicker":   "Actos societarios",
            "title":    "Constitución de s.r.l. simplificada · los pasos reales más allá del formulario",
            "date":     "Diciembre de 2025",
            "read_min": "7",
            "author":   "Notario Andrés Sironi",
            "lede":
                "La constitución de s.r.l. simplificada ex "
                "art. 2463-bis c.c. es en apariencia un trámite "
                "estándar de coste reducido. En la práctica, la "
                "escritura pública exige una serie de valoraciones "
                "previas que el modelo no cubre: objeto social, "
                "administración, aportaciones, modalidad de "
                "convocatoria de la junta.",
            "body": [
                ("p",
                 "La s.r.l. simplificada, introducida por el "
                 "D.L. 1/2012, representa una versión a coste "
                 "notarial reducido (aranceles notariales sin "
                 "cargo para la constitución, impuesto de "
                 "registro reducido) de la s.r.l. ordinaria. "
                 "El estatuto se ajusta al modelo ministerial y "
                 "no puede modificarse en fase de constitución."),
                ("h2", "Las decisiones preliminares"),
                ("p",
                 "Pese al estatuto-tipo, quedan por definir "
                 "algunas decisiones relevantes: el objeto social "
                 "(que debe ser lícito y determinado), la "
                 "composición del órgano de administración "
                 "(administrador único o consejo de "
                 "administración), la duración de la sociedad, "
                 "las modalidades de convocatoria de la junta, "
                 "las aportaciones dinerarias de los socios."),
                ("h2", "La escritura pública constitutiva"),
                ("p",
                 "La escritura constitutiva se autoriza en forma "
                 "de escritura pública conforme al art. 2463-bis "
                 "apartado 2 c.c. y se inscribe en el Registro "
                 "Mercantil a cargo del notario en los veinte "
                 "días siguientes al otorgamiento. La lectura a "
                 "los socios comparecientes es íntegra, en "
                 "italiano o en la lengua elegida entre aquellas "
                 "en las que el notario está habilitado."),
            ],
        },
        {
            "slug":     "donazione-coniugi-riforma-2024",
            "kicker":   "Donaciones",
            "title":    "Donación entre cónyuges · qué cambia con la reforma de 2024 y con la circular 32/E",
            "date":     "Octubre de 2025",
            "read_min": "10",
            "author":   "Notaria María Beatriz Conti",
            "lede":
                "La donación entre cónyuges es escritura pública "
                "típica conforme a los arts. 769 y ss. c.c. Las "
                "modificaciones normativas de 2024 y la circular "
                "32/E de la Agencia Tributaria han clarificado "
                "algunos aspectos aplicativos sobre el impuesto "
                "de donaciones, sobre las exenciones y sobre la "
                "revocabilidad por sobrevenida existencia de "
                "hijos.",
            "body": [
                ("p",
                 "La donación entre cónyuges está regulada por "
                 "los arts. 769 y ss. del código civil y está "
                 "sometida a la forma de la escritura pública "
                 "bajo pena de nulidad ex art. 782 c.c. La "
                 "exención del impuesto de donaciones entre "
                 "cónyuges es de un millón de euros por cada "
                 "donatario."),
                ("h2", "Reserva de usufructo y nuda propiedad"),
                ("p",
                 "Una opción habitual en las donaciones "
                 "inmobiliarias entre cónyuges es la donación de "
                 "la nuda propiedad con reserva de usufructo a "
                 "favor del donante. La operación, plenamente "
                 "legítima ex art. 796 c.c., permite al donante "
                 "conservar el disfrute del bien manteniendo sus "
                 "rentas."),
                ("h2", "Revocabilidad por sobrevenida existencia de hijos"),
                ("p",
                 "La donación es revocable por sobrevenida "
                 "existencia de hijos ex art. 803 c.c. cuando "
                 "el donante, al tiempo de la escritura, no "
                 "tenía hijos ni descendientes. La revocabilidad "
                 "se extiende a los hijos adoptados con adopción "
                 "legitimante intervenidos con posterioridad a "
                 "la donación."),
            ],
        },
        {
            "slug":     "procura-art-1387-cc-quando-serve",
            "kicker":   "Poderes notariales",
            "title":    "Poder notarial conforme al art. 1387 c.c. · cuándo se necesita y cómo se redacta (con apostilla)",
            "date":     "Julio de 2025",
            "read_min": "6",
            "author":   "Notaria María Beatriz Conti",
            "lede":
                "El poder notarial es el acto mediante el cual el "
                "representado confiere al representante la "
                "facultad de realizar uno o varios actos "
                "jurídicos en su nombre. Cuando el acto que ha "
                "de realizarse exige la forma de la escritura "
                "pública — por ejemplo, una compraventa "
                "inmobiliaria — también el poder debe autorizarse "
                "en forma de escritura pública.",
            "body": [
                ("p",
                 "El art. 1387 c.c. regula los supuestos en que "
                 "el poder notarial es necesario para realizar "
                 "actos jurídicos en nombre del representado. "
                 "Por el principio de simetría formal "
                 "(art. 1392 c.c.), el poder debe revestir la "
                 "misma forma exigida para el acto que el "
                 "representante haya de realizar."),
                ("h2", "Poder especial y poder general"),
                ("p",
                 "El poder especial confiere la facultad de "
                 "realizar un acto determinado (por ejemplo: la "
                 "venta de un inmueble concreto). El poder "
                 "general confiere la facultad de realizar todos "
                 "los actos comprendidos en una categoría (por "
                 "ejemplo: todos los actos de administración "
                 "ordinaria del patrimonio del representado)."),
                ("h2", "Poderes trilingües y apostilla"),
                ("p",
                 "Para los actos a otorgar en el extranjero, la "
                 "notaría redacta poderes en italiano y en la "
                 "lengua del país de destino (inglés o francés) "
                 "conforme al art. 54 de la Ley Notarial. La "
                 "apostilla conforme al Convenio de La Haya de "
                 "1961 se estampa a cargo del Fiscal Jefe ante "
                 "el Tribunal de Milán."),
            ],
        },
    ],

    # ════════════════════════════════════════════════════════════════════
    # CONTATTI (contact) — sede única milanesa, formulario orientación
    # ════════════════════════════════════════════════════════════════════
    "contatti": {
        "eyebrow":  "Primera reunión de orientación · gratuita · no vinculante",
        "headline": "Treinta minutos con un <em>notario</em> para encuadrar la escritura.",
        "intro":
            "La primera reunión se celebra directamente con uno de "
            "los tres notarios de la asociación. Se examina el tipo "
            "de escritura, el listado de documentos preliminares que "
            "conviene reunir y el cuadro de aranceles notariales "
            "aplicables. La reunión dura unos treinta minutos, es "
            "gratuita y no obliga a ningún trámite posterior.",

        # Form fields
        "form_label":   "Formulario de solicitud",
        "form_heading": "Solicite una primera reunión de orientación",
        "form_intro":
            "Recibirá confirmación de recepción en un plazo de "
            "cuarenta y ocho horas laborables por parte de la "
            "secretaría de la notaría, con la propuesta de tres "
            "franjas horarias disponibles y la indicación del "
            "notario responsable del tipo de escritura. Los datos "
            "se tratan conforme al Reglamento UE 679/2016 y se "
            "custodian en sistemas conformes a las directrices del "
            "Consiglio Nazionale del Notariato.",
        "form_fields": [
            {"name": "name", "label": "Nombre", "type": "text", "required": True,
             "placeholder": "P. ej. Ana",
             "helper": "Solo el nombre de pila, tal como figura en el documento de identidad."},
            {"name": "surname", "label": "Apellidos", "type": "text", "required": True,
             "placeholder": "P. ej. Blanco",
             "helper": "Tal como figuran en el documento de identidad del compareciente."},
            {"name": "email", "label": "Correo electrónico", "type": "email", "required": True,
             "placeholder": "ana.blanco@ejemplo.es",
             "helper": "Para la correspondencia preliminar. No utilizamos la dirección para otros fines."},
            {"name": "phone", "label": "Teléfono", "type": "tel", "required": True,
             "placeholder": "+34 ...",
             "helper": "Línea directa de la persona de contacto para acordar el horario."},
            {"name": "capacity", "label": "En calidad de", "type": "select", "required": True,
             "options": [
                 "Particular",
                 "Empresario o socio de sociedad",
                 "Administrador de sociedad",
                 "Heredero o legatario",
                 "Profesional (asesor fiscal, abogado, agente inmobiliario)",
                 "Entidad de crédito o aseguradora",
             ],
             "helper": "Para orientar la entrevista e identificar al notario responsable."},
            {"name": "act_type", "label": "Tipo de escritura", "type": "select", "required": True,
             "options": [
                 "Por definir en la entrevista",
                 "Escritura de compraventa inmobiliaria",
                 "Préstamo hipotecario o subrogación",
                 "Sucesión o declaración de sucesión",
                 "Testamento abierto o protocolización de ológrafo",
                 "Constitución de sociedad o acto societario",
                 "Fusión, escisión o transformación",
                 "Donación o pacto de familia",
                 "Poder especial o general",
                 "Legitimación de firma o autenticación de copia",
             ],
             "helper": "Elija \"Por definir\" si el tipo aún no está claro."},
            {"name": "timing", "label": "Plazos orientativos", "type": "select", "required": True,
             "options": [
                 "En el plazo de un mes",
                 "En el plazo de tres meses",
                 "En el plazo de seis meses",
                 "Exploratorio, sin fecha límite definida",
             ],
             "helper": "Para calendarizar la primera reunión y la tramitación de la escritura."},
            {"name": "language", "label": "Lengua de otorgamiento (si procede)", "type": "select", "required": False,
             "options": [
                 "Italiano",
                 "Italiano con traducción al inglés",
                 "Italiano con traducción al francés",
                 "Italiano con traducción al español",
                 "Por valorar en la entrevista",
             ],
             "helper": "La notaría autoriza escrituras públicas en italiano, inglés, francés y español."},
            {"name": "scope", "label": "Breve descripción de la escritura",
             "type": "textarea", "required": True, "full_width": True,
             "placeholder":
                 "Máximo 600 caracteres. Indique de forma sintética "
                 "el objeto de la escritura (por ejemplo: "
                 "\"compraventa de piso sito en Milán, parte "
                 "vendedora\"). Los datos de terceros se recaban "
                 "solo en la reunión, nunca en este formulario.",
             "helper":
                 "Lo justo para encuadrar el tipo de escritura y "
                 "derivar el expediente al notario responsable. "
                 "Los detalles se examinan en la primera reunión."},
        ],

        "form_sections": [
            {"num": "01", "title": "Persona de contacto",
             "meta": "La persona que participará en la primera reunión como compareciente.",
             "fields": ["name", "surname", "email", "phone"]},
            {"num": "02", "title": "Posición",
             "meta": "Para derivar la solicitud al notario responsable.",
             "fields": ["capacity"]},
            {"num": "03", "title": "Tipo de escritura",
             "meta":
                 "No incluya aquí datos de terceros — los nombres "
                 "de contrapartes, herederos o aportantes se "
                 "recaban en la primera reunión.",
             "fields": ["act_type", "timing", "language", "scope"]},
            {"num": "04", "title": "Documentos preliminares (opcionales)",
             "meta":
                 "Consultas registrales, escrituras anteriores, "
                 "planos o borradores pueden agilizar el encuadre.",
             "fields": ["__upload__"]},
        ],

        "upload_field": {
            "name":     "documenti_preliminari",
            "label":    "Documentos preliminares",
            "helper":
                "Consultas registrales, escrituras de procedencia, "
                "planos, borradores de estatutos. PDF / DOCX · "
                "máx. 15 MB en total. Los documentos se custodian "
                "en archivo cifrado conforme a las directrices del "
                "Consiglio Nazionale del Notariato.",
            "accept":   ".pdf,.docx",
            "multiple": True,
            "primary":  "Arrastre aquí los documentos o bien",
            "link":     "selecciónelos del archivo",
            "meta":     "PDF / DOCX · máx. 15 MB · archivo cifrado",
        },

        "form_submit_label": "Solicite una primera reunión",
        "form_submit_note":
            "Confirmación de recepción en un plazo de cuarenta y "
            "ocho horas laborables con la propuesta de tres "
            "franjas horarias. Sin automatización comercial, sin "
            "BDR, sin comunicaciones de marketing posteriores.",
        "form_consent":
            "Doy mi consentimiento al tratamiento de los datos "
            "personales conforme al Reglamento UE 679/2016 y "
            "declaro estar informado de que los datos se custodian "
            "en sistemas conformes a las directrices del Consiglio "
            "Nazionale del Notariato y del Archivo Notarial. Los "
            "datos no se comunican a terceros sin consentimiento "
            "expreso por escrito del compareciente.",

        # Office meta-row labels
        "office_address_label": "Dirección",
        "office_area_label":    "Zona",
        "office_phone_label":   "Teléfono",
        "office_email_label":   "Correo electrónico",
        "office_hours_label":   "Horario",

        # Sidebar — sede única, canales directos
        "offices_label":   "La sede",
        "offices": [
            {
                "city":    "Milán",
                "tag":     "Sede única de la notaría",
                "address": "Via Manzoni 18 · 20121",
                "area":    "Porta Nuova · a 200 metros de Repubblica M3",
                "phone":   "+39 02 7641 1898",
                "email":   "studio@notaiconti-sironi-verri.it",
                "hours":   "Lun – Vie · 09:00 – 18:30",
            },
        ],

        "channels_label": "Canales directos",
        "channels": [
            ("Secretaría de la notaría",
             "+39 02 7641 1898",
             "Lun – Vie · 09:00 – 18:30"),
            ("Correo institucional",
             "studio@notaiconti-sironi-verri.it",
             "Respuesta en 48 horas laborables"),
            ("PEC certificada",
             "studio.contisironi@postacertificata.notariato.it",
             "Para escrituras, notificaciones y depósitos telemáticos"),
        ],

        "footnote":
            "El Studio Notarile Conti–Sironi–Verri no emite "
            "dictámenes vinculantes por correo electrónico sin una "
            "primera reunión de orientación con uno de los tres "
            "notarios de la asociación. El cuadro de aranceles "
            "notariales aplicable al caso concreto se comunica "
            "por escrito al término de la primera reunión, antes "
            "de cualquier encargo formal.",
    },
}


# ─────────────────────────────────────────────────────────────────────
# D-047 — chrome-authoring contract.
# Every visible string in the lawyer/classic-gold skin templates
# must come from THIS file (or from chrome.* / dna.content.*).
# Zero literal "Conti", "Sironi", "Verri", "2007", "Milán",
# "Via Manzoni", notario names, headline text, or other brand-specific
# strings in the .html files. The skin is reused verbatim from Lex —
# the distinctness lives in the content tree, not in the templates.
# ─────────────────────────────────────────────────────────────────────
