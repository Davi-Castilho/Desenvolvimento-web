from django.urls import path
from . import views

from .views import (
    product_create,
    product_delete,
    product_detail,
    product_list,
    product_update,
    home,
)

urlpatterns = [
    path('', product_list, name='product_list'),
    path('produtos/novo/', product_create, name='product_create'),
    path('produtos/<int:pk>/', product_detail, name='product_detail'),
    path('produtos/<int:pk>/editar/', product_update, name='product_update'),
    path('produtos/<int:pk>/excluir/', product_delete, name='product_delete'),
    
    path('home', home, name='home'),
]
