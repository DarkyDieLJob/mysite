from django.shortcuts import render, redirect
from .actualizador import main
from .forms import Planilla_Form

# Create your views here.
def subir_planilla(request):
    if request.method == 'POST':
        form = Planilla_Form(request.POST)
        if form.is_valid:
            form.save()
        return redirect('subir_planilla')
    else:
        form = Planilla_Form()
    return render(request, 'subir_planilla.html', {'form':form})

def actualizador(request):
    viejo_si_o_no = request.GET["viejo_si_o_no"]
    tipo_de_planilla = request.GET["tipo_de_planilla"]
    fecha = request.GET["fecha"]
    main(tipo_de_planilla, viejo_si_o_no, fecha)
    return render(request, 'actualizador.html')
    
def index_actualizador(request):
    return render(request, 'index_actualizador.html')

