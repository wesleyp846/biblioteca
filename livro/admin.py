from django.contrib import admin
from .models import Livros, Categoria, Emprestimos

# registrando na area administrativa a tabela livro (model livros)
admin.site.register(Livros)
admin.site.register(Categoria)
admin.site.register(Emprestimos)