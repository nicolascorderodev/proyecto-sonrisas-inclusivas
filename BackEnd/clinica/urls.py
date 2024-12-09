from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('contacto/', include('contacto.urls')),
    path('api/', include('contacto.urls')),
]