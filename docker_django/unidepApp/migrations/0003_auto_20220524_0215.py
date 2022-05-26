# Generated by Django 2.2.27 on 2022-05-24 02:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unidepApp', '0002_propiedad_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propiedad',
            name='precio_arriendo',
            field=models.IntegerField(validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Solo están permitidos carácteres alfanuméricos.')]),
        ),
    ]
