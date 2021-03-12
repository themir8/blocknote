from django.urls import path, include
from main.views import Create, ArticleViewEdit
from main.views import RegisterPage, CustomLoginView, ListView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("login/", CustomLoginView.as_view()),
    path("logout/", LogoutView.as_view()),
    path("register/", RegisterPage.as_view()),

    path('', Create, name="index"),
    path('all/', ListView, name="postlist"),
    path('<slug:slug>', ArticleViewEdit, name="article"),
]