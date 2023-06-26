from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from frequencias.models import Campus, Projeto, Frequencia, Ponto
from bolsistas.users import managers

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
    matricula = models.CharField(max_length=150, default=0)
    
    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})

class ProReitor(models.Model):
    user = models.OneToOneField("User", on_delete=models.CASCADE)
    inicio_m = models.DateField(null=True)
    fim_m = models.DateField(null=True)
    objects = managers.ProReitorManager()

    class Meta:
        verbose_name = "Pro-reitor"
        verbose_name_plural = "Pro-reitores"

    def __str__(self):
        return f'{self.user.pk} | {self.user.name}'

class Coordenador(models.Model):
    user = models.OneToOneField("User", on_delete=models.CASCADE)
    campus = models.ForeignKey("frequencias.Campus", on_delete=models.CASCADE, default=None)
    objects = managers.CoodenadorManager()
    class Meta:
        verbose_name = "Coordenador"
        verbose_name_plural = "Coordenadores"

    def __str__(self):
        return f'{self.user.pk} | {self.user.name}'

class Orientador(models.Model):
    user = models.OneToOneField("User", on_delete=models.CASCADE)
    situacao = models.CharField(max_length=150)
    objects = managers.OrientadorManager()
    class Meta:
        verbose_name = "Orientador"
        verbose_name_plural = "Orientadores"

    def __str__(self):
        return f'{self.user.pk} | {self.user.name}'

class Bolsista(models.Model):
    user = models.OneToOneField("User", on_delete=models.CASCADE)
    orientador = models.ForeignKey("Orientador", on_delete=models.CASCADE, related_name="bolsistas", null=True)
    campus = models.ForeignKey("frequencias.Campus", on_delete=models.CASCADE, related_name="bolsistas")
    projeto = models.ForeignKey("frequencias.Projeto", on_delete=models.CASCADE, related_name="bolsistas")
    frequencias = models.ManyToManyField("frequencias.Frequencia", related_name="bolsista", blank=True)

    objects = managers.BolsistaManager()

    class Meta:
        verbose_name = "Bolsista"
        verbose_name_plural = "Bolsistas"

    def __str__(self):
        return f'{self.user.pk} | {self.user.name}'