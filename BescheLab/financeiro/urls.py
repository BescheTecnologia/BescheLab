from django.conf.urls import url
from .views import lancamento
from .views import operacao

urlpatterns = [    
    url(r'^operacao/adicionar$', operacao.adicionar, name='operacao_adicionar'),
    url(r'^operacao/(?P<pk>\d+)/editar$', operacao.editar, name='operacao_editar'),
    url(r'^operacao/(?P<pk>\d+)/apagar$', operacao.apagar, name='operacao_apagar'),
    
    url(r'^(?P<operacao>\w+)/(?P<pk>\d+)/editar$', lancamento.editar, name='lancamento_editar'),
    url(r'^(?P<operacao>\w+)/(?P<pk>\d+)/apagar$', lancamento.apagar, name='lancamento_apagar'),
    url(r'^gerenciar/(?P<operacao>\w+)s$', lancamento.adicionar, name='lancamento_adicionar'),
]
