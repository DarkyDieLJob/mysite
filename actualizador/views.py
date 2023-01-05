from django.shortcuts import render, redirect
#from .actualizador import main
from .forms import Planilla_Form
from .models import Proveedores
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
import time
from buscador.models import Item

@csrf_exempt
def subir_planilla(request):
    if request.method == 'POST':
        form = Planilla_Form(data=request.POST,files=request.FILES)
        if form.is_valid:
            nombre = request.POST['nombre']
            #archivo = request.POST['archivo']
            planilla = request.FILES['archivo']
            #print(planilla)
            form = Proveedores(nombre=nombre, archivo=planilla)
            form.save()
            time.sleep(30)
            #print(form.archivo)
            df_planilla = pd.read_excel("/home/darkydiel/mysite/media/{}".format(form.archivo),header=None)#columns=['Codigo','Nombre','Precio'])
            print(df_planilla)
            time.sleep(60)
            df_planilla = df_planilla.dropna()
            df_planilla.rename(columns={0:'Codigo',
                                            1:'Nombre',
                                            2:'Precio'},inplace=True)
            #print("df renamed:\n",df_planilla)
            #print(df_planilla['Precio'].dtype)
            df_planilla = df_planilla[df_planilla['Precio'] != 0]
            #print("df:\n",df_planilla)
            df_planilla['Codigo'] = df_planilla['Codigo'].astype(str)
            df_planilla['Codigo'] = df_planilla['Codigo'].str.strip() + nombre
            print(df_planilla)

            for item_p in df_planilla['Codigo']:
                #print('**************************************************')
                objeto = Item()
                try:
                    objeto = Item.objects.get(id=item_p)
                except objeto.DoesNotExist:
                    objeto = None
                if objeto == None:
                    #print('----------------------{} fuera de rango'.format(item_p))
                    id = item_p
                    nombre = df_planilla[df_planilla['Codigo'] == item_p]['Nombre'].values
                    precio = df_planilla[df_planilla['Codigo'] == item_p]['Precio'].values
                    objeto = Item(id=id,Nombre=nombre,Precio=precio)
                    objeto.save()
                else:
                    objeto.Precio = df_planilla[df_planilla['Codigo'] == item_p]['Precio'].values
                    objeto.save()
            print('Cargado con exito')
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