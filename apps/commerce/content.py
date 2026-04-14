"""Per-storefront commerce content in 5 locales.

What lives here vs elsewhere
----------------------------
- `apps/commerce/i18n.py` → skin-agnostic chrome (buttons, column
  headers, form labels, generic section titles). Same for both
  Bottega and Luxe.
- `apps/commerce/content.py` (this file) → brand-specific prose
  that belongs to one storefront and must not leak to the other:
  the bottega tagline, the maison manifesto, the real shipping /
  returns policy text, the footer bio line. 5 locales each.

The seed_commerce command pulls fields from this module when
creating/refreshing Storefront, Collection and some Product
translation blocks so the operational shop reads as coherent
as the live-preview template, in every language.

Shape
-----
STOREFRONT_CONTENT = {
  "<storefront-slug>": {
    "<locale>": {
      "tagline": "…",
      "about": "…",
      "footer_bio": "…",
      "shipping_policy": "…",
      "return_policy": "…",
      "bank_transfer_instructions": "…",
      "nav_maison_label": "…",      # optional per-skin chrome
      "nav_atelier_label": "…",
    }, ...
  }, ...
}

Collection and Product translations live on their rows as
JSON (`translations` field). The seed command authored by the
commerce team reads collection/product copy from the pre-existing
catalog template_content_* files; this file carries only the
storefront-level policy / manifesto text.
"""
from __future__ import annotations


# ──────────────────────────────────────────────────────────────────
# BOTTEGA — artisan workshop, warm Tuscan voice
# ──────────────────────────────────────────────────────────────────

BOTTEGA_CONTENT = {
    "it": {
        "tagline": "Bottega artigiana · Firenze · dal 1968",
        "footer_bio": "Bottega artigiana fondata nel 1968. Cuoio, ceramica e tessuti fatti a mano in Toscana, in piccole edizioni che non si ripetono.",
        "nav_atelier_label": "Atelier",
        "shipping_policy": (
            "Spediamo con corriere tracciato in 48 ore in tutta Italia e "
            "in quattro giorni lavorativi in Europa. Ogni pezzo è incartato "
            "a mano in carta cerata e cartone riciclato, senza plastica. "
            "I pezzi su ordinazione partono entro due settimane dalla "
            "conferma del pagamento."
        ),
        "return_policy": (
            "Cambi e resi entro 14 giorni, salvo edizioni numerate e "
            "conserve alimentari. Scrivici a bottega@martino.it con il "
            "numero ordine: preparaiamo l'etichetta di reso e rimborsiamo "
            "entro tre giorni dal ritiro."
        ),
        "bank_transfer_instructions": (
            "Per il bonifico bancario:\n"
            "Beneficiario · La Bottega di Martino\n"
            "IBAN · IT47 A030 6902 4780 0000 0472 011\n"
            "Causale · il numero ordine che trovi qui sotto.\n"
            "Riceverai conferma dell'ordine appena il bonifico arriva."
        ),
    },
    "en": {
        "tagline": "Artisan bottega · Florence · since 1968",
        "footer_bio": "Artisan bottega founded in 1968. Leather, ceramics and textiles handmade in Tuscany, in small editions that never repeat.",
        "nav_atelier_label": "Atelier",
        "shipping_policy": (
            "We ship with a tracked courier within 48 hours across Italy "
            "and four working days across Europe. Every piece is hand-wrapped "
            "in waxed paper and recycled cardboard, plastic-free. Made-to-order "
            "pieces leave the bottega within two weeks of payment confirmation."
        ),
        "return_policy": (
            "Exchanges and returns within 14 days, except numbered editions "
            "and food conserves. Write to bottega@martino.it with the order "
            "number: we prepare the return label and refund within three days "
            "of pickup."
        ),
        "bank_transfer_instructions": (
            "Bank transfer details:\n"
            "Beneficiary · La Bottega di Martino\n"
            "IBAN · IT47 A030 6902 4780 0000 0472 011\n"
            "Reference · the order number shown below.\n"
            "We confirm the order as soon as the transfer lands."
        ),
    },
    "fr": {
        "tagline": "Bottega artisanale · Florence · depuis 1968",
        "footer_bio": "Bottega artisanale fondée en 1968. Cuir, céramique et textiles façonnés à la main en Toscane, en petites éditions qui ne se répètent jamais.",
        "nav_atelier_label": "Atelier",
        "shipping_policy": (
            "Nous expédions avec un transporteur suivi en 48 heures en Italie "
            "et en quatre jours ouvrés en Europe. Chaque pièce est emballée "
            "à la main dans du papier ciré et du carton recyclé, sans plastique. "
            "Les pièces sur commande partent sous deux semaines après confirmation "
            "du paiement."
        ),
        "return_policy": (
            "Échanges et retours sous 14 jours, hors éditions numérotées et "
            "conserves alimentaires. Écrivez-nous à bottega@martino.it avec "
            "votre numéro de commande : nous préparons l'étiquette de retour "
            "et vous remboursons sous trois jours après réception."
        ),
        "bank_transfer_instructions": (
            "Coordonnées bancaires :\n"
            "Bénéficiaire · La Bottega di Martino\n"
            "IBAN · IT47 A030 6902 4780 0000 0472 011\n"
            "Référence · le numéro de commande ci-dessous.\n"
            "Nous confirmons la commande dès réception du virement."
        ),
    },
    "es": {
        "tagline": "Bottega artesanal · Florencia · desde 1968",
        "footer_bio": "Bottega artesanal fundada en 1968. Cuero, cerámica y tejidos hechos a mano en Toscana, en ediciones pequeñas que no se repiten.",
        "nav_atelier_label": "Atelier",
        "shipping_policy": (
            "Enviamos con transportista con seguimiento en 48 horas por toda "
            "Italia y en cuatro días laborables por Europa. Cada pieza se "
            "envuelve a mano en papel encerado y cartón reciclado, sin plástico. "
            "Las piezas por encargo salen de la bottega en dos semanas desde "
            "la confirmación del pago."
        ),
        "return_policy": (
            "Cambios y devoluciones en 14 días, salvo ediciones numeradas y "
            "conservas. Escribe a bottega@martino.it con el número de pedido: "
            "preparamos la etiqueta de devolución y reembolsamos en tres días "
            "desde la recogida."
        ),
        "bank_transfer_instructions": (
            "Datos para la transferencia:\n"
            "Beneficiario · La Bottega di Martino\n"
            "IBAN · IT47 A030 6902 4780 0000 0472 011\n"
            "Concepto · el número de pedido que ves abajo.\n"
            "Confirmamos el pedido en cuanto recibimos la transferencia."
        ),
    },
    "ar": {
        "tagline": "بوتيغا حِرَفيّة · فلورنسا · منذ 1968",
        "footer_bio": "بوتيغا حرفيّة تأسّست عام 1968. جلدٌ وسيراميكٌ ومنسوجاتٌ مصنوعةٌ يدوياً في توسكانا، بإصداراتٍ صغيرةٍ لا تتكرّر.",
        "nav_atelier_label": "الأتيليه",
        "shipping_policy": (
            "نشحن بناقلٍ مع تتبّع خلال 48 ساعة في إيطاليا، وأربعة أيام عمل في أوروبا. "
            "تُغلَّف كلّ قطعة يدويّاً بورقٍ مشمّعٍ وكرتونٍ مُعاد تدويره، دون بلاستيك. "
            "تُغادر القطع المصنوعة حسب الطلب البوتيغا خلال أسبوعين من تأكيد الدفع."
        ),
        "return_policy": (
            "الاستبدال والإرجاع خلال 14 يوماً، عدا الإصدارات المرقّمة والمعلّبات الغذائية. "
            "راسلنا على bottega@martino.it مع رقم الطلب: نجهّز بطاقة الإرجاع ونردّ المبلغ "
            "خلال ثلاثة أيام من الاستلام."
        ),
        "bank_transfer_instructions": (
            "تفاصيل التحويل البنكي:\n"
            "المستفيد · La Bottega di Martino\n"
            "IBAN · IT47 A030 6902 4780 0000 0472 011\n"
            "السبب · رقم الطلب الموضّح أدناه.\n"
            "نؤكّد الطلب فور وصول التحويل."
        ),
    },
}


# ──────────────────────────────────────────────────────────────────
# LUXE — fashion-editorial, maison editoriale voice
# ──────────────────────────────────────────────────────────────────

LUXE_CONTENT = {
    "it": {
        "tagline": "Maison · Milano · Parigi · Tokyo",
        "footer_bio": "Maison milanese di alta confezione. Capi fatti a mano a Biella, Como, Firenze e Sentier. Acquisto su appuntamento con la direzione clienti o per drop privati.",
        "nav_maison_label": "Maison",
        "shipping_policy": (
            "Consegna maison Milano in 24 ore, 48 ore nelle altre città italiane, "
            "tre giorni lavorativi in Europa. Ogni capo viaggia con stiratura a "
            "vapore, appendino firmato in legno di cedro, sacca in cotone grezzo "
            "e bolla di servizio. Il trasporto è sempre assicurato al valore."
        ),
        "return_policy": (
            "Cambi e resi su appuntamento in maison entro sette giorni dalla "
            "consegna. Scrivere a clienti@luxe.atelier: l'atelier concorda "
            "l'ingresso in Via Brera e rimborsa o propone alterazione. "
            "I drop privati e le misure su ordinazione non rientrano nel reso."
        ),
        "bank_transfer_instructions": (
            "Coordinate per bonifico maison:\n"
            "Beneficiario · Maison Luxe S.r.l.\n"
            "IBAN · IT14 K050 3401 6400 0000 0083 412\n"
            "BIC · BAPPIT22\n"
            "Causale · il codice ordine qui sotto.\n"
            "L'atelier conferma l'ordine alla ricezione del bonifico."
        ),
    },
    "en": {
        "tagline": "Maison · Milan · Paris · Tokyo",
        "footer_bio": "Milanese couture maison. Garments handmade in Biella, Como, Florence and Sentier. Purchase by appointment with client services or at private drops.",
        "nav_maison_label": "Maison",
        "shipping_policy": (
            "Maison delivery within 24 hours in Milan, 48 hours elsewhere in "
            "Italy, three working days across Europe. Every garment travels "
            "steam-pressed, on a signed cedarwood hanger, in a raw-cotton bag "
            "with service note. Shipments are always insured at full value."
        ),
        "return_policy": (
            "Exchanges and returns by appointment in maison within seven days "
            "of delivery. Write to clienti@luxe.atelier: the atelier will book "
            "your visit to Via Brera and either refund or propose an alteration. "
            "Private drops and made-to-measure fittings are non-returnable."
        ),
        "bank_transfer_instructions": (
            "Maison wire details:\n"
            "Beneficiary · Maison Luxe S.r.l.\n"
            "IBAN · IT14 K050 3401 6400 0000 0083 412\n"
            "BIC · BAPPIT22\n"
            "Reference · the order code shown below.\n"
            "The atelier confirms the order once the wire lands."
        ),
    },
    "fr": {
        "tagline": "Maison · Milan · Paris · Tokyo",
        "footer_bio": "Maison de couture milanaise. Pièces façonnées à la main à Biella, Côme, Florence et dans le Sentier. Achat sur rendez-vous auprès de la direction clientèle ou lors de drops privés.",
        "nav_maison_label": "Maison",
        "shipping_policy": (
            "Livraison maison en 24 heures dans Milan, 48 heures ailleurs en "
            "Italie, trois jours ouvrés en Europe. Chaque pièce voyage repassée "
            "à la vapeur, sur cintre signé en cèdre, dans une pochette en coton "
            "brut avec bon de service. Les envois sont toujours assurés à valeur."
        ),
        "return_policy": (
            "Échanges et retours sur rendez-vous à la maison dans les sept "
            "jours après livraison. Écrire à clienti@luxe.atelier : l'atelier "
            "fixe la visite Via Brera et propose remboursement ou retouche. "
            "Les drops privés et le sur-mesure sont non retournables."
        ),
        "bank_transfer_instructions": (
            "Coordonnées maison :\n"
            "Bénéficiaire · Maison Luxe S.r.l.\n"
            "IBAN · IT14 K050 3401 6400 0000 0083 412\n"
            "BIC · BAPPIT22\n"
            "Référence · le code commande ci-dessous.\n"
            "L'atelier confirme la commande à réception du virement."
        ),
    },
    "es": {
        "tagline": "Maison · Milán · París · Tokio",
        "footer_bio": "Maison milanesa de alta confección. Prendas hechas a mano en Biella, Como, Florencia y Sentier. Compra con cita con la dirección de clientes o en drops privados.",
        "nav_maison_label": "Maison",
        "shipping_policy": (
            "Entrega maison en 24 horas en Milán, 48 horas en el resto de Italia, "
            "tres días laborables en Europa. Cada prenda viaja planchada al vapor, "
            "en percha firmada de cedro, en funda de algodón crudo con hoja de "
            "servicio. Los envíos van siempre asegurados al valor completo."
        ),
        "return_policy": (
            "Cambios y devoluciones con cita en la maison en los siete días "
            "posteriores a la entrega. Escribir a clienti@luxe.atelier: el "
            "atelier concierta la visita en Via Brera y propone reembolso o "
            "retoque. Los drops privados y la confección a medida no se devuelven."
        ),
        "bank_transfer_instructions": (
            "Datos para la transferencia maison:\n"
            "Beneficiario · Maison Luxe S.r.l.\n"
            "IBAN · IT14 K050 3401 6400 0000 0083 412\n"
            "BIC · BAPPIT22\n"
            "Concepto · el código de pedido indicado abajo.\n"
            "El atelier confirma el pedido al recibir la transferencia."
        ),
    },
    "ar": {
        "tagline": "ميزون · ميلانو · باريس · طوكيو",
        "footer_bio": "ميزون ميلانيّة راقية. قطعٌ مصنوعةٌ يدويّاً في بييلّا وكومو وفلورنسا وسَنتْيِيه. الاقتناء بحجزٍ مع إدارة العملاء أو خلال الإطلاقات الخاصّة.",
        "nav_maison_label": "الميزون",
        "shipping_policy": (
            "توصيلٌ داخل الميزون خلال 24 ساعة في ميلانو، و48 ساعة في باقي إيطاليا، "
            "وثلاثة أيام عمل في أوروبا. تُشحن كلّ قطعةٍ مكويّةً بالبخار، على شمّاعةٍ "
            "مُوقَّعةٍ من خشب الأرز، في كيسٍ قطنيٍّ خامٍ مع بطاقة الخدمة. "
            "الشحنات مؤمّنةٌ دائماً بكامل القيمة."
        ),
        "return_policy": (
            "الاستبدال والإرجاع بموعدٍ داخل الميزون خلال سبعة أيّام من التسليم. "
            "راسل clienti@luxe.atelier: يحدّد الأتيليه زيارة Via Brera ويقترح "
            "ردّ المبلغ أو إجراء التعديل. الإطلاقات الخاصّة والخياطة على المقاس "
            "غير قابلةٍ للإرجاع."
        ),
        "bank_transfer_instructions": (
            "تفاصيل التحويل البنكي:\n"
            "المستفيد · Maison Luxe S.r.l.\n"
            "IBAN · IT14 K050 3401 6400 0000 0083 412\n"
            "BIC · BAPPIT22\n"
            "السبب · رمز الطلب الموضّح أدناه.\n"
            "يؤكّد الأتيليه الطلب عند وصول التحويل."
        ),
    },
}


STOREFRONT_CONTENT = {
    "bottega-shop-artigianale": BOTTEGA_CONTENT,
    "luxe-fashion-store":       LUXE_CONTENT,
}


def get_storefront_content(storefront_slug: str, locale: str) -> dict:
    """Return the storefront content block for (slug, locale), IT-fallback."""
    per_slug = STOREFRONT_CONTENT.get(storefront_slug) or {}
    return per_slug.get(locale) or per_slug.get("it") or {}


# ──────────────────────────────────────────────────────────────────
# COLLECTION translations — seeded on Collection.translations JSON
# ──────────────────────────────────────────────────────────────────
#
# Single flat map so seed_commerce can pick up the translated title
# without re-implementing a lookup path. Shape is
# `{<storefront_slug>: {<collection_slug>: {<locale>: {title, subtitle}}}}`.

COLLECTION_CONTENT = {
    "bottega-shop-artigianale": {
        "cuoio": {
            "it": {"title": "Cuoio",     "subtitle": "Pelle conciata al vegetale"},
            "en": {"title": "Leather",   "subtitle": "Vegetable-tanned leather"},
            "fr": {"title": "Cuir",      "subtitle": "Cuir tanné au végétal"},
            "es": {"title": "Cuero",     "subtitle": "Curtido vegetal"},
            "ar": {"title": "الجلد",     "subtitle": "مدبوغٌ بالطرق النباتية"},
        },
        "ceramica": {
            "it": {"title": "Ceramica",  "subtitle": "Smalti di Montelupo"},
            "en": {"title": "Ceramics",  "subtitle": "Montelupo-glazed pieces"},
            "fr": {"title": "Céramique", "subtitle": "Émaux de Montelupo"},
            "es": {"title": "Cerámica",  "subtitle": "Esmaltes de Montelupo"},
            "ar": {"title": "السيراميك", "subtitle": "طلاءات مونتيلوبو"},
        },
        "lino-tessuti": {
            "it": {"title": "Lino & tessuti",  "subtitle": "Telai pratesi"},
            "en": {"title": "Linen & textiles", "subtitle": "Prato handlooms"},
            "fr": {"title": "Lin & tissus",    "subtitle": "Métiers de Prato"},
            "es": {"title": "Lino & tejidos",  "subtitle": "Telares de Prato"},
            "ar": {"title": "الكتّان والمنسوجات", "subtitle": "منسوجات براتو"},
        },
        "conserve": {
            "it": {"title": "Conserve",  "subtitle": "Dispensa di Toscana"},
            "en": {"title": "Conserves", "subtitle": "Tuscan pantry"},
            "fr": {"title": "Conserves", "subtitle": "Garde-manger toscan"},
            "es": {"title": "Conservas", "subtitle": "Despensa toscana"},
            "ar": {"title": "المعلّبات", "subtitle": "مؤونة توسكانا"},
        },
    },
    "luxe-fashion-store": {
        "drop-01-spring-26": {
            "it": {"title": "Drop 01 · Primavera 26", "subtitle": "Maglieria e cappotti"},
            "en": {"title": "Drop 01 · Spring 26",    "subtitle": "Knitwear and coats"},
            "fr": {"title": "Drop 01 · Printemps 26", "subtitle": "Mailles et manteaux"},
            "es": {"title": "Drop 01 · Primavera 26", "subtitle": "Punto y abrigos"},
            "ar": {"title": "الإصدار 01 · ربيع 2026", "subtitle": "تريكو ومعاطف"},
        },
        "drop-02-spring-26": {
            "it": {"title": "Drop 02 · Primavera 26", "subtitle": "Tailoring e seta"},
            "en": {"title": "Drop 02 · Spring 26",    "subtitle": "Tailoring and silk"},
            "fr": {"title": "Drop 02 · Printemps 26", "subtitle": "Tailoring et soie"},
            "es": {"title": "Drop 02 · Primavera 26", "subtitle": "Tailoring y seda"},
            "ar": {"title": "الإصدار 02 · ربيع 2026", "subtitle": "تفصيل وحرير"},
        },
        "atelier": {
            "it": {"title": "Atelier",          "subtitle": "Su appuntamento"},
            "en": {"title": "Atelier",          "subtitle": "By appointment"},
            "fr": {"title": "Atelier",          "subtitle": "Sur rendez-vous"},
            "es": {"title": "Atelier",          "subtitle": "Con cita"},
            "ar": {"title": "الأتيليه",         "subtitle": "بحجزٍ مسبق"},
        },
        "archivio-editoriale": {
            "it": {"title": "Archivio editoriale", "subtitle": "Pezzi fuori drop"},
            "en": {"title": "Editorial archive",   "subtitle": "Pieces beyond the drops"},
            "fr": {"title": "Archives éditoriales","subtitle": "Pièces hors drop"},
            "es": {"title": "Archivo editorial",   "subtitle": "Piezas fuera de drop"},
            "ar": {"title": "الأرشيف التحريري",    "subtitle": "قطعٌ خارج الإصدارات"},
        },
    },
}


def collection_title(storefront_slug: str, collection_slug: str, locale: str,
                     fallback: str = "") -> str:
    per_slug = COLLECTION_CONTENT.get(storefront_slug) or {}
    per_coll = per_slug.get(collection_slug) or {}
    block = per_coll.get(locale) or per_coll.get("it") or {}
    return block.get("title") or fallback
