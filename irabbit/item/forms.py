from django import forms

from irabbit.item.models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['codigo', 'nome', 'valor']