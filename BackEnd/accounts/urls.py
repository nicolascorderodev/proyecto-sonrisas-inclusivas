from django.urls import path
from . import views
from django.contrib.auth import views as auth_views  # Importar vistas de autenticación

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin_page/', views.admin_page, name='admin_page'),
    path('auxadmin_page/', views.auxadmin_page, name='auxadmin_page'),
    path('dentista_page/', views.dentista_page, name='dentista_page'),
    path('paciente_page/', views.paciente_page, name='paciente_page'),
]