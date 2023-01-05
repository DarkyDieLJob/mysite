from django.urls import path
from . import views

urlpatterns = [
    path('carrito/',views.carrito),
    path('cantidad/<codigo>',views.carrito),
    path('eliminra/<codigo>',views.carrito),
]