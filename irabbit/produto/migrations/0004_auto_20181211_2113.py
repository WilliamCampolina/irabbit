# Generated by Django 2.1.3 on 2018-12-11 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0003_auto_20181211_2113'),
        ('produto', '0003_auto_20181211_1552'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.AlterField(
            model_name='produto',
            name='itens',
            field=models.ManyToManyField(blank=True, to='item.Item'),
        ),
    ]