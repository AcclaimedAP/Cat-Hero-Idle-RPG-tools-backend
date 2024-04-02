from django.db import migrations


def add_companion_skill_cooldown(apps, schema_editor):
    Companion = apps.get_model('stuff', 'Companion')
    Skill = apps.get_model('stuff', 'Skill')
    companions_skill_cooldown = {
        "sausage": ("dinner-time", {11: 20, 31: 40, 51: 60}),
        "bread": ("dinner-time", {11: 20, 31: 40, 51: 60}),
        "tamago": ("dinner-time", {21: 30, 51: 60, 81: 90}),
        "carrot": ("leaf-slash", {11: 30, 41: 60, 71: 90}),
        "clover": ("leaf-slash", {11: 30, 41: 60, 71: 90}),
        "trunk": ("leaf-slash", {21: 30, 51: 60, 81: 90}),
        "takoyaki": ("dinner-time", {21: 30, 51: 60, 81: 90}),
        "chick": ("chicken-run", {11: 30, 41: 60, 71: 90}),
        "mouse": ("rat-bomb", {11: 30, 51: 45, 91: 60}),
        "pingu": ("icy-thorns", {21: 30, 61: 45, 101: 60}),
        "ghost-cat": ("super-cat", {11: 30, 51: 45, 91: 60}),
        "bunny": ("magic-circus", {11: 30, 51: 45, 91: 60}),
        "tulip": ("magic-shield", {21: 30, 61: 45, 101: 60}),
        "whopper": ("burger-party", {31: 30, 71: 45, 111: 60}),
        "drake": ("tornado", {21: 30, 61: 45, 101: 60}),
        "spark": ("scratch", {31: 30, 71: 45, 111: 60}),
        "cookie-knight": ("magic-crossbow", {11: 30, 51: 45, 91: 60}),
        "pumpky": ("chakra", {11: 30, 51: 45, 91: 60}),
        "steel-fin": ("cluster-bomb", {21: 30, 61: 45, 101: 60}),
        "angry-bomb": ("grrrrrr", {21: 15, 61: 30, 101: 50}),
        "devil-cat": ("catteor", {21: 30, 61: 45, 101: 60}),
        "bro": ("fish-rain", {21: 30, 61: 45, 101: 60}),
        "sparrow": ("scarecrow", {21: 30, 61: 45, 101: 60}),
        "jack-striker": ("oceans-punishment", {21: 50, 61: 75, 101: 90}),
        "grom": ("howl", {21: 30, 61: 60, 101: 90}),
        "lulu": ("cat-heroes", {11: 50, 51: 75, 91: 90}),
        "jack-tiger": ("pirate-sign", {11: 50, 51: 75, 91: 90}),
        "jack-fly": ("nocturne-summon", {11: 50, 51: 75, 91: 90}),
        "war-wolf": ("full-moon", {31: 30, 71: 60, 111: 80}),
        "jackdaw": ("dreadnought-whale", {11: 50, 51: 75, 91: 90}),
        "tanker": ("cat-laser", {11: 50, 51: 75, 91: 90}),
        "captain-specter": ("bombshell-rain", {21: 30, 61: 60, 101: 90}),
        "fenrir": ("wild-nature", {21: 30, 61: 60, 101: 90}),
    }

    for companion_slug, (skill_slug, cooldown) in companions_skill_cooldown.items():
        skill = Skill.objects.get(slug=skill_slug)
        Companion.objects.filter(slug=companion_slug).update(affected_skill=skill, cooldown_per_level=cooldown)


class Migration(migrations.Migration):

    dependencies = [
        ("stuff", "0010_update_companion_fields"),
    ]

    operations = [
        migrations.RunPython(add_companion_skill_cooldown),
    ]
