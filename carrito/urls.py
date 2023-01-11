from django.urls import path
from . import views

urlpatterns = [
    path('carrito/',views.carrito),
    path('carrito/agregar/<str:codigo>/<str:proveedor>',views.agregar_al_carrito),
    path('carrito/eliminar/<int:id>',views.eliminar_carrito),
    path('carrito/editar/<int:id>',views.editar_carrito),
]