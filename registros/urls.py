from django.urls import path
from . import views

urlpatterns = [
    path('registros/',views.registros),
    
]