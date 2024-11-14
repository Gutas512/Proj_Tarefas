from django.db import models

class tbl_usuarios(models.Model):
    usu_name = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    usu_codigo = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )
    usu_email = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.usu_name


class tbl_tarefas(models.Model):
    tar_codigo = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )
    tar_descricao = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    tar_setor = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    tar_prioridade = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    tar_status = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    tar_data = models.DateField()

    usu_codigo = models.ForeignKey(
        tbl_usuarios,
        on_delete=models.CASCADE
    )

tarefas = models.Manager()