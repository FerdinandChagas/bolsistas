from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


from frequencias.models import Campus, Projeto, Ponto, Frequencia
from frequencias.api.serializers import CampusSerializer, ProjetoSerializer, PontoSerializer, FrequenciaSerializer

class CampusViewSet(ModelViewSet):

    permission_classes = [ AllowAny ]
    serializer_class = CampusSerializer
    queryset = Campus.objects.all()


class ProjetoViewSet(ModelViewSet):

    permission_classes = [ AllowAny ]
    serializer_class = ProjetoSerializer
    queryset = Projeto.objects.all()

class PontoViewSet(ModelViewSet):

    permission_classes = [ AllowAny ]
    serializer_class = PontoSerializer
    queryset = Ponto.objects.all()

    def create(self, request):
        data = request.data['data']
        hora_entrada = request.data['hora_entrada']
        hora_saida = request.data['hora_saida']
        frequencia_id = request.data['frequencia']
        bolsista_id = request.data['bolsista']
        novo_ponto = Ponto.objects.create(
            data=data,
            hora_entrada=hora_entrada,
            hora_saida=hora_saida,
            frequencia_id=frequencia_id,
            bolsista_id=bolsista_id
        )
        serializer = PontoSerializer(novo_ponto)
        return Response({"Notice": "Ponto registrado.", "data": serializer.data}, status=status.HTTP_201_CREATED)

class FrequenciaViewSet(ModelViewSet):

    permission_classes = [ AllowAny ]
    serializer_class = FrequenciaSerializer
    queryset = Frequencia.objects.all()


