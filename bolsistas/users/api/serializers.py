from django.contrib.auth import get_user_model
from rest_framework import serializers

from bolsistas.users.models import ProReitor, Coordenador, Orientador, Bolsista


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["matricula","name", "email"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"}
        }

class ProReitorSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = ProReitor
        fields = "__all__"

class CoodenadorSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Coordenador
        fields = "__all__"

class OrientadorSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Orientador
        fields = "__all__"

class BolsistaSerializer(serializers.ModelSerializer):
    
    user = UserSerializer()

    class Meta:
        model = Bolsista
        fields = fields = "__all__"