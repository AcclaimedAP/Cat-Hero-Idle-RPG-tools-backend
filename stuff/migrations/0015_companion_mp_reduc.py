# Generated by Django 5.0.9 on 2024-09-25 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stuff", "0014_alter_subrune_type_alter_subrune_values"),
    ]

    operations = [
        migrations.AddField(
            model_name="companion",
            name="mp_reduc",
            field=models.BooleanField(blank=True, null=True),
        ),
    ]