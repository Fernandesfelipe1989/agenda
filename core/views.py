from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from core.models import Evento


def consultaevento(resquest, titulo_evento ):
    descricao = Evento.objects.get(titulo=titulo_evento)
    return HttpResponse('<h1>O local do evento será: {}</h1>'.format(descricao.local))


def lista_eventos(request):
    # usuario = request.user
    # evento = Evento.objects.filter(usuario=usuario)
    evento = Evento.objects.all()
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)
# def index(request):
#     return redirect('/agenda/')
