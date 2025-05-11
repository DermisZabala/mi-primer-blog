from django.urls import path
from . import views

urlpatterns = [
    path('inicio-sesion/', views.inicio_sesion, name='login'),
    path('registrarse/', views.registro, name='registro'),
    path('cerrar-sesion/', views.cierre, name='logout'),
]