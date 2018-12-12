from django.shortcuts import render

# Create your views here.
from irabbit.pedido.models import Pedido


def index(request):

    #pedidos = Pedido.objects.all()
    pedidos = Pedido.objects.prefetch_related('produtos').prefetch_related('acrescimos').all()
    return render(request, 'view-pedido.html', {'pedidos': pedidos})


    # for pedido in pedidos:
    #     produtos = pedido.produtos.all()
    #
    #     for produto in produtos:
    #         print(produto.nome)
    #         print(pedido.numero_pedido, produto)


    # t1, t2 = list(Pedido.objects.all())
    # produtos = t1.produtos.all()
    #
    # for produto in produtos:
    #      print(produto.nome)