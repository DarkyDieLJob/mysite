from django.shortcuts import render
from .models import Carrito, Items_Carrito, Finalizar_Venta
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def carrito(request):
    carrito = Carrito.objects.all()
    try:
        carrito = Carrito.objects.all()
    except:
        print("Hay un error en los valores de entrada")
    try:
        items = Items_Carrito.objects.all()
        #manipular
        items = items.values()
    except:
        print("Hay un error en los valores de entrada")
    items_carrito = {}
    
    return render(request, 'carrito.html', {
        'carrito': carrito,
        'items': items,
        'items_carrito': items_carrito,
    })