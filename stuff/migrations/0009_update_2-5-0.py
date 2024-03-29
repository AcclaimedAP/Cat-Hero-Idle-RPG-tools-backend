# Generated by Django 4.2.10 on 2024-03-21 07:56

from django.db import migrations


def update(apps, schema_editor):
    Companion = apps.get_model('stuff', 'Companion')
    Skill = apps.get_model('stuff', 'Skill')
    MainRune = apps.get_model('stuff', 'MainRune')
    Type = apps.get_model('stuff', 'Type')

    wolf_type, _ = Type.objects.get_or_create(slug='wolf')
    large_type, _ = Type.objects.get_or_create(slug='large')
    animal_type, _ = Type.objects.get_or_create(slug='animal')

    fenrir, _ = Companion.objects.get_or_create(
        name="Fenrir",
        slug='fenrir',
        rarity="mythic",
        base_mp=12,
    )
    fenrir.types.add(large_type, animal_type, wolf_type)
    fenrir.save()

    wild_nature_skill, _ = Skill.objects.get_or_create(
        name='Wild Nature',
        slug='wild-nature',
        rarity='mythic',
        description='Increases Wolf CRIT chance by 5% per Wolf companion equipped for 8s. The Wolf CRIT deals 3000% damage of the original CRIT DMG',
        cooldown=100.0,
    )
    wild_nature_skill.types.add(wolf_type)
    wild_nature_skill.save()

    wild_nature_rune, _ = MainRune.objects.get_or_create(
        name="Wild Nature Enhanced",
        slug="wild-nature-enhanced",
        rarity="mythic",
        description="Increases the Wolf Crit DMG of Wild Nature by 5000%.",
    )

    try:
        companion = Companion.objects.get(slug='angry-bomb')
        companion.name = 'Angry Wolf'
        companion.slug = 'angry-wolf'
        companion.types.add(wolf_type)
        companion.save()
    except Companion.DoesNotExist:
        pass

    try:
        skill = Skill.objects.get(slug='cat-heros')
        skill.slug = 'cat-heroes'
        skill.save()
    except Skill.DoesNotExist:
        pass


class Migration(migrations.Migration):

    dependencies = [
        ("stuff", "0008_update_slugs"),
    ]

    operations = [
        migrations.RunPython(update),
    ]
