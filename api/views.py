import base64 #decodificador de arquivos imagem,pdf...

from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy, reverse
from django.db.models import Count, Min, Sum, Avg
from django.contrib.auth import authenticate, login as logon, logout
from django.contrib.auth.decorators import login_required
import tempfile
from django.http import HttpResponse
from django.contrib import messages
from django.core import serializers
from django.template.loader import render_to_string
from django.core.files.storage import FileSystemStorage
from datetime import datetime, timedelta #um dia precisar criar data para api
import json
import urllib
from urllib.request import urlopen
from decimal import Decimal
from cliente.models import Cliente, Pedido
from restaurantes.models import Restaurante, Produto
from rest_framework.generics import ListAPIView, CreateAPIView, GenericAPIView
from rest_framework import serializers
from .serializers import ClienteSerializer, PedidoSerializer
from rest_framework import generics, permissions, pagination, mixins,authentication #responsaveis por permições em uma api
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

class ClienteApi(APIView):
    def get(self, request): #uma requisição dos campos, quero fazer um json com todos os meus clientes
        
        l = {} #recebe uma lista/fila vazia onde vou guardar os registros que vou guardar via json
        lista = [] #dicionario é um container de listas 
        cliente = Cliente.objects.all() #recuperar todos os clientes   
        for x in cliente: 
            id = x.id
            nome = x.nome 
            endereco = x.endereco
            cidade = x.cidade
            l = {               #pego os dados transformo em uma lista(l)
                'id' : id,
                'nome': nome,
                'endereco' : endereco,
                'cidade' : cidade
            }
            lista.append(l) #envio essa lista para o dicionario "lista"
        return Response({ #retorna minha lista 
            "lista": lista,
        }) #esse é o GET que é quando eu preciso consultar/recuperar dados
    

    def post(self, request):
       
#verificando se eu tenho algo no request
        
        cliente = Cliente()
        cliente.nome = 'João'


        cliente.save()

        
        return Response({"Sucesso": True})

        

class PedidoApi(APIView):
    def get(self, request): #uma requisição dos campos, quero fazer um json com todos os meus clientes
        
        l = {} 
        lista = []  
        pedido = Pedido.objects.all() 
        for x in pedido: 
            id = x.id
            produto = x.produto.produto 
            quantidade = x.quantidade
            cliente = x.cliente.nome
            l = {               
                'id' : id,
                'produto': produto,
                'quantidade' : quantidade,
                'cliente' : cliente,
                
            }
            lista.append(l) 
        
        return Response({  
            "lista": lista,
        
        })
    

    def post(self, request):
       
        
        pedido = Pedido()


        pedido.save()

        
        return Response({"Sucesso": True})

class RestauranteApi(APIView):
    def get(self, request): 

        l = {} 
        lista = []  
        restaurante = Restaurante.objects.all() 
        for x in restaurante: 
            id = x.id
            nome = x.nome
            endereco = x.endereco
            cidade = x.cidade
            l = {               
                'id' : id,
                'nome': nome,
                'endereco' : endereco,
                'cidade' : cidade,
                
            }
            lista.append(l) 
        
        return Response({  
            "lista": lista,
        })
    

    def post(self, request):
       
        
        restaurante = Restaurante()
        restaurante.nome = 'Sei la'

        restaurante.save()

        
        return Response({"Sucesso": True})


class ProdutoApi(APIView):
    def get(self, request): 

        l = {} 
        lista = []  
        produto = Produto.objects.all() 
        for x in produto: 
            id = x.id
            produto = x.produto
            descricao = x.descricao
            preco = x.preco
            restaurante_que_vende = x.restaurante_que_vende
            l = {               
                'id' : id,
                'produto' : produto,
                'descricao' : descricao,
                'preco' : preco,
                'restaurante_que_vende' : restaurante_que_vende,
                
            }
            lista.append(l) 
        
        return Response({  
            "lista": lista,
        })
    

    def post(self, request):
       
        
        produto = Produto()
        produto.nome = 'Coca Cola'

        produto.save()

        
        return Response({"Sucesso": True})

