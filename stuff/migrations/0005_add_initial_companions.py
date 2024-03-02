from django.db import migrations


def create_companions(apps, schema_editor):
    Type = apps.get_model('stuff', 'Type')
    Companion = apps.get_model('stuff', 'Companion')

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

    companions_data = [
        {'name': "Sausage", 'rarity': "uncommon", 'base_mp': 1, 'types': ['small', 'food']},
        {'name': "Sunny", 'rarity': "uncommon", 'base_mp': 1, 'types': ['small', 'food']},
        {'name': "Bread", 'rarity': "uncommon", 'base_mp': 1, 'types': ['small', 'food']},
        {'name': "Cracker", 'rarity': "uncommon", 'base_mp': 2, 'types': ['small', 'food', 'dessert']},
        {'name': "Pudding", 'rarity': "uncommon", 'base_mp': 2, 'types': ['small', 'food', 'dessert']},
        {'name': "Cake", 'rarity': "uncommon", 'base_mp': 2, 'types': ['small', 'food', 'dessert']},

        {'name': "Tamago", 'rarity': "rare", 'base_mp': 3, 'types': ['small', 'food']},
        {'name': "Carrot", 'rarity': "rare", 'base_mp': 3, 'types': ['small', 'plant']},
        {'name': "Clover", 'rarity': "rare", 'base_mp': 3, 'types': ['small', 'plant']},
        {'name': "Trunk", 'rarity': "rare", 'base_mp': 3, 'types': ['small', 'plant']},
        {'name': "Takoyaki", 'rarity': "rare", 'base_mp': 3, 'types': ['small', 'food']},
        {'name': "Chick", 'rarity': "rare", 'base_mp': 3, 'types': ['small', 'animal', 'chicken']},
        {'name': "Burger", 'rarity': "rare", 'base_mp': 3, 'types': ['small', 'food', 'hamburger']},

        {'name': "Jackdolf", 'rarity': "epic", 'base_mp': 4, 'types': ['small', 'pirate', 'animal', 'wolf']},
        {'name': "Mouse", 'rarity': "epic", 'base_mp': 4, 'types': ['small', 'machine']},
        {'name': "Pingu", 'rarity': "epic", 'base_mp': 4, 'types': ['small', 'animal']},
        {'name': "Ghost Cat", 'rarity': "epic", 'base_mp': 4, 'types': ['small', 'animal', 'cat']},
        {'name': "Bunny", 'rarity': "epic", 'base_mp': 4, 'types': ['small', 'animal', 'magic']},
        {'name': "Fire Chick", 'rarity': "epic", 'base_mp': 4, 'types': ['small', 'animal', 'chicken']},
        {'name': "Tulip", 'rarity': "epic", 'base_mp': 4, 'types': ['small', 'plant']},
        {'name': "Phoenix", 'rarity': "epic", 'base_mp': 4, 'types': ['small', 'animal', 'chicken']},
        {'name': "Lightree", 'rarity': "epic", 'base_mp': 4, 'types': ['small', 'plant']},
        {'name': "Whopper", 'rarity': "epic", 'base_mp': 4, 'types': ['small', 'food', 'hamburger']},
        {'name': "Drake", 'rarity': "epic", 'base_mp': 4, 'types': ['small', 'animal', 'dragon']},
        {'name': "Spark", 'rarity': "epic", 'base_mp': 4, 'types': ['small', 'animal', 'dragon']},
        {'name': "Cookie Knight", 'rarity': "epic", 'base_mp': 4, 'types': ['small', 'food', 'dessert', 'magic']},
        {'name': "Pumpky", 'rarity': "epic", 'base_mp': 4, 'types': ['small', 'plant', 'magic']},
        {'name': "Steel Fin", 'rarity': "epic", 'base_mp': 4, 'types': ['small', 'machine', 'pirate', 'shark']},
        {'name': "Angry Bomb", 'rarity': "epic", 'base_mp': 4, 'types': ['small', 'machine']},
        {'name': "Devil Cat", 'rarity': "epic", 'base_mp': 4, 'types': ['small', 'animal', 'cat']},
        {'name': "Bro", 'rarity': "epic", 'base_mp': 4, 'types': ['small', 'animal', 'cat']},
        {'name': "Sparrow", 'rarity': "epic", 'base_mp': 4, 'types': ['small', 'animal']},

        {'name': "Cat Black", 'rarity': "legendary", 'base_mp': 6, 'types': ['medium', 'cat', 'machine']},
        {'name': "Jack Striker", 'rarity': "legendary", 'base_mp': 8, 'types': ['large', 'pirate', 'animal', 'shark']},
        {'name': "Werewolf", 'rarity': "legendary", 'base_mp': 8, 'types': ['large', 'wolf', 'animal']},
        {'name': "Grom", 'rarity': "legendary", 'base_mp': 8, 'types': ['small', 'animal', 'wolf']},
        {'name': "Lulu", 'rarity': "legendary", 'base_mp': 8, 'types': ['large', 'animal', 'cat', 'cloud', 'magic']},
        {'name': "Roro", 'rarity': "legendary", 'base_mp': 6, 'types': ['medium', 'animal', 'cat', 'cloud', 'magic']},
        {'name': "Jack Tiger", 'rarity': "legendary", 'base_mp': 6, 'types': ['medium', 'pirate', 'animal', 'cat']},
        {'name': "Jack Jaws", 'rarity': "legendary", 'base_mp': 6, 'types': ['medium', 'pirate', 'shark', 'machine']},
        {'name': "Jack Fly", 'rarity': "legendary", 'base_mp': 6, 'types': ['medium', 'pirate', 'dragon', 'magic']},
        {'name': "War Wolf", 'rarity': "legendary", 'base_mp': 6, 'types': ['medium', 'machine', 'wolf']},
        {'name': "Jackdaw", 'rarity': "legendary", 'base_mp': 8, 'types': ['large', 'animal', 'pirate']},
        {'name': "Tanker", 'rarity': "legendary", 'base_mp': 8, 'types': ['large', 'machine', 'cat']},

        {'name': "Oracle", 'rarity': "mythic", 'base_mp': 12, 'types': ['large', 'animal', 'cat', 'cloud', 'magic']},
        {'name': "Captain Specter", 'rarity': "mythic", 'base_mp': 12, 'types': ['large', 'pirate']},
    ]

    for i, companion in enumerate(companions_data):
        companion['id'] = i

    for companion_data in companions_data:
        companion, created = Companion.objects.get_or_create(
            id=companion_data["id"],
            name=companion_data['name'],
            rarity=companion_data['rarity'],
            base_mp=companion_data['base_mp'],
        )
        for type_slug in companion_data['types']:
            companion_type = Type.objects.get(slug=type_slug)
            companion.types.add(companion_type)


class Migration(migrations.Migration):

    dependencies = [
        ("stuff", "0004_add_initial_skills"),
    ]

    operations = [
        migrations.RunPython(create_companions),
    ]
