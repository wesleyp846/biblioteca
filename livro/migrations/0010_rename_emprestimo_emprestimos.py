# Generated by Django 5.0 on 2023-12-31 00:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0009_remove_emprestimo_tempo_duracao'),
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Emprestimo',
            new_name='Emprestimos',
        ),
    ]
