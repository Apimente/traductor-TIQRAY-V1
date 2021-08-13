from django.db import models

# Create your models here.
class Diccionario_QUECHUA_ESP(models.Model):
    palabradb_quechua=models.CharField(max_length=100,verbose_name=("Palabra en Quechua"))
    palabradb_esp=models.CharField(max_length=100,verbose_name=("palabra en español (Traduccion)"))
    palabradb_ejemplo_uso=models.TextField(verbose_name=("Contexto o ejemplo de uso"))