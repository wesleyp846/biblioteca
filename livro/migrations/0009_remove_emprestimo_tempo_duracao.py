# Generated by Django 5.0 on 2023-12-30 23:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0008_alter_emprestimo_nome_emprestado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emprestimo',
            name='tempo_duracao',
        ),
    ]
