from django.contrib import admin
from .models import Article, Profile


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'url')
	list_display_links = ('title',)
	search_fields = ('title',)
	save_as = True

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	list_display = ('id', 'user', 'location')
	list_display_links = ('user',)
	# search_fields = ('title',)
	save_as = True