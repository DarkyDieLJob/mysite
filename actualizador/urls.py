from django.urls import path
from . import views

urlpatterns = [
    path('index_actualizador/',views.index_actualizador),
    path('actualizador/',views.actualizador),
    path('subir_planilla/',views.subir_planilla),
]