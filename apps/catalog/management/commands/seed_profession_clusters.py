"""Seed the 52 catalog ProfessionCluster rows (X.2 Commit 2 · seed-only).

ProfessionCluster is the profession-level taxonomy layer introduced in
X.2 Commit 1. The public catalog exposes clusters as both a sidebar
facet and as dedicated discovery pages (``/templates/clusters/<slug>/``
in later commits).

Idempotent: re-running the command creates zero duplicates. The cluster
slug is the natural key; every row uses ``get_or_create`` so operators
can tune cluster attributes in the admin without a re-seed overwrite.

Scope note. Out of the 15 target macro-categories only 8 are present in
``seed_categories`` today (the current MVP set). The remaining 7 (
``education``, ``events``, ``travel``, ``fitness``, ``construction``,
``beauty``, ``nonprofit``) are required by 18 of the 52 clusters; this
command creates them inline via ``Category.objects.get_or_create`` so
the seed is self-contained and does not require modifying
``seed_categories`` (which sits outside this commit's approved scope).
A later commit may fold these 7 rows into the canonical
``seed_categories`` command without any data loss — the
``get_or_create`` is idempotent on the slug either way.
"""

from django.core.management.base import BaseCommand

from apps.catalog.models import Category, ProfessionCluster


# 7 macro-categories required by Wave 2/3 clusters that are not yet in
# ``seed_categories`` (which carries only the 8 MVP rows). Created inline
# here so ``seed_profession_clusters`` can run standalone. ``order`` is
# sequenced right after the existing 8 rows (orders 1–8).
EXTRA_CATEGORIES = [
    {
        "name": "Formazione",
        "slug": "education",
        "description": (
            "Siti web per scuole, accademie, piattaforme di corsi online e tutor. "
            "Enrolment, calendario lezioni, area studente."
        ),
        "icon": "mortarboard",
        "order": 9,
    },
    {
        "name": "Eventi",
        "slug": "events",
        "description": (
            "Siti web per wedding planner, location, conferenze e festival. "
            "Programma, biglietti, lineup e galleria eventi passati."
        ),
        "icon": "calendar-event",
        "order": 10,
    },
    {
        "name": "Viaggi & ospitalità",
        "slug": "travel",
        "description": (
            "Siti web per boutique hotel, agriturismi, tour operator. "
            "Prenotazione, disponibilità, esperienze e itinerari."
        ),
        "icon": "suitcase",
        "order": 11,
    },
    {
        "name": "Fitness & sport",
        "slug": "fitness",
        "description": (
            "Siti web per palestre, personal trainer, studi di yoga e Pilates. "
            "Listini, orari, trainer e programmi di allenamento."
        ),
        "icon": "bicycle",
        "order": 12,
    },
    {
        "name": "Edilizia & design",
        "slug": "construction",
        "description": (
            "Siti web per studi di architettura, interior designer e imprese "
            "edili. Portfolio progetti, servizi e processo di lavoro."
        ),
        "icon": "tools",
        "order": 13,
    },
    {
        "name": "Bellezza",
        "slug": "beauty",
        "description": (
            "Siti web per parrucchieri, barber shop, centri estetici e spa. "
            "Prenotazione trattamenti, listini, team."
        ),
        "icon": "scissors",
        "order": 14,
    },
    {
        "name": "Nonprofit",
        "slug": "nonprofit",
        "description": (
            "Siti web per associazioni, fondazioni, enti culturali. "
            "Missione, progetti, donazioni e volontariato."
        ),
        "icon": "heart",
        "order": 15,
    },
]


# 52 profession clusters mapped to macro-category slugs. Each cluster
# carries ``search_aliases`` with lowercase space-separated terms the
# typeahead endpoint treats as additional prefix-match candidates.
PROFESSION_CLUSTERS = [
    # ── Agency (4) ────────────────────────────────────────────────
    {
        "slug": "creative",
        "name": "Creative agency",
        "category_slug": "agency",
        "description": "Agenzie di brand, advertising, direzione creativa.",
        "icon": "palette",
        "search_aliases": "brand design pubblicità art-direction creativa editoriale",
        "order": 10,
    },
    {
        "slug": "digital-growth",
        "name": "Digital & growth",
        "category_slug": "agency",
        "description": "Agenzie digital, performance marketing, growth studio.",
        "icon": "graph-up-arrow",
        "search_aliases": "digital growth performance seo sem marketing tech",
        "order": 20,
    },
    {
        "slug": "pr-comms",
        "name": "PR & comunicazione",
        "category_slug": "agency",
        "description": "Uffici stampa, agenzie di relazioni pubbliche, comunicazione corporate.",
        "icon": "megaphone",
        "search_aliases": "pr relazioni-pubbliche ufficio-stampa comunicazione press",
        "order": 30,
    },
    {
        "slug": "freelance",
        "name": "Freelance & studio indipendente",
        "category_slug": "agency",
        "description": "Consulenti indipendenti, studi solo-founder, freelance creativi.",
        "icon": "person-workspace",
        "search_aliases": "freelance consulente indipendente solo-founder one-person",
        "order": 40,
    },
    # ── Business (5) ──────────────────────────────────────────────
    {
        "slug": "corporate",
        "name": "Corporate",
        "category_slug": "business",
        "description": "Aziende strutturate, istituzionali, gruppi industriali.",
        "icon": "building",
        "search_aliases": "corporate istituzionale enterprise spa srl gruppo",
        "order": 10,
    },
    {
        "slug": "saas-landing",
        "name": "SaaS & landing prodotto",
        "category_slug": "business",
        "description": "Startup SaaS, prodotti tech, landing ad alta conversione.",
        "icon": "rocket-takeoff",
        "search_aliases": "saas startup prodotto tech landing b2b api",
        "order": 20,
    },
    {
        "slug": "professional-services",
        "name": "Servizi professionali",
        "category_slug": "business",
        "description": "Consulenza strategica, management, engineering consulting.",
        "icon": "briefcase",
        "search_aliases": "consulenza consulting strategia management servizi-professionali",
        "order": 30,
    },
    {
        "slug": "financial-services",
        "name": "Servizi finanziari",
        "category_slug": "business",
        "description": "Commercialisti, fiscalisti, consulenti finanziari, wealth management.",
        "icon": "cash-coin",
        "search_aliases": "commercialista fiscale finanza tasse contabilità wealth",
        "order": 40,
    },
    {
        "slug": "coaching",
        "name": "Coaching & training",
        "category_slug": "business",
        "description": "Business coach, training aziendale, formazione executive.",
        "icon": "mortarboard",
        "search_aliases": "coach coaching training formazione executive mentor",
        "order": 50,
    },
    # ── Restaurant (5) ────────────────────────────────────────────
    {
        "slug": "fine-dining",
        "name": "Fine dining",
        "category_slug": "restaurant",
        "description": "Ristoranti gourmet, stellati, cucina d'autore.",
        "icon": "cup-hot",
        "search_aliases": "stellato chef haute-cuisine gourmet ristorante-alta-cucina michelin",
        "order": 10,
    },
    {
        "slug": "trattoria",
        "name": "Trattoria & pizzeria",
        "category_slug": "restaurant",
        "description": "Trattorie tradizionali, pizzerie, osterie regionali.",
        "icon": "egg-fried",
        "search_aliases": "trattoria pizzeria osteria tradizionale regionale pizza",
        "order": 20,
    },
    {
        "slug": "street-casual",
        "name": "Street & casual",
        "category_slug": "restaurant",
        "description": "Street food, burger, cloud kitchen, casual dining moderno.",
        "icon": "basket",
        "search_aliases": "street-food burger casual cloud-kitchen fast-casual",
        "order": 30,
    },
    {
        "slug": "bar-bistrot",
        "name": "Bar & bistrot",
        "category_slug": "restaurant",
        "description": "Bar, bistrot, enoteche, aperitivo di quartiere.",
        "icon": "cup-straw",
        "search_aliases": "bar bistrot enoteca aperitivo caffè cocktail",
        "order": 40,
    },
    {
        "slug": "bakery-pasticceria",
        "name": "Pasticceria & bakery",
        "category_slug": "restaurant",
        "description": "Pasticcerie, bakery artigianali, laboratori del dolce.",
        "icon": "cake2",
        "search_aliases": "pasticceria bakery panetteria dolci cornetto torta",
        "order": 50,
    },
    # ── Medical (6) ───────────────────────────────────────────────
    {
        "slug": "specialist",
        "name": "Specialista medico",
        "category_slug": "medical",
        "description": "Cardiologi, dermatologi, ortopedici, gastroenterologi, specialisti singoli.",
        "icon": "heart-pulse",
        "search_aliases": "specialista cardiologo dermatologo ortopedico gastroenterologo studio-medico",
        "order": 10,
    },
    {
        "slug": "multi-clinic",
        "name": "Clinica multi-specialistica",
        "category_slug": "medical",
        "description": "Poliambulatori, cliniche con più specialisti, centri diagnostici.",
        "icon": "hospital",
        "search_aliases": "clinica poliambulatorio centro-medico multispecialistica diagnostica",
        "order": 20,
    },
    {
        "slug": "wellness-holistic",
        "name": "Wellness olistico",
        "category_slug": "medical",
        "description": "Centri olistici, medicine integrate, nutrizionisti, naturopati.",
        "icon": "flower2",
        "search_aliases": "olistico wellness naturopatia nutrizione medicina-integrata benessere",
        "order": 30,
    },
    {
        "slug": "family-pediatric",
        "name": "Pediatria & famiglia",
        "category_slug": "medical",
        "description": "Pediatri, studi medici della famiglia, ginecologi.",
        "icon": "people",
        "search_aliases": "pediatria famiglia bambini ginecologo medico-famiglia",
        "order": 40,
    },
    {
        "slug": "dental",
        "name": "Studio dentistico",
        "category_slug": "medical",
        "description": "Dentisti, ortodontisti, implantologia, igiene orale.",
        "icon": "emoji-smile",
        "search_aliases": "dentista odontoiatra ortodonzia implantologia igiene-dentale",
        "order": 50,
    },
    {
        "slug": "veterinary",
        "name": "Veterinario",
        "category_slug": "medical",
        "description": "Cliniche veterinarie, ambulatori per animali da compagnia.",
        "icon": "heart",
        "search_aliases": "veterinario clinica-animali ambulatorio-veterinario pet cane gatto",
        "order": 60,
    },
    # ── Lawyer (3) · Note: category slug is 'lawyer' not 'law' ────
    {
        "slug": "classic-law",
        "name": "Avvocato classico",
        "category_slug": "lawyer",
        "description": "Studi legali tradizionali, civile, penale, commerciale.",
        "icon": "bank",
        "search_aliases": "avvocato legale civile penale commerciale studio-legale tribunale",
        "order": 10,
    },
    {
        "slug": "modern-law-tech",
        "name": "Avvocato moderno & tech",
        "category_slug": "lawyer",
        "description": "Studi legali moderni, IP, startup, diritto tecnologico.",
        "icon": "laptop",
        "search_aliases": "avvocato ip startup diritto-tech proprietà-intellettuale gdpr privacy",
        "order": 20,
    },
    {
        "slug": "notary-commercialista",
        "name": "Notaio & commercialista",
        "category_slug": "lawyer",
        "description": "Notai, commercialisti, revisori contabili.",
        "icon": "file-earmark-text",
        "search_aliases": "notaio commercialista revisore contabile fiscale atti-notarili",
        "order": 30,
    },
    # ── Real estate (3) ───────────────────────────────────────────
    {
        "slug": "real-estate-mass-market",
        "name": "Immobiliare mass-market",
        "category_slug": "real-estate",
        "description": "Agenzie immobiliari residenziali, grande pubblico.",
        "icon": "house",
        "search_aliases": "immobiliare agenzia-immobiliare residenziale casa appartamento",
        "order": 10,
    },
    {
        "slug": "real-estate-luxury",
        "name": "Immobiliare luxury",
        "category_slug": "real-estate",
        "description": "Ville di lusso, portfolio high-end, mercato premium.",
        "icon": "gem",
        "search_aliases": "villa lusso luxury prestigio estate proprietà-esclusive",
        "order": 20,
    },
    {
        "slug": "real-estate-commercial",
        "name": "Immobiliare commerciale",
        "category_slug": "real-estate",
        "description": "Uffici, retail, industriale, property management.",
        "icon": "building-fill",
        "search_aliases": "commerciale uffici retail capannone industriale property-management",
        "order": 30,
    },
    # ── Portfolio (4) ─────────────────────────────────────────────
    {
        "slug": "designer-editorial",
        "name": "Designer editoriale",
        "category_slug": "portfolio",
        "description": "Graphic designer, art director, portfolio editoriale.",
        "icon": "vector-pen",
        "search_aliases": "graphic-designer art-director editoriale tipografia brand-identity",
        "order": 10,
    },
    {
        "slug": "photographer",
        "name": "Fotografo",
        "category_slug": "portfolio",
        "description": "Fotografi di moda, ritratto, architettura, fine-art.",
        "icon": "camera",
        "search_aliases": "fotografo fotografia moda ritratto architettura fine-art still-life",
        "order": 20,
    },
    {
        "slug": "illustrator",
        "name": "Illustratore",
        "category_slug": "portfolio",
        "description": "Illustratori editoriali, artisti visivi, art toy.",
        "icon": "brush",
        "search_aliases": "illustratore illustrazione editoriale arte-visiva disegno",
        "order": 30,
    },
    {
        "slug": "videomaker",
        "name": "Videomaker & motion",
        "category_slug": "portfolio",
        "description": "Videomaker, motion designer, filmmaker, director.",
        "icon": "camera-reels",
        "search_aliases": "videomaker motion-design filmmaker regia cinematografia director",
        "order": 40,
    },
    # ── Ecommerce (4) ─────────────────────────────────────────────
    {
        "slug": "artisan-workshop",
        "name": "Atelier artigiano",
        "category_slug": "ecommerce",
        "description": "Artigiani, maker, atelier di produzione su misura.",
        "icon": "hammer",
        "search_aliases": "artigiano atelier maker produzione artigianale bottega",
        "order": 10,
    },
    {
        "slug": "fashion-editorial",
        "name": "Fashion editorial",
        "category_slug": "ecommerce",
        "description": "Maison fashion, concept store, editorial luxury.",
        "icon": "handbag",
        "search_aliases": "fashion moda maison concept-store luxury editoriale abbigliamento",
        "order": 20,
    },
    {
        "slug": "wine-food-boutique",
        "name": "Boutique vino & food",
        "category_slug": "ecommerce",
        "description": "Enoteche online, gastronomie, prodotti gourmet.",
        "icon": "cup-hot",
        "search_aliases": "enoteca vino wine food gastronomia gourmet prodotti-tipici",
        "order": 30,
    },
    {
        "slug": "jewelry",
        "name": "Gioielleria",
        "category_slug": "ecommerce",
        "description": "Gioiellerie, orafi, atelier di alta gioielleria.",
        "icon": "gem",
        "search_aliases": "gioielleria gioielli orafo oro anello collana alta-gioielleria",
        "order": 40,
    },
    # ── Education (3) ─────────────────────────────────────────────
    {
        "slug": "school-academy",
        "name": "Scuola & accademia",
        "category_slug": "education",
        "description": "Scuole private, accademie, istituti di formazione.",
        "icon": "book",
        "search_aliases": "scuola accademia istituto formazione educazione università",
        "order": 10,
    },
    {
        "slug": "online-course",
        "name": "Corso online",
        "category_slug": "education",
        "description": "Piattaforme di corsi online, masterclass, elearning.",
        "icon": "laptop",
        "search_aliases": "corso-online elearning masterclass formazione-digitale mooc",
        "order": 20,
    },
    {
        "slug": "tutor-language",
        "name": "Tutor & lingue",
        "category_slug": "education",
        "description": "Insegnanti privati, scuole di lingua, lezioni one-to-one.",
        "icon": "chat-dots",
        "search_aliases": "tutor ripetizioni lingua inglese insegnante privato lezioni",
        "order": 30,
    },
    # ── Events (2) ────────────────────────────────────────────────
    {
        "slug": "wedding-venue",
        "name": "Wedding & location",
        "category_slug": "events",
        "description": "Wedding planner, location matrimoni, catering eventi privati.",
        "icon": "flower1",
        "search_aliases": "wedding matrimonio location sposi wedding-planner villa-eventi",
        "order": 10,
    },
    {
        "slug": "conference-corporate",
        "name": "Conferenze & corporate",
        "category_slug": "events",
        "description": "Organizzazione conferenze, eventi corporate, meeting aziendali.",
        "icon": "mic",
        "search_aliases": "conferenza corporate meeting evento-aziendale congresso convegno",
        "order": 20,
    },
    # ── Travel (3) ────────────────────────────────────────────────
    {
        "slug": "boutique-hotel",
        "name": "Boutique hotel",
        "category_slug": "travel",
        "description": "Boutique hotel, relais, design hotel.",
        "icon": "building",
        "search_aliases": "boutique-hotel relais design-hotel resort 5-stelle albergo",
        "order": 10,
    },
    {
        "slug": "bnb-agriturismo",
        "name": "B&B & agriturismo",
        "category_slug": "travel",
        "description": "Bed & breakfast, agriturismi, case vacanza.",
        "icon": "tree",
        "search_aliases": "bnb bed-and-breakfast agriturismo casa-vacanza country-house",
        "order": 20,
    },
    {
        "slug": "tour-operator",
        "name": "Tour operator",
        "category_slug": "travel",
        "description": "Tour operator, agenzie di viaggio esperienziali.",
        "icon": "airplane",
        "search_aliases": "tour-operator viaggio agenzia-viaggi esperienze-di-viaggio escursioni",
        "order": 30,
    },
    # ── Fitness (3) ───────────────────────────────────────────────
    {
        "slug": "gym-functional",
        "name": "Palestra & functional",
        "category_slug": "fitness",
        "description": "Palestre, box CrossFit, functional training, allenamento di gruppo.",
        "icon": "speedometer2",
        "search_aliases": "palestra crossfit functional-training fitness allenamento gym",
        "order": 10,
    },
    {
        "slug": "personal-trainer",
        "name": "Personal trainer",
        "category_slug": "fitness",
        "description": "Personal trainer, coach di allenamento one-to-one.",
        "icon": "person-arms-up",
        "search_aliases": "personal-trainer pt coach allenamento-personalizzato one-to-one",
        "order": 20,
    },
    {
        "slug": "yoga-pilates",
        "name": "Yoga & Pilates",
        "category_slug": "fitness",
        "description": "Studi di yoga, pilates reformer, mindfulness, corpo-mente.",
        "icon": "flower2",
        "search_aliases": "yoga pilates reformer mindfulness meditazione corpo-mente",
        "order": 30,
    },
    # ── Construction (3) ──────────────────────────────────────────
    {
        "slug": "architect-studio",
        "name": "Studio di architettura",
        "category_slug": "construction",
        "description": "Studi di architettura, progettazione residenziale e commerciale.",
        "icon": "bounding-box",
        "search_aliases": "architetto studio-architettura progettazione residenziale urbanistica",
        "order": 10,
    },
    {
        "slug": "interior-design",
        "name": "Interior design",
        "category_slug": "construction",
        "description": "Interior designer, home staging, arredamento su misura.",
        "icon": "house-door",
        "search_aliases": "interior-design arredamento home-staging architettura-interni",
        "order": 20,
    },
    {
        "slug": "trades-practical",
        "name": "Imprese & artigiani edili",
        "category_slug": "construction",
        "description": "Imprese edili, idraulici, elettricisti, imbianchini, ristrutturazioni.",
        "icon": "tools",
        "search_aliases": "impresa-edile ristrutturazione idraulico elettricista imbianchino",
        "order": 30,
    },
    # ── Beauty (2) ────────────────────────────────────────────────
    {
        "slug": "salon-hair-barber",
        "name": "Parrucchiere & barber",
        "category_slug": "beauty",
        "description": "Parrucchieri, barber shop, hairstylist indipendenti.",
        "icon": "scissors",
        "search_aliases": "parrucchiere barber hairstylist hair taglio salone",
        "order": 10,
    },
    {
        "slug": "spa-wellness",
        "name": "Spa & wellness",
        "category_slug": "beauty",
        "description": "Spa, centri estetici, wellness resort, trattamenti estetici.",
        "icon": "droplet",
        "search_aliases": "spa wellness centro-estetico estetica massaggi trattamenti-benessere",
        "order": 20,
    },
    # ── Nonprofit (2) ─────────────────────────────────────────────
    {
        "slug": "charity-foundation",
        "name": "Charity & fondazione",
        "category_slug": "nonprofit",
        "description": "Fondazioni, onlus, organizzazioni non-profit con raccolta fondi.",
        "icon": "heart",
        "search_aliases": "onlus fondazione charity ong raccolta-fondi donazioni non-profit",
        "order": 10,
    },
    {
        "slug": "cultural-association",
        "name": "Associazione culturale",
        "category_slug": "nonprofit",
        "description": "Associazioni culturali, enti artistici, realtà del terzo settore.",
        "icon": "bookmark-star",
        "search_aliases": "associazione-culturale cultura ente-artistico terzo-settore arte",
        "order": 20,
    },
]


class Command(BaseCommand):
    help = "Seed the 52 catalog ProfessionCluster rows (idempotent)."

    def handle(self, *args, **options):
        # Step 1 · Ensure the 7 macro-categories required by Wave 2/3
        # clusters exist. Creates inline; does not touch seed_categories.
        extra_cat_created = 0
        for cat_data in EXTRA_CATEGORIES:
            _, created = Category.objects.get_or_create(
                slug=cat_data["slug"],
                defaults=cat_data,
            )
            if created:
                extra_cat_created += 1
                self.stdout.write(f"  Category created: {cat_data['name']}")

        if extra_cat_created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"  ({extra_cat_created} macro-categories added inline.)"
                )
            )

        # Step 2 · Seed the 52 profession clusters.
        cluster_created = 0
        cluster_existing = 0
        missing_categories = set()
        for data in PROFESSION_CLUSTERS:
            try:
                category = Category.objects.get(slug=data["category_slug"])
            except Category.DoesNotExist:
                missing_categories.add(data["category_slug"])
                continue

            _, created = ProfessionCluster.objects.get_or_create(
                slug=data["slug"],
                defaults={
                    "name": data["name"],
                    "category": category,
                    "description": data.get("description", ""),
                    "icon": data.get("icon", ""),
                    "order": data["order"],
                    "is_active": True,
                    "search_aliases": data.get("search_aliases", ""),
                },
            )
            if created:
                cluster_created += 1
                self.stdout.write(f"  Created: {data['name']} ({data['category_slug']})")
            else:
                cluster_existing += 1
                self.stdout.write(f"  Exists:  {data['name']} ({data['category_slug']})")

        if missing_categories:
            self.stdout.write(
                self.style.WARNING(
                    f"\nSkipped clusters for missing categories: "
                    f"{sorted(missing_categories)}"
                )
            )

        self.stdout.write(
            self.style.SUCCESS(
                f"\nDone. {cluster_created} profession clusters created, "
                f"{cluster_existing} already existed. "
                f"Total in DB: {ProfessionCluster.objects.count()}."
            )
        )
