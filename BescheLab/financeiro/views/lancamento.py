from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.forms.models import modelform_factory
from ..models import Operacao
from ..models import Pessoa
from ..models import Lancamento


def listar(request, operacao):
    if request.method == 'POST':
        form = LancamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('financeiro/lancamento_listar', {'pessoa': pessoa, 'operacao': operacao}))
    else:
        form = LancamentoForm()

    lancamentos = Lancamento.objects.filter(pessoa_id=pessoa)
    return render(request, 'financeiro/lancamento/listar.html',
                  {'lancamentos': lancamentos, 'form': form})


LancamentoForm = modelform_factory(Lancamento, fields=('__all__'))


def listarpessoa(request, operacao):
    pessoas = Pessoa.objects.all()
    return render(request, 'financeiro/lancamento/listarpessoa.html', {'pessoas': pessoas, 'operacao': operacao})


def adicionar(request, pessoa, operacao):
    if request.method == 'POST':
        form = LancamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('lancamento_listar', {'pessoa': pessoa, 'operacao': operacao}))
    else:
        form = LancamentoForm()
    return render(request, 'financeiro/lancamento/adicionar.html', {'form': form})


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
