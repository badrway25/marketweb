"""SALUTE_CONTENT_ES — native translation per D-072 multilingual voice law.

Voice contract (ES): registro Sanitas / Hospital Clinico peninsular, trato de
"usted" formal pero cercano. "Consulta", "cita medica", "equipo medico",
"centro medico". Nombres propios italianos preservados (SaluteVita, Dra
Elisa Conti, Via Galvani, Milan Centrale). Convenios y aseguradoras italianas
preservados con glosa contextual. Precios en euros (centro italiano). Horarios
estilo peninsular: "Lun - Sab · 7:00 - 21:00".
"""
from __future__ import annotations

from typing import Any

from apps.catalog.template_content_salute import (
    ICO_STETHOSCOPE,
    ICO_BABY,
    ICO_DERM,
    ICO_ULTRASOUND,
    ICO_WOMAN,
    ICO_BONE,
    ICO_BRAIN,
    ICO_EYE,
)


SALUTE_CONTENT_ES: dict[str, Any] = {
    "pages": [
        {"slug": "home",        "label": "Inicio",             "kind": "home"},
        {"slug": "studio",      "label": "El centro",          "kind": "about"},
        {"slug": "servizi",     "label": "Servicios",          "kind": "services"},
        {"slug": "prevenzione", "label": "Prevención",         "kind": "prevention"},
        {"slug": "medici",      "label": "Médicos",            "kind": "team"},
        {"slug": "contatti",    "label": "Contacto",           "kind": "contact"},
        {"slug": "prenota",     "label": "Reservar",           "kind": "appointment"},
    ],

    "site": {
        "logo_initial": "S",
        "logo_word":    "SaluteVita",
        "tag":          "Centro médico multidisciplinar · Milán Centrale",
        "phone_label":  "Teléfono gratuito",
        "phone":        "800 123 456",
        "phone_tel":    "+39800123456",
        "email":        "cita@salutevita.clinic",
        "address":      "Via Galvani 18 · 20124 Milán",
        "hours_compact": "Lun – Sáb · 7:00 – 21:00",
        "hours_footer_rows": [
            "Lun – Vie · 7:00 – 21:00",
            "Sáb · 8:00 – 18:00",
            "Domingo · cerrado",
        ],
        "foot_extra_label": "Convenios",
        "foot_extra_rows": [
            "Inail · Unisalute · Generali",
            "RBM Salute · Previmedical",
            "Caspie · MioDottore",
        ],
        "license": "Inscrito en el registro de centros sanitarios ATS Milán · CIF 09812345678",
        "footer_intro":
            "Centro médico multidisciplinar en el corazón de Milán "
            "Centrale. Más de 40 profesionales repartidos en 12 servicios, "
            "abierto seis días a la semana — un referente médico cercano "
            "a las familias desde 1998.",
    },

    "home": {
        "eyebrow":   "Centro médico · Milán Centrale · desde 1998",
        "headline":  'Su salud, nuestro <em>trabajo</em> diario.',
        "subhead":
            "Más de 40 especialistas, itinerarios diagnósticos integrados "
            "y una experiencia pensada para que el paciente se sienta "
            "atendido desde la primera llamada. Reserve en línea en 30 "
            "segundos, de lunes a sábado, de 7:00 a 21:00.",
        "primary_cta":    "Reservar cita",
        "primary_href":   "prenota",
        "secondary_cta":  "Gratuito 800 123 456",
        "secondary_href": "contatti",
        "trust_note":     "Respuesta en menos de 2 horas · sin compromiso",

        "stats": [
            ("40+",  "Médicos especialistas"),
            ("12",   "Servicios"),
            ("98 %", "Pacientes que volverían"),
        ],

        "booking_widget": {
            "aria_label":  "Reserva en línea en tres pasos",
            "title":       "Reserve en 30 segundos",
            "subtitle":    "Primera cita habitualmente en 48 h laborables",
            "badge":       "6 huecos libres hoy",
            "specialty_label": "Especialidad",
            "specialty_value": "Cardiología",
            "date_label":      "Primer hueco disponible",
            "date_value":      "Mar. 14 abr. · 10:30",
            "doctor_label":    "Facultativo",
            "doctor_value":    "Dra. Elisa Conti",
            "cta":             "Confirmar cita",
            "footnote":        "Gratis · anulable hasta 24 h antes",
            "secure_label":    "Datos cifrados",
        },

        "stats_strip": [
            ("1998",    "Año de fundación"),
            ("28.000",  "Pacientes atendidos cada año"),
            ("6",       "Días de apertura a la semana"),
            ("0 €",     "Coste de la primera llamada"),
        ],

        "specialties_label": "Nuestras especialidades",
        "specialties_heading": 'Doce servicios <em>bajo un mismo techo</em>.',
        "specialties_intro":
            "Todas las consultas que una familia milanesa puede "
            "necesitar, coordinadas entre sí: si su cardiólogo solicita "
            "una ecografía, la reservamos el mismo día, en el mismo edificio.",
        "specialties": [
            {
                "icon_svg": ICO_STETHOSCOPE,
                "title":    "Cardiología",
                "blurb":    "Consulta cardiológica, ECG en reposo y de "
                            "esfuerzo, ecocardiografía, holter de presión "
                            "arterial y ECG de 24 horas.",
                "link_label": "Ver el servicio",
            },
            {
                "icon_svg": ICO_BABY,
                "title":    "Pediatría",
                "blurb":    "Revisiones de salud de 0 a 14 años, "
                            "vacunación y consulta pediátrica urgente en 24 horas.",
                "link_label": "Ver el servicio",
            },
            {
                "icon_svg": ICO_DERM,
                "title":    "Dermatología",
                "blurb":    "Mapa de nevus por dermatoscopia digital, "
                            "dermatitis, acné y controles oncológicos de la piel.",
                "link_label": "Ver el servicio",
            },
            {
                "icon_svg": ICO_ULTRASOUND,
                "title":    "Radiología y diagnóstico",
                "blurb":    "Ecografía multiorgánica, TAC, resonancia "
                            "magnética y mamografía. Informe en el mismo día si lo solicita.",
                "link_label": "Ver el servicio",
            },
            {
                "icon_svg": ICO_WOMAN,
                "title":    "Ginecología",
                "blurb":    "Consulta ginecológica y obstétrica, "
                            "ecografía transvaginal, citología e "
                            "itinerarios de embarazo.",
                "link_label": "Ver el servicio",
            },
            {
                "icon_svg": ICO_BONE,
                "title":    "Traumatología y fisioterapia",
                "blurb":    "Consulta traumatológica, infiltraciones "
                            "ecoguiadas y rehabilitación postoperatoria "
                            "con fisioterapeuta dedicado.",
                "link_label": "Ver el servicio",
            },
            {
                "icon_svg": ICO_BRAIN,
                "title":    "Neurología",
                "blurb":    "Consulta neurológica, electroencefalograma "
                            "y valoración de cefaleas recurrentes y "
                            "trastornos del sueño.",
                "link_label": "Ver el servicio",
            },
            {
                "icon_svg": ICO_EYE,
                "title":    "Oftalmología",
                "blurb":    "Revisión oftalmológica completa, OCT de "
                            "retina, campo visual y valoración de "
                            "cataratas en colaboración con centros quirúrgicos concertados.",
                "link_label": "Ver el servicio",
            },
        ],

        "journey_label":    "El itinerario del paciente",
        "journey_heading":  'De la cita al informe, <em>cuatro pasos sencillos</em>.',
        "journey_intro":
            "Hemos diseñado cada paso pensando en cómo una familia "
            "querría ser atendida: sin colas de pie, sin papeles "
            "perdidos, sin tener que contar dos veces la misma historia.",
        "journey_steps": [
            {"num": "01", "title": "Reserva en línea",
             "body": "Elija especialidad, facultativo y franja horaria en "
                     "30 segundos. Recibe un SMS de recordatorio dos días antes."},
            {"num": "02", "title": "Recepción",
             "body": "La recepción abre a las 7:00. Le acompañamos a la "
                     "sala de espera y le llamamos por su nombre cuando "
                     "el facultativo esté listo."},
            {"num": "03", "title": "Consulta",
             "body": "El médico ya tiene su historia clínica delante. "
                     "Consulta en profundidad y pruebas el mismo día cuando es posible."},
            {"num": "04", "title": "Informe digital",
             "body": "Informe y prescripciones en su área de paciente en "
                     "24 horas, descargables en PDF y compartibles con "
                     "su médico de cabecera."},
        ],

        "prevenzione_label":   "Revisiones de prevención",
        "prevenzione_heading": 'Prevenir cuesta <em>menos</em> que tratar.',
        "prevenzione_intro":
            "Tres paquetes pensados para las franjas de edad en las que "
            "los controles regulares importan más. 15 % de descuento al "
            "renovar la revisión dentro de 12 meses.",
        "prevenzione_cards": [
            {
                "eyebrow":  "Mujer 40+",
                "title":    "Revisión Mujer 40+",
                "desc":     "Consulta ginecológica, ecografía pélvica, "
                            "citología, mamografía y asesoramiento "
                            "nutricional en una sola mañana.",
                "includes": [
                    "Consulta ginecológica completa",
                    "Citología y prueba HPV",
                    "Ecografía pélvica + mamografía",
                    "Asesoramiento nutricional de 30 minutos",
                ],
                "duration_label": "Duración",
                "duration":       "3 horas",
                "price_label":    "Precio todo incluido",
                "price":          "320 €",
                "cta":            "Reservar la revisión",
            },
            {
                "eyebrow":  "Hombre 45+",
                "title":    "Revisión Hombre 45+",
                "desc":     "Cardiología, urología, control metabólico, "
                            "ecografía abdominal y de próstata. Informe "
                            "único en 48 horas.",
                "includes": [
                    "Consulta cardiológica + ECG",
                    "Consulta urológica + PSA",
                    "Ecografía abdominal completa",
                    "Perfil metabólico lipídico",
                ],
                "duration_label": "Duración",
                "duration":       "3,5 horas",
                "price_label":    "Precio todo incluido",
                "price":          "280 €",
                "cta":            "Reservar la revisión",
            },
            {
                "eyebrow":  "Más de 60",
                "title":    "Revisión Senior 60+",
                "desc":     "Valoración cardiovascular, ósea, neurológica "
                            "y oftalmológica, coordinada por un médico "
                            "internista que mantiene unido el cuadro.",
                "includes": [
                    "Cardiología + ecocardio + holter",
                    "Densitometría ósea DEXA",
                    "Consulta neurológica cognitiva",
                    "Oftalmología + tonometría",
                ],
                "duration_label": "Duración",
                "duration":       "4 horas",
                "price_label":    "Precio todo incluido",
                "price":          "420 €",
                "cta":            "Reservar la revisión",
            },
        ],

        "team_label":   "Nuestros especialistas",
        "team_heading": 'Ocho rostros <em>de los servicios con más demanda</em>.',
        "team_intro":
            "Más de 40 médicos colaboran con SaluteVita. Aquí presentamos "
            "a los responsables de los ocho servicios con más reservas — "
            "el equipo completo figura en una página dedicada.",
        "team_ribbon_people": [
            {
                "avatar": "https://images.pexels.com/photos/5327585/pexels-photo-5327585.jpeg?auto=compress&cs=tinysrgb&w=400&h=400&fit=crop",
                "name":     "Dra. Elisa Conti",
                "specialty":"Cardiología",
            },
            {
                "avatar": "https://images.pexels.com/photos/5452293/pexels-photo-5452293.jpeg?auto=compress&cs=tinysrgb&w=400&h=400&fit=crop",
                "name":     "Dr. Marco Ferri",
                "specialty":"Pediatría",
            },
            {
                "avatar": "https://images.pexels.com/photos/5452274/pexels-photo-5452274.jpeg?auto=compress&cs=tinysrgb&w=400&h=400&fit=crop",
                "name":     "Dra. Sofia Lenzi",
                "specialty":"Dermatología",
            },
            {
                "avatar": "https://images.pexels.com/photos/4173239/pexels-photo-4173239.jpeg?auto=compress&cs=tinysrgb&w=400&h=400&fit=crop",
                "name":     "Dr. Luca Russo",
                "specialty":"Radiología",
            },
            {
                "avatar": "https://images.pexels.com/photos/5327921/pexels-photo-5327921.jpeg?auto=compress&cs=tinysrgb&w=400&h=400&fit=crop",
                "name":     "Dra. Chiara Moretti",
                "specialty":"Ginecología",
            },
            {
                "avatar": "https://images.pexels.com/photos/6129507/pexels-photo-6129507.jpeg?auto=compress&cs=tinysrgb&w=400&h=400&fit=crop",
                "name":     "Dr. Paolo Serra",
                "specialty":"Traumatología",
            },
            {
                "avatar": "https://images.pexels.com/photos/7659562/pexels-photo-7659562.jpeg?auto=compress&cs=tinysrgb&w=400&h=400&fit=crop",
                "name":     "Dr. Andrea Villa",
                "specialty":"Neurología",
            },
            {
                "avatar": "https://images.pexels.com/photos/5215024/pexels-photo-5215024.jpeg?auto=compress&cs=tinysrgb&w=400&h=400&fit=crop",
                "name":     "Dra. Laura Bianchi",
                "specialty":"Oftalmología",
            },
        ],
        "team_footnote_prefix": "Más de 40 especialistas componen el equipo médico completo.",
        "team_footnote_link":   "Ver a todos los facultativos",

        "partners_label":   "Convenios y aseguradoras",
        "partners_heading": "Trabajamos en red con las principales mutuas y aseguradoras sanitarias italianas.",
        "partners": [
            "Inail", "Unisalute", "Generali Welion",
            "RBM Salute", "Previmedical", "Caspie",
            "MioDottore", "Consap",
        ],

        "cta_band": {
            "heading":      "¿Necesita cita esta semana?",
            "body":         "Reserve en línea en 30 segundos o llame a nuestro teléfono gratuito: el equipo atiende todos los días de 7:00 a 21:00.",
            "primary_cta":  "Reservar en línea",
            "primary_href": "prenota",
            "secondary_cta":"Llamar al 800 123 456",
        },
    },

    "studio": {
        "eyebrow":   "El centro · en Milán desde 1998",
        "headline":  'Un referente médico <em>cerca</em> de las personas.',
        "intro":
            "SaluteVita nació en 1998 de la mano de tres médicos milaneses "
            "con una idea: reducir la distancia entre el hospital y la "
            "familia, ofreciendo un centro médico completo a dos pasos de "
            "la estación de Milán Centrale.",

        "values_label":   "Nuestros valores",
        "values_heading": 'Cuatro cosas que <em>no cambiaremos</em>.',
        "values": [
            {"title": "Atención multidisciplinar",
             "body":  "Ningún paciente se queda sin respuesta: si hace "
                      "falta una prueba, se la reservamos en el mismo "
                      "edificio. Informes compartidos entre especialistas."},
            {"title": "Acogida",
             "body":  "La recepción responde desde las 7:00. Le llamamos "
                      "por su nombre — sin números de turno, sin colas de pie."},
            {"title": "Tecnología al servicio",
             "body":  "Historia clínica digital, informes en PDF en 24 "
                      "horas, dermatoscopia digital y resonancia 1,5 T "
                      "de última generación."},
            {"title": "Continuidad",
             "body":  "Si su hija vio a nuestro pediatra hace tres años, "
                      "el traumatólogo encuentra hoy la misma historia "
                      "clínica cuando la necesita. Sin empezar de cero."},
        ],

        "photo_label":   "El centro",
        "photo_heading": "Cuatro plantas, doce servicios, una sola recepción.",
        "photo_body":
            "El edificio de Via Galvani 18 alberga consultorios, sala de "
            "extracciones, diagnóstico por imagen y fisioterapia. Todo en "
            "planta baja o primera, sin barreras arquitectónicas, con "
            "aparcamiento concertado a 40 metros.",
        "photo_caption": "Via Galvani 18 · zona Milán Centrale",
        "photo_src":     "https://images.pexels.com/photos/7108324/pexels-photo-7108324.jpeg?auto=compress&cs=tinysrgb&w=1200&h=900&fit=crop",

        "timeline_label":   "Nuestra historia",
        "timeline_heading": 'Veintiséis años, <em>una sola constante</em>: la persona que tenemos delante.',
        "timeline": [
            {"year": "1998", "title": "El comienzo",
             "body": "Tres médicos — un internista, una pediatra y un "
                     "cardiólogo — abren el primer consultorio en Via "
                     "Galvani, con 180 metros cuadrados."},
            {"year": "2008", "title": "La segunda planta",
             "body": "Inauguramos el diagnóstico por imagen con "
                     "resonancia, TAC y mamografía. Los servicios pasan a ser ocho."},
            {"year": "2018", "title": "Historia digital",
             "body": "Pasamos por completo a la historia clínica digital "
                     "y al área de paciente en línea. Informes en 24 "
                     "horas para cada prueba."},
            {"year": "2024", "title": "Hoy",
             "body": "Más de 40 especialistas, 12 servicios, 28.000 "
                     "pacientes atendidos cada año. Seguimos siendo la "
                     "clínica de familia que quisimos ser."},
        ],

        "cta_band": {
            "heading":    "¿Quiere conocernos en persona?",
            "body":       "Reserve su primera cita o venga a vernos: la recepción abre a las 7:00 de la mañana, sin cita previa.",
            "primary_cta":"Reservar cita",
            "secondary_cta": "Llamar al 800 123 456",
        },
    },

    "servizi": {
        "eyebrow":   "Servicios · 12 servicios · 40+ especialistas",
        "headline":  'Todas las consultas <em>que una familia necesita</em>.',
        "intro":
            "De la cardiología a la fisioterapia, pasando por pediatría, "
            "dermatología y diagnóstico por imagen. Cada consulta "
            "reservable en línea, con precios claros y paquetes de "
            "prevención específicos.",

        "svc_label":   "Todos los servicios",
        "svc_heading": 'Consultas especializadas, <em>precios transparentes</em>.',
        "price_label": "Primera consulta",
        "book_cta":    "Reservar",

        "services": [
            {
                "icon_svg": ICO_STETHOSCOPE,
                "eyebrow":  "Cardiología",
                "title":    "Consulta cardiológica con ECG",
                "desc":     "Anamnesis detallada, auscultación, ECG de "
                            "12 derivaciones, valoración del riesgo "
                            "cardiovascular e indicación de pruebas "
                            "adicionales cuando procede.",
                "items":    ["ECG incluido", "Informe el mismo día", "40 min"],
                "price":    "140 €",
            },
            {
                "icon_svg": ICO_ULTRASOUND,
                "eyebrow":  "Cardiología",
                "title":    "Ecocardiografía Doppler color",
                "desc":     "Valoración morfológica y funcional del "
                            "corazón con ecógrafo de última generación. "
                            "Útil para soplos, hipertensión y seguimiento postevento.",
                "items":    ["Doppler incluido", "Informe en 24 h", "35 min"],
                "price":    "160 €",
            },
            {
                "icon_svg": ICO_BABY,
                "eyebrow":  "Pediatría",
                "title":    "Consulta pediátrica 0–14",
                "desc":     "Revisión de salud, crecimiento, desarrollo "
                            "psicomotor y alimentación. Asesoramiento "
                            "vacunal según calendario regional bajo demanda.",
                "items":    ["0–14 años", "Hueco urgente en 24 h", "45 min"],
                "price":    "120 €",
            },
            {
                "icon_svg": ICO_DERM,
                "eyebrow":  "Dermatología",
                "title":    "Mapa de nevus por dermatoscopia digital",
                "desc":     "Control oncológico de la piel con "
                            "videodermatoscopio. Imágenes archivadas para "
                            "comparación anual. Recomendado a partir de 30 años.",
                "items":    ["Archivo de 5 años", "Imágenes digitales", "40 min"],
                "price":    "180 €",
            },
            {
                "icon_svg": ICO_WOMAN,
                "eyebrow":  "Ginecología",
                "title":    "Consulta obstétrico-ginecológica + ecografía",
                "desc":     "Consulta completa con ecografía transvaginal "
                            "o abdominal. Itinerarios específicos para "
                            "primer embarazo y menopausia.",
                "items":    ["Citología disponible", "Ecografía incluida", "45 min"],
                "price":    "150 €",
            },
            {
                "icon_svg": ICO_ULTRASOUND,
                "eyebrow":  "Radiología",
                "title":    "Resonancia magnética 1,5 T",
                "desc":     "Equipo abierto de última generación, apto "
                            "también para pacientes claustrofóbicos. "
                            "Informe radiológico en 24 horas laborables.",
                "items":    ["Abierta · sin claustrofobia", "Informe en 24 h", "30 min"],
                "price":    "desde 220 €",
            },
            {
                "icon_svg": ICO_BONE,
                "eyebrow":  "Traumatología",
                "title":    "Consulta traumatológica + ecografía muscular",
                "desc":     "Valoración clínica y ecográfica en una sola "
                            "sesión. Infiltraciones ecoguiadas con ácido "
                            "hialurónico o corticoide cuando está indicado.",
                "items":    ["Ecografía incluida", "Infiltraciones disponibles", "40 min"],
                "price":    "150 €",
            },
            {
                "icon_svg": ICO_BONE,
                "eyebrow":  "Fisioterapia",
                "title":    "Sesión de fisioterapia rehabilitadora",
                "desc":     "Itinerario personalizado con fisioterapeuta "
                            "dedicado, por prescripción del traumatólogo "
                            "o del médico de cabecera. Bonos de 5 y 10 sesiones.",
                "items":    ["Bonos disponibles", "Postquirúrgica", "50 min"],
                "price":    "55 € · sesión",
            },
            {
                "icon_svg": ICO_BRAIN,
                "eyebrow":  "Neurología",
                "title":    "Consulta neurológica con EEG",
                "desc":     "Valoración de cefaleas, trastornos del "
                            "sueño y temblores, con posibilidad de "
                            "electroencefalograma en la misma sesión. "
                            "Pruebas cognitivas bajo demanda.",
                "items":    ["EEG disponible", "Pruebas cognitivas", "50 min"],
                "price":    "170 €",
            },
            {
                "icon_svg": ICO_EYE,
                "eyebrow":  "Oftalmología",
                "title":    "Revisión oftalmológica completa",
                "desc":     "Medición de la vista, tonometría, fondo de "
                            "ojo, OCT de retina. Valoración quirúrgica "
                            "de la catarata en colaboración con centros concertados.",
                "items":    ["OCT incluido", "Tonometría", "35 min"],
                "price":    "130 €",
            },
        ],

        "faq_label":   "Preguntas frecuentes",
        "faq_heading": 'Las <em>tres</em> preguntas que más recibimos.',
        "faqs": [
            ("¿Puedo utilizar mi seguro médico o mutua?",
             "Sí. SaluteVita tiene convenio con Unisalute, Generali "
             "Welion, RBM Salute, Previmedical, Caspie y Consap. En la "
             "mayoría de los casos la mutua cubre directamente la "
             "prestación, sin anticipo. Envíenos su tarjeta al reservar "
             "y confirmamos la cobertura en 24 horas."),
            ("¿En cuántos días recibo el informe?",
             "Consultas clínicas: informe digital en su área de "
             "paciente en 24 horas laborables. Diagnóstico por imagen "
             "(ecografía, TAC, resonancia): informe radiológico en 24 "
             "a 48 horas. Si lo necesita el mismo día, solicítelo al "
             "reservar: casi siempre es posible."),
            ("¿Puedo anular o cambiar la cita?",
             "Por supuesto. Puede modificar o anular desde su área de "
             "paciente hasta 24 horas antes, sin coste. Por debajo de "
             "las 24 horas, llame al teléfono gratuito 800 123 456: "
             "valoramos cada caso, sin penalización por motivos médicos."),
        ],

        "cta_band": {
            "heading":    "Elija el servicio, nosotros nos encargamos del resto.",
            "body":       "Reserve en línea en pocos segundos: si no encuentra la especialidad que busca, llame al teléfono gratuito y le orientamos.",
            "primary_cta":"Reservar cita",
            "secondary_cta":"Llamar al 800 123 456",
        },
    },

    "prevenzione": {
        "eyebrow":   "Prevención · tres itinerarios específicos",
        "headline":  'Una revisión completa en <em>media jornada</em>.',
        "intro":
            "Tres paquetes pensados para las franjas de edad en las que "
            "los controles cuentan más: mujer 40+, hombre 45+, senior "
            "60+. Un médico internista lo coordina todo y entrega un "
            "único informe en 48 horas.",

        "pack_label":   "Los tres itinerarios",
        "pack_heading": 'Elija según <em>la edad y el perfil</em>.',
        "duration_label": "Duración",
        "exams_label":    "Pruebas",

        "packages": [
            {
                "eyebrow": "MUJER 40+",
                "title":   "Revisión Mujer 40+",
                "desc":    "Pensado para mantener bajo control la salud "
                           "ginecológica, senológica y metabólica en una sola mañana.",
                "price":   "320 €",
                "price_meta": "todo incluido",
                "duration": "3 horas",
                "exams_count": "7 pruebas",
                "includes": [
                    "Consulta ginecológica con ecografía pélvica",
                    "Citología y prueba HPV",
                    "Mamografía bilateral",
                    "Asesoramiento nutricional de 30 minutos",
                    "Analítica de perfil metabólico",
                    "Consulta senológica de control",
                    "Informe único en 48 horas",
                ],
                "cta":      "Reservar la revisión",
                "is_popular": True,
                "popular_label": "La más solicitada",
            },
            {
                "eyebrow": "HOMBRE 45+",
                "title":   "Revisión Hombre 45+",
                "desc":    "El control que todos aplazamos y que no hay "
                           "que aplazar nunca: corazón, próstata, "
                           "metabolismo, hígado.",
                "price":   "280 €",
                "price_meta": "todo incluido",
                "duration": "3,5 horas",
                "exams_count": "7 pruebas",
                "includes": [
                    "Consulta cardiológica con ECG",
                    "Ecocardiografía Doppler color",
                    "Consulta urológica con PSA",
                    "Ecografía abdominal completa",
                    "Perfil lipídico y glucémico",
                    "Valoración del riesgo cardiovascular",
                    "Informe único en 48 horas",
                ],
                "cta":      "Reservar la revisión",
                "is_popular": False,
                "popular_label": "",
            },
            {
                "eyebrow": "SENIOR 60+",
                "title":   "Revisión Senior 60+",
                "desc":    "Un cuadro completo coordinado por un médico "
                           "internista que mantiene unidos corazón, "
                           "huesos, cerebro y ojos.",
                "price":   "420 €",
                "price_meta": "todo incluido",
                "duration": "4 horas",
                "exams_count": "9 pruebas",
                "includes": [
                    "Cardiología + ecocardio + holter de 24 h",
                    "Densitometría ósea DEXA",
                    "Consulta neurológica con pruebas cognitivas",
                    "Consulta oftalmológica con OCT de retina",
                    "Tonometría y campo visual",
                    "Perfil metabólico completo",
                    "Consulta internista de coordinación",
                    "Entrevista final con el médico responsable",
                    "Informe único en 48 horas",
                ],
                "cta":      "Reservar la revisión",
                "is_popular": False,
                "popular_label": "",
            },
        ],

        "how_label":   "Cómo funciona",
        "how_heading": 'Cuatro pasos <em>sin sorpresas</em>.',
        "how_steps": [
            {"num": "01", "title": "Reserve en línea",
             "body": "Elija la revisión más adecuada y el día. Recibe "
                     "confirmación por correo con las instrucciones de preparación."},
            {"num": "02", "title": "Ayuno por la mañana",
             "body": "La analítica requiere 8 horas de ayuno. Agua mineral "
                     "natural permitida hasta una hora antes de llegar."},
            {"num": "03", "title": "Media mañana con nosotros",
             "body": "Llega a las 7:30 y sale antes del mediodía. Todas "
                     "las pruebas encadenadas, sin tiempos muertos."},
            {"num": "04", "title": "Informe único en 48 horas",
             "body": "El médico coordinador le llama para comentar los "
                     "resultados y entregarle el PDF resumen."},
        ],

        "cta_band": {
            "heading":    "Una revisión al año para dormir mejor.",
            "body":       "Reserve hoy: le devolvemos la llamada en dos horas laborables para confirmar fecha e instrucciones de preparación.",
            "primary_cta":"Reservar una revisión",
            "secondary_cta":"Llamar al 800 123 456",
        },
    },

    "medici": {
        "eyebrow":   "Médicos · 40+ especialistas",
        "headline":  'El equipo que <em>le atenderá</em>.',
        "intro":
            "Aquí presentamos a los seis facultativos que dirigen "
            "nuestros servicios con más demanda. El equipo completo "
            "supera los 40 especialistas: si busca a alguien en "
            "concreto, llame a la recepción y le ayudamos a encontrarlo.",

        "book_cta": "Reservar con este facultativo",

        "doctors": [
            {
                "portrait": "https://images.pexels.com/photos/5327585/pexels-photo-5327585.jpeg?auto=compress&cs=tinysrgb&w=600&h=600&fit=crop",
                "role":     "Cardiología · jefa de servicio",
                "name":     "Dra. Elisa Conti",
                "credentials":
                    "Especialización en Cardiología en la Universidad "
                    "de Milán. 22 años de práctica clínica, formación "
                    "en el Centro Cardiologico Monzino. Socia de la "
                    "Sociedad Italiana de Cardiología.",
                "tags": ["Cardiología", "Ecocardiografía", "Prevención CV"],
            },
            {
                "portrait": "https://images.pexels.com/photos/5452293/pexels-photo-5452293.jpeg?auto=compress&cs=tinysrgb&w=600&h=600&fit=crop",
                "role":     "Pediatría · jefe de servicio",
                "name":     "Dr. Marco Ferri",
                "credentials":
                    "Pediatra de familia, especialización en la "
                    "Clínica De Marchi. 18 años al servicio de las "
                    "familias milanesas, con interés por la "
                    "neonatología y los trastornos respiratorios infantiles.",
                "tags": ["0–14 años", "Vacunación", "Neumología pediátrica"],
            },
            {
                "portrait": "https://images.pexels.com/photos/5452274/pexels-photo-5452274.jpeg?auto=compress&cs=tinysrgb&w=600&h=600&fit=crop",
                "role":     "Dermatología",
                "name":     "Dra. Sofia Lenzi",
                "credentials":
                    "Dermatóloga, especialización en la Universidad "
                    "Vita-Salute San Raffaele. Diez años de experiencia "
                    "en dermatoscopia digital y seguimiento oncológico cutáneo.",
                "tags": ["Dermatoscopia", "Oncología cutánea", "Acné"],
            },
            {
                "portrait": "https://images.pexels.com/photos/4173239/pexels-photo-4173239.jpeg?auto=compress&cs=tinysrgb&w=600&h=600&fit=crop",
                "role":     "Radiología · director de diagnóstico",
                "name":     "Dr. Luca Russo",
                "credentials":
                    "Radiólogo, 25 años de experiencia hospitalaria "
                    "antes de incorporarse a SaluteVita en 2015. "
                    "Referente de resonancia y TAC, dirige un equipo "
                    "de seis técnicos.",
                "tags": ["Resonancia 1,5 T", "TAC", "Ecografía multiorgánica"],
            },
            {
                "portrait": "https://images.pexels.com/photos/5327921/pexels-photo-5327921.jpeg?auto=compress&cs=tinysrgb&w=600&h=600&fit=crop",
                "role":     "Ginecología · obstetricia",
                "name":     "Dra. Chiara Moretti",
                "credentials":
                    "Ginecóloga y obstetra, especialización en la "
                    "Clínica Mangiagalli. Atiende embarazos fisiológicos, "
                    "menopausia y prevención oncológica femenina.",
                "tags": ["Embarazo", "Menopausia", "Citología + HPV"],
            },
            {
                "portrait": "https://images.pexels.com/photos/6129507/pexels-photo-6129507.jpeg?auto=compress&cs=tinysrgb&w=600&h=600&fit=crop",
                "role":     "Traumatología · medicina deportiva",
                "name":     "Dr. Paolo Serra",
                "credentials":
                    "Traumatólogo, especialización en el Istituto "
                    "Galeazzi. Experto en ecografía músculo-esquelética "
                    "e infiltraciones ecoguiadas, atiende a deportistas "
                    "de Serie A y aficionados.",
                "tags": ["Ecografía muscular", "Infiltraciones", "Medicina deportiva"],
            },
        ],

        "footnote_strong": "Más de 40 especialistas componen el equipo médico completo.",
        "footnote_body":
            "Neurología, oftalmología, otorrinolaringología, urología, "
            "endocrinología y otras siete especialidades. Contacte con "
            "la recepción para identificar al facultativo adecuado para "
            "su solicitud: ",
        "footnote_link": "escríbanos desde la página de contacto",
    },

    "contatti": {
        "eyebrow":   "Contacto · Via Galvani 18 · Milán",
        "headline":  'Estamos <em>donde hace falta</em>: a dos pasos de Milán Centrale.',
        "intro":
            "La recepción abre de 7:00 a 21:00 de lunes a viernes. "
            "Escríbanos o llame: respondemos en dos horas laborables, "
            "sin contestador automático.",

        "map_aria":    "Mapa ilustrativo del centro SaluteVita en Via Galvani 18, Milán",
        "map_stamp":   "Via Galvani 18 · Milán Centrale",

        "address_label": "Dirección",
        "email_label":   "Correo electrónico",

        "hours_heading": "Horario de apertura",
        "hours_table": [
            ("Lunes – Viernes", "7:00 – 21:00"),
            ("Sábado",          "8:00 – 18:00"),
            ("Domingo",         "Cerrado"),
            ("Festivos",        "Cerrado · teléfono gratuito activo"),
        ],

        "access": [
            {"icon": "car",        "title": "Aparcamiento concertado",
             "body": "Garage Centrale a 40 metros. 2 €/hora para pacientes SaluteVita."},
            {"icon": "metro",      "title": "Metro",
             "body": "M2/M3 Milano Centrale · 4 minutos a pie. Tranvías 5 y 9 delante."},
            {"icon": "wheelchair", "title": "Acceso sin barreras",
             "body": "Entrada sin barreras, ascensor y aseo adaptado en planta baja."},
            {"icon": "info",       "title": "Urgencias",
             "body": "No somos un servicio de urgencias. Para emergencias sanitarias llame al 112."},
        ],

        "form_title": "Envíenos un mensaje",
        "form_intro":
            "Para una consulta general o información previa a la "
            "reserva, escríbanos aquí. Respondemos en dos horas laborables.",

        "form_fields": [
            {"name": "nome",       "label": "Nombre",     "type": "text",     "placeholder": "Mario",                  "required": True},
            {"name": "cognome",    "label": "Apellidos",  "type": "text",     "placeholder": "Rossi",                  "required": True},
            {"name": "email",      "label": "Correo electrónico", "type": "email",    "placeholder": "mario.rossi@email.es", "required": True},
            {"name": "telefono",   "label": "Teléfono",   "type": "tel",      "placeholder": "+39 ...",                "required": False},
            {"name": "specialita", "label": "Especialidad de interés", "type": "select", "required": False,
             "options": ["Cardiología", "Pediatría", "Dermatología", "Radiología",
                         "Ginecología", "Traumatología", "Neurología", "Oftalmología",
                         "Otra / información general"]},
            {"name": "oggetto",    "label": "Asunto",     "type": "text",     "placeholder": "Información de prevención", "required": True},
            {"name": "messaggio",  "label": "Mensaje",    "type": "textarea", "placeholder": "Cuéntenos brevemente qué necesita…",
             "required": True, "full_width": True,
             "helper": "No envíe datos sanitarios sensibles por este formulario: para informes utilice su área de paciente."},
        ],
        "consent":
            "Consiento el tratamiento de mis datos personales conforme al "
            "Reglamento UE 2016/679, con el único fin de responder a esta consulta.",
        "submit_label": "Enviar mensaje",
        "form_note":    "Respuesta en dos horas laborables",
    },

    "prenota": {
        "eyebrow":   "Reservar · en línea en 30 segundos",
        "headline":  'Indíquenos cuándo, <em>nosotros nos encargamos del resto</em>.',
        "intro":
            "Rellene el formulario a continuación: le devolvemos la "
            "llamada en dos horas laborables para confirmar fecha, "
            "facultativo y preparación. Si prefiere hablar con una "
            "persona, llame al teléfono gratuito 800 123 456.",

        "form_sections": [
            {"num": "01", "title": "Sus datos", "meta": "para poder contactarle",
             "fields": ["nome", "cognome", "email", "telefono", "data_nascita", "codice_fiscale"]},
            {"num": "02", "title": "Detalles de la cita", "meta": "tipo y especialidad",
             "fields": ["specialita", "medico_preferito", "tipo_visita", "convenzione"]},
            {"num": "03", "title": "Su disponibilidad", "meta": "le llamamos para confirmar",
             "fields": ["data_preferita", "fascia_orario", "note"]},
        ],

        "form_fields": [
            {"name": "nome",            "label": "Nombre",          "type": "text",  "placeholder": "Mario",                    "required": True},
            {"name": "cognome",         "label": "Apellidos",       "type": "text",  "placeholder": "Rossi",                    "required": True},
            {"name": "email",           "label": "Correo electrónico","type": "email","placeholder": "mario.rossi@email.es",    "required": True,
             "helper": "Enviamos los SMS de recordatorio y el informe digital a esta dirección."},
            {"name": "telefono",        "label": "Teléfono",        "type": "tel",   "placeholder": "+39 335 ...",              "required": True},
            {"name": "data_nascita",    "label": "Fecha de nacimiento","type": "date","placeholder": "dd/mm/aaaa",              "required": True},
            {"name": "codice_fiscale",  "label": "Codice fiscale (identificador fiscal italiano)", "type": "text",  "placeholder": "RSSMRA80A01F205X", "required": False,
             "helper": "Útil si tiene convenio: agilizamos la tramitación."},
            {"name": "specialita",      "label": "Especialidad",    "type": "select","required": True,
             "options": ["Cardiología", "Pediatría", "Dermatología",
                         "Radiología y diagnóstico", "Ginecología",
                         "Traumatología y fisioterapia", "Neurología", "Oftalmología",
                         "Revisión de prevención", "Otra especialidad"]},
            {"name": "medico_preferito","label": "Facultativo de preferencia","type": "select","required": False,
             "options": ["Sin preferencia · primer hueco libre",
                         "Dra. Elisa Conti · Cardiología",
                         "Dr. Marco Ferri · Pediatría",
                         "Dra. Sofia Lenzi · Dermatología",
                         "Dr. Luca Russo · Radiología",
                         "Dra. Chiara Moretti · Ginecología",
                         "Dr. Paolo Serra · Traumatología",
                         "Dr. Andrea Villa · Neurología",
                         "Dra. Laura Bianchi · Oftalmología"]},
            {"name": "tipo_visita",     "label": "Tipo de consulta","type": "select","required": True,
             "options": ["Primera consulta", "Consulta de seguimiento", "Prueba diagnóstica",
                         "Consulta urgente (24–48 h)"]},
            {"name": "convenzione",     "label": "¿Usa convenio?",  "type": "select", "required": False,
             "options": ["Ninguno · pago privado",
                         "Unisalute", "Generali Welion", "RBM Salute",
                         "Previmedical", "Caspie", "MioDottore", "Consap",
                         "Inail", "Otra aseguradora / mutua"]},
            {"name": "data_preferita",  "label": "Fecha preferida", "type": "date",  "placeholder": "dd/mm/aaaa", "required": True,
             "helper": "Dentro de los próximos 30 días. Si se libera un hueco antes, le avisamos."},
            {"name": "fascia_orario",   "label": "Franja horaria",  "type": "select","required": True,
             "options": ["Primera hora · 7:00 – 9:00",
                         "Mañana · 9:00 – 12:00",
                         "Primera tarde · 13:00 – 16:00",
                         "Última tarde · 16:00 – 19:00",
                         "Noche · 19:00 – 21:00",
                         "Sin preferencia"]},
            {"name": "note",            "label": "Notas para el facultativo", "type": "textarea",
             "placeholder": "Escriba aquí posibles síntomas, tratamientos en curso o preguntas concretas…",
             "required": False, "full_width": True,
             "helper": "Opcional. Solo pedimos lo que el facultativo necesita para prepararse."},
        ],

        "consent":
            "Consiento el tratamiento de mis datos personales conforme al "
            "Reglamento UE 2016/679 y al aviso sanitario de SaluteVita. "
            "Los datos se utilizarán únicamente para la gestión de esta cita.",
        "submit_label":     "Confirmar cita",
        "form_submit_note": "Le devolvemos la llamada en dos horas laborables",

        "help_title": "Cómo funciona la reserva",
        "help_steps": [
            {"num": "1", "title": "Rellena el formulario",
             "body": "90 segundos bastan. No se requiere pago por adelantado."},
            {"num": "2", "title": "Le devolvemos la llamada en 2 horas",
             "body": "Un miembro de la recepción confirma fecha, facultativo e indicaciones de preparación."},
            {"num": "3", "title": "Recordatorio por SMS",
             "body": "Dos días antes recibe un SMS con fecha, hora y consulta."},
            {"num": "4", "title": "Informe digital",
             "body": "En 24–48 h llegan informe y prescripciones a su área de paciente, descargables en PDF."},
        ],

        "alt_title": "¿Prefiere hablar con una persona?",
        "alt_body":
            "El teléfono gratuito está activo los 7 días de la semana, "
            "de 7:00 a 21:00. Descolgamos de media en menos de 40 segundos.",

        "trust": [
            "Datos cifrados de extremo a extremo (AES-256, estándar sanitario)",
            "Anulación o cambio hasta 24 h antes, sin coste",
            "Convenios con 8 grandes aseguradoras y mutuas sanitarias",
        ],
    },
}

__all__ = ["SALUTE_CONTENT_ES"]
