from django.db import models
from datetime import date

class Livros(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=30)
    co_autor = models.CharField(max_length=30, blank=True)
    data_cadastro = models.DateField(default=date.today)
    empretado = models.BooleanField(default=False)
    nome_emprestado = models.CharField(max_length=30, blank=True, null=True)
    data_emprestimo = models.DateField(blank=True, null=True)
    data_devolucao = models.DateField(blank=True, null=True)
    tempo_duracao = models.DateField(blank=True, null=True)

    class Meta:
        #Para não aparecer livros com 2 s na area administrativa
        verbose_name = 'Livro'

    def __str__(self):
        return self.nome