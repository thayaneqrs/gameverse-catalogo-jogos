
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_jogos, name='listar_jogos'),
]
