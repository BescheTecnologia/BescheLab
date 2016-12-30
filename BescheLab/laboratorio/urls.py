from django.conf.urls import url
from .views import exame


urlpatterns = [
#Urls de Exame
    url(r'^exame/adicionar$', exame.adicionar, name='exame_adicionar'),
    url(r'^exame/editar/(?P<pk>\d+)$', exame.editar, name='exame_editar'),
    url(r'^exame/apagar/(?P<pk>\d+)$', exame.apagar, name='exame_apagar'),
    url(r'^exame/detalhar/(?P<pk>\d+)$', exame.detalhar,name='exame_detalhar'),
    url(r'^laboratorio/exame$', exame.listar, name='exame_listar'),
]
