from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaSocios, name='lista-socios'),
]
