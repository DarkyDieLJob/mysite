from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Factura_Proveedor, Factura_Blanco, Factura_Negro

# Create your views here.
@login_required
def registros(request):
    

    return render(request, 'registros.html', {})