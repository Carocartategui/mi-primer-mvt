"""project URL Configuration

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
from django.urls import path

from blog.views import index as blog_index
from PrimerApp.views import index, monstrar_familiares, BuscarFamiliar, AltaFamiliar, mostrar_amigos, mostrar_colegas, Altacolega

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludar/', index),
    path('mi-familia/', monstrar_familiares),
    path('blog/', blog_index),
    path('mi-familia/buscar', BuscarFamiliar.as_view()),
    path('mi-familia/alta', AltaFamiliar.as_view()),
    path('mis-amigos/', mostrar_amigos),
    path('mis-colegas/', mostrar_colegas),
    path('mis-colegas/alta', Altacolega.as_view()),
]


