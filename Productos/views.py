from django.shortcuts import render
from Productos.models import productos
from django.template import loader
from django.http import HttpResponse

def sardo(request):
    Sardo = productos(nombre = 'Sardo', calidad = 'Semi', tipo = 'Horma')
    Sardo.save()

    return render(request, '/Productos/sardo.html')

def reggiano(request):
    Reggiano = productos(nombre = 'Reggiano', calidad = 'Duro', tipo = 'Medio')
    Reggiano.save()

    return render(request, '/Productos/regg.html')

def provolone(request):
    Provolone = productos(nombre = 'Provolone', calidad = 'Duro', tipo = 'Medio')
    Provolone.save()

    return render(request, '/Productos/prov.html')

def catalogo(self):

    plantilla = loader.get_template('Productos/catalogo.html')
    catalog = plantilla.render()
    return HttpResponse(catalog)
