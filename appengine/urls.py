from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('main.urls')),
    path('todo/', include('todoapp.urls'), name="todo"),
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
]
