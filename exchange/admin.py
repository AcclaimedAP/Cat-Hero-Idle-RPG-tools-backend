from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import ExchangeTrade


class RarityFilter(admin.SimpleListFilter):
    title = _('rarity')
    parameter_name = 'rarity'

    def lookups(self, request, model_admin):
        return ExchangeTrade.RARITY_CHOICES

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(rarity=self.value())


class GearTypeFilter(admin.SimpleListFilter):
    title = _('gear type')
    parameter_name = 'gear_type'

    def lookups(self, request, model_admin):
        return ExchangeTrade.TYPE_CHOICES

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(gear_type=self.value())


class LevelFilter(admin.SimpleListFilter):
    title = _('level')
    parameter_name = 'level'

    def lookups(self, request, model_admin):
        levels = set([c.level for c in model_admin.model.objects.all()])
        return [(level, str(level)) for level in levels]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(level=self.value())


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
    list_filter = (
        RarityFilter,
        GearTypeFilter,
        LevelFilter,
        'exchange_left',
        'durability',
    )
    ordering = ("price",)


admin.site.register(ExchangeTrade, ExchangeTradeAdmin)
