from django.shortcuts import render, redirect
from .models import Carrito, Carrito_Items, Finalizar_Venta
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from buscador.models import Item
from .forms import Editar_Carrito_Form

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
    try:
        objeto = Carrito_Items.objects.filter(carrito=carrito, codigo=items['id'])
        cant = objeto.values().first()
        objeto = objeto.first()
        cantidad = cant['cantidad']
        cantidad = float(cantidad) + 1.0
        objeto.cantidad = cantidad
    except:
        print("except")
        objeto = Carrito_Items(carrito=carrito, codigo=items['id'], nombre=items['Nombre'], cantidad=1.1, precio=items['Precio'])
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

def editar_carrito(request, id):
    p = Carrito_Items.objects.get(id=id)
    if request.method == 'POST':
        form = Editar_Carrito_Form(request.POST, instance=p)
        if form.is_valid():
            p.cantidad = request.POST['cantidad']
            p.save()
            return redirect('/carrito/')
    else:
        form = Editar_Carrito_Form(instance=p)
    return render(request, 'carrito_editar.html', {
        'form':form,
        })

def eliminar_carrito(request, id):
    p = Carrito_Items.objects.get(id=id)
    print(p)
    if request.method == 'GET':
        p.delete()
        print(p)
    else:
        print('metodo no es POST')
    return redirect('/carrito/')