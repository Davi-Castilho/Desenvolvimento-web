from django.forms import modelform_factory
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from rest_framework import viewsets

from .models import Product, Projeto
from .serializers import ProductSerializer, ProjetoSerializer


ProductForm = modelform_factory(Product, fields=['name', 'description', 'price', 'stock'])


def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'products/product_form.html', {'form': form})


def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/product_form.html', {'form': form, 'product': product})


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'products/product_confirm_delete.html', {'product': product})


from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    # Define que este ViewSet exige um token JWT válido
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    @action(detail=False, methods=['GET'])
    def count_produtos(self, request):
        return Response({'count': Product.objects.count()})


class ProjetoViewSet(viewsets.ModelViewSet):
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer
    
    
    
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

# Endpoint público para teste
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def home(request):
    return Response({"mensagem": "Bem-vindo à API pública!"})

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def count_produtos(request):
    return Response({'count': Product.objects.count()})



from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages



# Página de registro
def register_view(request):
  if request.method == "POST":
    # Valores informados no cadastro
    username = request.POST['username']
    password = request.POST['password']
    confirm_password = request.POST['confirm_password']

    if password == confirm_password:
      # Inclusão no banco de dados do novo usuário
      user = User.objects.create_user(username=username, password=password)
      messages.success(request, "Usuário criado com sucesso!")
      return redirect('login')
    else:
      messages.error(request, "As senhas não conferem!")

  return render(request, 'products/register.html')


# Página de login
def login_view(request):
  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']
    # Método para verificar as credenciais
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user) # cria a sessão
      return redirect('dashboard')
    else:
      messages.error(request, "Usuário ou senha inválidos!")
  return render(request, 'products/login.html')


# Página de logout
def logout_view(request):
  logout(request)
  return redirect('login')

# Dashboard protegido
@login_required(login_url='login')
def dashboard(request):
  return render(request, 'products/dashboard.html')
