from django.db import models


class ExchangeTrade(models.Model):
    TYPE_CHOICES = [
        ('shoes', 'Shoes'),
        ('gloves', 'Gloves'),
        ('hat', 'Hat'),
        ('scarf', 'Scarf'),
    ]

    RARITY_CHOICES = [
        ('common', 'Common'),
        ('uncommon', 'Uncommon'),
        ('rare', 'Rare'),
        ('epic', 'Epic'),
        ('legendary', 'Legendary'),
    ]
    exchange_uuid = models.UUIDField(unique=True, primary_key=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    listing_time = models.DateTimeField()
    rarity = models.CharField(max_length=50, choices=RARITY_CHOICES)
    gear_type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    level = models.IntegerField(default=0)
    exchange_left = models.IntegerField(default=0)
    durability = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.gear_type} - {self.level} - {self.price}"
