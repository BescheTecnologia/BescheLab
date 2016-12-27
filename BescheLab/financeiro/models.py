from django.db import models
from datetime import datetime


class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=12)
    email = models.EmailField()
    
    def __str__(self):
        return self.nome


class Endereco(models.Model):
    logradouro = models.CharField(max_length=50)
    numero = models.IntegerField()
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    complemento = models.CharField(max_length=50)
