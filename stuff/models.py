from django.db import models
from django.contrib.postgres.fields import ArrayField


class Companion(models.Model):
    RARITY_CHOICES = [
        ('common', 'Common'),
        ('uncommon', 'Uncommon'),
        ('rare', 'Rare'),
        ('epic', 'Epic'),
        ('legendary', 'Legendary'),
        ('mythic', 'Mythic'),
        ('supreme', 'Supreme'),
    ]
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, blank=True)
    rarity = models.CharField(max_length=10, choices=RARITY_CHOICES)
    base_mp = models.IntegerField()
    types = models.ManyToManyField('Type')
    affected_skill = models.ForeignKey('Skill', on_delete=models.SET_NULL, null=True, blank=True)
    mp_reduc = models.BooleanField(null=True, blank=True)


class Skill(models.Model):
    RARITY_CHOICES = [
        ('common', 'Common'),
        ('uncommon', 'Uncommon'),
        ('rare', 'Rare'),
        ('epic', 'Epic'),
        ('legendary', 'Legendary'),
        ('mythic', 'Mythic'),
        ('supreme', 'Supreme'),
    ]
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, blank=True)
    rarity = models.CharField(max_length=10, choices=RARITY_CHOICES)
    description = models.TextField(max_length=2048)
    types = models.ManyToManyField('Type')
    cooldown = models.FloatField()


class Type(models.Model):
    # ['food', 'plant', 'animal', 'machine', 'dessert', 'chicken', 'hamburger', 'cloud', 'pirate', 'wolf', 'cat', 'magic', 'dragon', 'shark', 'small', 'medium', 'large']
    slug = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.slug


class RuneType(models.Model):
    RUNE_TYPES = [
        'increase_crit_percent',  # ["percentage"],
        'atk_boost',  # ["percentage"],
        'fish_dmg_boost',  # ["percentage"],
        'boss_dmg',  # ["percentage"],
        'crit_dmg_boost',  # ["percentage"],
        'triple_shot',  # ["percentage"],
        'double_shot',  # ["percentage"],
        'increase_all_dmg_per_companion_type',  # ["percentage", "companion_type"],
        'increase_skill_type_dmg_per_companion_type',  # ["percentage", "type"],
        'reduce_mp_for_companion_type_and_rarity',  # ["mp_reduction", "type", "rarity"],
        'increase_skill_rarity_dmg_per_companion_rarity',  # ["percentage", "skill_rarity", "companion_rarity"],
        'increase_final_dmg_after_skill',  # ["percentage", "duration", "skill_type"],
        'increase_deal_ratio_per_companion_type',  # ["percentage", "type"],
        'increase_crit_dmg_boost_per_companion_type',  # ["percentage", "type"],
        'increase_crit_dmg_per_companion_type',  # ["percentage", "type"],
        'increase_max_mp',  # ["mp_increase"]
    ]
    name = models.CharField(max_length=80, unique=True)
    values_required = ArrayField(models.CharField(max_length=100), default=list)

    def __str__(self) -> str:
        return self.name


class SubRune(models.Model):
    RARITY_CHOICES = [
        ('uncommon', 'Uncommon'),
        ('rare', 'Rare'),
        ('epic', 'Epic'),
        ('legendary', 'Legendary'),
        ('mythic', 'Mythic'),
        ('supreme', 'Supreme'),
    ]
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255, blank=True)
    rarity = models.CharField(max_length=10, choices=RARITY_CHOICES)
    description = models.TextField(max_length=2048)
    type = models.ForeignKey(RuneType, on_delete=models.SET_NULL, related_name='runes', null=True, blank=True)
    values = ArrayField(models.CharField(max_length=100), default=list, blank=True)


class MainRune(models.Model):
    RARITY_CHOICES = [
        ('uncommon', 'Uncommon'),
        ('rare', 'Rare'),
        ('epic', 'Epic'),
        ('legendary', 'Legendary'),
        ('mythic', 'Mythic'),
        ('supreme', 'Supreme'),
    ]
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255, blank=True)
    rarity = models.CharField(max_length=10, choices=RARITY_CHOICES)
    description = models.TextField(max_length=2048)
