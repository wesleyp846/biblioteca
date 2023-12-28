from django.contrib import admin
#inclidu foi importado para dar a responsabilidade de urls para a pasta da aplicação
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #o include redireciona para urls do app livro
    path('livro/', include('livro.urls')),
    path('auth/', include('usuarios.urls')),
]
