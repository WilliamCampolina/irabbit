# -*- coding: utf-8 -*-
from django import forms

from irabbit.pedido.models import Pedido


class pedidoForm(forms.ModelForm):


    class Meta:
        model = Pedido
        fields = ['produtos', 'acrescimos', 'numero_pedido', 'endereco', 'referencia', 'meio_pagamento', 'valor_total', 'valor_pago', 'valor_taxa_entrega' ]
        widgets = {
            'produtos': forms.SelectMultiple(attrs={'size': '12'}),
            'acrescimos': forms.SelectMultiple(attrs={'size': '12'}),
        }



