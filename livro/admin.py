from django.contrib import admin
from .models import Livros, Categoria

# registrando na area administrativa a tabela livro (model livros)
admin.site.register(Livros)
admin.site.register(Categoria)