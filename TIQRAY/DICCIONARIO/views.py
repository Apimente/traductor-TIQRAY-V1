from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import View
from DICCIONARIO.models import Diccionario_QUECHUA_ESP
from DICCIONARIO.forms import Formulario_Ingresar_Diccionario

# Create your views here.
def VISTA_DICCIONARIO_CONSULTA(request):
    return render(request, "TEMPLATE_DICCIONARIO/Diccionario.html")

class RESPUESTA_DICCIONARIO_CONSULTA(View):
    def get(self, request):
        palabra=request.GET["palabra_quechua2"]
        if palabra:
            palbraQuechua= Diccionario_QUECHUA_ESP.objects.filter(palabradb_quechua__icontains = palabra)
            return render(request,"TEMPLATE_DICCIONARIO/respuesta.html",{"palbraQuechua":palbraQuechua,"query":palabra})
        else:
            return HttpResponse("Algo salio mal")

class FormularioAlimentarBD(View):
    def get(self, request):
        Palabarasdb_Campos=Formulario_Ingresar_Diccionario()
        return render(request, 'TEMPLATE_DICCIONARIO/ingresardb.html',{"Palabarasdb_Campos":Palabarasdb_Campos})
        
    def post(self, request):
        formulario=Formulario_Ingresar_Diccionario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('IngresarDiccionario')
        else:
            return HttpResponse("Algo fallo")