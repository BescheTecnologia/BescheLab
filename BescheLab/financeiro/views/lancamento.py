from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.forms.models import modelform_factory
from ..models import Operacao
from ..models import Pessoa
from ..models import Lancamento


LancamentoForm = modelform_factory(Lancamento, fields=('__all__'))


def listar(request, pk):
    lancamentos = Lancamento.objects.filter(id=pk)
    return render(request, 'financeiro/lancamento/listar.html', {'lancamentos': lancamentos})


def listarpessoa(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'financeiro/lancamento/listarpessoa.html', {'pessoas': pessoas})


def adicionar(request):
    if request.method == 'POST':
        form = LancamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('lancamento_listar'))
    else:
        form = LancamentoForm()
    operacoes = Operacao.objects.all()
    return render(request, 'financeiro/lancamento/adicionar.html', {'operacoes': operacoes, 'form': form})


def detalhar(request, pk):
    lancamento = Lancamento.objects.get(pk=pk)
    return render(request, 'financeiro/lancamento/detalhar.html', {'lancamento': lancamento})


def editar(request, pk):
    lancamento = Lancamento.objects.get(pk=pk)
    if request.method == 'POST':
        form = LancamentoForm(request.POST, instance=lancamento)
        if form.is_valid():
            form.save()
            return redirect(reverse('lancamento_listar'))
    else:
        form = LancamentoForm(instance=lancamento)
    return render(request, 'financeiro/lancamento/editar.html', {'form': form})


def apagar(request, pk):
    lancamento = Lancamento.objects.get(pk=pk)
    if request.method == 'POST':
        lancamento.delete()
        return redirect(reverse('lancamento_listar'))
    return render(request, 'financeiro/lancamento/apagar.html', {'lancamento': lancamento})
