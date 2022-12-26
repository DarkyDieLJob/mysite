from django.shortcuts import render, redirect
from .actualizador import main
from .forms import Planilla_Form
from .models import Proveedores

# Create your views here.
def subir_planilla(request):
    if request.method == 'POST':
        form = Planilla_Form(data=request.POST,files=request.FILES)
        if form.is_valid:
            nombre = request.POST['nombre']
            fecha = request.POST['fecha']
            #archivo = request.POST['archivo']
            planilla = request.FILES['archivo']
            print(planilla)
            form = Proveedores(nombre=nombre, fecha=fecha, archivo=planilla)
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

