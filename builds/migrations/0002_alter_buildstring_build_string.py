# Generated by Django 5.0.2 on 2024-02-20 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builds', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buildstring',
            name='build_string',
            field=models.CharField(max_length=9000),
        ),
    ]
