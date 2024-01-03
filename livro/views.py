from django.shortcuts import render, redirect
from usuarios.models import Usuario
from django.http import HttpResponse
from .models import Livros, Emprestimos

def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id=request.session['usuario'])
        livros = Livros.objects.filter(usuario=usuario)            
        return render(request, 'home.html', {'livros': livros, 'usuario_logado': request.session.get('usuario')})
    else:
        return redirect('/auth/login/?status=2')
    
def ver_livros(request, id):
    if request.session.get('usuario'):
        livros = Livros.objects.get(id=id)
        if request.session.get('usuario') == livros.usuario.id:
            emprestimos = Emprestimos.objects.filter(livro=livros)
            return render(request, 'ver_livro.html', {'livro': livros, 'emprestimos': emprestimos, 'usuario_logado': request.session.get('usuario')})
        else:
            return HttpResponse('Esse livro não é seu')
    else:
        return redirect('/auth/login/?status=2')