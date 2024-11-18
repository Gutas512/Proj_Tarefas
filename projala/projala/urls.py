from django.contrib import admin
from django.urls import path
from website.views import *

urlpatterns = [

    path('home/', HomePageView.as_view(), name='home'),

    path('usuarios/', lista_usuarios.as_view(), name='usuarios-list'),
    path('tarefas/', lista_tarefas.as_view(), name='tarefas-list'),

    path('usuarios/cadastrar/', UsuarioCreateView.as_view(), name='cadastrar-usuario'),
    path('tarefas/cadastrar/', TarefaCreateView.as_view(), name='cadastrar-tarefa'),

    path('usuarios/editar/<int:pk>/', UsuarioUpdateView.as_view(), name='editar-usuario'),
    path('tarefas/editar/<int:pk>/', TarefaUpdateView.as_view(), name='editar-tarefa'),

    path('usuarios/excluir/<int:pk>/', UsuarioDeleteView.as_view(), name='excluir_usuario'),
    path('tarefas/excluir/<int:pk>/', TarefaDeleteView.as_view(), name='excluir-tarefa'),
]
