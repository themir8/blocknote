from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('main.urls')),
    path('todo/', include('todoapp.urls'), name="todo"),
    path('admin/', admin.site.urls),
    path('editorjs/', include('django_editorjs_fields.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
