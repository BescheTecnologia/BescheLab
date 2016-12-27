from django.db import models
from datetime import datetime


class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=12)
    email = models.EmailField()
    
    def __str__(self):
        return self.nome


class PessoaFisica(models.Model):
    pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE)
    cpf = models.CharField('CPF', max_length=11)
    cns = models.CharField('CNS', max_length=15, blank=True, null=True)


class PessoaJuridica(models.Model):
    pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE)
    razao = models.CharField('Razão Social', max_length=50)
    cnpj = models.CharField('CNPJ', max_length=14)


class Usuario(models.Model):
    pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE)
    login = models.CharField(max_length=20)
    senha = models.CharField(max_length=20)
    cbo = models.IntegerField('CBO', blank=True, null=True)
    n_conselho = models.IntegerField('Conselho de Classe', blank=True, null=True)
    admissao = models.DateField(default=datetime.today())
    ativo = models.BooleanField(default=False)


class Operacao(models.Model):
    tipo = models.CharField(max_length=10)


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


class Endereco(models.Model):
    logradouro = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    uf = models.CharField('UF', max_length=2)
    
    def __str__(self):
        return self.logradouro+ ', ' +str(self.numero)+ ' - ' +self.bairro+ ', ' +self.cidade+ '/' +self.uf   


class Complemento(models.Model):
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE)
    numero = models.IntegerField('Número', blank=True, null=True)
    complemento = models.CharField(max_length=50, blank=True, null=True)


class Exame(models.Model):
    tipo = models.CharField(max_length=50)
    valor = models.DecimalField("Valor", "valor", 10, 2)

    def __str__(self):
        return self.tipo
