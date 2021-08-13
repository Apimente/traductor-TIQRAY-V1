from django.urls import path, include
from DICCIONARIO.views import VISTA_DICCIONARIO_CONSULTA,RESPUESTA_DICCIONARIO_CONSULTA,FormularioAlimentarBD

urlpatterns =[
    path("",VISTA_DICCIONARIO_CONSULTA,name ="Diccionario"),
    path("RespuestaDIC/",RESPUESTA_DICCIONARIO_CONSULTA.as_view(),name ="RespuestaDIC"),
    path("IngresarDiccionario/",FormularioAlimentarBD.as_view(),name ="IngresarDiccionario"),

]