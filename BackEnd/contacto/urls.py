from django.urls import path
from .views import contacto_view, gracias_view

urlpatterns = [
    path('', contacto_view, name='contacto'),
        path('gracias/', gracias_view, name='gracias'),
]