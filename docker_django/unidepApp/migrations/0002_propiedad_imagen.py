# Generated by Django 2.2.27 on 2022-05-23 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unidepApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='propiedad',
            name='imagen',
            field=models.ImageField(null=True, upload_to='fotos'),
        ),
    ]
