from django.db import models

# Create your models here.

class Bolsista(models.Model):

    nome = models.CharField(max_length=100)
    matricula = models.IntegerField()
    curso = models.CharField(max_length=140)
    periodo = models.CharField(max_length=20)
    email = models.EmailField()
    
class Orientador(models.Model):

    nome = models.CharField(max_length=100)
    matricula = models.IntegerField()
    email = models.EmailField()
    bolsistas = models.ManyToManyField(Bolsista, blank=True, related_name='orientador')

class Registro(models.Model):

    hora_entrada = models.TimeField()
    hora_saida = models.TimeField()
    data = models.DateField()
    bolsista = models.ForeignKey(Bolsista, on_delete=models.CASCADE)
    carga_horaria = models.IntegerField()

class Frequencia(models.Model):

    mes = models.CharField(max_length=20)
    bolsista = models.ForeignKey(Bolsista, on_delete=models.CASCADE)
    registros = models.ManyToManyField(Registro, blank=True)
    carga_horaria_total = models.IntegerField()
