from django.shortcuts import redirect, render
from django.contrib import messages

from .forms import ProdutoForm
from .models import Produto, Cliente

# Create your views here.

def index(request):
    return render(request, 'web/index.html')

def sobre(request):
    return render(request, 'web/sobre.html')

def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, "web/listar_produtos.html", {'produtos': produtos})

def detalhar_produto(request, id):
    produto = Produto()
    try:
        produto = Produto.objects.get(pk=id)
    except Exception as e:
        produto.nome = 'Não existe'
    return render(request, "web/produto_detail.html", {'produto': produto})

def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, "web/listar_clientes.html", {'clientes': clientes})

def detalhar_cliente(request, id):
    cliente = Cliente()
    try:
        cliente = Cliente.objects.get(pk=id)
    except Exception as e:
        cliente.nome = 'Não existe'
    return render(request, "web/cliente_detail.html", {'cliente': cliente})

def create_product(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto cadastro com sucesso.')
            return redirect("listar_produtos")
        else:
            messages.error(request, 'Informe todos os campos.')
    else:
        form = ProdutoForm()
    return render(request, "web/produto_form.html", {'form': form})

def update_product(request, id):
    produto = Produto.objects.get(pk=id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto alterado com sucesso.')
            return redirect("listar_produtos")
        else:
            messages.error(request, 'Informe todos os campos.')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, "web/produto_form.html", {'form': form, 'editar': True})

def remove_product(request, id):
    produto = Produto.objects.get(pk=id)
    if request.method == 'POST':
        try:
            produto.delete()
            messages.success(request, 'Produto deletado com sucesso.')
            return redirect("listar_produtos")
        except:
            messages.error(request, 'Não foi possível deletar o Produto.')
    return render(request, "web/produto_delete.html", {'produto': produto})