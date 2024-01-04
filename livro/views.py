from django.shortcuts import render, redirect
from usuarios.models import Usuario
from django.http import HttpResponse
from .models import Livros, Emprestimos
from .forms import CadastroLivro

def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id=request.session['usuario'])
        livros = Livros.objects.filter(usuario=usuario)
        form= CadastroLivro()            
        return render(request, 'home.html', {'livros': livros, 'usuario_logado': request.session.get('usuario'), 'form': form})
    else:
        return redirect('/auth/login/?status=2')
    
def ver_livros(request, id):
    if request.session.get('usuario'):
        livros = Livros.objects.get(id=id)
        if request.session.get('usuario') == livros.usuario.id:
            emprestimos = Emprestimos.objects.filter(livro=livros)
            form= CadastroLivro() 
            return render(request, 'ver_livro.html', {'livro': livros, 'emprestimos': emprestimos, 'usuario_logado': request.session.get('usuario'), 'form': form})
        else:
            return HttpResponse('Esse livro não é seu')
    else:
        return redirect('/auth/login/?status=2')
    
def cadastrar_livro(request):
    # Só permite ao formulario navegar por essa url, digitando na barra de endereço  ele proibe
    if request.method == 'POST':
        # Recebe os dados do formulario
        form = CadastroLivro(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse('Cadastrado com sucesso')
        else:
            return HttpResponse('Erro ao cadastrar')
