from django.urls import path
from . import views

urlpatterns = [
    path('buscador/',views.registros),
    
]