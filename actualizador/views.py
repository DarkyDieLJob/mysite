from django.shortcuts import render
#from tablib import Dataset 

# Create your views here.

def actualizador(request):
    #template = loader.get_template('export/importar.html')  
    if request.method == 'POST':  
        prueva_resource = Prueva_Resource()  
        dataset = Dataset()  
        #print(dataset)  
        lista = request.FILES['xlsfile']  
        #print(nuevas_personas)  
        imported_data = dataset.load(lista.read())  
        #print(dataset)  
        result = prueva_resource.import_data(dataset, dry_run=True) # Test the data import  
        #print(result.has_errors())  
        if not result.has_errors():  
            prueva_resource.import_data(dataset, dry_run=False) # Actually import now 
    return render(request, 'actualizador.html')