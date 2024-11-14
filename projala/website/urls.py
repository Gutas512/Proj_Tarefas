from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projala/', include('projala.urls')),  # Inclui as URLs do app projala
]
