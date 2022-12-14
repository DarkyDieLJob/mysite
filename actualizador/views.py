from django.shortcuts import render 

# Create your views here.

def actualizador(request):
    return render(request, 'actualizador.html')
    