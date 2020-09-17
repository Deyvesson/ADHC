from django.db import models

# Create your models here.

class Socio(models.Model):

    socio_numero = models.IntegerField()
    socio_rg = models.CharField(max_length=7)
    socio_cpf = models.CharField(max_length=11)
    socio_patente = models.CharField(max_length=20)
    socio_nome = models.CharField(max_length=50)
    socio_email = models.CharField(max_length=50)
    socio_telefone = models.CharField(max_length=100)
    socio_endereco = models.CharField(max_length=100)
    socio_cidade = models.CharField(max_length=30)
    socio_cep = models.CharField(max_length=8)
    socio_estado = models.CharField(max_length=2)
    socio_data_criacao = models.DateTimeField(auto_now_add=True)
    socio_data_ult_atu = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.socio_nome
