from rest_framework.serializers import ModelSerializer

from frequencia.models import Bolsista, Frequencia, Orientador, Registro

class BolsistaSerializer(ModelSerializer):

    class Meta:
        model = Bolsista
        fields = [ 'nome', 'matricula', 'curso', 'periodo', 'email']

class OrientadorSerializer(ModelSerializer):

    class Meta:
        model = Orientador
        fields = '__all__'

class RegistroSerializer(ModelSerializer):

    class Meta:
        model = Registro
        fields = '__all__'

class FrequenciaSerializer(ModelSerializer):

    class Meta:
        model = Frequencia
        fields = '__all__'