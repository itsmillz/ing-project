from django.contrib import admin
from unidepApp.models import Propiedad, Propietario, Estudiante
# Register your models here.

admin.site.register(Propietario)
admin.site.register(Propiedad)
admin.site.register(Estudiante)