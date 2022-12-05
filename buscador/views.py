from django.http import HttpResponse, JsonResponse
from .models import Item
# Create your views here.
def saludo(request, codigo_barras):
    items = list(Item.objects.get(Barras=codigo_barras))
    print(items)
    return JsonResponse(items)

