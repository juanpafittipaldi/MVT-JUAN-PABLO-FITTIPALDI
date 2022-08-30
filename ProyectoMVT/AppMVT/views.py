from django.shortcuts import render
from .models import familiar
from django.http import HttpResponse
from django.template import loader
import datetime

# Create your views here.
def familiares(request):
    familiar_1=familiar(nombre="Jose",apellido="Fittpaldi",edad=40,fecha_nacimiento=datetime.date(1982,4,4))
    familiar_2=familiar(nombre="Mabel",apellido="Boga",edad=43,fecha_nacimiento=datetime.date(1979,3,6))
    familiar_3=familiar(nombre="Juana",apellido="Fittipaldi",edad=15,fecha_nacimiento=datetime.date(2007,3,30))
    familiar_1.save()
    familiar_2.save()
    familiar_3.save()
    diccionario={"PrimerFamiliar":familiar_1, "SegundoFamiliar":familiar_2,"TercerFamiliar":familiar_3}
    plantilla=loader.get_template("PlantillaCargaFlia.html")
    documento=plantilla.render(diccionario)
    
    return HttpResponse(documento)

def mostrar_familiares(request):
    listaDeFamilia = familiar.objects.all()
    diccionario = {"listaDeFamilia":listaDeFamilia}
    plantilla=loader.get_template("PlantillaDatosFlia.html")
    documento= plantilla.render(diccionario)
    return HttpResponse(documento)