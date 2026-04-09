from django.core.management.base import BaseCommand

from apps.catalog.models import Category

MVP_CATEGORIES = [
    {
        "name": "Agency",
        "slug": "agency",
        "description": "Siti web per agenzie digitali e creative",
        "icon": "bi-rocket-takeoff",
        "order": 1,
    },
    {
        "name": "Business",
        "slug": "business",
        "description": "Siti web per aziende e corporate",
        "icon": "bi-briefcase",
        "order": 2,
    },
    {
        "name": "Restaurant",
        "slug": "restaurant",
        "description": "Siti web per ristoranti, bar e food delivery",
        "icon": "bi-cup-hot",
        "order": 3,
    },
    {
        "name": "Medical",
        "slug": "medical",
        "description": "Siti web per cliniche, studi medici e professionisti sanitari",
        "icon": "bi-heart-pulse",
        "order": 4,
    },
    {
        "name": "Lawyer",
        "slug": "lawyer",
        "description": "Siti web per studi legali e avvocati",
        "icon": "bi-shield-check",
        "order": 5,
    },
    {
        "name": "Real Estate",
        "slug": "real-estate",
        "description": "Siti web per agenzie immobiliari e annunci",
        "icon": "bi-house-door",
        "order": 6,
    },
    {
        "name": "Portfolio",
        "slug": "portfolio",
        "description": "Siti web portfolio per freelancer, designer e fotografi",
        "icon": "bi-palette",
        "order": 7,
    },
    {
        "name": "eCommerce",
        "slug": "ecommerce",
        "description": "Siti web per negozi online e vetrine prodotti",
        "icon": "bi-cart3",
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
