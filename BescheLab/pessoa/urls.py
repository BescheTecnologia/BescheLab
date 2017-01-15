from django.conf.urls import url
from .views import pessoa


urlpatterns = [
    url(r'^paciente/adicionar$', pessoa.adicionar, name='pessoa_adicionar'),
    url(r'^paciente/(?P<pk>\d+)/editar$', pessoa.editar, name='pessoa_editar'),
    url(r'^paciente/(?P<pk>\d+)/apagar$', pessoa.apagar, name='pessoa_apagar'),
    url(r'^pacientes$', pessoa.listar, name='pessoa_listar'),
]
