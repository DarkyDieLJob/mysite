#from django.http import HttpResponse, JsonResponse
from . import models
from django.shortcuts import render
# Create your views here.

def saludo(request):
    items = models.Item.objects.all()
    print(items)
    return render(request,'index.html',{
        'item': items
    })

