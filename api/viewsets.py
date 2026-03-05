from rest_framework import viewsets
from telemetria import models
from api import serializers
from drf_yasg.utils import swagger_auto_schema

class MarcaViewSet(viewsets.ModelViewSet):
    queryset = models.Marca.objects.all()
    serializer_class = serializers.MarcaSerializer
    @swagger_auto_schema(
        operation_description="Retorna uma lista de todas as marcas de veículos registradas.",
        responses = {200: serializers.MarcaSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Cria uma nova marca de veículo.",
        responses = {201: serializers.MarcaSerializer(many=False)}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Retorna o registro de uma marca de veículo específica com base no ID fornecido.",
        responses = {200: serializers.MarcaSerializer(many=False)}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Atualiza o registro de uma marca de veículo específica com base no ID fornecido.",
        responses = {200: serializers.MarcaSerializer(many=False)}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Exclui o registro de uma marca de veículo específica com base no ID fornecido.",
        responses = {200: serializers.MarcaSerializer(many=False)}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class ModeloViewSet(viewsets.ModelViewSet):
    queryset = models.Modelo.objects.all()
    serializer_class = serializers.ModeloSerializer
    @swagger_auto_schema(
        operation_description="Retorna uma lista de todos os modelos de veículos registrados.",
        responses = {200: serializers.ModeloSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Cria um novo modelo de veículo.",
        responses = {201: serializers.ModeloSerializer(many=False)}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Retorna o registro de um modelo de veículo específico com base no ID fornecido.",
        responses = {200: serializers.ModeloSerializer(many=False)}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Atualiza o registro de um modelo de veículo específico com base no ID fornecido.",
        responses = {200: serializers.ModeloSerializer(many=False)}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Exclui o registro de um modelo de veículo específico com base no ID fornecido.",
        responses = {200: serializers.ModeloSerializer(many=False)}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class VeiculoViewSet(viewsets.ModelViewSet):
    queryset = models.Veiculo.objects.all()
    serializer_class = serializers.VeiculoSerializer
    @swagger_auto_schema(
        operation_description="Retorna uma lista de todos os veículos registrados.",
        responses = {200: serializers.VeiculoSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Cria um novo veículo.",
        responses = {201: serializers.VeiculoSerializer(many=False)}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Retorna o registro de um veículo específico com base no ID fornecido.",
        responses = {200: serializers.VeiculoSerializer(many=False)}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Atualiza o registro de um veículo específico com base no ID fornecido.",
        responses = {200: serializers.VeiculoSerializer(many=False)}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Exclui o registro de um veículo específico com base no ID fornecido.",
        responses = {200: serializers.VeiculoSerializer(many=False)}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class MedicaoViewSet(viewsets.ModelViewSet):
    queryset = models.Medicao.objects.all()
    serializer_class = serializers.MedicaoSerializer
    @swagger_auto_schema(
        operation_description="Retorna uma lista de todas as medições registradas para um veículo específico.",
        responses = {200: serializers.MedicaoSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Cria uma nova medição para um veículo específico.",
        responses = {201: serializers.MedicaoSerializer(many=True)}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Retorna o registro de uma medição específica com base no ID fornecido.",
        responses = {200: serializers.MedicaoSerializer(many=True)}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Atualiza o registro de uma medição específica com base no ID fornecido.",
        responses = {200: serializers.MedicaoSerializer(many=True)}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Exclui o registro de uma medição específica com base no ID fornecido.",
        responses = {200: serializers.MedicaoSerializer(many=True)}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class UnidadeMedidaViewSet(viewsets.ModelViewSet):
    queryset = models.UnidadeMedida.objects.all()
    serializer_class = serializers.UnidadeMedidaSerializer
    @swagger_auto_schema(
        operation_description="Retorna uma lista de todas as unidades de medida registradas.",
        responses = {200: serializers.UnidadeMedidaSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Cria uma nova unidade de medida.",
        responses = {201: serializers.UnidadeMedidaSerializer(many=False)}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Retorna o registro de uma unidade de medida específica com base no ID fornecido.",
        responses = {200: serializers.UnidadeMedidaSerializer(many=False)}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Atualiza o registro de uma unidade de medida específica com base no ID fornecido.",
        responses = {200: serializers.UnidadeMedidaSerializer(many=False)}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Exclui o registro de uma unidade de medida específica com base no ID fornecido.",
        responses = {200: serializers.UnidadeMedidaSerializer(many=False)}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class MedicaoVeiculoViewSet(viewsets.ModelViewSet):
    queryset = models.MedicaoVeiculo.objects.all()
    serializer_class = serializers.MedicaoVeiculoSerializer
    @swagger_auto_schema(
        operation_description="Retorna uma lista de todas as medições de veículos registradas.",
        responses = {200: serializers.MedicaoVeiculoSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Cria uma nova medição de veículo.",
        responses = {201: serializers.MedicaoVeiculoSerializer(many=False)}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Retorna o registro de uma medição de veículo específica com base no ID fornecido.",
        responses = {200: serializers.MedicaoVeiculoSerializer(many=False)}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Atualiza o registro de uma medição de veículo específica com base no ID fornecido.",
        responses = {200: serializers.MedicaoVeiculoSerializer(many=False)}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @swagger_auto_schema(
        operation_description="Exclui o registro de uma medição de veículo específica com base no ID fornecido.",
        responses = {200: serializers.MedicaoVeiculoSerializer(many=False)}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)