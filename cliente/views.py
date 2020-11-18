from django.shortcuts import render
from .forms import ClienteForm,PedidoForm
from .models import Cliente, Pedido
from django.contrib import messages
from django.shortcuts import render, redirect, get_list_or_404
from weasyprint import HTML, CSS
from django.http import HttpResponse
from django.template.loader import render_to_string, get_template
from django.core.files.storage import FileSystemStorage
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

def Cliente_edit(request,pk):

    cliente = Cliente.objects.get(pk=pk)

    form = ClienteForm(request.POST or None, instance=cliente)
  
    if form.is_valid():
        form.save()
        messages.success(request,'Cliente editado com sucesso')
        return redirect('cliente')

    context = {
        'form':form,
        'id':cliente.id
    }

    return render(request,'cliente/cliente_edit.html', context)

def Cliente_delete(request,pk):

    cliente = Cliente.objects.get(pk=pk)
    cliente.delete()
    messages.error(request,'Cliente removido com sucesso')
    return redirect('cliente')

def Pedido_edit(request,pk):

    pedido = Pedido.objects.get(pk=pk)

    form = PedidoForm(request.POST or None, instance=pedido)
  
    if form.is_valid():
        form.save()
        messages.success(request,'Pedido editado com sucesso')
        return redirect('pedido')

    context = {
        'form':form,
        'id':pedido.id
    }

    return render(request,'cliente/pedido_edit.html', context)

def Pedido_delete(request,pk):

    pedido = Pedido.objects.get(pk=pk)
    pedido.delete()
    messages.error(request,'Pedido removido com sucesso')
    return redirect('pedido')

def Cliente_Print_pdf(request):

    cliente = Cliente.objects.all()
    
    context = {
        'cliente' : cliente,
    
    }
    html_string = render_to_string('cliente/cliente_print.html', context)
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    html.write_pdf(target='/tmp/cliente_print_pdf.pdf')


    fs = FileSystemStorage('/tmp')

    with fs.open('cliente_print_pdf.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = "inline; filename='print.pdf'"
        
        return response

    return response

    return render(request, 'cliente/cliente_print.html', context)

def Pedido_Print_pdf(request):

    pedido = Pedido.objects.all()
    
    context = {
        'pedido' : pedido,
    
    }
    html_string = render_to_string('cliente/pedido_print.html', context)
    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    html.write_pdf(target='/tmp/pedido_print_pdf.pdf')


    fs = FileSystemStorage('/tmp')

    with fs.open('pedido_print_pdf.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = "inline; filename='print.pdf'"
        
        return response

    return response

    return render(request, 'cliente/pedido_print.html', context)
