# Generated by Django 4.2.10 on 2024-03-05 20:49

from django.db import migrations


def add_main_runes(apps, schema_editor):
    MainRune = apps.get_model('stuff', 'MainRune')

    runes_data = [
        {"name": "Leaf Slash Enhanced", "slug": "leaf-slash-enhanced", "rarity": "uncommon", "description": "Enhances Leaf Slash increasing Skill DMG by 50 % and area of effect."},
        {"name": "Magic Circus Enhanced", "slug": "magic-circus-enhanced", "rarity": "uncommon", "description": "Enhances Magic Circus to increase the shoot speed per second by 100 %."},
        {"name": "Random Uncommon Skill", "slug": "random-uncommon-skill", "rarity": "uncommon", "description": "Casts Uncommon skill that is equipped in the skill slot every 15 seconds."},
        {"name": "Rat Bomb Enhanced", "slug": "rat-bomb-enhanced", "rarity": "uncommon", "description": "Enhances Rat Bomb to expand the explosion range while increasing Skill DMG by 50 %."},
        {"name": "Cluster Bomb Enhanced", "slug": "cluster-bomb-enhanced", "rarity": "uncommon", "description": "Enhances Cluster Bomb to expand the explosion range while increasing Skill DMG by 50 %."},
        {"name": "Scraaatch Enhanced", "slug": "scraaatch-enhanced", "rarity": "uncommon", "description": "Enhances Scraaatch to kill the target immediately when its HP is lower than 10%."},
        {"name": "Grrrrrrr! Enhanced", "slug": "grrrrrrr-enhanced", "rarity": "uncommon", "description": "Enhances Grrrrrrr! to increase the duration by 5 seconds."},
        {"name": "Dessert Coma Enhanced", "slug": "dessert-coma-enhanced", "rarity": "uncommon", "description": "Enhances Dessert Coma increasing Skill DMG by 50%."},
        {"name": "Dinner Time Enhanced", "slug": "dinner-time-enhanced", "rarity": "uncommon", "description": "Enhances Dinner Time increasing Skill DMG by 50%."},
        {"name": "Icy Thorns Enhanced", "slug": "icy-thorns-enhanced", "rarity": "uncommon", "description": "Enhances Icy Thorns to shoot 2 orbs."},
        {"name": "Super Cat Enhanced-II", "slug": "super-cat-enhanced-ii", "rarity": "uncommon", "description": "Enhances Super Cat to bounce 1 times."},
        {"name": "Black Cloud Enhanced", "slug": "black-cloud-enhanced", "rarity": "rare", "description": "Summons extra 1 Black Cloud upon casting Black Cloud."},
        {"name": "Magic Shield Enhanced", "slug": "magic-shield-enhanced", "rarity": "rare", "description": "Enhances Magic Shield to become immune to attacks by 30% chance."},
        {"name": "Tornado Enhanced", "slug": "tornado-enhanced", "rarity": "rare", "description": "Enhances Tornado to increase DMG by 100%."},
        {"name": "Cluster Bomb Enhanced", "slug": "cluster-bomb-enhanced", "rarity": "rare", "description": "Enhances Cluster Bomb to expand the explosion range while increasing Skill DMG by 150%."},
        {"name": "Chakra Enhanced", "slug": "chakra-enhanced", "rarity": "rare", "description": "Enhances Chakra to give an electric shock to the hit target by 20% chance increasing received DMG by 30% for 5 seconds."},
        {"name": "Dinner Time Enhanced", "slug": "dinner-time-enhanced", "rarity": "rare", "description": "Enhances Dinner Time to summon extra 8 food missiles dealing 150% damage of Skill DMG."},
        {"name": "Chicken Run Enhanced", "slug": "chicken-run-enhanced", "rarity": "rare", "description": "Enhances Chicken Run to summon extra 3 while increasing Skill DMG by 70%."},
        {"name": "Random Rare Skill", "slug": "random-rare-skill", "rarity": "rare", "description": "Casts Rare skill that is equipped in the skill slot every 15 seconds."},
        {"name": "Super Cat Enhanced-II", "slug": "super-cat-enhanced-ii", "rarity": "rare", "description": "Enhances Super Cat to bounce 2 times."},
        {"name": "Rat Bomb Enhanced", "slug": "rat-bomb-enhanced", "rarity": "rare", "description": "Enhances Rat Bomb to summon extra 3 while increasing Skill DMG by 100%."},
        {"name": "Super Cat Enhanced-I", "slug": "super-cat-enhanced-i", "rarity": "rare", "description": "Enhances Super Cat to summon extra 3 while increasing Skill DMG by 70%."},
        {"name": "Fish Rain Enhanced", "slug": "fish-rain-enhanced", "rarity": "rare", "description": "Enhances Fish Rain to shoot extra 8 red fish dealing 150% of Skill DMG."},
        {"name": "Scarecrow Enhanced", "slug": "scarecrow-enhanced", "rarity": "rare", "description": "Enhances Scarecrow to explode at the end of the skill duration dealing 20% of Max HP of enemies in the area. (N/A for Boss)"},
        {"name": "Dessert Coma Enhanced", "slug": "dessert-coma-enhanced", "rarity": "rare", "description": "Enhances Dessert Coma to summon extra cookies dealing 500% damage of Skill DMG."},
        {"name": "Random Epic Skill", "slug": "random-epic-skill", "rarity": "epic", "description": "Casts Epic skill that is equipped in the skill slot every 15 seconds."},
        {"name": "Full Moon Enhanced", "slug": "full-moon-enhanced", "rarity": "epic", "description": "Enhances Full Moon to increase the enlargement duration by 5 seconds."},
        {"name": "Catteor Enhanced", "slug": "catteor-enhanced", "rarity": "epic", "description": "Enhances Catteor to drop an extra huge meteorite dealing 1,000% of Skill DMG."},
        {"name": "Black Cloud Enhanced", "slug": "black-cloud-enhanced", "rarity": "epic", "description": "Enhances Black Cloud increasing Skill DMG by 300% and the skill duration by 5 seconds."},
        {"name": "Howl Enhanced", "slug": "howl-enhanced", "rarity": "epic", "description": "Enhances Howl to increase the duration by 5 seconds."},
        {"name": "Cat Laser Enhanced", "slug": "cat-laser-enhanced", "rarity": "epic", "description": "Enhances Cat Laser increasing Skill DMG by 500%."},
        {"name": "Magic Crossbow Enhanced", "slug": "magic-crossbow-enhanced", "rarity": "epic", "description": "Enhances Magic Crossbow to increase DMG by 500%."},
        {"name": "Burger Party Enhanced", "slug": "burger-party-enhanced", "rarity": "epic", "description": "Enhances Burger Party to shoot an electronic patty by 10% chance. A target hit by the electronic patty receives an electric shock with received DMG increased by 30% for 5 seconds."},
        {"name": "Random Legendary Skill", "slug": "random-legendary-skill", "rarity": "legendary", "description": "Casts Legendary skill that is equipped in the skill slot every 15 seconds."},
        {"name": "Claw Punch Enhanced", "slug": "claw-punch-enhanced", "rarity": "legendary", "description": "Enhances Claw Punch to deal wide AoE DMG and increase Skill DMG by 1,000%."},
        {"name": "Shaman Cat Enhanced", "slug": "shaman-cat-enhanced", "rarity": "legendary", "description": "Summons 2 times as many red clouds, increasing hit speed by 2 times."},
        {"name": "Bombshell Rain Enhanced", "slug": "bombshell-rain-enhanced", "rarity": "legendary", "description": "Increases the number of bombshells of Bombshell Rain by 5 and increase Skill DMG by 1,000%."},
        {"name": "Cloud Enhanced", "slug": "cloud-enhanced", "rarity": "legendary", "description": "Increases the duration of Cloud type skills by 5s and the Skill DMG of Cloud type skill by 1,000%."},
        {"name": "Black Hole Enhanced", "slug": "black-hole-enhanced", "rarity": "legendary", "description": "Enhances Black Hole to create an electric shock wave upon casting the skill. The electric shock wave deals 2,000% of ATK and gives an electric shock increasing the received DMG by 500% for 5 seconds."},
        {"name": "Dreadnought Whale Enhanced", "slug": "dreadnought-whale-enhanced", "rarity": "legendary", "description": "Enhances Dreadnought Whale to fire missiles to the front in succession. A missile deals 1,000% of the Skill DMG."},
        {"name": "Pirate x2", "slug": "pirate-x2", "rarity": "legendary", "description": "Activates one more time at a 30% chance when casting a Pirate type skill. Skill DMG of a recurrent Skill increases by 500%."},
        {"name": "Summon Cat Laser", "slug": "summon-cat-laser", "rarity": "legendary", "description": "Casts a bonus Cat Laser by a 30 % chance upon casting a Cat type skill. Increases the CRIT DMG of the bonus Cat Laser by 500 %."},
        {"name": "Cat Electric Shock", "slug": "cat-electric-shock", "rarity": "legendary", "description": "Gives an electric shock by 10 % chance upon hitting an enemy with Cat type skills increasing DMG received by the target by 500 % for 5 seconds."},
        {"name": "Shaman Cat Enhanced 2", "slug": "shaman-cat-enhanced-2", "rarity": "mythic", "description": "Increases the extra DMG of Shaman Cat by 5,000 %."},
        {"name": "Cat Heroes Enhanced", "slug": "cat-heroes-enhanced", "rarity": "mythic", "description": "Enhances Cat Heroes to increase extra DMG by 5,000 %."},
        {"name": "Guardian Angel", "slug": "guardian-angel", "rarity": "mythic", "description": "Resurrects upon death. Increases final DMG by 5,000 % for 5s after the resurrection."},
        {"name": "Ocean's Punishment Enhanced", "slug": "oceans-punishment-enhanced", "rarity": "mythic", "description": "Reduces the DMG dealt by the target with a Shark Sign by 50 %. Increases DMG dealt to the target with a Shark Sign by 5,000 %."},
        {"name": "Bombshell Rain Enhanced 2", "slug": "bombshell-rain-enhanced-2", "rarity": "mythic", "description": "Increases the extra DMG of Bombshell Rain by 5,000 %."}
    ]

    for rune_data in runes_data:
        MainRune.objects.create(**rune_data)


class Migration(migrations.Migration):

    dependencies = [
        ("stuff", "0006_mainrune_subrune_companion_slug_skill_slug_and_more"),
    ]

    operations = [
        migrations.RunPython(add_main_runes),
    ]
