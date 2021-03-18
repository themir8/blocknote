from django.contrib import admin
from .models import Article, GroupArticles
from simple_history.admin import SimpleHistoryAdmin


class ArticleHistoryAdmin(SimpleHistoryAdmin):
    list_display = ["id", "title", "url"]
    history_list_display = ["url"]
    list_display_links = ('title',)
    search_fields = ['title', 'author__username']


@admin.register(GroupArticles)
class GroupArticlesAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'author')
	list_display_links = ('name',)
	search_fields = ('name',)
	readonly_fields = ('slug', 'created_date')
	save_as = True


admin.site.register(Article, ArticleHistoryAdmin)
