#from django.http import HttpResponse, JsonResponse
from .models import Item
from django.shortcuts import render
from .forms import Consultar_id, Consultar_Barras, Consultar_Nombre

# Create your views here.

def saludo(request):
    id = request.GET['id']
    barras = request.GET['barras']
    nombre = request.GET['nombre']

    items_id = Item.objects.filter(id__startswith=id)
    items_id = items_id.values()
    items_barras = Item.objects.filter(id__startswith=barras)
    items_barras = items_barras.values()
    items_nombre = Item.objects.filter(id__startswith=nombre)
    items_nombre = items_nombre.values()
    return render(request,'index.html',{
        'form_id': Consultar_id,
        'form_barras': Consultar_Barras,
        'form_nombre': Consultar_Nombre,
        'item_id': items_id,
        'item_barra': items_barras,
        'item_nombre': items_nombre,
    })

