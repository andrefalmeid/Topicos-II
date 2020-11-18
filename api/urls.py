from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ClienteApi, PedidoApi, RestauranteApi, ProdutoApi

urlpatterns = {
    
    url(r'cliente_api/', ClienteApi.as_view(), name='cliente_api'),
    url(r'pedido_api/', PedidoApi.as_view(), name='pedido_api'),
    url(r'restaurante_api/', RestauranteApi.as_view(), name='restaurante_api'),
    url(r'produto_api/', ProdutoApi.as_view(), name='produto_api'),
    
}

urlpatterns = format_suffix_patterns(urlpatterns)