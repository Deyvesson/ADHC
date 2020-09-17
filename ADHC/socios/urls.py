from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaSocios, name='lista-socios'),
    path('socio/<int:id>', views.socioView, name="socio-View"),
    path('novosocio/', views.novoSocio, name='novo-socio'),
    path('edit/<int:id>', views.editSocio, name="edit-socio"),
    path('delete/<int:id>', views.deleteSocio, name="delete-socio")
]
