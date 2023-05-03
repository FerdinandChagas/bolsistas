from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from frequencia.api.serializers import BolsistaSerializer, FrequenciaSerializer, OrientadorSerializer, RegistroSerializer

from frequencia.models import Bolsista, Frequencia, Orientador, Registro

class BolsistaViewSet(ModelViewSet): # GET, POST, UPDATE, DELETE, PATCH

    permission_classes = [ IsAuthenticated ]
    serializer_class = BolsistaSerializer
    queryset = Bolsista.objects.all()

class OrientadorViewSet(ModelViewSet):

    permission_classes = [ IsAuthenticated ]
    serializer_class = OrientadorSerializer
    queryset = Orientador.objects.all()

class RegistroViewSet(ModelViewSet):

    permission_classes = [ IsAuthenticated ]
    serializer_class = RegistroSerializer
    queryset = Registro.objects.all()

class FrequenciaViewSet(ModelViewSet):

    permission_classes = [ IsAuthenticated ]
    serializer_class = FrequenciaSerializer
    queryset = Frequencia.objects.all()