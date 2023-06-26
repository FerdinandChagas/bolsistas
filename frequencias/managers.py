from django.db.models import Manager

from bolsistas.users import models as umd
from frequencias import models as fmd


class PontoManager(Manager):

    def create(self, data, hora_entrada, hora_saida, frequencia_id, bolsista_id):
        frequencia = fmd.Frequencia.objects.get(id=frequencia_id)
        bolsista = umd.Bolsista.objects.get(id=bolsista_id)

        novo_ponto = super().create(data=data, hora_entrada=hora_entrada, hora_saida=hora_saida, frequencia=frequencia, bolsista=bolsista)
        novo_ponto.save()
        return novo_ponto