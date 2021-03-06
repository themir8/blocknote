from django.contrib import admin
from .models import Article
from simple_history.admin import SimpleHistoryAdmin


class ArticleHistoryAdmin(SimpleHistoryAdmin):
    list_display = ["id", "title", "url"]
    history_list_display = ["url"]
    list_display_links = ('title',)
    search_fields = ['title', 'author__username']

admin.site.register(Article, ArticleHistoryAdmin)
