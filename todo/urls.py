from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='todo'),
    path('vista/<int:id>', views.vista, name='vista_todo'),
    path('editar/<int:id>', views.editar, name='editar_todo'),
    path('crear/', views.crear, name='crear_todo'),
    path('borrar/<int:id>', views.borrar, name= 'borrar_todo'),
]
