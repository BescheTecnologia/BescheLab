from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.forms.models import modelform_factory
from ..models import Pessoa


def listar(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'financeiro/pessoa/listar.html', {'pessoas': pessoas})


def detalhar(request, pk):
    pessoa = Pessoa.objects.get(pk=pk)
    return render(request, 'financeiro/pessoa/detalhar.html', {'pessoa': pessoa})


PessoaForm = modelform_factory(Pessoa, fields=('__all__'))


def adicionar(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('pessoa_listar'))
    else:
        form = PessoaForm()
    return render(request, 'financeiro/pessoa/adicionar.html', {'form': form})


def editar(request, pk):
    pessoa = Pessoa.objects.get(pk=pk)
    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return redirect(reverse('pessoa_listar'))
    else:
        form = PessoaForm(instance=pessoa)
    return render(request, 'financeiro/pessoa/editar.html', {'form': form})


def apagar(request, pk):
    pessoa = Pessoa.objects.get(pk=pk)
    if request.method == 'POST':
        pessoa.delete()
        return redirect(reverse('pessoa_listar'))
    return render(request, 'financeiro/pessoa/apagar.html', {'pessoa': pessoa})
