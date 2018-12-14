from django.db import models

# Create your models here.
from irabbit.produto.models import Produto, Item


class Pedido(models.Model):
    produtos = models.ManyToManyField(Produto)
    acrescimos = models.ManyToManyField(Item, blank=True)
    numero_pedido = models.IntegerField(default=0)
    endereco = models.CharField('Endereço', max_length=255)
    referencia = models.CharField('Referência',max_length=255, default='')
    meio_pagamento = models.CharField('Tipo Pagamento', max_length=255)

    valor_total = models.DecimalField('Total', max_digits=9, decimal_places=2)
    valor_pago = models.DecimalField('Valor Pago ', max_digits=9, decimal_places=2)
    valor_taxa_entrega = models.DecimalField('Taxa Entrega', max_digits=9, decimal_places=2)

    # def __str__(self):
    #     return str(self.numero_pedido)
