from django.contrib import admin
from .models import ApiKey


class ApiKeyAdmin(admin.ModelAdmin):
    list_display = ('user', 'id', 'usage_count', 'usable')
    search_fields = ('user',)
    readonly_fields = ('id',)


admin.site.register(ApiKey, ApiKeyAdmin)
