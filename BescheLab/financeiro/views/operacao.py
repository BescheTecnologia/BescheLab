from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.forms.models import modelform_factory
from ..models import Operacao


def listar(request):
    operacoes = Operacao.objects.all()
    return render(request, 'financeiro/operacao/listar.html', {'operacoes': operacoes})


def detalhar(request, pk):
    operacao = Operacao.objects.get(pk=pk)
    return render(request, 'financeiro/operacao/detalhar.html', {'operacao': operacao})


OperacaoForm = modelform_factory(Operacao, fields=('__all__'))


def adicionar(request):
    if request.method == 'POST':
        form = OperacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('operacao_listar'))
    else:
        form = OperacaoForm()
    return render(request, 'financeiro/operacao/adicionar.html', {'form': form})


def editar(request, pk):
    operacao = Operacao.objects.get(pk=pk)
    if request.method == 'POST':
        form = OperacaoForm(request.POST, instance=operacao)
        if form.is_valid():
            form.save()
            return redirect(reverse('operacao_listar'))
    else:
        form = OperacaoForm(instance=operacao)
    return render(request, 'financeiro/operacao/editar.html', {'form': form})


def apagar(request, pk):
    operacao = Operacao.objects.get(pk=pk)
    if request.method == 'POST':
        operacao.delete()
        return redirect(reverse('operacao_listar'))
    return render(request, 'financeiro/operacao/apagar.html', {'operacao': operacao})
