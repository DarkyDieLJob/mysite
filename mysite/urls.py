"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from buscador import urls as urls_buscador
from carrito import urls as urls_carrito
from inicio import urls as urls_inicio
from actualizador import urls as urls_actualizador
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',include(urls_actualizador)),
    path('',include(urls_inicio)),
    path('',include(urls_buscador)),
    path('',include(urls_carrito)),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

