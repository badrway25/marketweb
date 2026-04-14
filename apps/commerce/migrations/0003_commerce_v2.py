"""Commerce v2 — Session 45 (Phase 3b).

Adds:
- Storefront.translations JSONField (locale-keyed overrides)
- Collection.translations, Product.translations, ShippingMethod.translations
- Stripe as a PaymentProvider choice
- StorefrontMember (merchant scoping)
"""
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("commerce", "0002_alter_order_fulfillment_status_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="storefront",
            name="translations",
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AddField(
            model_name="collection",
            name="translations",
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AddField(
            model_name="product",
            name="translations",
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AddField(
            model_name="shippingmethod",
            name="translations",
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AlterField(
            model_name="storefront",
            name="payment_provider",
            field=models.CharField(
                choices=[
                    ("stub", "Stub · auto-conferma (dev)"),
                    ("offline_bank_transfer", "Bonifico bancario"),
                    ("stripe", "Stripe"),
                ],
                default="stub",
                max_length=40,
            ),
        ),
        migrations.CreateModel(
            name="StorefrontMember",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("role", models.CharField(
                    choices=[("owner", "Owner"), ("editor", "Editor")],
                    default="owner",
                    max_length=20,
                )),
                ("storefront", models.ForeignKey(
                    on_delete=models.deletion.CASCADE,
                    related_name="members",
                    to="commerce.storefront",
                )),
                ("user", models.ForeignKey(
                    on_delete=models.deletion.CASCADE,
                    related_name="storefront_memberships",
                    to=settings.AUTH_USER_MODEL,
                )),
            ],
            options={
                "ordering": ["storefront__template__name"],
                "unique_together": {("storefront", "user")},
            },
        ),
    ]
