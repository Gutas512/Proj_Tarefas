# Generated by Django 5.1.2 on 2024-11-07 23:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usu_name', models.CharField(max_length=100)),
                ('usu_codigo', models.IntegerField(default=0)),
                ('usu_email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='tbl_tarefas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tar_codigo', models.IntegerField(default=0)),
                ('tar_descricao', models.CharField(max_length=100)),
                ('tar_setor', models.CharField(max_length=100)),
                ('tar_prioridade', models.CharField(max_length=100)),
                ('tar_status', models.CharField(max_length=100)),
                ('tar_data', models.DateField()),
                ('usu_codigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projala.tbl_usuarios')),
            ],
        ),
    ]
