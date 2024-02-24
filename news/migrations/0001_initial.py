# Generated by Django 4.2.10 on 2024-02-24 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="News",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("slug", models.SlugField(max_length=255, unique=True)),
                ("title", models.CharField(max_length=255)),
                ("body", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("website", "Website News"),
                            ("game", "Game News"),
                            ("discord", "Discord News"),
                            ("guides", "Guides"),
                            ("other", "Other"),
                        ],
                        max_length=50,
                    ),
                ),
                ("author", models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]