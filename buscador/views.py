#from django.http import HttpResponse, JsonResponse
from .models import Item
from django.shortcuts import render
from .forms import Consultar_id, Consultar_Barras, Consultar_Nombre

# Create your views here.

def buscar(request):
    try:
        id = request.GET['id']
        items = Item.objects.filter(id__startswith=id)
        items = items.values()
    except:
        print("Hay un error en los valores de entrada")
    try:
        barras = request.GET['barras']
        items = Item.objects.filter(Barras__startswith=barras)
        items = items.values()
    except:
        print("Hay un error en los valores de entrada")
    try:
        nombre = request.GET['nombre'] 
        items = Item.objects.filter(Nombre__contains=nombre)
        items = items.values()
    except:
        print("Hay un error en los valores de entrada")

    
    return render(request,'buscando.html',{
        'form_id': Consultar_id,
        'form_barras': Consultar_Barras,
        'form_nombre': Consultar_Nombre,
        'item': items
    })

def buscador(request):
    return render(request, 'buscador.html',{
        'form_id': Consultar_id,
        'form_barras': Consultar_Barras,
        'form_nombre': Consultar_Nombre,
        })

def inicio(request):
    return render(request,'inicio.html',{
        'form_id': Consultar_id,
        'form_barras': Consultar_Barras,
        'form_nombre': Consultar_Nombre,
        })

