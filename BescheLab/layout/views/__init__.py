from django.shortcuts import render
from ...financeiro.models import Operacao


def index(request):    
    operacoes = Operacao.objects.all()
    return render(request, 'index.html', {'operacoes': operacoes})
