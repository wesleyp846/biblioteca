from django.contrib import admin
from .models import Livros

# registrando na area administrativa a tabela livro (model livros)
admin.site.register(Livros)