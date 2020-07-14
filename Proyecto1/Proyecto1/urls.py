"""Proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

#Para crear un nuevo proyecto django: 
#django-admin startproject nameProyect
#python manage.py startapp nameapp

from django.contrib import admin
from django.urls import path
from Proyecto1.views import saludo
from Proyecto1.views import despedida, dameFecha, calculaEdad, mostrarPlantilla, mostrarPlantilla2, mostrarProductores, mostrarProductor, htmlCondicionales, CursoC, busqueda_productos
from Proyecto1.views import buscar, seleccion, index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('', index),
    path("chau/", despedida),
    path("si/", dameFecha),
    path("edades/<int:edad>/<int:agno>", calculaEdad),
    path("mostrarPlantilla/", mostrarPlantilla),
    path("mostrarPlantilla2/", mostrarPlantilla2),
    path("mostrarProductores/", mostrarProductores),
    path("mostrarProductor/<idd>", mostrarProductor),
    path("htmlCondicionales/", htmlCondicionales),
    path("CursoC/", CursoC),
    path("busqueda_productos/", busqueda_productos),
    path("buscar/", buscar),
    path("seleccion/<int:selec>", seleccion),
]
