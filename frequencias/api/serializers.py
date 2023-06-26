from rest_framework.serializers import ModelSerializer

from frequencias.models import Campus, Projeto, Ponto, Frequencia
from bolsistas.users.api.serializers import BolsistaSerializer

class CampusSerializer(ModelSerializer):

    class Meta:
        model = Campus
        fields = "__all__"

class ProjetoSerializer(ModelSerializer):

    class Meta:
        model = Projeto
        fields = "__all__"

class PontoSerializer(ModelSerializer):

    bolsista = BolsistaSerializer(many = True)

    class Meta:
        model = Ponto
        fields = "__all__"
    
class FrequenciaSerializer(ModelSerializer):

    class Meta:
        model = Frequencia
        fields = "__all__"

