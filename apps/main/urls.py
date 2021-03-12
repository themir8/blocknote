from django.urls import path, include
from main.views import Create, ArticleViewEdit
from main.views import RegisterPage, CustomLoginView, ListView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", RegisterPage.as_view(), name="register"),

    path('', Create, name="index"),
    path('all/', ListView, name="postlist"),
    path('<slug:slug>', ArticleViewEdit, name="article"),
]