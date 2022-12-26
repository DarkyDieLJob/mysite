from django.urls import path, re_path
from . import views
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('index_actualizador/',views.index_actualizador),
    path('subir_planilla/',views.subir_planilla, name='subir_planilla'),
    path('subir_planilla/actualizador/',views.actualizador),
]

urlpatterns += [
    re_path(r'^media/(?P<path>.*)$',serve,{
        'document_root':settings.MEDIA_ROOT,
    })
]