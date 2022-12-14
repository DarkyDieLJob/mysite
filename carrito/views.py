from django.shortcuts import render
from .models import Carrito, Items_Carrito, Finalizar_Venta

# Create your views here.
def carrito(request):
    carrito = Carrito.objects.all()
    
    items = Items_Carrito.objects.all()
    #manipular
    items = items.values()
    
    
    
    return render(request, 'carrito.html', {
        'carrito': carrito,
        'item': items
    })