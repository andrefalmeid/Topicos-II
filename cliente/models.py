from django.db import models


class Cliente(models.Model):
    nome = models.CharField(
        'Nome', max_length=120)
    endereco = models.CharField(
        'Endereço', max_length=80, blank=True, null=True)
    cidade = models.CharField(
        'Cidade', max_length=20, blank=True, null=True)
    idade = models.CharField(
        'Idade', max_length=20)
    aniversario = models.DateField(
        'Aniversário', blank=True, null=True)
    status = models.BooleanField(
        'Status', default=True)
    
    
         

    class Meta:

        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nome


class Pedido(models.Model):
    produto = models.CharField('Produto', max_length=120)
    Quantidade = models.CharField(
        'Quantidade', max_length=2, blank=True, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    
    class Meta:

        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.produto        
        
