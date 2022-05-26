from email.policy import default
from random import choices
from django.db import models
from multiselectfield import MultiSelectField
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Solo están permitidos carácteres alfanuméricos.')

UNIVERSIDADES = (
    ('Universidad del Bio Bio', 'Universidad del Bio Bio'),
    ('Universidad De La Santisima Concepcion', 'Universidad De La Santisima Concepcion'),
    ('Universidad San Sebastián', 'Universidad San Sebastián'),
    ('Advance Universidad San Sebastián', 'Advance Universidad San Sebastián'),
    ('Universidad Diego Portales', 'Universidad Diego Portales'),
    ('Universidad del Desarrollo', 'Universidad del Desarrollo'),
    ('Universidad del Pacífico', 'Universidad del Pacífico'),
    ('Universidad Técnica Federico Santa María', 'Universidad Técnica Federico Santa María'),
    ('INACAP - Universidad Tecnológica de Chile', 'INACAP - Universidad Tecnológica de Chile'),
    ('INACAP - Universidad Andrés Bello', 'INACAP - Universidad Andrés Bello'),
    ('Universidad Andrés Bello Postgrados', 'Universidad Andrés Bello Postgrados'),
    ('Universidad Arcis - Concepción', 'Universidad Arcis - Concepción'),
    ('Universidad Santo Tomás', 'Universidad Santo Tomás'),
    ('DUOC UC' , 'DUOC UC'),
    ('Instituto Profesional DUOC UC', 'Instituto Profesional DUOC UC'),
    ('Universidad del Desarrollo', 'Universidad del Desarrollo'),
    ('Educacion Ejecutiva - Facultad de Economía y Negocios - UDD (Universidad del Desarrollo)','Educacion Ejecutiva - Facultad de Economía y Negocios - UDD (Universidad del Desarrollo)'),
    ('Universidad de Concepcion','Universidad de Concepcion')
)

# Create your models here.
class Propietario(models.Model):
    nombre_propietario = models.CharField(max_length=50, null=False)
    apellido_propietario = models.CharField(max_length=50, null=False)
    rut = models.CharField(max_length=9)
    def __str__(self):
        return self.nombre_propietario

class Propiedad(models.Model):
    TIPO_PROPIEDAD=[
        ('departamento', 'departamento'),
        ('casa', 'casa')
    ]
    universidades_cercanas = MultiSelectField(choices=UNIVERSIDADES, default=None)
    sector_propiedad = models.CharField(max_length=50)
    direccion = models.CharField(max_length=80, default=None)
    precio_arriendo = models.IntegerField(blank=True, null=True, validators= [alphanumeric])
    tipo_propiedad = models.CharField(choices=TIPO_PROPIEDAD, default=None, max_length=20)
    cantidad_banos = models.IntegerField(default=None)
    cantidad_habitaciones = models.IntegerField(default=None)
    amoblado = models.BooleanField(default=None)
    superficie_total = models.IntegerField(default=None)
    estacionamiento = models.BooleanField(default=None)
    gastos_comunes = models.IntegerField(default=None)
    servicio_aseo = models.BooleanField(default=None)
    propietario = models.ManyToManyField(Propietario)
    imagen = models.ImageField(upload_to="fotos_propiedad", null=True)
    def __str__(self):
        return self.tipo_propiedad


class Estudiante(models.Model):
    rut_estudiante = models.CharField(max_length=9)
    nombre_estudiante = models.CharField(max_length=50)
    apellido_estudiante = models.CharField(max_length=50)
    universidad = models.CharField(choices=UNIVERSIDADES, default=None, max_length=100)
    presupuesto = models.IntegerField()
    propiedad = models.ManyToManyField(Propiedad)
