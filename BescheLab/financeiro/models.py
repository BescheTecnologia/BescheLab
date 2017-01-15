from django.db import models
from datetime import datetime, date
from django.utils.timezone import now
from ..pessoa.models import Pessoa


class Operacao(models.Model):
    nome = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)
    icone = models.CharField(max_length=20)
    
    
    def __str__(self):
        return self.tipo;


class Lancamento(models.Model):
    pessoa = models.ForeignKey(Pessoa, blank=True, null=True)
    tipo = models.ForeignKey(Operacao, blank=True, null=True)
    descricao = models.CharField('Descrição', max_length=100)
    valor = models.DecimalField("Valor", "valor", 10, 2)
    #data = models.DateTimeField(default=datetime.today())
    parcelado = models.BooleanField(default=False)
    n_parcelas = models.IntegerField('Número de Parcelas', null=True, blank=True)

    def __str__(self):
        return str(self.valor)+ ' R$ - ' +self.descricao;


class Pagamento(models.Model):
    lancamento = models.ForeignKey(Lancamento, on_delete=models.CASCADE, blank=True, null=True)
    parcela = models.IntegerField(blank=True, null=True)
    valor = models.DecimalField("Valor", "valor", 10, 2, blank=True, null=True)
    #vencimento = models.DateField()
    pago = models.BooleanField(default=False)
    #pagamento = models.DateTimeField(default=datetime.today(), blank=True, null=True)
    