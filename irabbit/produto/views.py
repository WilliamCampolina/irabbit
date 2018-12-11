from django.shortcuts import render, redirect
from irabbit.produto.forms import ProdutoForm

# Create your views here.
from irabbit.produto.models import Produto




def index(request):
    produtos = Produto.objects.all()
    return render(request, 'produto/view-produto.html', {'produtos': produtos})

def cadastro(request):
    form = ProdutoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('produto.index')

    return render(request, 'produto/create-produto.html', {'form': form})

def atualizar(request, id):
    produto = Produto.objects.get(id=id)
    form = ProdutoForm(request.POST or None, instance=produto)

    if form.is_valid():
        form.save()
        return redirect('produto.index')

    return render(request, 'produto/create-produto.html', {'form': form, 'produto': produto})

def apagar(request, id):
    produto = Produto.objects.get(id=id)
    form = ProdutoForm(request.POST or None, instance=produto)

    if request.method == 'POST':
        produto.delete()
        return redirect('produto.index')

    return render(request, 'produto/delete-produto.html', {'form': form, 'produto': produto})








