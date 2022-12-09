from django.urls import path
from . import views

urlpatterns = [
    path('actualizador/',views.actualizador),
]