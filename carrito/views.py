from django.shortcuts import render
from .models import Carrito, Carrito_Items, Finalizar_Venta
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

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
    
    try:
        items = carrito
        items = items.values()
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
def carrito_editar(request, codigo):
    return render(request, 'carrito.html', {})

@login_required
def carrito_eliminar(request, codigo):
    return render(request, 'carrito.html', {})