from django.db import migrations, models


def create_skills(apps, schema_editor):
    Type = apps.get_model('stuff', 'Type')
    Skill = apps.get_model('stuff', 'Skill')

    # Types
    types_data = [
        {'slug': 'food'}, {'slug': 'plant'}, {'slug': 'animal'}, {'slug': 'machine'},
        {'slug': 'dessert'}, {'slug': 'chicken'}, {'slug': 'hamburger'}, {'slug': 'pirate'},
        {'slug': 'wolf'}, {'slug': 'cat'}, {'slug': 'cloud'}, {'slug': 'magic'},
        {'slug': 'dragon'}, {'slug': 'shark'}, {'slug': 'small'}, {'slug': 'medium'},
        {'slug': 'large'}
    ]
    for type_data in types_data:
        Type.objects.get_or_create(slug=type_data['slug'])

    skills_data = [
        {'name': "Dinner Time", 'rarity': "common", 'description': "Summons 8 food missiles that deal value1% of ATK.", 'cooldown': 20.0, 'types': ['food']},
        {'name': "Rat Bomb", 'rarity': "common", 'description': "Summons a rat bomb that explodes soon dealing AoE DMG of 85% of ATK.", 'cooldown': 13.0, 'types': ['machine']},
        {'name': 'Super Cat', 'rarity': 'common', 'description': 'Flies a super cat dealing 178% of ATK.', 'cooldown': 13.0, 'types': ['cat']},
        {'name': 'Magic Circus', 'rarity': 'common', 'description': 'Throws a ball 2 times a second for 4s that deals 53% of ATK.', 'cooldown': 13.0, 'types': ['magic']},
        {'name': 'Dessert Coma', 'rarity': 'uncommon', 'description': 'Drops 5 desserts dealing 45% of ATK on every enemy hit.', 'cooldown': 20.0, 'types': ['food', 'dessert']},
        {'name': 'Leaf Slash', 'rarity': 'uncommon', 'description': 'Deals AoE DMG of 14% of ATK on a straight line.', 'cooldown': 10.0, 'types': ['plant']},
        {'name': 'Icy Thorns', 'rarity': 'uncommon', 'description': 'Summons a spinning snowflake scattering icy thorns that deal 18% of ATK.', 'cooldown': 20.0, 'types': ['magic']},
        {'name': 'Scratch', 'rarity': 'uncommon', 'description': 'Scratches the surface dealing 32% of ATK for 12 times.', 'cooldown': 13, 'types': ['cat', 'dragon']},
        {'name': 'Grrrrrr', 'rarity': 'uncommon', 'description': 'Increases ASPD by 40% for 5s. Grrrrrr! effect stacks.', 'cooldown': 30.0, 'types': ['wolf']},
        {'name': 'Cluster Bomb', 'rarity': 'uncommon', 'description': 'Shoots a cluster bomb dealing AoE DMG of 107% of ATK.', 'cooldown': 13.0, 'types': ['machine', 'pirate', 'shark']},
        {'name': 'Fish Rain', 'rarity': 'rare', 'description': 'Summons 12 fish missiles that deal 60% of ATK.', 'cooldown': 20.0, 'types': ['animal']},
        {'name': 'Scarecrow', 'rarity': 'rare', 'description': 'Summons a scarecrow dealing AoE DMG of 7% of ATK each second for 3s and adds a terror effect to increase DMG to enemies by 50% for 2s.', 'cooldown': 38.0, 'types': []},
        {'name': 'Tornado', 'rarity': 'rare', 'description': 'Forms a tornado for 5s that deals AoE DMG of 13% of ATK 4 times a second.', 'cooldown': 25.0, 'types': ['magic']},
        {'name': 'Magic Shield', 'rarity': 'rare', 'description': 'Decreases received DMG by 30% for 13s.', 'cooldown': 25.0, 'types': ['magic']},
        {'name': 'Chicken Run', 'rarity': 'rare', 'description': 'Summons 3 chickens that explode soon dealing AoE DMG of 79% of ATK.', 'cooldown': 20.0, 'types': ['chicken', 'machine']},
        {'name': 'Chakra', 'rarity': 'rare', 'description': 'Deals AoE DMG of 45% of ATK and drags the enemies to the center.', 'cooldown': 20.0, 'types': ['magic']},
        {'name': 'Howl', 'rarity': 'epic', 'description': 'Increases Skill DMG by 300% for 5s.', 'cooldown': 30.0, 'types': ['wolf']},
        {'name': 'Black Cloud', 'rarity': 'epic', 'description': 'Summons a black cloud for 3s and blasts a Penetrating Bolt dealing 200% of ATK upon tapping the screen to attack.', 'cooldown': 15.0, 'types': ['cloud', 'magic']},
        {'name': 'Spray Ink', 'rarity': 'epic', 'description': 'Summons Pirate Octopus and sprays ink to deal 1000% AoE DMG and blind enemies, decreasing the targets\' ATK by 40% for 8s.', 'cooldown': 24.0, 'types': ['pirate']},
        {'name': 'Burger Party', 'rarity': 'epic', 'description': 'Throws burger ingredients 2 times a second for 4s that deals 350% of ATK.', 'cooldown': 38.0, 'types': ['hamburger', 'food']},
        {'name': 'Magic Crossbow', 'rarity': 'epic', 'description': 'Summons a magic crossbow for 5s that shoots a penetrating arrow 5 times a second dealing 240% of ATK.', 'cooldown': 60.0, 'types': ['magic']},
        {'name': 'Full Moon', 'rarity': 'epic', 'description': 'Enlarges the cat hero for 5s, throwing extra 6 moon fish with basic attack that deal 80% of ATK.', 'cooldown': 60.0, 'types': ['wolf', 'magic']},
        {'name': 'Catteor', 'rarity': 'epic', 'description': 'Drops 15 Cat meteors dealing 600% of ATK on every enemy hit.', 'cooldown': 50.0, 'types': ['cat', 'magic']},
        {'name': 'Cat Laser', 'rarity': 'epic', 'description': 'Summons a robot cat that beams laser out for 10s dealing AoE DMG of 400% of ATK 3 times a second.', 'cooldown': 60.0, 'types': ['cat', 'machine']},
        {'name': 'Claw Punch', 'rarity': 'legendary', 'description': 'Scratches the enemy with wolf claws dealing 1500% damage for 2 times.', 'cooldown': 13.0, 'types': ['wolf']},
        {'name': 'Pirate Sign', 'rarity': 'legendary', 'description': 'Summons Pirate Cat and leaves a Pirate Sign on all enemies. The sign bursts and deals 300% extra DMG when enemies with the sign attack with a Cat or Pirate type skill.', 'cooldown': 18.75, 'types': ['cat', 'pirate']},
        {'name': 'Nocturne Summon', 'rarity': 'legendary', 'description': 'Summons Nocturne dealing AoE DMG of 3000% of ATK and adds a Terror effect to increase DMG received by the targets by 50% for 5s.', 'cooldown': 75.0, 'types': ['dragon', 'pirate']},
        {'name': 'Black Hole', 'rarity': 'legendary', 'description': 'Creates a black hole for 5s that drags the enemies to the front and deals AoE DMG of 300% of ATK 2 times a second.', 'cooldown': 15.0, 'types': ['magic']},
        {'name': 'Dreadnought Whale', 'rarity': 'legendary', 'description': 'Summons a dreadnought whale that moves forward dealing AoE DMG of 1200% of ATK 3 times a second.', 'cooldown': 75.0, 'types': ['machine', 'pirate']},
        {'name': 'Bombshell Rain', 'rarity': 'mythic', 'description': 'Pours down several bombshells from the sky. The skill lasts for 20s showering 5 bombshells per second. Each bombshell deals 60000% DMG to the enemy.', 'cooldown': 100.0, 'types': ['machine']},
        {'name': 'Shaman Cat', 'rarity': 'mythic', 'description': 'Summons a shaman cat. The shaman cat summons 3 clouds that strike red lightning. The clouds last for 10s, dealing DMG of 4 times the second. The red lightning deals 200% of DMG at an area at first attack, and the DMG increases by 200% every attack.', 'cooldown': 100.0, 'types': ['magic', 'cat', 'cloud']},
        {'name': 'Cat Heroes', 'rarity': 'mythic', 'description': 'Opens a door in the sky for 10s, and uses an enhanced skill additionally upon casting a Cat type skill of legendary grade and under. The enhanced skill deals extra DMG of 2000% of the original skill DMG.', 'cooldown': 100.0, 'types': ['cat', 'magic', 'cloud']},
        {'name': 'Ocean\'s Punishment', 'rarity': 'mythic', 'description': 'Leaves a Shark Sign on all enemies. The sign stores the DMG received by the target. Deals 3000% of ATK after the sign, and then additionally deals 1500% DMG stored in the sign.', 'cooldown': 40.0, 'types': ['shark', 'pirate']}
    ]

    for skill_data in skills_data:
        skill, created = Skill.objects.get_or_create(
            name=skill_data['name'],
            rarity=skill_data['rarity'],
            description=skill_data['description'],
            cooldown=skill_data['cooldown']
        )
        for type_slug in skill_data['types']:
            skill_type = Type.objects.get(slug=type_slug)
            skill.types.add(skill_type)


class Migration(migrations.Migration):

    dependencies = [
        ("stuff", "0003_add_initial_rune_types"),
    ]

    operations = [
        migrations.RunPython(create_skills),
    ]
