from django import forms
from projala.models import *

class usuarioForm(forms.ModelForm):
    class Meta:
        model = tbl_usuarios
        fields = ['usu_name',
                  'usu_email'
        ]

class tarefasForm(forms.ModelForm):
    class Meta:
        model = tbl_tarefas
        fields = [
                  'tar_descricao',
                  'tar_setor',
                  'tar_prioridade',
                  'tar_status',
                  'tar_data',
                  'usu_codigo'
        ]
