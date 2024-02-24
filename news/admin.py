from django.contrib import admin

from .models import News


class NewsAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_display = (
        "slug",
        "title",
        "body",
        "created_at",
        "type",
        "author"
    )


admin.site.register(News, NewsAdmin)
