from django.http import HttpResponse

# Create your views here.
def saludo(request, codigo_barras):
    print(codigo_barras)
    return HttpResponse("<h2>Hola carlossss<h2/>Codigo Buscado:  %s" %codigo_barras)
