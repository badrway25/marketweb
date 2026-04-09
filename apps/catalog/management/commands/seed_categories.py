from django.core.management.base import BaseCommand

from apps.catalog.models import Category

MVP_CATEGORIES = [
    {
        "name": "Agency",
        "slug": "agency",
        "description": "Siti web per agenzie digitali e creative. Layout dinamici con portfolio interattivo e sezioni case study.",
        "icon": "megaphone",
        "order": 1,
    },
    {
        "name": "Business",
        "slug": "business",
        "description": "Siti web per aziende e corporate. Sezioni servizi, team, partnership e modulo contatto avanzato.",
        "icon": "building",
        "order": 2,
    },
    {
        "name": "Ristorante",
        "slug": "restaurant",
        "description": "Siti web per ristoranti, bar e food delivery. Menu digitale, prenotazione tavoli e galleria fotografica.",
        "icon": "cup-hot",
        "order": 3,
    },
    {
        "name": "Medico",
        "slug": "medical",
        "description": "Siti web per cliniche, studi medici e professionisti sanitari. Prenotazione online e area paziente.",
        "icon": "heart-pulse",
        "order": 4,
    },
    {
        "name": "Avvocato",
        "slug": "lawyer",
        "description": "Siti web per studi legali e avvocati. Aree di pratica, profili avvocati e consulenza online.",
        "icon": "briefcase",
        "order": 5,
    },
    {
        "name": "Immobiliare",
        "slug": "real-estate",
        "description": "Siti web per agenzie immobiliari e annunci. Ricerca immobili, schede proprietà e tour virtuali.",
        "icon": "house-door",
        "order": 6,
    },
    {
        "name": "Portfolio",
        "slug": "portfolio",
        "description": "Siti web portfolio per freelancer, designer e fotografi. Galleria filtrata e integrazione social.",
        "icon": "palette",
        "order": 7,
    },
    {
        "name": "eCommerce",
        "slug": "ecommerce",
        "description": "Siti web per negozi online e vetrine prodotti. Catalogo, carrello e checkout integrato.",
        "icon": "cart3",
        "order": 8,
    },
]


class Command(BaseCommand):
    help = "Seed the database with the 8 MVP marketplace categories"

    def handle(self, *args, **options):
        created_count = 0
        for cat_data in MVP_CATEGORIES:
            _, created = Category.objects.get_or_create(
                slug=cat_data["slug"],
                defaults=cat_data,
            )
            if created:
                created_count += 1
                self.stdout.write(f"  Created: {cat_data['name']}")
            else:
                self.stdout.write(f"  Exists:  {cat_data['name']}")

        self.stdout.write(
            self.style.SUCCESS(f"\nDone. {created_count} categories created.")
        )
