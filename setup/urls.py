"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from rest_framework import routers
from api import viewsets

route = routers.DefaultRouter()
route.register(r'marcas', viewsets.MarcaViewSet, basename='marca')
route.register(r'modelos', viewsets.ModeloViewSet, basename='modelo')
route.register(r'veiculos', viewsets.VeiculoViewSet, basename='veiculo')
route.register(r'medicoes', viewsets.MedicaoViewSet, basename='medicao')
route.register(r'unidades', viewsets.UnidadeMedidaViewSet, basename='unidade')
route.register(r'medicoes-veiculo', viewsets.MedicaoVeiculoViewSet, basename='medicao_veiculo')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
]
