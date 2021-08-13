from django import forms
from .models import Diccionario_QUECHUA_ESP

class Formulario_Ingresar_Diccionario(forms.ModelForm):
    class Meta:
        model=Diccionario_QUECHUA_ESP
        fields='__all__'