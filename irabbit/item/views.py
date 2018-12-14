from django.shortcuts import render, redirect
from django.core.paginator import Paginator

# Create your views here.
from irabbit.item.forms import ItemForm
from irabbit.item.models import Item


def index(request):
    itens = Item.objects.all()

    paginator = Paginator(itens, 5)
    page = request.GET.get('page')
    itens = paginator.get_page(page)

    return render(request, 'view-acrescimo.html', {'itens': itens})


def cadastro(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('item.index')

    return render(request, 'create-acrescimo.html', {'form': form})


def atualizar(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('item.index')

    return render(request, 'create-acrescimo.html', {'form': form, 'item': item})


def apagar(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)

    if request.method == 'POST':
        item.delete()
        return redirect('item.index')

    return render(request, 'delete-acrescimo.html', {'form': form, 'item': item})