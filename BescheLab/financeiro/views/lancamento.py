from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.forms.models import modelform_factory
from ..models import Operacao
from ..models import Pessoa
from ..models import Lancamento
from ..models import Pagamento


LancamentoForm = modelform_factory(Lancamento, fields=('__all__'))
PagamentoForm = modelform_factory(Pagamento, fields=('__all__'))


def adicionar(request, operacao):
    operacoes = Operacao.objects.all()
    lancamentos = Lancamento.objects.all()
    pessoas = Pessoa.objects.all()
    operacao = Operacao.objects.get(tipo=operacao)
    
    if request.method == 'POST':
        forml = LancamentoForm(request.POST)
        
        if forml.is_valid():
            l = forml.save(commit=False)
            l.tipo = operacao
            l.pessoa = Pessoa.objects.get(pk=1)
            l.save()
        
            if(l.parcelado==True):
                for i in range(l.n_parcelas):
                    p = Pagamento(lancamento=l, parcela=(i+1), valor=l.valor/l.n_parcelas, pago=False)
                    p.save()
            else:
                p = Pagamento(lancamento=l, parcela=0, valor=l.valor, pago=False)
                p.save()
            #return redirect(reverse('pessoa_listar'))
    else:
        forml = LancamentoForm()
    return render(request, 'lancamento/gerenciar.html', 
                  {'operacoes': operacoes, 'operacao': operacao, 'lancamentos': lancamentos, 'pessoas': pessoas})


def detalhar(request, pk):
    operacoes = Operacao.objects.all()
    lancamento = Lancamento.objects.get(pk=pk)
    return render(request, 'lancamento/detalhar.html', {'operacoes': operacoes, 'lancamento': lancamento})


def editar(request, pk):
    operacoes = Operacao.objects.all()
    lancamento = Lancamento.objects.get(pk=pk)
    if request.method == 'POST':
        form = LancamentoForm(request.POST, instance=lancamento)
        if form.is_valid():
            form.save()
            return redirect(reverse('lancamento_listar'))
    else:
        form = LancamentoForm(instance=lancamento)
    return render(request, 'lancamento/editar.html', {'operacoes': operacoes, 'form': form})


def apagar(request, pk):
    operacoes = Operacao.objects.all()
    lancamento = Lancamento.objects.get(pk=pk)
    if request.method == 'POST':
        lancamento.delete()
        return redirect(reverse('lancamento_listar'))
    return render(request, 'lancamento/apagar.html', {'operacoes': operacoes, 'lancamento': lancamento})


def listar(request, operacao):
    operacoes = Operacao.objects.all()
    
    if request.method == 'POST':
        form = LancamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('lancamento_listar', {'operacoes': operacoes, 'pessoa': pessoa, 'operacao': operacao}))
    else:
        form = LancamentoForm()

    lancamentos = Lancamento.objects.filter(pessoa_id=pessoa)
    return render(request, 'lancamento/listar.html',{'lancamentos': lancamentos, 'form': form})
