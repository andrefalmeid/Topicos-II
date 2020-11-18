from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from cliente.models import Cliente, Pedido


class ClienteSerializer(ModelSerializer):

    class Meta:
        model = Cliente
        field = '__all__'
        exclude = (
            'status',
            'id',
        )
class PedidoSerializer(ModelSerializer):

    class Meta:
        model = Pedido
        field = '__all__'
        exclude = (
            'status',
            'id',
        )

