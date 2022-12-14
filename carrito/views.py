from django.shortcuts import render
from .models import Carrito, Items_Carrito, Finalizar_Venta

# Create your views here.
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
    
    
    return render(request, 'base_carrito.html', {
        'carrito': carrito,
        'items': items
    })