from django.urls import path
from . import views

urlpatterns = [
    path('', views.listas_publicaciones, name='listas_publicaciones'),
    path('post/<int:pk>/', views.detalle_publicacion, name='detalle_publicacion'),
    path('sobre-mi/', views.sobre_mi, name='sobre_mi'),
    path('inicio-sesion/', views.inicio_sesion, name='inicio_sesion'),
    path('registro/', views.registro, name='registro'),
    path('contacto/', views.contacto, name='contacto'),
]