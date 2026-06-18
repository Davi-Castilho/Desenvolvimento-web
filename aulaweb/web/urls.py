# inicio/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre', views.sobre, name='sobre'),
    path('listar_produto', views.listar_produtos, name='listar_produtos'),
    path('produto/<int:id>', views.detalhar_produto, name='detalhar_produto'),
    path('create_product', views.create_product, name='create_product'),
    path('update_product/<int:id>', views.update_product, name='update_product'),
    path('remove_product/<int:id>', views.remove_product, name='remove_product'),
    path('listar_cliente', views.listar_clientes, name='listar_clientes'),
    path('cliente/<int:id>', views.detalhar_cliente, name='detalhar_cliente'),
]
