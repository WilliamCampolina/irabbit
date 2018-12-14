from django.shortcuts import render, redirect
from django.core.paginator import Paginator

# Create your views here.
from irabbit.pedido.forms import pedidoForm
from irabbit.pedido.models import Pedido


def index(request):

    pedidos = Pedido.objects.all().order_by('-id')
    paginator = Paginator(pedidos, 5)
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

def cadastro(request):
    form = pedidoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('pedido.index')

    return render(request, 'create-pedido.html', {'form': form})

def atualizar(request, id):
    pedido = Pedido.objects.get(id=id)
    form = pedidoForm(request.POST or None, instance=pedido)

    if form.is_valid():
        form.save()
        return redirect('pedido.index')

    return render(request, 'create-pedido.html', {'form': form, 'pedido': pedido})


def apagar(request, id):
    pedido = Pedido.objects.get(id=id)
    form = pedidoForm(request.POST or None, instance=pedido)

    if request.method == 'POST':
        pedido.delete()
        return redirect('pedido.index')

    return render(request, 'delete-pedido.html', {'form': form, 'pedido': pedido})