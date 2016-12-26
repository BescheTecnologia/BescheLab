from django.conf.urls import url
from .views import index
from .views import pessoa


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^pessoa/adicionar$', pessoa.adicionar, name='pessoa_adicionar'),
    url(r'^pessoa/editar/(?P<pk>\d+)$', pessoa.editar, name='pessoa_editar'),
    url(r'^pessoa/apagar/(?P<pk>\d+)$', pessoa.apagar, name='pessoa_apagar'),
    url(r'^pessoa/detalhar/(?P<pk>\d+)$', pessoa.detalhar,name='pessoa_detalhar'),
    url(r'^financeiro/pessoa$', pessoa.listar, name='pessoa_listar'),
]
