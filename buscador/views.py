#from django.http import HttpResponse, JsonResponse
from .models import Item
from django.shortcuts import render, redirect
from .forms import Consultar_id, Consultar_Barras, Consultar_Nombre
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def buscar(request):
    try:
        id = request.GET['id']
        if id != '':
            items = Item.objects.filter(id__startswith=id)
            items = items.values()
    except:
        print("Hay un error en los valores de entrada")
    try:
        barras = request.GET['barras']
        if barras != '':
            items = Item.objects.filter(Barras__startswith=barras)
            items = items.values()
    except:
        print("Hay un error en los valores de entrada")
    try:
        nombre = request.GET['nombre']
        if nombre != '': 
            items = Item.objects.filter(Nombre__contains=nombre)
            items = items.values()
    except:
        print("Hay un error en los valores de entrada")

    
    return render(request,'buscando.html',{
        'form_id': Consultar_id,
        'form_barras': Consultar_Barras,
        'form_nombre': Consultar_Nombre,
        'items': items
    })

@login_required
def buscador(request):
    return render(request, 'buscador.html',{
        'form_id': Consultar_id,
        'form_barras': Consultar_Barras,
        'form_nombre': Consultar_Nombre,
        })

@login_required 
def buscando(request):
    try:
        codigo = request.GET["txtCodigo"]
        if codigo != '':
            items = Item.objects.filter(id__startswith=codigo)
            items = items.values()
    except:
        print("Hay un error en los valores de entrada")
        codigo = ''
    try:
        barras = request.GET['txtBarras']
        if barras != '':
            items = Item.objects.filter(Barras__startswith=barras)
            items = items.values()
    except:
        print("Hay un error en los valores de entrada")
        barras = ''
    try:
        nombre = request.GET['txtNombre']
        if nombre != '':
            items = Item.objects.filter(Nombre__contains=nombre)
            items = items.values()
    except:
        print("Hay un error en los valores de entrada")
        nombre = ''
        
    if codigo == '' and barras == '' and nombre == '':
            items = {}
        
    
    return render(request,'buscando.html',{
        'form_id': Consultar_id,
        'form_barras': Consultar_Barras,
        'form_nombre': Consultar_Nombre,
        'items': items,
    })

@login_required   
def añadir_al_carrito(request):
    #descuenta y añade al carro
    return redirect('../')


