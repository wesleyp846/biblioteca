# Generated by Django 5.0 on 2023-12-30 23:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0006_remove_livros_data_devolucao_and_more'),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emprestimo',
            name='nome_emprestado_anonimo',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='nome_emprestado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.usuario'),
        ),
    ]