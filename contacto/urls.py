from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='contacto'),
    path('<letra>', views.inicio, name= 'contacto'),
    path('vista/<int:id>', views.vista, name='vista_contacto'),
    path('editar/<int:id>', views.editar, name='editar_contacto'),
    path('crear/', views.crear, name='crear_contacto'),
    path('eliminar/<int:id>', views.borrar, name='borrar_contacto'),
]
