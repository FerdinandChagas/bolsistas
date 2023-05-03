from django.contrib import admin
from django.urls import path
from rest_framework_extensions.routers import ExtendedDefaultRouter as DefaultRouter

from frequencia.api.views import BolsistaViewSet, FrequenciaViewSet, OrientadorViewSet, RegistroViewSet

router = DefaultRouter()

router.register('api/bolsistas', BolsistaViewSet, basename='bolsistas')
router.register('api/orientadores', OrientadorViewSet, basename='orientadores')
router.register('api/registros', RegistroViewSet, basename='registros')
router.register('api/frequencias', FrequenciaViewSet, basename='frequencias')

urlpatterns = [
    path("admin/", admin.site.urls),
] + router.urls
