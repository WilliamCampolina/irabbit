from django.shortcuts import render

# Create your views here.
from irabbit.pedido.models import Pedido


def index(request):
    #pedidos = Pedido.objects.prefetch_related('produtos__pedido_set').all()
    pedidos = Pedido.objects.all()

    for pedido in pedidos:
        print(pedido.produtos)

    # for produto in pedidos.produtos.all():
    #      print(produto.nome)

    return render(request, 'view-pedido.html', {'pedidos': pedidos})