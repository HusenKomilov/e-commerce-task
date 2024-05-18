# Generated by Django 4.2.7 on 2024-05-17 23:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0009_customer"),
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="author_review", to="users.customer"
            ),
        ),
    ]
