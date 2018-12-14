from django import forms
from .models import Produto


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['codigo', 'nome', 'valor', 'itens']
        widgets = {
            'itens': forms.SelectMultiple(attrs={'class': 'form-control','size':'12' }),
             }



