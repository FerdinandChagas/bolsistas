from django.db import models

# Create your models here.

class Campus(models.Model):

    nome = models.CharField(max_length=150)
    endereco = models.CharField(max_length=150)

    class Meta:
        verbose_name = "Campus"
        verbose_name_plural = "Campus"

    def __str__(self):
        return f'{self.pk} | {self.nome}'


class Projeto(models.Model):

    nome = models.CharField(max_length=150)
    descricao = models.CharField(max_length=150)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    campus = models.ForeignKey("Campus", on_delete=models.CASCADE, related_name="projetos")

    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"

    def __str__(self):
        return f'{self.pk} | {self.nome}'
    

class Ponto(models.Model):

    data = models.DateField()
    hora_entrada = models.TimeField()
    hora_saida = models.TimeField()

    class Meta:
        verbose_name = "Ponto"
        verbose_name_plural = "Pontos"

    def __str__(self):
        return f'{self.pk} | {self.data} | {self.bolsista.user.name}'

class Frequencia(models.Model):

    mes = models.CharField(max_length=100)
    pontos = models.ManyToManyField("Ponto", related_name="frequencia")
    ch_total = models.FloatField()

    class Meta:
        verbose_name = "Frequencia"
        verbose_name_plural = "Frequencias"

    def __str__(self):
        return f'{self.pk} | {self.mes} | {self.bolsista.user.name}'