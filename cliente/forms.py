from django import forms
from cliente.models import *


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        field = '__all__'
        exclude = ()

class PedidoForm(forms.ModelForm):

    class Meta:
        model = Pedido
        field = '__all__'
        exclude = ()