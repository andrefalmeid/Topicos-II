from django.shortcuts import render
from .forms import RestauranteForm,ProdutoForm
from .models import Restaurante,Produto
from django.contrib import messages
from django.shortcuts import render, redirect, get_list_or_404
from weasyprint import HTML, CSS
from django.http import HttpResponse
from django.template.loader import render_to_string, get_template
from django.core.files.storage import FileSystemStorage

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

def Restaurante_edit(request,pk):

    restaurante = Restaurante.objects.get(pk=pk)

    form = RestauranteForm(request.POST or None, instance=restaurante)
  
    if form.is_valid():
        form.save()
        messages.success(request,'Restaurante editado com sucesso')
        return redirect('restaurante')

    context = {
        'form':form,
        'id':restaurante.id
    }

    return render(request,'restaurante/restaurante_edit.html', context)

def Restaurante_delete(request,pk):

    restaurante = Restaurante.objects.get(pk=pk)
    restaurante.delete()
    messages.error(request,'Restaurante removido com sucesso')
    return redirect('restaurante')

def Produto_edit(request,pk):

    produto = Produto.objects.get(pk=pk)

    form = ProdutoForm(request.POST or None, instance=produto)
  
    if form.is_valid():
        form.save()
        messages.success(request,'Produto editado com sucesso')
        return redirect('produto')

    context = {
        'form':form,
        'id':produto.id
    }

    return render(request,'restaurante/produto_edit.html', context)

def Produto_delete(request,pk):

    produto = Produto.objects.get(pk=pk)
    produto.delete()
    messages.error(request,'Produto removido com sucesso')
    return redirect('produto')   

def Restaurante_Print_pdf(request):

    restaurante = Restaurante.objects.all()
    
    context = {
        'restaurante' : restaurante,
    
    }
    html_string = render_to_string('restaurante/restaurante_print.html', context)
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    html.write_pdf(target='/tmp/restaurante_print_pdf.pdf')


    fs = FileSystemStorage('/tmp')

    with fs.open('restaurante_print_pdf.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = "inline; filename='print.pdf'"
        
        return response

    return response

    return render(request, 'restaurante/restaurante_print.html', context)

def Produto_Print_pdf(request):

    produto = Produto.objects.all()
    
    context = {
        'produto' : produto,
    
    }
    html_string = render_to_string('restaurante/produto_print.html', context)
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    html.write_pdf(target='/tmp/produto_print_pdf.pdf')


    fs = FileSystemStorage('/tmp')

    with fs.open('produto_print_pdf.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = "inline; filename='print.pdf'"
        
        return response

    return response

    return render(request, 'restaurante/produto_print.html', context)