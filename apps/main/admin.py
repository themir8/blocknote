from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'url')
	list_display_links = ('title',)
	search_fields = ('title',)
	save_as = True