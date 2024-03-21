from django.contrib import admin

from .models import BuildModel


class BuildModelAdmin(admin.ModelAdmin):
    search_fields = ["id"]
    list_display = (
        "id",
        "build",
        "created",
        "last_accessed",
    )


admin.site.register(BuildModel, BuildModelAdmin)
