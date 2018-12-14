from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.
from irabbit.pedido.models import Pedido


def index(request):

    pedidos = Pedido.objects.all().order_by('-id')
    paginator = Paginator(pedidos,2)
    page = request.GET.get('page')

    pedidos = paginator.get_page(page)
    #pedidos = Pedido.objects.prefetch_related('produtos').prefetch_related('acrescimos').all().order_by('-id')
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