from django.db import models

# Create your models here.
class Marca(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome    

class Modelo(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Veiculo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    ano = models.IntegerField()
    descricao = models.CharField(max_length=200)
    horimetro = models.FloatField()

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.ano}) - {self.descricao} - Horímetro: {self.horimetro}"

class Medicao(models.Model):
    tipo = models.CharField(max_length=100)
    unidademedida = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.tipo} ({self.unidademedida})"

class UnidadeMedida(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
class MedicaoVeiculo(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    medicao = models.ForeignKey(Medicao, on_delete=models.CASCADE)
    valor = models.FloatField()
    data_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.veiculo} - {self.medicao}: {self.valor} em {self.data_hora}"
    
class MedicaoVeiculoTemp(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    medicao = models.ForeignKey(Medicao, on_delete=models.CASCADE)
    valor = models.FloatField()
    data_hora = models.DateTimeField(auto_now_add=True)
    arquivoid = models.CharField(max_length=256, db_index=True)