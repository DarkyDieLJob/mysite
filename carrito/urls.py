from django.urls import path
from . import views

urlpatterns = [
    path('carrito/',views.carrito),
    path('carrito/agregar/<str:codigo>/<str:proveedor>',views.agregar_al_carrito),
    path('carrito/eliminra/<codigo>',views.carrito),
]