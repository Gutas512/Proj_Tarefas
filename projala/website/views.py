from django.shortcuts import render
from projala.models import *
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, TemplateView
from projala.forms import *
from django.urls import reverse_lazy

# Create your views here.

class lista_usuarios(ListView):
    model = tbl_usuarios
    template_name = 'usuarios_list.html'
    context_object_name = 'usuarios'


class lista_tarefas(ListView):
    model = tbl_tarefas
    template_name = 'tarefas_list.html'
    context_object_name = 'tarefas'

class UsuarioCreateView(CreateView):
    model = tbl_usuarios
    form_class = usuarioForm
    template_name = 'cadastrar_usuario.html'
    success_url = reverse_lazy('usuarios-list')


class TarefaCreateView(CreateView):
    model = tbl_tarefas
    form_class = tarefasForm
    template_name = 'cadastrar_tarefas.html'
    success_url = reverse_lazy('tarefas-list')
class UsuarioUpdateView(UpdateView):
    model = tbl_usuarios
    form_class = usuarioForm
    template_name = 'editar_usuario.html'
    success_url = reverse_lazy('usuarios-list')

class TarefaUpdateView(UpdateView):
    model = tbl_tarefas
    form_class = tarefasForm
    template_name = 'editar_tarefa.html'
    success_url = reverse_lazy('tarefas-list')
class UsuarioDeleteView(DeleteView):
    model = tbl_usuarios
    template_name = 'excluir_usuario.html'
    success_url = reverse_lazy('usuarios-list')

class TarefaDeleteView(DeleteView):
    model = tbl_tarefas
    template_name = 'excluir_tarefa.html'
    success_url = reverse_lazy('tarefas-list')

class HomePageView(TemplateView):
    template_name = 'home.html'

class TarefasPageView(TemplateView):
    template_name = 'Tarefas.html'