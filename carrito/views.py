from django.shortcuts import render
from .models import Carrito, Carrito_Items, Finalizar_Venta
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from buscador.models import Item

# Create your views here.
@login_required
def carrito(request):
    user = User.objects.get(username="Ferre")
    try:
        carrito = Carrito.objects.create(id=user.id)
    except:
        print("Hay un error en los valores de entrada")
        carrito = {}
        
    items = {}
    try:
        carrito = Carrito.objects.get(id=user.id)
    except:
        print("Hay un error en los valores de entrada")
     
    try:#Buscador
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
    except:
        print("Hay un error en los valores de entrada")
        items = {}
        
    try:
        items_carrito = Carrito_Items.objects.filter(carrito=carrito)
        #manipular
        items_carrito = items_carrito.values()
    except:
        print("Hay un error en los valores de entrada")
        items_carrito = {}
    
    
    return render(request, 'carrito.html', {
        'user':user,
        'carrito': carrito,
        'items': items,
        'items_carrito': items_carrito,
    })

@login_required
def agregar_al_carrito(request, codigo, proveedor):

    user = User.objects.get(username="Ferre")
    carrito = Carrito.objects.get(id=user.id)
    id = codigo + "/" + proveedor
    items = Item.objects.filter(id=id)
    items = items.values().first()
    print(items['id'])
    print(items)
    try:
        print("filtro")
        objeto = Carrito_Items.objects.filter(carrito=carrito, codigo=items['id'])
        print("objeto")
        print(objeto)

        cant = objeto.values().first()
        objeto = objeto.first()
        print("cant")
        print(cant)
        print("cant['cantidad']")
        print(cant['cantidad'])
        print("cant['cantidad'] + 1")
        cantidad = cant['cantidad']
        cantidad = float(cantidad) + 1.0
        print(cantidad)
        objeto.cantidad = cantidad
        print("objeto")
        print(objeto)
    
    except:
        print("except")
        objeto = Carrito_Items(carrito=carrito, codigo=items['id'], nombre=items['Nombre'], precio=items['Precio'])
    objeto.save()
        
    items_carrito = Carrito_Items.objects.filter(carrito=carrito)
    #manipular
    items_carrito = items_carrito.values()

    items = Item.objects.filter(id=id)
    items = items.values()

    return render(request, 'carrito.html', {
        'user':user,
        'carrito': carrito,
        'items': items,
        'items_carrito': items_carrito,
    })