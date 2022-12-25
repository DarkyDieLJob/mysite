from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('index_actualizador/',views.index_actualizador),
    path('subir_planilla/',views.subir_planilla, name='subir_planilla'),
    path('subir_planilla/actualizador/',views.actualizador),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)