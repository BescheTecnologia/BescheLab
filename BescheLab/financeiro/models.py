from django.db import models
from datetime import datetime, date
from django.utils.timezone import now


class Operacao(models.Model):
    tipo = models.CharField(max_length=10)
    
    
    def __str__(self):
        return self.tipo;


class Lancamento(models.Model):
    pessoa = models.ForeignKey(Pessoa)
    tipo = models.ForeignKey(Operacao)
    descricao = models.CharField('Descrição', max_length=100)
    valor = models.DecimalField("Valor", "valor", 10, 2)
    data = models.DateTimeField(default=datetime.today())
    parcelado = models.BooleanField(default=False)
    n_parcelas = models.IntegerField('Número de Parcelas', null=True, blank=True)

    def __str__(self):
        return str(self.valor)+ ' R$ - ' +self.descricao;


class Pagamento(models.Model):
    lancamento = models.ForeignKey(Lancamento, on_delete=models.CASCADE)
    parcela = models.IntegerField()
    valor = models.DecimalField("Valor", "valor", 10, 2)
    vencimento = models.DateField()
    pago = models.BooleanField(default=False)
    pagamento = models.DateTimeField(default=datetime.today(), blank=True, null=True)
    