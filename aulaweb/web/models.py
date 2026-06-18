from django.db import models


# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)  # nome do categoria

    class Meta:
        db_table = "categoria"              # nome da tabela no banco
        ordering = ["nome"]               # ordenação padrão (por nome)
        verbose_name = "Categoria"          # nome singular para admin
        verbose_name_plural = "Categorias"  # nome plural para admin

    def __str__(self):
        return f"{self.nome}"

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=100, unique=True)  # nome do produto
    descricao = models.TextField(blank=True, null=True)   # descrição opcional
    preco = models.DecimalField(max_digits=10, decimal_places=2)  # 2 casas decimais
    quantidade_estoque = models.PositiveIntegerField(default=0)   # estoque inicial
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    data_criacao = models.DateTimeField(auto_now=True)  # preenchido na criação
    data_atualizacao = models.DateTimeField(auto_now=True)  # atualizado sempre que salvar

    class Meta:
        db_table = "produto"              # nome da tabela no banco
        ordering = ["nome"]               # ordenação padrão (por nome)
        verbose_name = "Produto"          # nome singular para admin
        verbose_name_plural = "Produtos"  # nome plural para admin

    def __str__(self):
        return f"{self.nome} - R${self.preco}"
    

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=100)  # nome do produto
    email = models.CharField(max_length=200, unique=True)  # nome do produto

    class Meta:
        db_table = "cliente"              # nome da tabela no banco
        ordering = ["nome"]               # ordenação padrão (por nome)
        verbose_name = "Cliente"          # nome singular para admin
        verbose_name_plural = "Clientes"  # nome plural para admin

    def __str__(self):
        return f"{self.nome}"

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)  
    produtos = models.ManyToManyField(Produto)
    data = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "pedido"              
        ordering = ["data"]              
        verbose_name = "Pedido"          
        verbose_name_plural = "Pedidos"  

    def __str__(self):
        return f"{self.data}"
    
class ItemPedido(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)  
    quantidade = models.IntegerField(default=1)

    class Meta:
        db_table = "item_pedido"              
        verbose_name = "ItemPedido"          
        verbose_name_plural = "ItensPedido"  