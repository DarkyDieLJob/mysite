from django.shortcuts import render 
from .actualizador import main

# Create your views here.
def subir_planilla(request):
    return render(request, 'subir_planilla.html')

def actualizador(request):
    viejo_si_o_no = request.GET["viejo_si_o_no"]
    tipo_de_planilla = request.GET["tipo_de_planilla"]
    main(tipo_de_planilla, viejo_si_o_no)
    return render(request, 'actualizador.html')
    
def index_actualizador(request):
    return render(request, 'index_actualizador.html')

