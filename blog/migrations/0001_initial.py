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
            name="Contact",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_ad", models.DateTimeField(auto_now_add=True)),
                ("updated_ad", models.DateTimeField(auto_now=True)),
                ("full_name", models.CharField(max_length=128)),
                ("email", models.EmailField(max_length=254)),
                ("message", models.TextField()),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Mail",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_ad", models.DateTimeField(auto_now_add=True)),
                ("updated_ad", models.DateTimeField(auto_now=True)),
                ("email", models.EmailField(max_length=254)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_ad", models.DateTimeField(auto_now_add=True)),
                ("updated_ad", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=256)),
                ("main_photo", models.ImageField(upload_to="posts/")),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="author", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="PostGallery",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_ad", models.DateTimeField(auto_now_add=True)),
                ("updated_ad", models.DateTimeField(auto_now=True)),
                ("image", models.ImageField(upload_to="post/")),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="blog", to="blog.post"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
