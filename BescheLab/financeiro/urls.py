from django.conf.urls import url
from .views import index
from .views import pessoa
from .views import operacao
from .views import lancamento


urlpatterns = [
    #Index
    url(r'^$', index, name='index'),
    #Urls de Pessoa
    url(r'^pessoa/adicionar$', pessoa.adicionar, name='pessoa_adicionar'),
    url(r'^pessoa/editar/(?P<pk>\d+)$', pessoa.editar, name='pessoa_editar'),
    url(r'^pessoa/apagar/(?P<pk>\d+)$', pessoa.apagar, name='pessoa_apagar'),
    url(r'^pessoa/detalhar/(?P<pk>\d+)$', pessoa.detalhar,name='pessoa_detalhar'),
    url(r'^financeiro/pessoa$', pessoa.listar, name='pessoa_listar'),
    #Urls de Operacao
    url(r'^operacao/adicionar$', operacao.adicionar, name='operacao_adicionar'),
    url(r'^operacao/editar/(?P<pk>\d+)$', operacao.editar, name='operacao_editar'),
    url(r'^operacao/apagar/(?P<pk>\d+)$', operacao.apagar, name='operacao_apagar'),
    url(r'^operacao/detalhar/(?P<pk>\d+)$', operacao.detalhar,name='operacao_detalhar'),
    url(r'^financeiro/operacao$', operacao.listar, name='operacao_listar'),
    #Urls de Lancamento
    url(r'^lancamento/editar/(?P<pk>\d+)$', lancamento.editar, name='lancamento_editar'),
    url(r'^lancamento/apagar/(?P<pk>\d+)$', lancamento.apagar, name='lancamento_apagar'),
    url(r'^lancamento/detalhar/(?P<pk>\d+)$', lancamento.detalhar,name='lancamento_detalhar'),
    url(r'^financeiro/lancamento/listarpessoa$', lancamento.listarpessoa, name='lancamento_listarpessoa'),
    url(r'^financeiro/lancamento/listar/(?P<pk>\d+)$', lancamento.listar, name='lancamento_listar'),
]
