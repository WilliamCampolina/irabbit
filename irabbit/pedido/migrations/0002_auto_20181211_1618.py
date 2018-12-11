# Generated by Django 2.1.3 on 2018-12-11 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='numero_pedido',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pedido',
            name='referencia',
            field=models.CharField(default='', max_length=255, verbose_name='Referência'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='meio_pagamento',
            field=models.CharField(max_length=255, verbose_name='Tipo Pagamento'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='valor_pago',
            field=models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Valor Pago '),
        ),
    ]