from django.db import models
from datetime import datetime, date
from django.utils.timezone import now


class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=12)
    email = models.EmailField('email', max_length=50, blank=True, null=True)
    
    def __str__(self):
        return self.nome


class PessoaFisica(models.Model):
    pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE, blank=True, null=True)
    cpf = models.CharField('CPF', max_length=11)
    cns = models.CharField('CNS', max_length=15, blank=True, null=True)
    sexo = models.CharField('Sexo', max_length=10, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)


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
    admissao = models.DateField(default=date.day)
    ativo = models.BooleanField(default=False)


class Endereco(models.Model):
    logradouro = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    uf = models.CharField('UF', max_length=2)
    
    def __str__(self):
        return self.logradouro+ ' - ' +self.bairro+ ', ' +self.cidade+ '/' +self.uf   


class Complemento(models.Model):
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, blank=True, null=True)
    pessoa = models.OneToOneField(Pessoa, on_delete=models.CASCADE, blank=True, null=True)
    numero = models.IntegerField('Número', blank=True, null=True)
    complemento = models.CharField(max_length=50, blank=True, null=True)
