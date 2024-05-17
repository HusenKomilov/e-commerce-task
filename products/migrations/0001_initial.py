# Generated by Django 4.2.7 on 2024-05-17 16:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_ad", models.DateTimeField(auto_now_add=True)),
                ("updated_ad", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=128, unique=True)),
                ("image", models.ImageField(upload_to="category/")),
                ("slug", models.SlugField(null=True, unique=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_ad", models.DateTimeField(auto_now_add=True)),
                ("updated_ad", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=128)),
                ("slug", models.SlugField(unique=True)),
                ("description", models.TextField()),
                ("width", models.IntegerField()),
                ("height", models.IntegerField()),
                ("length", models.IntegerField()),
                ("weight", models.FloatField()),
                ("quantity", models.IntegerField(default=0)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("discount", models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ("is_new", models.BooleanField(default=False)),
                ("is_hot", models.BooleanField(default=False)),
                ("category", models.ManyToManyField(related_name="categories", to="products.category")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Review",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_ad", models.DateTimeField(auto_now_add=True)),
                ("updated_ad", models.DateTimeField(auto_now=True)),
                ("description", models.TextField()),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="product", to="products.product"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="author_review",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Gallery",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_ad", models.DateTimeField(auto_now_add=True)),
                ("updated_ad", models.DateTimeField(auto_now=True)),
                ("image", models.ImageField(upload_to="products/")),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="images", to="products.product"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="FavouriteProducts",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_ad", models.DateTimeField(auto_now_add=True)),
                ("updated_ad", models.DateTimeField(auto_now=True)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="like", to="products.product"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="user", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]