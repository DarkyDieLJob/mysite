from django.shortcuts import render
from .models import Carrito, Carrito_Items, Finalizar_Venta
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required
def carrito(request):
    user = User.objects.get(username="Ferre")
    carrito = Carrito.objects.all()
    carrito.delete()
    carrito = Carrito.objects.create(usuario=user.id)
    
    items = {}
    try:
        carrito = Carrito.objects.get(usuario=user.id)
    except:
        print("Hay un error en los valores de entrada")
    try:
        items_carrito = Carrito_Items.objects.filter(carrito=carrito.usuario)
        #manipular
        items_carrito = items.values()
    except:
        print("Hay un error en los valores de entrada")
        items_carrito = {}
    
    
    return render(request, 'carrito.html', {
        'carrito': carrito,
        'items': items,
        'items_carrito': items_carrito,
    })