# Generated by Django 2.1.3 on 2018-12-11 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0002_auto_20181211_1550'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='acrescimos',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='produtos',
        ),
        migrations.DeleteModel(
            name='Pedido',
        ),
    ]
