from django.urls import path, include
from main.views import (
	RegisterPage, 
	CustomLoginView, 
	ArticleList, 
	ArticleViewEdit,
	ArticleCreate,
    PublicGroupList,
	GroupList,
    GroupDetail
	)
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", RegisterPage.as_view(), name="register"),

    path('', ArticleCreate.as_view(), name="index"),
    path('all/', ArticleList.as_view(), name="postlist"),
    path('post/<slug:slug>', ArticleViewEdit, name="article"),

    path('group/', GroupList.as_view(), name="privategrouplist"),
    path('groups/', PublicGroupList.as_view(), name="publicgrouplist"),
    path('groups/<slug:slug>/', GroupDetail.as_view(), name="groupdetail"),
]