from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.forms.models import modelform_factory
from ..models import Operacao
from ..models import Pessoa
from ..models import Lancamento


def listar(request, pk):
    if request.method == 'POST':
        form = LancamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('financeiro/lancamento_listar', kwargs={'pk': pk}))
    else:
        form = LancamentoForm()

    lancamentos = Lancamento.objects.filter(lancamento_id=pk)
    operacoes = Operacao.objects.all()
    return render(request, 'financeiro/lancamento/listar.html',
                  {'lancamentos': lancamentos, 'operacoes': operacoes,
                   'lancamento_id': pk, 'form': form})


LancamentoForm = modelform_factory(Lancamento, fields=('__all__'))


def listarpessoa(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'financeiro/lancamento/listarpessoa.html', {'pessoas': pessoas})


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
