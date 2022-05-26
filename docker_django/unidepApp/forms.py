from dataclasses import field, fields
from django import forms
from .models import Propiedad
from django.contrib.auth.models import User


class FormPropiedad(forms.ModelForm):
    imagen = forms.BooleanField(required=False)
    amoblado = forms.BooleanField(required=False)
    estacionamiento = forms.BooleanField(required=False)
    servicio_aseo = forms.BooleanField(required=False)
    # precio_arriendo = forms.IntegerField(min_value=1, max_value=9)
    class Meta:
        model = Propiedad
        fields = ('universidades_cercanas', 'sector_propiedad', 'direccion', 'precio_arriendo', 'tipo_propiedad', 'cantidad_banos', 'cantidad_habitaciones', 'amoblado', 'superficie_total', 'estacionamiento', 'gastos_comunes', 'servicio_aseo')
        widgets = {
            'sector_propiedad': forms.TextInput(attrs={
                'class': 'carac'
                    
            }),
            'direccion': forms.TextInput(attrs={
                'class': 'carac'    
            }),
            'precio_arriendo': forms.NumberInput(attrs={
                'class': 'carac',
                'name': 'precio_arriendo'  
            }),
            'tipo_propiedad': forms.Select(attrs={
                'class': 'carac'    
            }),
            'cantidad_banos': forms.NumberInput(attrs={
                'class': 'carac'    
            }),
            'cantidad_habitaciones': forms.NumberInput(attrs={
                'class': 'carac'    
            }),
            'amoblado': forms.CheckboxInput(attrs={
                'class': 'carac'
            }),
            'superficie_total': forms.NumberInput(attrs={
                'class': 'carac'
            }),
            'estacionamiento': forms.CheckboxInput(attrs={
                'class': 'carac'
            }),
            'gastos_comunes': forms.NumberInput(attrs={
                'class': 'carac'
            }),
            'servicio_aseo': forms.CheckboxInput(attrs={
                'class': 'carac'
            }),
        }
        






