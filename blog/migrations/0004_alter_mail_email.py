# Generated by Django 4.2.7 on 2024-05-17 19:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0003_post_main_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mail",
            name="email",
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]