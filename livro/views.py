from django.shortcuts import render, redirect
from usuarios.models import Usuario
from django.http import HttpResponse

def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id=request.session['usuario']).nome              
        return HttpResponse(f'ola {usuario}')
    else:
        return redirect('/auth/login/?status=2')
    