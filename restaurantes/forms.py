from django import forms
from restaurantes.models import *


class RestauranteForm(forms.ModelForm):

    class Meta:
        model = Restaurante
        field = '__all__'
        exclude = ()

class ProdutoForm(forms.ModelForm):

    class Meta:
        model = Produto
        field = '__all__'
        exclude = ()