from django.db import models


class Restaurante(models.Model):
    nome = models.CharField('Nome', max_length=120)
    endereco = models.CharField(
        'Endereço', max_length=80, blank=True, null=True)
    cidade = models.CharField(
        'Cidade', max_length=20, blank=True, null=True)
    status = models.BooleanField(
        'Status', default=True)


    class Meta:

        verbose_name = 'Restaurante'
        verbose_name_plural = 'Restaurantes'

    def __str__(self):
        return f'{self.nome}'


class Produto(models.Model):
    produto = models.CharField(
        'Produto', max_length=120)
    descricao = models.CharField(
        'Descricao', max_length=280)
    preco = models.DecimalField(
        'Preço' ,max_digits=4, decimal_places=2, blank=True, null=True)
    restaurante_que_vende = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    
    class Meta:

        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.produto
