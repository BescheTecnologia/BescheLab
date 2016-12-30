from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.forms.models import modelform_factory
from ..models import Exame


def listar(request):
    exames = Exame.objects.all()
    return render(request, 'laboratorio/exame/listar.html', {'exames': exames})


def detalhar(request, pk):
    exame = Exame.objects.get(pk=pk)
    return render(request, 'laboratorio/exame/detalhar.html', {'exame': exame})


ExameForm = modelform_factory(Exame, fields=('__all__'))


def adicionar(request):
    if request.method == 'POST':
        form = ExameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('exame_listar'))
    else:
        form = ExameForm()
    return render(request, 'laboratorio/exame/adicionar.html', {'form': form})


def editar(request, pk):
    exame = Exame.objects.get(pk=pk)
    if request.method == 'POST':
        form = ExameForm(request.POST, instance=exame)
        if form.is_valid():
            form.save()
            return redirect(reverse('exame_listar'))
    else:
        form = ExameForm(instance=exame)
    return render(request, 'laboratorio/exame/editar.html', {'form': form})


def apagar(request, pk):
    exame = Exame.objects.get(pk=pk)
    if request.method == 'POST':
        exame.delete()
        return redirect(reverse('exame_listar'))
    return render(request, 'laboratorio/exame/apagar.html', {'exame': exame})
