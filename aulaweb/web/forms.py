from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'descricao', 'quantidade_estoque', 'categoria']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do produto'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 4,}),
            'quantidade_estoque': forms.NumberInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'nome': 'Nome do Produto',
            'preco': 'Preço',
            'descricao': 'Descrição',
            'quantidade_estoque': 'Quantidade em Estoque',
            'categoria': 'Categoria',
        }
        
    def clean_quantidade_estoque(self):
        quantidade = self.cleaned_data.get('quantidade_estoque')
        if quantidade is None or quantidade <= 0:
            raise forms.ValidationError("Informe a quantidade do produto")
        return quantidade
