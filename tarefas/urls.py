from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tarefas, name='lista_tarefas'),  # URL que renderiza a view de lista de tarefas
]