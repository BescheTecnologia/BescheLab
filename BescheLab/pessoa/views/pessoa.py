from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.forms.models import modelform_factory
from ..models import Pessoa
from ..models import PessoaFisica
from ..models import Endereco
from ..models import Complemento
from ...financeiro.models import Operacao


PessoaForm = modelform_factory(Pessoa, fields=('__all__'))
PessoaFisicaForm = modelform_factory(PessoaFisica, fields=('__all__'))
EnderecoForm = modelform_factory(Endereco, fields=('__all__'))
ComplementoForm = modelform_factory(Complemento, fields=('__all__'))


def adicionar(request):
    operacoes = Operacao.objects.all()
    enderecos = Endereco.objects.all()
    
    if request.method == 'POST':
        formp = PessoaForm(request.POST)
        formpf = PessoaFisicaForm(request.POST)
        forme = EnderecoForm(request.POST) 
        formc = ComplementoForm(request.POST)
        
        if formp.is_valid() & formpf.is_valid() & forme.is_valid() & formc.is_valid():
            p = formp.save()
            e = forme.save()
            
            instancia = formpf.save(commit=False) 
            instancia.pessoa = p
            instancia.save()
            
            instancia = formc.save(commit=False)
            instancia.pessoa = p
            instancia.endereco = e
            instancia.save()
            return redirect(reverse('pessoa_listar'))
    else:
        formp = PessoaForm()
        formpf = PessoaFisicaForm()
        forme = EnderecoForm()
        formc = ComplementoForm()
    return render(request, 'gerenciar.html', 
                  {'operacoes': operacoes, 'formp': formp, 'formpf': formpf, 'forme': forme, 'formc': formc, 'enderecos': enderecos})


def editar(request, pk):
    operacoes = Operacao.objects.all()
    pfisica = PessoaFisica.objects.get(pessoa_id=pk)
    complemento = Complemento.objects.get(pessoa_id=pk)
    
    if request.method == 'POST':
        formp = PessoaForm(request.POST, instance=pfisica.pessoa)
        formpf = PessoaFisicaForm(request.POST, instance=pfisica)
        forme = EnderecoForm(request.POST, instance=complemento.endereco)
        formc = ComplementoForm(request.POST, instance=complemento)
        
        if formp.is_valid() & formpf.is_valid() & forme.is_valid() & formc.is_valid():
            p = formp.save()
            e = forme.save()
            
            instancia = formpf.save(commit=False) 
            instancia.pessoa = p
            instancia.save()
            
            instancia = formc.save(commit=False)
            instancia.pessoa = p
            instancia.endereco = e
            instancia.save()
            return redirect(reverse('pessoa_listar'))
    else:
        formp = PessoaForm(instance=pfisica.pessoa)
        formpf = PessoaFisicaForm(instance=pfisica)
        forme = EnderecoForm(instance=complemento.endereco)
        formc = ComplementoForm(instance=complemento)
    return render(request, 'gerenciar.html', {'operacoes': operacoes, 'formp': formp, 'formpf': formpf, 'forme': forme, 'formc': formc})


def apagar(request, pk):
    operacoes = Operacao.objects.all()
    pessoa = Pessoa.objects.get(pk=pk)
    
    if request.method == 'POST':
        pessoa.delete()
        return redirect(reverse('pessoa_listar'))
    return render(request, 'apagar.html', {'operacoes': operacoes, 'pessoa': pessoa})


def listar(request):
    operacoes = Operacao.objects.all()
    pessoas = Pessoa.objects.all()
    
    return render(request, 'listar.html', {'operacoes': operacoes, 'pessoas': pessoas})
