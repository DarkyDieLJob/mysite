#from django.http import HttpResponse, JsonResponse
from .models import Item
from django.shortcuts import render
from .forms import Consultar_id

# Create your views here.

def saludo(request):
    id = request.GET['id']
    items = Item.objects.filter(id__startswith=id)
    items = items.values()
    return render(request,'index.html',{
        'form': Consultar_id,
        'item': items
    })

