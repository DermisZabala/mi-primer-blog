from django.urls import path
from . import views

urlpatterns = [
    path('', views.listas_publicaciones, name='listas_publicaciones'),
    path('post/<int:pk>/', views.detalle_publicacion, name='detalle_publicacion'),
]