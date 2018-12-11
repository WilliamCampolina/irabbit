from django.db import models
from django.utils.timezone import now

# Create your models here.
class TipoConta(models.Model):
    descricao = models.CharField('Descricao', max_length=100)
    deb_cred = models.CharField('Débito ou Crédito', max_length=1)


    def __str__(self):
        return self.descricao


class Conta(models.Model):
    tipo = models.ForeignKey(TipoConta, on_delete=models.CASCADE)
    valor = models.DecimalField('Valor',max_digits=9, decimal_places=2)
    descricao = models.TextField('Descricao')
    data = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.descricao