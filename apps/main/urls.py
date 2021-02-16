from django.urls import path, include
from main.views import MainView


urlpatterns = [
    path('', MainView.as_view(), name="index"),
]