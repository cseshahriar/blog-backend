from django.contrib import admin  # noqa
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_active', )
    list_display_links = ('title', )
    list_filter = ('is_active', 'created_user')
    search_fields = ('title', )
