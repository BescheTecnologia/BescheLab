from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.forms.models import modelform_factory
from ..models import Pessoa
from ..models import PessoaFisica
from ..models import Endereco
from ..models import Complemento


PessoaForm = modelform_factory(Pessoa, fields=('__all__'))
PessoaFisicaForm = modelform_factory(PessoaFisica, fields=('__all__'))
EnderecoForm = modelform_factory(Endereco, fields=('__all__'))
ComplementoForm = modelform_factory(Complemento, fields=('__all__'))


def adicionar(request):
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
    return render(request, 'financeiro/pessoa/gerenciar.html', {'formp': formp, 'formpf': formpf, 'forme': forme, 'formc': formc})


def editar(request, pk):
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
    return render(request, 'financeiro/pessoa/gerenciar.html', {'formp': formp, 'formpf': formpf, 'forme': forme, 'formc': formc})


def listar(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'financeiro/pessoa/listar.html', {'pessoas': pessoas})


def apagar(request, pk):
    pessoa = Pessoa.objects.get(pk=pk)
    if request.method == 'POST':
        pessoa.delete()
        return redirect(reverse('pessoa_listar'))
    return render(request, 'financeiro/pessoa/apagar.html', {'pessoa': pessoa})
