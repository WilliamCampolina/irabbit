from django import forms
from .models import Conta, TipoConta


class ContaForm(forms.ModelForm):
    class Meta:
        model = Conta
        fields = ['tipo', 'valor', 'descricao']




# class ContaForm(forms.Form):
#     # tipo = forms.ModelChoiceField(
#     #     queryset=TipoConta.objects.all(),
#     #     attrs={'class': "form-control"}
#     # )
#     valor = forms.DecimalField(
#         widget=forms.NumberInput(attrs={'class': "form-control"}),
#     )
#     descricao = forms.CharField(
#         widget=forms.Textarea(attrs={'class': "form-control"})
#     )