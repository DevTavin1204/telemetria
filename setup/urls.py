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
from rest_framework import routers, permissions
from api import viewsets
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API para telemetria de veículos agricolas.",
        default_version='v1',
        description="Sistema para cadastro e controle por telemetria de frotas de veículos agrícolas.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contato@telemetria.com.br"),
        license=openapi.License(name="free"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


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

# URLs para a documentação Swagger
urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger.json/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]