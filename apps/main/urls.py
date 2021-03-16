from django.urls import path, include
from main.views import ArticleCreate, ArticleDetail
from main.views import RegisterPage, CustomLoginView, ArticleList, ArticleViewEdit
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", RegisterPage.as_view(), name="register"),

    path('', ArticleCreate.as_view(), name="index"),
    path('all/', ArticleList.as_view(), name="postlist"),
    path('<slug:slug>', ArticleViewEdit, name="article"),
]