"""
URL configuration for Prueba project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views

urlpatterns = [
    path('', views.RecetaListView.as_view(), name="recetas_listado"),
    path('detalle/<pk>', views.RecetaDetailView.as_view(), name="receta_detalle"),
    path('crear', views.RecetaCreateView.as_view(), name="receta_crear"),
    path('borrar/<pk>', views.RecetaDeleteView.as_view(), name="receta_borrar"),
    path('modificar/<pk>', views.RecetaUpdateView.as_view(), name="receta_modificar"),
]
