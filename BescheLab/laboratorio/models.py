from django.db import models


class Exame(models.Model):
    tipo = models.CharField(max_length=50)
    valor = models.DecimalField("Valor", "valor", 10, 2)

    def __str__(self):
        return self.tipo