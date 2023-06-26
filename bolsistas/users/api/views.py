from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from bolsistas.users.models import ProReitor, Coordenador, Orientador, Bolsista

from .serializers import UserSerializer, ProReitorSerializer, CoodenadorSerializer, OrientadorSerializer, BolsistaSerializer

User = get_user_model()


class UserViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "username"

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        return self.queryset.filter(id=self.request.user.id)

    @action(detail=False)
    def me(self, request):
        serializer = UserSerializer(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class ProReitorViewSet(ModelViewSet):

    permission_classes = [ AllowAny ]
    serializer_class = ProReitorSerializer
    queryset = ProReitor.objects.all()

class CoordenadorViewSet(ModelViewSet):

    permission_classes = [ AllowAny ]
    serializer_class = CoodenadorSerializer
    queryset = Coordenador.objects.all()

class OrientadorViewSet(ModelViewSet):

    permission_classes = [ AllowAny ]
    serializer_class = OrientadorSerializer
    queryset = Orientador.objects.all()

class BolsistaViewSet(ModelViewSet):

    permission_classes = [ AllowAny ]
    serializer_class = BolsistaSerializer
    queryset = Bolsista.objects.all()

    def create(self, request):
        matricula = request.data['matricula']
        nome = request.data['nome']
        email = request.data['email']
        username = request.data['username']
        password = request.data['password']
        projeto_id = request.data['projeto_id']
        campus_id = request.data['campus_id']

        novo_bolsista = Bolsista.objects.create(
            matricula=matricula,
            nome=nome,
            email=email,
            username=username,
            password=password,
            project_id=projeto_id,
            campus_id=campus_id,
        )
        novo_bolsista.save()

        serializer = BolsistaSerializer(novo_bolsista)
        return Response({"Notice": "Bolsista cadastrado com sucesso!", "data": serializer.data}, status=status.HTTP_201_CREATED)

