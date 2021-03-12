from django.urls import path, include
from main.views import Create, ArticleViewEdit
from main.views import RegisterPage, CustomLoginView, ListView



urlpatterns = [
    path('', Create, name="index"),
    path('all/', ListView, name="postlist"),
    path('<slug:slug>', ArticleViewEdit, name="article"),
    path("register/", RegisterPage.as_view()),
    path("login/", CustomLoginView.as_view()),
]