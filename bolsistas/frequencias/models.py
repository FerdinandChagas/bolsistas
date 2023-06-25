from django.db import models

from users.models import Coordenador

# Create your models here.

class Campus(models.Model):

    nome = models.CharField(max_length=150)
    endereco = models.CharField(max_length=150)
    responsavel = models.ForeignKey(Coordenador, on_delete=models.CASCADE, null=True)

class Projeto(models.Model):

    nome = models.CharField(max_length=150)
    descricao = models.CharField(max_length=150)
    data_inicio = models.DateField()
    data_fim = models.DateField()

