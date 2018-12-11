from django.db import models

# Create your models here.


class Item(models.Model):

    codigo = models.IntegerField('Código')
    nome = models.CharField('Nome', max_length=255)
    valor = models.DecimalField('Preço', max_digits=9, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.nome