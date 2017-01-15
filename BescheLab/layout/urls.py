from django.conf.urls import url
from .views import index
from ..financeiro.views import operacao


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^configuracoes$', operacao.listar, name='operacao_listar'),
]
