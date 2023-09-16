from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from bolsistas.users.models import User, ProReitor, Coordenador, Orientador, Bolsista

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        username_or_email = request.data.get('username', '')
        password = request.data.get('password', '')

        is_email = '@' in username_or_email

        if is_email:
            user = User.objects.filter(email=username_or_email).first()
        else:
            user = User.objects.filter(username=username_or_email).first()

        if user is not None and user.check_password(password):
            token, created = Token.objects.get_or_create(user=user)

            user_type = 'Usuário Padrão'
            if ProReitor.objects.filter(user=user).exists():
                user_type = 'ProReitor'
            elif Coordenador.objects.filter(user=user).exists():
                user_type = 'Coordenador'
            elif Orientador.objects.filter(user=user).exists():
                user_type = 'Orientador'
            elif Bolsista.objects.filter(user=user).exists():
                user_type = 'Bolsista'

            return Response({'token': token.key, 'user_type': user_type})
        else:
            return Response({'error': 'Credenciais inválidas'}, status=400)
