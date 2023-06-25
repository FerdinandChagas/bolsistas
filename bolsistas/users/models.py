from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from frequencias.models import Campus, Projeto


class User(AbstractUser):
    """
    Default custom user model for bolsistas.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    #: First and last name do not cover name patterns around the globe
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})

class ProReitor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    inicio_m = models.DateField(null=True)
    fim_m = models.DateField(null=True)

class Coordenador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)

class Orientador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    situacao = models.CharField(max_length=150)

class Bolsista(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    orientador = models.ForeignKey(Orientador, on_delete=models.CASCADE, related_name="bolsistas")
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)