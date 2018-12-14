from django.shortcuts import render
from .forms import ClienteForm,PedidoForm
from .models import Cliente, Pedido
from django.contrib import messages
from django.shortcuts import render, redirect, get_list_or_404
def teste(request):

    nome = "André Almeida"

    soma = 4+4
    
    context = { 
        'nome' : nome,
        'soma' : soma,  
    }

    return render(request, 'cliente/teste.html', context)

def home(request):

    context = {

    }

    return render(request, 'cliente/home.html', context)

def Cliente_list(request):
    ##ORM DE SELECT NO DNJANGO
    cliente = Cliente.objects.filter()
    

    if request.method == 'POST':

        form = ClienteForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,'Cliente cadastrado com sucesso')
            return redirect('cliente')
        context = {
            
            'form': form
        }

        return render(request, 'legacy/cliente.html', context)

    form = ClienteForm()

    context = {
        'cliente' : cliente,
        'form': form
    }
    return render(request, 'cliente/cliente.html', context)

def Pedido_list(request):
    ##ORM DE SELECT NO DNJANGO
    pedido = Pedido.objects.filter()
    

    if request.method == 'POST':

        form = PedidoForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,'Pedido cadastrado com sucesso')
            return redirect('pedido')
        context = {
            
            'form': form
        }

        return render(request, 'legacy/pedido.html', context)

    form = PedidoForm()

    context = {
        'pedido' : pedido,
        'form': form
    }
    return render(request, 'cliente/pedido.html', context)

