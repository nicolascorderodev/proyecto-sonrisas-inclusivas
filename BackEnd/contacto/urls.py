from django.urls import path
from .views import contacto_view, gracias_view, ContactoListCreate, ContactoDetail

urlpatterns = [
    path('', contacto_view, name='contacto'),
    path('gracias/', gracias_view, name='gracias'),
    path('contactos/', ContactoListCreate.as_view(), name='contacto-list-create'),
    path('contactos/<int:pk>/', ContactoDetail.as_view(), name='contacto-detail'),
]