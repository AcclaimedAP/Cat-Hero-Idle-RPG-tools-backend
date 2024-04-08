from django.contrib import admin

from .models import ExchangeTrade


class ExchangeTradeAdmin(admin.ModelAdmin):
    search_fields = ["exchange_uuid"]
    list_display = (
        "exchange_uuid",
        "price",
        "listing_time",
        "gear_type",
        "rarity",
        "level",
        "exchange_left",
        "durability"
    )


admin.site.register(ExchangeTrade, ExchangeTradeAdmin)
