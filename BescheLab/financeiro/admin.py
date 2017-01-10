from django.contrib import admin
from .models import*

# Register your models here.
admin.site.register(Pessoa)
admin.site.register(PessoaFisica)
admin.site.register(PessoaJuridica)
admin.site.register(Usuario)
admin.site.register(Operacao)
admin.site.register(Lancamento)
admin.site.register(Pagamento)
admin.site.register(Endereco)
admin.site.register(Complemento)
