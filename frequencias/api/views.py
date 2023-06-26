from rest_framework.permissions import AllowAny
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

class FrequenciaViewSet(ModelViewSet):

    permission_classes = [ AllowAny ]
    serializer_class = FrequenciaSerializer
    queryset = Frequencia.objects.all()


