from django.conf.urls import url
from .views import lancamento


urlpatterns = [
    url(r'^lancamento/adicionar$', lancamento.adicionar, name='lancamento_adicionar'),
    url(r'^lancamento/editar/(?P<lancamento>\d+)$', lancamento.editar, name='lancamento_editar'),
    url(r'^lancamento/apagar/(?P<lancamento>\d+)$', lancamento.apagar, name='lancamento_apagar'),
    url(r'^lancamento/detalhar/(?P<lancamento>\d+)$', lancamento.detalhar,name='lancamento_detalhar'),
    url(r'^financeiro/lancamento/listarpessoa(?P<pk>\d+)$', lancamento.listarpessoa, name='lancamento_listarpessoa'),
    url(r'^financeiro/lancamento/listar/(?P<operacao>\d+)$', lancamento.listar, name='lancamento_listar'),
]
