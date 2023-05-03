from django.contrib import admin

from frequencia.models import Bolsista, Orientador, Registro, Frequencia

# Register your models here.


admin.site.register(Bolsista)
admin.site.register(Orientador)
admin.site.register(Registro)
admin.site.register(Frequencia)