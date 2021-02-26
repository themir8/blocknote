from django.urls import path, include
from main.views import Create, ArticleViewEdit
from main.views import Registration, LoginView



urlpatterns = [
    path('', Create, name="index"),
    path('<slug:slug>', ArticleViewEdit, name="article"),
    path("signup/", Registration),
    path("login/", LoginView),
]