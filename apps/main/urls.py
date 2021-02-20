from django.urls import path, include
from main.views import Create, ArticleViewEdit


urlpatterns = [
    path('', Create, name="index"),
    path('<slug:slug>', ArticleViewEdit, name="article"),
]