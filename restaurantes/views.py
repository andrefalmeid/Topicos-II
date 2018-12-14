from django.shortcuts import render
from .forms import RestauranteForm,ProdutoForm
from .models import Restaurante,Produto
from django.contrib import messages
from django.shortcuts import render, redirect, get_list_or_404

def home(request):

    context = {

    }

    return render(request, 'restaurante/home.html', context)

def Restaurante_list(request):

    restaurante = Restaurante.objects.filter(status = True)

    if request.method == 'POST':

        form = RestauranteForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,'Restaurante cadastrado com sucesso')
            return redirect('restaurante')
        context = {
            
            'form': form
        }

        return render(request, 'legacy/restaurante.html', context)
        
    form = RestauranteForm()

    context = {
        'restaurante' : restaurante,
        'form': form
    }
    return render(request, 'restaurante/restaurante.html', context)

def Produto_list(request):

    produto = Produto.objects.filter()

    if request.method == 'POST':

        form = ProdutoForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,'Produto cadastrado com sucesso')
            return redirect('produto')
        context = {
            
            'form': form
        }

        return render(request, 'legacy/restaurante.html', context)
        
    form = ProdutoForm()

    context = {
        'produto' : produto,
        'form': form
    }
    return render(request, 'restaurante/produto.html', context)