from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.forms.models import modelform_factory
from ..models import Operacao


OperacaoForm = modelform_factory(Operacao, fields=('__all__'))


def adicionar(request):
    operacoes = Operacao.objects.all()
    
    if request.method == 'POST':
        form = OperacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('operacao_listar'))
    else:
        form = OperacaoForm()
    return render(request, 'operacao/gerenciar.html', {'operacoes': operacoes, 'form': form})


def editar(request, pk):
    operacoes = Operacao.objects.all()
    operacao = Operacao.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = OperacaoForm(request.POST, instance=operacao)
        if form.is_valid():
            form.save()
            return redirect(reverse('operacao_listar'))
    else:
        form = OperacaoForm(instance=operacao)
    return render(request, 'operacao/gerenciar.html', {'operacoes': operacoes, 'operacao': operacao, 'form': form})


def apagar(request, pk):
    operacoes = Operacao.objects.all()
    operacao = Operacao.objects.get(pk=pk)
    
    if request.method == 'POST':
        operacao.delete()
        return redirect(reverse('operacao_listar'))
    return render(request, 'operacao/apagar.html', {'operacoes': operacoes, 'operacao': operacao})


def listar(request):
    operacoes = Operacao.objects.all()
    
    return render(request, 'operacao/listar.html', {'operacoes': operacoes})
