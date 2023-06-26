from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from bolsistas.users.api.views import UserViewSet, ProReitorViewSet, CoordenadorViewSet, OrientadorViewSet, BolsistaViewSet
from frequencias.api.views import CampusViewSet, ProjetoViewSet, PontoViewSet, FrequenciaViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("proreitoria", ProReitorViewSet, basename="proreitoria")
router.register("coodenadores", CoordenadorViewSet, basename="coordenadores")
router.register("orientadores", OrientadorViewSet, basename="orientadores")
router.register("bolsistas", BolsistaViewSet, basename="bolsistas")
router.register("campus", CampusViewSet, basename="campus")
router.register("projetos", ProjetoViewSet, basename="projetos")
router.register("pontos", PontoViewSet, basename="pontos")
router.register("frequencias", FrequenciaViewSet, basename="frequencias")


app_name = "api"
urlpatterns = router.urls
